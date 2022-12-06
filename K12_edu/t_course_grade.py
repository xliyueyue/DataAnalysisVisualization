from pyspark.sql import SparkSession
from pyspark.sql.functions import monotonically_increasing_id
from mysql_config import MYSQL_CONN, MYSQL_DRIVER, MYSQL_PWD, MYSQL_USER

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
sc = spark.sparkContext

local_file = r"E:\PyCharm 2019.1.3\workplace\spiders\myspider\K12_edu_data\course_grade_price.csv"
df1 = spark.read.load(local_file, format="csv", sep=",", inferSchema="true", header="true", encoding="gbk")
df2 = spark.read.load(local_file, format="csv", sep=",", inferSchema="true", header="true", encoding="gbk")

df1.createTempView("t_course")
df2.createTempView("t_grade")

course_df = spark.sql("select course,avg(price)as price,count(course)as count from t_course group by course order by course")
grade_df = spark.sql("select grade,AVG(price) as price,count(grade) as count from t_grade group by grade order by grade")

course_df = course_df.withColumn("id", monotonically_increasing_id())
grade_df = grade_df.withColumn("id", monotonically_increasing_id())

course_df.show()
grade_df.show()

conn_param = {}
conn_param["user"] = MYSQL_USER
conn_param["password"] = MYSQL_PWD
conn_param["driver"] = MYSQL_DRIVER

course_df.write.jdbc(MYSQL_CONN, "t_course", "overwrite", conn_param)
grade_df.write.jdbc(MYSQL_CONN, "t_grade", "overwrite", conn_param)
print("执行完毕")
