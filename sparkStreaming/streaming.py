# Spark Stateful Streaming with Python
# Takes text from input network socket and prints the accumulated count for each word

# To Run this:
# 1. spark-submit streaming.py localhost 9999 
# 2. nc -nlk 9999 (type messages) [new terminal]


from pyspark import SparkContext
from pyspark.streaming import StreamingContext

# define the update function
def updateTotalCount(currentCount, countState):
    if countState is None:
       countState = 0
    return sum(currentCount, countState)

# create spark and streaming contexts
sc = SparkContext("local[*]", "StreamWordCounter")
ssc = StreamingContext(sc, 10)

# defining the checkpoint directory
ssc.checkpoint("/tmp")

# read text from input socket
text = ssc.socketTextStream("localhost", 9999)

# count words
countStream = text.flatMap(lambda line: line.split(" "))\
                   .map(lambda word: (word, 1))\
                   .reduceByKey(lambda a, b: a + b)

# update total count for each key
totalCounts = countStream.updateStateByKey(updateTotalCount)

# print the resulting tuples
totalCounts.pprint()

# start the streaming context
ssc.start()
ssc.awaitTermination()
