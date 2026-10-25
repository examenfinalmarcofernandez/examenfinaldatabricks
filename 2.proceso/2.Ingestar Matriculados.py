dbutils.widgets.removeAll()

from pyspark.sql.functions import *
from pyspark.sql.types import *

dbutils.widgets.text("container", "s3examenfinal")
dbutils.widgets.text("catalogo", "s3examenfinal")
dbutils.widgets.text("esquema", "bronze")

container = dbutils.widgets.get("container")
catalogo = dbutils.widgets.get("catalogo")
esquema = dbutils.widgets.get("esquema")

ruta = f"s3://s3examenfinal/data/matriculados.csv"

matriculados_schema = StructType(fields=[StructField("percanvas", StringType(), False),
                                     StructField("codas400", StringType(), True),
                                     StructField("flag_retiro", StringType(), True),
                                     StructField("rango_edad_ingreso", StringType(), True),
                                     StructField("rango_edad_matricula", DateType(), True)
])

df_matriculados = (
    spark.read
    .option("header", True)
    .option("matriculados_schema", True)
    .option("sep", ";")
    .csv(ruta)
)

df_matriculados.write.mode("overwrite").insertInto(f"{catalogo}.{esquema}.matriculados")