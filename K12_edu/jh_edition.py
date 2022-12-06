from pyspark import Row
from pyspark.sql import SparkSession
from pyspark.sql.functions import monotonically_increasing_id

from mysql_config import MYSQL_CONN, MYSQL_DRIVER, MYSQL_PWD, MYSQL_USER

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

sc = spark.sparkContext
path ="E:\PyCharm 2019.1.3\workplace\spiders\myspider\K12_edu_data\jh_high_school.txt,E:\PyCharm 2019.1.3\workplace\spiders\myspider\K12_edu_data\jh_junior_high_school.txt,E:\PyCharm 2019.1.3\workplace\spiders\myspider\K12_edu_data\jh_junior_high_school.txt"
edition_rdd = sc.textFile(path)

def group(item):
    tmp_list = item.split(",")
    edition = tmp_list[3]
    return edition, 1

edition_pair_rdd = edition_rdd.map(lambda x: group(x)).\
    reduceByKey(lambda x, y: x+y).\
    map(lambda x: Row(edition=x[0], count=x[1]))

df = spark.createDataFrame(edition_pair_rdd)
df = df.withColumn("id", monotonically_increasing_id())

conn_param = {}
conn_param["user"] = MYSQL_USER
conn_param["password"] = MYSQL_PWD
conn_param["driver"] = MYSQL_DRIVER
df.write.jdbc(MYSQL_CONN, "jh_edition", "overwrite", conn_param)
print("执行完毕")
