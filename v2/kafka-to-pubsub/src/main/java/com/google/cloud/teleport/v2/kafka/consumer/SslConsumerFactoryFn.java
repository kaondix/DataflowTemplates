/*
 * Copyright (C) 2020 Google Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not
 * use this file except in compliance with the License. You may obtain a copy of
 * the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 * License for the specific language governing permissions and limitations under
 * the License.
 */

package com.google.cloud.teleport.v2.kafka.consumer;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.nio.channels.FileChannel;
import java.nio.channels.ReadableByteChannel;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.security.KeyStore;
import java.security.KeyStoreException;
import java.security.NoSuchAlgorithmException;
import java.security.cert.CertificateException;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;
import org.apache.beam.sdk.io.FileSystems;
import org.apache.beam.sdk.transforms.SerializableFunction;
import org.apache.kafka.clients.CommonClientConfigs;
import org.apache.kafka.clients.consumer.Consumer;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.common.config.SslConfigs;
import org.apache.kafka.common.security.auth.SecurityProtocol;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/** Class to create Kafka Consumer with configured SSL. */
public class SslConsumerFactoryFn
    implements SerializableFunction<Map<String, Object>, Consumer<byte[], byte[]>> {
  private final Map<String, String> sslConfig;
  private final Map<String, String> keyStoreExtension;
  private static final String TRUSTSTORE_LOCAL_PATH = "/tmp/kafka.truststore";
  private static final String KEYSTORE_LOCAL_PATH = "/tmp/kafka.keystore";

  /* Logger for class.*/
  private static final Logger LOG = LoggerFactory.getLogger(SslConsumerFactoryFn.class);

  public SslConsumerFactoryFn(Map<String, String> sslConfig) {
    this.sslConfig = sslConfig;
    keyStoreExtension = new HashMap<>();
    keyStoreExtension.put("jks", "jks");
    keyStoreExtension.put("pkcs12", "p12");
  }

  @Override
  public Consumer<byte[], byte[]> apply(Map<String, Object> config) {
    logConfig(config);
    String bucket = sslConfig.get("bucket");
    String trustStorePath = sslConfig.get(SslConfigs.SSL_TRUSTSTORE_LOCATION_CONFIG);
    String keyStorePath = sslConfig.get(SslConfigs.SSL_KEYSTORE_LOCATION_CONFIG);
    String trustStorePassword = sslConfig.get(SslConfigs.SSL_TRUSTSTORE_PASSWORD_CONFIG);
    String keyStorePassword = sslConfig.get(SslConfigs.SSL_KEYSTORE_PASSWORD_CONFIG);
    String keyPassword = sslConfig.get(SslConfigs.SSL_KEY_PASSWORD_CONFIG);
    String trustStoreType = sslConfig.get(SslConfigs.SSL_TRUSTSTORE_TYPE_CONFIG).toLowerCase();
    String keyStoreType = sslConfig.get(SslConfigs.SSL_KEYSTORE_TYPE_CONFIG).toLowerCase();
    String outputTrustStoreFilePath;
    String outputKeyStoreFilePath;
    try {
      outputTrustStoreFilePath =
          TRUSTSTORE_LOCAL_PATH + '.' + this.keyStoreExtension.get(trustStoreType);
      outputKeyStoreFilePath = KEYSTORE_LOCAL_PATH + '.' + this.keyStoreExtension.get(keyStoreType);
      if (isLocalFileNotExist(outputTrustStoreFilePath)) {
        getGcsFileAsLocal(bucket, trustStorePath, outputTrustStoreFilePath);
      }
      if (isLocalFileNotExist(outputKeyStoreFilePath)) {
        getGcsFileAsLocal(bucket, keyStorePath, outputKeyStoreFilePath);
      }
    } catch (IOException e) {
      LOG.error("Failed to retrieve data for SSL", e);
      return new KafkaConsumer<>(config);
    }
    try {
      validateCertificate(outputKeyStoreFilePath, keyStorePassword, keyStoreType);
      validateCertificate(outputTrustStoreFilePath, trustStorePassword, trustStoreType);
    } catch (IOException | KeyStoreException | CertificateException | NoSuchAlgorithmException e) {
      LOG.error("Certificate validation failed", e);
      return new KafkaConsumer<>(config);
    }

    config.put(CommonClientConfigs.SECURITY_PROTOCOL_CONFIG, SecurityProtocol.SASL_SSL.name());
    config.put(SslConfigs.SSL_TRUSTSTORE_LOCATION_CONFIG, outputTrustStoreFilePath);
    config.put(SslConfigs.SSL_KEYSTORE_LOCATION_CONFIG, outputKeyStoreFilePath);
    config.put(SslConfigs.SSL_TRUSTSTORE_PASSWORD_CONFIG, trustStorePassword);
    config.put(SslConfigs.SSL_KEYSTORE_PASSWORD_CONFIG, keyStorePassword);
    config.put(SslConfigs.SSL_KEY_PASSWORD_CONFIG, keyPassword);

    return new KafkaConsumer<>(config);
  }

  /**
   * Reads a file from GCS and writes it locally.
   *
   * @param bucket GCS bucket name
   * @param filePath path to file in GCS
   * @param outputFilePath path where to save file locally
   * @throws IOException thrown if not able to read or write file
   */
  public static void getGcsFileAsLocal(String bucket, String filePath, String outputFilePath)
      throws IOException {
    String gcsFilePath = String.format("gs://%s/%s", bucket, filePath);
    LOG.info("Reading contents from GCS file: {}", gcsFilePath);
    Set<StandardOpenOption> options = new HashSet<>(2);
    options.add(StandardOpenOption.CREATE);
    options.add(StandardOpenOption.WRITE);
    options.add(StandardOpenOption.TRUNCATE_EXISTING);
    // Copy the GCS file into a local file and will throw an I/O exception in case file not found.
    copyGcsFileToLocal(gcsFilePath, outputFilePath, options);
  }

  private static void copyGcsFileToLocal(String gcsFilePath, String outputFilePath,
      Set<StandardOpenOption> options) throws IOException {
    long transferredBytes;
    for (int i = 1; i <= 5; i++) {
      try (ReadableByteChannel readerChannel =
          FileSystems.open(FileSystems.matchSingleFileSpec(gcsFilePath).resourceId())) {
        try (FileChannel writeChannel = FileChannel.open(Paths.get(outputFilePath), options)) {
          transferredBytes = writeChannel.transferFrom(readerChannel, 0, Long.MAX_VALUE);
        }
      }
      if (new File(outputFilePath).exists()) {
        LOG.info("Contents from GCS file {} was written in {}. Length of file: {}", gcsFilePath, outputFilePath, transferredBytes);
        return;
      }
      LOG.warn("Failed to write file, {} retries remaining", 5 - i);
      try {
        Thread.sleep(5);
      } catch (InterruptedException e) {
        LOG.error(e.getMessage());
      }
    }
    throw new IOException("Failed to write file");
  }

  /**
   Validate if the given keystore format is supported and loads a keystore to check
   for the format and validity of the password.

   @param storePath path to keystore file.
   @param password password from keystore
   @param keyStoreType type of keystore
   @throws KeyStoreException if specified keyStoreType is not supported.
   @throws IOException if there is an I/O or format problem with the keystore data or
   if the given password was incorrect.
   @throws CertificateException if any of the certificates in the keystore could not be loaded.
   @throws NoSuchAlgorithmException if the algorithm used to check the integrity of
   the keystore cannot be found.
   */
  private static void validateCertificate(String storePath, String password, String keyStoreType)
      throws KeyStoreException, IOException, CertificateException, NoSuchAlgorithmException {
    KeyStore keystore = KeyStore.getInstance(keyStoreType);
    keystore.load(new FileInputStream(storePath), password.toCharArray());
  }

  private static void logConfig(Map<String, Object> config) {
    StringBuilder builder = new StringBuilder();
    config.forEach((key, value) -> {
      builder.append(String.format("\t%s: %s\n", key, value));
    });
    LOG.info("Current config:\n" + builder);
  }

  private static boolean isLocalFileNotExist(String outputFilePath) {
    File outputFile = new File(outputFilePath);
    if (outputFile.exists()) {
      LOG.info("Certificates file {} already exists. Certificate content size: {}", outputFile, outputFile.length());
    } else {
      LOG.info("Certificate doesn't exist on local fs.");
    }
    return !outputFile.exists();
  }
}
