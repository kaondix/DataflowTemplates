/*
 * Copyright (C) 2024 Google LLC
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
package com.google.cloud.teleport.v2.templates;

import com.google.cloud.teleport.v2.source.reader.Reader;
import com.google.cloud.teleport.v2.source.reader.io.schema.SourceSchema;
import com.google.cloud.teleport.v2.source.reader.io.schema.SourceSchemaReference;
import com.google.cloud.teleport.v2.source.reader.io.transform.ReaderTransform;

/** DELETE THIS CLASS ONCE READER IS INCORPORATED INTO MAIN PIPELINE. */
public class FakeReader2 implements Reader {
  private static final String dbName = "fakeDb";

  private SourceSchemaReference sourceSchemaReference;
  private ReaderTransformTestUtils2 readerTransformTestUtils;
  private long rowCountPerTable;
  private long tableCount;

  FakeReader2(int rowCount, int tableCount) {
    this.rowCountPerTable = rowCount;
    this.tableCount = tableCount;
    this.sourceSchemaReference = SourceSchemaReference.builder().setDbName(this.dbName).build();
    this.readerTransformTestUtils =
        new ReaderTransformTestUtils2(
            this.rowCountPerTable, this.tableCount, this.sourceSchemaReference);
  }

  @Override
  public SourceSchema getSourceSchema() {
    var builder = SourceSchema.builder().setSchemaReference(this.sourceSchemaReference);
    this.readerTransformTestUtils
        .getTestTableSchemas()
        .forEach(tableSchema -> builder.addTableSchema(tableSchema));
    return builder.build();
  }

  @Override
  public ReaderTransform getReaderTransform() {
    return this.readerTransformTestUtils.getTestReaderTransform();
  }
}
