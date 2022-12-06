from pyspark import Row
from pyspark.sql import SparkSession
from pyspark.sql.functions import monotonically_increasing_id

from mysql_config import MYSQL_CONN, MYSQL_DRIVER, MYSQL_PWD, MYSQL_USER

spark = SparkSession\
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

sc = spark.sparkContext
path = "E:\PyCharm 2019.1.3\workplace\spiders\myspider\K12_edu_data\\xdf_high_school.txt,E:\PyCharm 2019.1.3\workplace\spiders\myspider\K12_edu_data\\xdf_primary_school.txt"
type_rdd = sc.textFile(path)

def group(item):
    tmp_list = item.split(",")
    type = tmp_list[3]
    price = int(tmp_list[2])
    period = int(tmp_list[4])
    per_price = price/period
    return type, (1, per_price)

type_pair_rdd = type_rdd.map(lambda x: group(x)).\
    reduceByKey(lambda x, y: (x[0]+y[0], x[1]+y[1])).\
    map(lambda x: Row(type=x[0], count=x[1][0], per_price=x[1][1]/x[1][0]))

df = spark.createDataFrame(type_pair_rdd)
df = df.withColumn("id", monotonically_increasing_id())

conn_param = {}
conn_param["user"] = MYSQL_USER
conn_param["password"] = MYSQL_PWD
conn_param["driver"] = MYSQL_DRIVER
df.write.jdbc(MYSQL_CONN, "xdf_type", "overwrite", conn_param)
print("执行完毕")

