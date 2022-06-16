import sys
from pyspark.context import SparkContext
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

a ="Acompanhe"
b ="o" 
c = "canal"
d = "da"
e = "Stack"
f = "Tecnologias"
g = "no"
h = "Youtube"

a1=('Este',a)
b1=('é',b)
c1=('um',c)
d1=('exemplo',d)
e1=('de', e)
f1=('ultilização',f)
g1=('do', g)
h1=('Spark',h)

data=[a1, b1, c1, d1, e1, f1, g1, h1]
teste1 = spark.createDataFrame(data, ["Mensagem", "Lembrete"])
teste1.show()

sample=teste1.sample(0.6, seed=1234)
sample.show()
