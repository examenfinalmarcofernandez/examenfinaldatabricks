
-- =====================================================
-- PROYECTO: Academic Lakehouse Analytics
-- REVERSION DE TABLAS DEL ETL
-- AWS DATABRICKS - UNITY CATALOG
-- =====================================================

-- ATENCION:
-- Script destructivo. Ejecutar solamente cuando
-- se requiera reconstruir el proyecto.
-- No ejecutar durante la entrega.

DROP TABLE IF EXISTS workspace.bronze.PLACEMENT;
DROP TABLE IF EXISTS workspace.bronze.MATRICULADOS;
