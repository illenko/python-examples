from typing import List

Vector = List[float]

height_weight_age = [70, 170, 40]

grades = [95, 80, 75, 62]


def add(v: Vector, w: Vector) -> Vector:
    """Adds corresponding elements"""
    assert len(v) == len(w), "vectors must be the same length"

    return [v_i + w_i for v_i, w_i in zip(v, w)]


print(add([1, 2, 3], [4, 5, 6]))  # [5, 7, 9]


def subtract(v: Vector, w: Vector) -> Vector:
    """Subtracts corresponding elements"""
    assert len(v) == len(w), "vectors must be the same length"

    return [v_i - w_i for v_i, w_i in zip(v, w)]


print(subtract([5, 7, 9], [4, 5, 6]))  # [1, 2, 3]


def vector_sum(vectors: List[Vector]) -> Vector:
    assert vectors, "no vectors provided"

    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "different sizes"

    return [sum(vector[i] for vector in vectors) for i in range(num_elements)]


print(vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]))  # [16, 20]


def scalar_multiply(c: float, v: Vector) -> Vector:
    return [c * v_i for v_i in v]


print(scalar_multiply(2, [1, 2, 3]))  # [2, 4, 6]


def vector_mean(vectors: List[Vector]) -> Vector:
    n = len(vectors)
    s = 1 / n
    return scalar_multiply(s, vector_sum(vectors))


print(vector_mean([[1, 2], [3, 4], [5, 6]]))  # [3, 4]


def dot(v: Vector, w: Vector) -> float:
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


print(dot([1, 2, 3], [4, 5, 6]))  # 32


def sum_of_squares(v: Vector) -> float:
    return dot(v, v)


print(sum_of_squares([1, 2, 3]))  # 14

from math import sqrt


def length(v: Vector) -> float:
    return sqrt(dot(v, v))


print(length([3, 4]))  # 5


def distance(v: Vector, w: Vector) -> float:
    return length(subtract(v, w))

print(distance([1, 2, 3], [4, 6, 8]))
