from collections import Counter, defaultdict

users = [
    {'id': 0, 'name': 'Hero'},
    {'id': 1, 'name': 'Dunn'},
    {'id': 2, 'name': 'Sue'},
    {'id': 3, 'name': 'Chi'},
    {'id': 4, 'name': 'Thor'},
    {'id': 5, 'name': 'Clive'},
    {'id': 6, 'name': 'Hicks'},
    {'id': 7, 'name': 'Devin'},
    {'id': 8, 'name': 'Kate'},
    {'id': 9, 'name': 'Klein'}
]

friendships_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

friendships = defaultdict(list)

for (i, j) in friendships_pairs:
    friendships[i].append(j)
    friendships[j].append(i)


def number_of_friends(user):
    user_id = user["id"]
    friends = friendships[user_id]
    return len(friends)


total_connections = sum(number_of_friends(user) for user in users)

num_users = len(users)
avg_connections = total_connections / num_users

num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]

num_friends_by_id.sort(key=lambda x: x[1], reverse=True)

print(f"Number of friends by id: {num_friends_by_id}")


def foaf_ids_bad(user):
    return [foaf_id for friend_id in friendships[user["id"]] for foaf_id in friendships[friend_id]]


print(f"Friends of friends of user (bad implementation) 0: {foaf_ids_bad(users[0])}")


def friends_of_friends(user):
    user_id = user["id"]
    return Counter(foaf_id for friend_id in friendships[user_id] for foaf_id in friendships[friend_id] if
                   foaf_id != user_id and foaf_id not in friendships[user_id])


print(f"Friends of friends of user 3: {friends_of_friends(users[3])}")

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

words_and_counts = Counter(word for user_id, interest in interests for word in interest.lower().split())

for word, count in words_and_counts.most_common():
    if count > 1:
        print(f"{word}: {count}")
