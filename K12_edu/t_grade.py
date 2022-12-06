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
df1.createTempView("g_price")
price_df = spark.sql("select course,avg(price)as price,count(course)as count from g_price group by course")
price_df = price_df.withColumn("id", monotonically_increasing_id())
price_df.show()

conn_param = {}
conn_param["user"] = MYSQL_USER
conn_param["password"] = MYSQL_PWD
conn_param["driver"] = MYSQL_DRIVER

price_df.write.jdbc(MYSQL_CONN, "g_price", "overwrite", conn_param)

print("执行完毕")

# df2 = spark.read.load(local_file, format="csv", sep=",", inferSchema="true", header="true", encoding="gbk")
# df2.createTempView("t_grade")
# grade_df = spark.sql("select grade,AVG(price) as price,count(grade) as count from t_grade group by grade order by grade")
# grade_df = grade_df.withColumn("id", monotonically_increasing_id())
# grade_df.show()
# grade_df.write.jdbc(MYSQL_CONN, "t_grade", "overwrite", conn_param)









