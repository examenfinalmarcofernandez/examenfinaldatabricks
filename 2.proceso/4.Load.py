dbutils.widgets.removeAll()

from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql import functions as F

dbutils.widgets.text("catalogo", "s3examenfinal")
dbutils.widgets.text("esquema_source", "silver")
dbutils.widgets.text("esquema_sink", "golden")

catalogo = dbutils.widgets.get("catalogo")
esquema_source = dbutils.widgets.get("esquema_source")
esquema_sink = dbutils.widgets.get("esquema_sink")

df_transformed = spark.table(f"{catalogo}.{esquema_source}.transformed")

df_transformed = (
    df_transformed
    .groupBy(
        col("percanvas"),
        col("carrera"),
        col("tipo_ciclo"),
        col("flag_retiro"),
        col("rango_edad_ingreso"),
        col("rango_edad_matricula"),
        col("tipo_carrera")
    )
    .agg(
        count(col("codas400")).alias("conteo"),
        max(col("ciclo")).alias("max_ciclo"),
        min(col("ciclo")).alias("min_ciclo")
    )
    .orderBy(
        col("percanvas"),
        col("carrera"),
        col("tipo_ciclo"),
        col("flag_retiro"),
        col("rango_edad_ingreso"),
        col("rango_edad_matricula"),
        col("tipo_carrera").desc()
    )
)

df_transformed = df_transformed.select(
    "percanvas",
    "conteo",
    "carrera",
    "max_ciclo",
    "min_ciclo",
    "flag_retiro",
    "rango_edad_ingreso",
    "rango_edad_matricula",
    "tipo_carrera",
    "tipo_ciclo"
)

df_transformed.write.mode("overwrite").insertInto(f"{catalogo}.{esquema_sink}.golden")