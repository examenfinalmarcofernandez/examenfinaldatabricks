-- Databricks notebook source
-- MAGIC %python
-- MAGIC dbutils.widgets.removeAll()

-- COMMAND ----------

CREATE WIDGET TEXT catalogo default "s3examenfinal";

-- COMMAND ----------

SELECT :catalogo AS CATALOGO

-- COMMAND ----------

DROP CATALOG IF EXISTS s3examenfinal CASCADE;

-- COMMAND ----------

-- DBTITLE 1,Untitled
--Crear container metastore previamente en el datalake de la celda 2
CREATE CATALOG IF NOT EXISTS s3examenfinal
MANAGED LOCATION 's3://${storageName}/s3examenfinal'
COMMENT 'Catalogo para almacenar las tablas metastore;'

-- COMMAND ----------

CREATE SCHEMA IF NOT EXISTS $catalogo.raw;
CREATE SCHEMA IF NOT EXISTS $catalogo.bronze;
CREATE SCHEMA IF NOT EXISTS $catalogo.silver;
CREATE SCHEMA IF NOT EXISTS $catalogo.golden;
CREATE SCHEMA IF NOT EXISTS $catalogo.exploratory;

CREATE VOLUME IF NOT EXISTS $catalogo.raw.datasets;

-- COMMAND ----------

CREATE TABLE $catalogo.bronze.placement (
  percanvas STRING,
  codas400 STRING,
  carrera STRING,
  ciclo STRING,
  placement STRING,
  fechaplacement STRING,
  tipoBD STRING)
USING DELTA
LOCATION 's3://s3examenfinal/s3examenfinal/bronze/placement/'

-- COMMAND ----------

CREATE TABLE $catalogo.bronze.matriculados (
  periodo STRING,
  codas400 STRING,
  flag_retiro STRING,
  rango_edad_ingreso STRING,
  rango_edad_matricula STRING)
USING DELTA
LOCATION 's3://s3examenfinal/s3examenfinal/bronze/matriculados/'

-- COMMAND ----------

CREATE TABLE $catalogo.silver.transformed (
  percanvas STRING,
  codas400 STRING,
  carrera STRING,
  ciclo STRING,
  placement STRING,
  fechaplacement STRING,
  tipoBD STRING,
  flag_retiro STRING,
  rango_edad_ingreso STRING,
  rango_edad_matricula STRING,
  tipo_carrera STRING,
  tipo_ciclo STRING)
USING DELTA
LOCATION 's3://s3examenfinal/s3examenfinal/silver/transformed/'

-- COMMAND ----------

CREATE TABLE $catalogo.golden.golden (
  percanvas STRING,
  conteo LONG,
  carrera STRING,
  max_ciclo STRING,
  min_ciclo STRING,
  flag_retiro STRING,
  rango_edad_ingreso STRING,
  rango_edad_matricula STRING,
  tipo_carrera STRING,
  tipo_ciclo STRING)
USING DELTA
LOCATION 's3://s3examenfinal/s3examenfinal/golden/golden/'