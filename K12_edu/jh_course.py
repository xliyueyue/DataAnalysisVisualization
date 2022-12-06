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
path ="E:\PyCharm 2019.1.3\workplace\spiders\myspider\K12_edu_data\jh_primary_school.txt,E:\PyCharm 2019.1.3\workplace\spiders\myspider\K12_edu_data\jh_high_school.txt,E:\PyCharm 2019.1.3\workplace\spiders\myspider\K12_edu_data\jh_junior_high_school.txt"
course_rdd = sc.textFile(path)

def group(item):
    tmp_list = item.split(",")
    coursename = tmp_list[0]
    price = tmp_list[2]
    if price == "None":
        return coursename, (1, 0)
    else:
        return coursename, (1, int(price))


course_pair_rdd = course_rdd.map(lambda x: group(x)).\
    reduceByKey(lambda x, y: (x[0]+y[0], x[1]+y[1])).\
    map(lambda x: Row(courcename=x[0], count=x[1][0], price=x[1][1]/x[1][0]))

df = spark.createDataFrame(course_pair_rdd)
df = df.withColumn("id", monotonically_increasing_id())

conn_param = {}
conn_param["user"] = MYSQL_USER
conn_param["password"] = MYSQL_PWD
conn_param["driver"] = MYSQL_DRIVER
df.write.jdbc(MYSQL_CONN, "jh_course", "overwrite", conn_param)
print("执行完毕")

