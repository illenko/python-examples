from collections import Counter
from typing import List
import matplotlib.pyplot as plt

num_friends = [100, 49, 41, 40, 25, 21, 21, 19, 19, 18, 18, 16, 15, 15, 15, 15, 14, 14, 13, 13, 13, 13, 12, 12, 11]

friend_counts = Counter(num_friends)

xs = range(101)

ys = [friend_counts[x] for x in xs]

plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])
plt.title("Histogram of Friend Counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")

plt.show()


def mean(l: List[float]) -> float:
    return sum(l) / len(l)


print(mean(num_friends))


def median(v: List[float]) -> float:
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2

    if n % 2 == 1:
        return sorted_v[midpoint]
    else:
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2


print(median(num_friends))


def quantile(x: List[float], p: float) -> float:
    p_index = int(p * len(x))
    return sorted(x)[p_index]


print(quantile(num_friends, 0.10))
print(quantile(num_friends, 0.25))
print(quantile(num_friends, 0.75))
print(quantile(num_friends, 0.90))


def mode(x: List[float]) -> List[float]:
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items() if count == max_count]


print(mode(num_friends))


def data_range(x: List[float]) -> float:
    return max(x) - min(x)


print(data_range(num_friends))


def de_mean(x: List[float]) -> List[float]:
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]


print(de_mean(num_friends))


def dot(v: List[float], w: List[float]) -> float:
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def sum_of_squares(v: List[float]) -> float:
    return dot(v, v)


def variance(x: List[float]) -> float:
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)


print(variance(num_friends))

def standard_deviation(x: List[float]) -> float:
    return variance(x) ** 0.5


print(standard_deviation(num_friends))

def interquartile_range(x: List[float]) -> float:
    return quantile(x, 0.75) - quantile(x, 0.25)


print(interquartile_range(num_friends))