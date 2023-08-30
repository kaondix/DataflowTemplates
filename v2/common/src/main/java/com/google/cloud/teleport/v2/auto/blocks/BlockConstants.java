/*
 * Copyright (C) 2023 Google LLC
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
package com.google.cloud.teleport.v2.auto.blocks;

import com.google.api.services.bigquery.model.TableRow;
import com.google.cloud.teleport.v2.values.FailsafeElement;
import org.apache.beam.sdk.io.gcp.pubsub.PubsubMessage;
import org.apache.beam.sdk.values.TupleTag;

public final class BlockConstants {

  /** The default suffix for error tables if dead letter table is not specified. */
  public static final String DEFAULT_DEADLETTER_TABLE_SUFFIX = "_error_records";

  public static final TupleTag<FailsafeElement<PubsubMessage, String>> ERROR_TAG_PS =
      new TupleTag<FailsafeElement<PubsubMessage, String>>();

  public static final TupleTag<FailsafeElement<String, String>> ERROR_TAG_STR =
      new TupleTag<FailsafeElement<String, String>>();

  public static final TupleTag<TableRow> OUTPUT_TAG = new TupleTag<TableRow>();
}
