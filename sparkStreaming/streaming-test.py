# Spark Stateful Streaming with Python
# Takes text from input network socket and prints the filter word as scala

# To Run:
# 1. spark-submit streaming-test.py localhost 9999 
# 2. nc -nlk 9999 (type messages) [new terminal]

from pyspark import SparkContext
from pyspark.streaming import StreamingContext


# create spark and streaming contexts
sc = SparkContext("local[*]", "StreamWordCounter")
ssc = StreamingContext(sc, 10)

# defining the checkpoint directory
ssc.checkpoint("/tmp")

# read text from input socket
text = ssc.socketTextStream("localhost", 9999)

# filter word as scala
filterStream = text.filter(lambda line: "scala" in line)


# print the resulting tuples
filterStream.pprint()

# start the streaming context
ssc.start()
ssc.awaitTermination()
