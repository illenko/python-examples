from collections import Counter

duplicated_interests = [
    "Hadoop", "Big Data", "HBase", "Java", "Storm", "Cassandra",
    "Hadoop", "HBase", "Java", "Spark", "Storm", "Cassandra",
    "Hadoop", "Big Data", "HBase", "Spark", "HBase", "Storm", "Cassandra"
]

interests = Counter(duplicated_interests)

print(f"Interests: {interests}")

print(f"Most common interests: {interests.most_common(3)}")
