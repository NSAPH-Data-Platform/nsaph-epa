#!/usr/bin/env cwl-runner
### Full Medicaid Processing Pipeline

cwlVersion: v1.2
class: Workflow

requirements:
  SubworkflowFeatureRequirement: {}
  StepInputExpressionRequirement: {}
  InlineJavascriptRequirement: {}

doc: |
  This workflow downloads AirNow data from the government
  servers, introspects it to infer the database schema
  and ingests the data into the database

inputs:
  proxy:
    type: string?
    default: ""
    doc: HTTP/HTTPS Proxy if required
  api-key:
    type: string
    doc: API key for AirNow
  database:
    type: File
    doc: Path to database connection file, usually database.ini
  connection_name:
    type: string
    doc: The name of the section in the database.ini file
  from:
    type: string
    doc: Start date for downolading, in YYYY-MM-DD format
  to:
    type: string
    doc: End date for downolading, in YYYY-MM-DD format
  parameter_code:
    type: string
    doc: |
      Parameter code. Either a numeric code (e.g. 88101, 44201)
      or symbolic name (e.g. PM25, NO2).
      See more: [AQS Code List](https://www.epa.gov/aqs/aqs-code-list)
  table:
    doc: Name of the table to be created in the database
    type: string

steps:
  setup:
    run: setup_airnow.cwl
    in:
      api-key: api-key
    out:
      - cfg
      - shapes
      - log

  download:
    run: download_airnow.cwl
    in:
      api-key: api-key
      cfg: setup/cfg
      shapes: setup/shapes
      from: from
      to: to
      table: table
      parameter_code: parameter_code
      proxy: proxy
    out: [log, data]

  introspect:
    run: introspect.cwl
    in:
      depends_on: download/log
      input: download/data
      table: table
      output:
        valueFrom: epa.yaml
    out: [log, model]

  ingest:
    run: ingest.cwl
    doc: Uploads data into the database
    in:
      registry: introspect/model
      table: table
      input: download/data
      database: database
      connection_name: connection_name
    out: [log]

  index:
    run: index.cwl
    in:
      depends_on: ingest/log
      registry: introspect/model
      domain:
        valueFrom: "epa"
      table: table
      database: database
      connection_name: connection_name
    out: [log]


outputs:
  setup_log:
    type: File
    outputSource: setup/log
  cfg:
    type: File
    outputSource: setup/cfg
#  shape_dir:
#    type: Directory
#    outputSource: setup/shape_dir
#  shapes:
#    type: File[]
#    outputSource: setup/shapes
  download_log:
    type: File
    outputSource: download/log
  ingest_log:
    type: File
    outputSource: ingest/log
  index_log:
    type: File
    outputSource: index/log
  download_data:
    type: File
    outputSource: download/data
  model:
    type: File
    outputSource: introspect/model
