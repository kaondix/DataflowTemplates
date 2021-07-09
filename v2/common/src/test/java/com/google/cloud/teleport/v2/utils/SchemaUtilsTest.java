/*
 * Copyright (C) 2019 Google Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package com.google.cloud.teleport.v2.utils;

import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertEquals;

import com.google.api.services.bigquery.model.TableSchema;
import com.google.common.io.Resources;
import com.google.gson.Gson;
import com.google.protobuf.DescriptorProtos.FileDescriptorSet;
import com.google.protobuf.Descriptors.Descriptor;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.apache.avro.Schema;
import org.apache.beam.sdk.extensions.protobuf.ProtoDomain;
import org.apache.beam.sdk.testing.TestPipeline;
import org.junit.Rule;
import org.junit.Test;

/** Test cases for the {@link SchemaUtils} class. */
public class SchemaUtilsTest {
  @Rule public final transient TestPipeline pipeline = TestPipeline.create();

  private static final String RESOURCES_DIR = "SchemaUtilsTest/";

  private static final String AVRO_SCHEMA_FILE_PATH =
      Resources.getResource(RESOURCES_DIR + "avro_schema.json").getPath();
  private static final String PROTO_AS_BQ_SCHEMA_PATH =
      Resources.getResource(RESOURCES_DIR + "proto_definition_as_bq_schema.json").getPath();
  // This file, along with all the necessary protos, is generated by Maven.
  private static final String PROTO_SCHEMA_FILE_PATH =
      Paths.get("target", "generated-test-sources", "protobuf", "schema", "schema.pb").toString();

  private static final String PROTO_MESSAGE_NAME =
      "com.google.cloud.teleport.v2.proto.testing.MyMessage";
  private static final String PROTO_MESSAGE_INVALID_FOR_BQ =
      "com.google.cloud.teleport.v2.proto.testing.CircularlyReferencedMessage";

  @Test
  public void testGetGcsFileAsBytes() throws IOException {
    assertArrayEquals(
        getFileBytes(PROTO_SCHEMA_FILE_PATH),
        SchemaUtils.getGcsFileAsBytes(PROTO_SCHEMA_FILE_PATH));
  }

  /**
   * Test whether {@link SchemaUtils#getGcsFileAsString(String)} reads a file correctly as a String.
   */
  @Test
  public void testGetGcsFileAsString() {
    String expectedContent =
        "{\n"
            + "  \"type\" : \"record\",\n"
            + "  \"name\" : \"test_file\",\n"
            + "  \"namespace\" : \"com.test\",\n"
            + "  \"fields\" : [\n"
            + "    {\n"
            + "      \"name\": \"id\",\n"
            + "      \"type\": \"string\"\n"
            + "    },\n"
            + "    {\n"
            + "      \"name\": \"price\",\n"
            + "      \"type\": \"double\"\n"
            + "    }\n"
            + "  ]\n"
            + "}\n";
    String actualContent = SchemaUtils.getGcsFileAsString(AVRO_SCHEMA_FILE_PATH);

    assertEquals(expectedContent, actualContent);
  }

  /**
   * Test whether {@link SchemaUtils#getAvroSchema(String)} reads an Avro schema correctly and
   * returns a {@link Schema} object.
   */
  @Test
  public void testGetAvroSchema() {
    String avroSchema =
        "{\n"
            + "  \"type\" : \"record\",\n"
            + "  \"name\" : \"test_file\",\n"
            + "  \"namespace\" : \"com.test\",\n"
            + "  \"fields\" : [\n"
            + "    {\n"
            + "      \"name\": \"id\",\n"
            + "      \"type\": \"string\"\n"
            + "    },\n"
            + "    {\n"
            + "      \"name\": \"price\",\n"
            + "      \"type\": \"double\"\n"
            + "    }\n"
            + "  ]\n"
            + "}";
    Schema expectedSchema = new Schema.Parser().parse(avroSchema);
    Schema actualSchema = SchemaUtils.getAvroSchema(AVRO_SCHEMA_FILE_PATH);

    assertEquals(expectedSchema, actualSchema);
  }

  @Test
  public void testGetProtoDomain() throws IOException {
    ProtoDomain expected =
        ProtoDomain.buildFrom(FileDescriptorSet.parseFrom(getFileBytes(PROTO_SCHEMA_FILE_PATH)));
    ProtoDomain actual = SchemaUtils.getProtoDomain(PROTO_SCHEMA_FILE_PATH);
    assertEquals(expected, actual);
  }

  @Test(expected = IllegalArgumentException.class)
  public void testGetProtoDomainInvalidFile() {
    SchemaUtils.getProtoDomain(AVRO_SCHEMA_FILE_PATH);
  }

  @Test
  public void testGetBigQuerySchema() throws IOException {
    Descriptor descriptor =
        SchemaUtils.getProtoDomain(PROTO_SCHEMA_FILE_PATH).getDescriptor(PROTO_MESSAGE_NAME);
    TableSchema actual = SchemaUtils.createBigQuerySchema(descriptor);
    assertEquals(getProtoTableSchema(), actual);
  }

  @Test(expected = IllegalArgumentException.class)
  public void testGetBigQuerySchemaWithTooManyNestingLevels() {
    SchemaUtils.createBigQuerySchema(
        SchemaUtils.getProtoDomain(PROTO_SCHEMA_FILE_PATH)
            .getDescriptor(PROTO_MESSAGE_INVALID_FOR_BQ));
  }

  /** Convenience method for getting raw bytes from a file. */
  private static byte[] getFileBytes(String filePath) throws IOException {
    return Files.readAllBytes(Paths.get(filePath));
  }

  /** Creates the {@link TableSchema} that meets MyMessage in proto_definition.proto. */
  private TableSchema getProtoTableSchema() throws IOException {
    String asJson = new String(getFileBytes(PROTO_AS_BQ_SCHEMA_PATH), StandardCharsets.UTF_8);
    return new Gson().fromJson(asJson, TableSchema.class);
  }
}
