/*
 * Copyright (C) 2022 Google LLC
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not
 * use this file except in compliance with the License. You may obtain a copy of
 * the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 * License for the specific language governing permissions and limitations under
 * the License.
 */
package com.google.cloud.teleport.it.common.utils;

import com.google.common.base.CaseFormat;
import java.time.Duration;
import java.time.Instant;
import java.time.ZoneId;
import java.time.format.DateTimeFormatter;
import java.util.function.Supplier;
import org.apache.beam.sdk.PipelineResult;
import org.apache.beam.sdk.PipelineRunner;
import org.apache.beam.sdk.options.PipelineOptions;
import org.apache.beam.sdk.options.PipelineOptionsFactory;

/** Utilities to make working with Dataflow easier. */
public class PipelineUtils {

  private PipelineUtils() {}

  /**
   * Waits for a specified pipeline to reach a particular state, up to a specified timeout.
   *
   * @param pipeline the PipelineResult object to monitor
   * @param expectedState the pipeline state to wait for
   * @param timeoutMillis the maximum amount of time to wait for the expected state, in milliseconds
   * @return true if the pipeline reaches the expected state within the timeout, false otherwise
   * @throws InterruptedException if the thread is interrupted while waiting
   */
  public static boolean waitUntilState(
      PipelineResult pipeline, PipelineResult.State expectedState, Long timeoutMillis)
      throws InterruptedException {
    return waitUntil(pipeline, () -> pipeline.getState().equals(expectedState), timeoutMillis);
  }

  /**
   * Waits until a specified condition is true, up to a specified timeout.
   *
   * @param pipeline the PipelineResult object to monitor
   * @param lambda a Supplier that returns a boolean indicating whether the condition is true
   * @param timeoutMillis the maximum amount of time to wait for the condition to be true, in
   *     milliseconds
   * @return true if the condition becomes true within the timeout, false otherwise
   * @throws InterruptedException if the thread is interrupted while waiting
   */
  public static boolean waitUntil(
      PipelineResult pipeline, Supplier<Boolean> lambda, Long timeoutMillis)
      throws InterruptedException {
    Instant start = Instant.now();
    while (true) {
      Thread.sleep(5_000);
      if (lambda.get()) {
        return true;
      }
      if (Duration.between(start, Instant.now()).compareTo(Duration.ofMillis(timeoutMillis)) > 0) {
        return false;
      }
    }
  }

  /**
   * Creates a job name.
   *
   * <p>If there are uppercase characters in {@code prefix}, then this will convert them into a dash
   * followed by the lowercase equivalent of that letter.
   *
   * <p>The job name will normally be unique, but this is not guaranteed if multiple jobs with the
   * same prefix are requested in a short period of time.
   *
   * @param prefix a prefix for the job
   * @return the prefix plus some way of identifying it separate from other jobs with the same
   *     prefix
   */
  public static String createJobName(String prefix) {
    String convertedPrefix =
        CaseFormat.UPPER_CAMEL.converterTo(CaseFormat.LOWER_HYPHEN).convert(prefix);
    String formattedTimestamp =
        DateTimeFormatter.ofPattern("yyyyMMddHHmmssSSS")
            .withZone(ZoneId.of("UTC"))
            .format(Instant.now());
    return String.format("%s-%s", convertedPrefix, formattedTimestamp);
  }

  /*
   * Get runner class from name.
   *
   * <p>This avoids to have all runner dependency (e.g. Dataflow, Flink, etc) explicitly in specific
   * test.
   *
   * @param runner The runner name string
   * @return runner class
   */
  public static Class<? extends PipelineRunner<?>> getRunnerClass(String runner) {
    PipelineOptions options = PipelineOptionsFactory.fromArgs("--runner=" + runner).create();
    return options.getRunner();
  }
}
