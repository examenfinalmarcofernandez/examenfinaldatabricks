-- Databricks notebook source
-- Acceso al catálogo
GRANT USE CATALOG
ON CATALOG s3examenfinal
TO `ahuaccachi28@gmail.com`;

-- BRONZE
GRANT USE SCHEMA
ON SCHEMA s3examenfinal.bronze
TO `ahuaccachi28@gmail.com`;

GRANT CREATE TABLE
ON SCHEMA s3examenfinal.bronze
TO `ahuaccachi28@gmail.com`;

-- SILVER
GRANT USE SCHEMA
ON SCHEMA s3examenfinal.silver
TO `ahuaccachi28@gmail.com`;

GRANT CREATE TABLE
ON SCHEMA s3examenfinal.silver
TO `ahuaccachi28@gmail.com`;

-- GOLDEN
GRANT USE SCHEMA
ON SCHEMA s3examenfinal.golden
TO `ahuaccachi28@gmail.com`;

GRANT CREATE TABLE
ON SCHEMA s3examenfinal.golden
TO `ahuaccachi28@gmail.com`;

-- COMMAND ----------

GRANT SELECT, MODIFY
ON TABLE s3examenfinal.golden.golden
TO `ahuaccachi28@gmail.com`;