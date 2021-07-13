"""
Maximum path sum I

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.
Find the maximum total from top to bottom of the triangle below:
"""
from typing import List

TRIANGLE = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
]


def triangle_to_matrix(triangle: List[List[int]]) -> List[List[int]]:
    max_len = max([len(rowlist) for rowlist in triangle])
    for data_row in triangle:
        n_to_fill = max_len - len(data_row)
        data_row.extend([0]*n_to_fill)
    return triangle


def get_sum_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """
    Starting from the second to last layer it selects the maximum sum if the current item in layer and
    its the adjacent numbers. Then, it proceeds to the top
    :param matrix: list of list of numbers
    :return: list of list of numbers
    """
    col_len = len(matrix)
    row_len = len(matrix[0]) - 1
    for row_id in range(col_len - 2, -1, -1):
        for item_id in range(row_len):
            matrix[row_id][item_id] = max([matrix[row_id][item_id] + matrix[row_id + 1][item_id],
                                           matrix[row_id][item_id] + matrix[row_id + 1][item_id + 1]])
    return matrix


if __name__ == "__main__":
    data = get_sum_matrix(triangle_to_matrix(TRIANGLE))
    print(f"The maximum total from top to bottom of the triangle below is: {max(data[0])}")



