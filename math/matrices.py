from typing import List, Tuple

Vector = List[float]
Matrix = List[List[float]]

A = [[1, 2, 3],
     [4, 5, 6]]

B = [[1, 2],
     [3, 4],
     [5, 6]]


def shape(m: Matrix) -> Tuple[int, int]:
    num_rows = len(m)
    num_cols = len(m)

    return num_rows, num_cols

print(f"shape = {shape(A)}")

def get_row(m: Matrix, row_id: int) -> Vector:
    return m[row_id]


def get_col(m: Matrix, col_id: int) -> Vector:
    return [m_i[col_id] for m_i in m]


print(f"row 1 {get_row(A, 1)}")

print(f"col 1 {get_col(B, 1)}")
