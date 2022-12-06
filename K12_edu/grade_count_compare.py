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

# 使用spark算子
# path1 =r"E:\PyCharm 2019.1.3\workplace\spiders\myspider\K12_edu_data\jh_primary_school.txt,E:\PyCharm 2019.1.3\workplace\spiders\myspider\K12_edu_data\jh_high_school.txt,E:\PyCharm 2019.1.3\workplace\spiders\myspider\K12_edu_data\jh_junior_high_school.txt"
# path2 =r"E:\PyCharm 2019.1.3\workplace\spiders\myspider\K12_edu_data\\xdf_high_school.txt," \
#       "E:\PyCharm 2019.1.3\workplace\spiders\myspider\K12_edu_data\\xdf_primary_school.txt"
# jh_rdd = sc.textFile(path1)
# xdf_rdd = sc.textFile(path2)
#
# def group(item):
#     tmp_list = item.split(",")
#     grade = tmp_list[1]
#     return grade, (1, 0)
#
# jh_pair_rdd = jh_rdd.map(lambda x: group(x)).reduceByKey(lambda x, y: ( x[0]+y[0], "jh"))
# xdf_pair_rdd = xdf_rdd.map(lambda x: group(x)).reduceByKey(lambda x, y: ( x[0]+y[0], "xdf"))
# union_rdd = jh_pair_rdd.union(xdf_pair_rdd).map(lambda x: Row(grade=x[0], count=x[1][0], data_type=x[1][1]))
#
# df = spark.createDataFrame(union_rdd)
# df = df.withColumn("id", monotonically_increasing_id())

local_file1 = r"E:\PyCharm 2019.1.3\workplace\spiders\myspider\K12_edu_data\jh.csv"
local_file2 = r"E:\PyCharm 2019.1.3\workplace\spiders\myspider\K12_edu_data\xdf.csv"

df1 = spark.read.load(local_file1, format="csv", sep=",", inferSchema="true", header="true", encoding="gbk")
df2 = spark.read.load(local_file2, format="csv", sep=",", inferSchema="true", header="true", encoding="gbk")

df1.createTempView("jh")
df2.createTempView("xdf")

jh_df = spark.sql("select course,avg(price)as price,count(course)as count from jh group by course order by case course "
                  "when '语文' then 1 when '数学' then 2 when '英语' then 3 "
                  "when '物理' then 4 when '化学' then 5 when '生物' then 6 "
                  "when '联报' then 7 end")
xdf_df = spark.sql("select course,AVG(price)as price,count(course) as count from xdf group by course order by case "
                   "when course='语文' then 1 when course='数学' then 2 when course='英语' then 3 "
                   "when course='物理' then 4 when course='化学' then 5 when course='生物' then 6 "
                   "when course='联报' then 7 when course='历史' then 8 when course='政治' then 9 "
                   "when course='地理' then 10 when course='科学' then 11 end")

jh_df = jh_df.withColumn("id", monotonically_increasing_id())
xdf_df = xdf_df.withColumn("id", monotonically_increasing_id())

jh_df.show()
xdf_df.show()

conn_param = {}
conn_param["user"] = MYSQL_USER
conn_param["password"] = MYSQL_PWD
conn_param["driver"] = MYSQL_DRIVER

jh_df.write.jdbc(MYSQL_CONN, "jh", "overwrite", conn_param)
xdf_df.write.jdbc(MYSQL_CONN, "xdf", "overwrite", conn_param)
print("执行完毕")
