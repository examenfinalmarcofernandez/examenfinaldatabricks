dbutils.widgets.removeAll()

from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql import functions as F

dbutils.widgets.text("catalogo", "s3examenfinal")
dbutils.widgets.text("esquema_source", "bronze")
dbutils.widgets.text("esquema_sink", "silver")

catalogo = dbutils.widgets.get("catalogo")
esquema_source = dbutils.widgets.get("esquema_source")
esquema_sink = dbutils.widgets.get("esquema_sink")

df_placement = spark.table(f"{catalogo}.{esquema_source}.placement")
df_matriculados = spark.table(f"{catalogo}.{esquema_source}.matriculados")

df_placement = df_placement.withColumn(
    "tipo_carrera",
    when(col("carrera").contains("Ing"), "ingeniería")
    .when(col("carrera").contains("Adm"), "administración")
    .otherwise("otros")
)

df_placement = df_placement.withColumn(
    "tipo_ciclo",
    when(col("ciclo") <= 5, "cachimbos")
    .otherwise("adultos")
)

df_joined = df_placement.alias("x").join(df_matriculados.alias("y"), col("x.codas400") == col("y.codas400"), "inner").select(
        col("x.percanvas").alias("perCanvas"),
        col("x.codas400").alias("codas400"),
        col("x.carrera").alias("carrera"),
        col("x.ciclo").alias("Ciclo"),
        col("x.placement").alias("placement"),
        col("x.fechaplacement").alias("fechaPlacement"),
        col("x.tipoBD").alias("tipoBD"),
        col("y.flag_retiro").alias("flag_retiro"),
        col("y.rango_edad_ingreso").alias("rango_edad_ingreso"),
        col("y.rango_edad_matricula").alias("rango_edad_matricula"),
        col("x.tipo_carrera").alias("tipo_carrera"),
        col("x.tipo_ciclo").alias("tipo_ciclo")
    )

df_joined.write.mode("overwrite").insertInto(f"{catalogo}.{esquema_sink}.transformed")