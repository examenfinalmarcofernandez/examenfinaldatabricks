dbutils.widgets.removeAll()

from pyspark.sql.functions import *
from pyspark.sql.types import *

dbutils.widgets.text("container", "s3examenfinal")
dbutils.widgets.text("catalogo", "s3examenfinal")
dbutils.widgets.text("esquema", "bronze")

container = dbutils.widgets.get("container")
catalogo = dbutils.widgets.get("catalogo")
esquema = dbutils.widgets.get("esquema")

ruta = f"s3://s3examenfinal/data/placement.csv"

placement_schema = StructType(fields=[StructField("percanvas", StringType(), False),
                                     StructField("codas400", StringType(), True),
                                     StructField("carrera", StringType(), True),
                                     StructField("ciclo", StringType(), True),
                                     StructField("placement", DateType(), True),
                                     StructField("fechaplacement", DateType(), True),
                                     StructField("tipoBD", DoubleType(), True)
])

df_placement = (
    spark.read
    .option("header", True)
    .option("placement_schema", True)
    .option("sep", ";")
    .csv(ruta)
)

df_placement.write.mode("overwrite").insertInto(f"{catalogo}.{esquema}.placement")