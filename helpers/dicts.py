from collections import defaultdict

"""defauldict example

defaultdict - dict subclass that calls a factory function to supply missing values

"""

duplicated_interests = [
    "Hadoop", "Big Data", "HBase", "Java", "Storm", "Cassandra",
    "Hadoop", "HBase", "Java", "Spark", "Storm", "Cassandra",
    "Hadoop", "Big Data", "HBase", "Spark", "HBase", "Storm", "Cassandra"
]

interests = defaultdict(int)

for interest in duplicated_interests:
    interests[interest] += 1

print(f"Interests: {interests}")


