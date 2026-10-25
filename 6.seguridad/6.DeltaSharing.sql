-- Databricks notebook source
CREATE SHARE GOLDEN_SHARE

-- COMMAND ----------

ALTER SHARE GOLDEN_SHARE
ADD TABLE s3examenfinal.golden.golden
WITH HISTORY

-- COMMAND ----------

CREATE RECIPIENT ExternalCompanys

-- COMMAND ----------

GRANT SELECT
ON SHARE GOLDEN_SHARE
TO RECIPIENT ExternalCompanys