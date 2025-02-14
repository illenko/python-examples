from typing import List


def dot(v: List[float], w: List[float]) -> float:
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


num_friends = [100, 49, 41, 40, 25, 21, 21, 19, 19, 18, 18, 16, 15, 15, 15, 15, 14, 14, 13, 13, 13, 13, 12, 12, 11]
num_minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]


def mean(l: List[float]) -> float:
    return sum(l) / len(l)


print(mean(num_friends))


def de_mean(x: List[float]) -> List[float]:
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]


def covariance(v: List[float], w: List[float]) -> float:
    n = len(v)
    return dot(de_mean(v), de_mean(w)) / (n - 1)


print(covariance(num_friends, num_minutes))


def sum_of_squares(v: List[float]) -> float:
    return dot(v, v)


def variance(x: List[float]) -> float:
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)


def standard_deviation(x: List[float]) -> float:
    return variance(x) ** 0.5


def correlation(v: List[float], w: List[float]) -> float:
    stdev_v = standard_deviation(v)
    stdev_w = standard_deviation(w)
    if stdev_v > 0 and stdev_w > 0:
        return covariance(v, w) / stdev_v / stdev_w
    else:
        return 0
