from collections import defaultdict


def check_symbol2(matrix, pos):
    i, j = pos
    m = len(matrix)
    n = len(matrix[0])
    if i < 0 or j < 0:
        return False
    if i >= m or j >= n:
        return False

    return not matrix[i][j].isdigit() and matrix[i][j] != "."


def check_surroading(matrix, pos):
    i, j = pos
    m = len(matrix)
    n = len(matrix[0])
    if i < 0 or j < 0:
        return False
    if i >= m or j >= n:
        return False

    return (
        check_symbol2(matrix, (i + 1, j))
        or check_symbol2(matrix, (i - 1, j))
        or check_symbol2(matrix, (i + 1, j))
        or check_symbol2(matrix, (i, j + 1))
        or check_symbol2(matrix, (i, j - 1))
        or check_symbol2(matrix, (i + 1, j + 1))
        or check_symbol2(matrix, (i + 1, j - 1))
        or check_symbol2(matrix, (i - 1, j + 1))
        or check_symbol2(matrix, (i - 1, j - 1))
    )


def check_valid_number(end_pos, len_number, matrix):
    i, j = end_pos
    for k in range(len_number):
        if check_surroading(matrix, (i, j - k)):
            return True
    return False


def process_matrix(matrix):
    ans = 0
    buffer = ""
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j].isdigit():
                buffer += matrix[i][j]
            if (not matrix[i][j].isdigit() or j == n - 1) and buffer:
                if check_valid_number((i, j - 1), len(buffer), matrix):
                    ans += int(buffer)
                buffer = ""
    return ans


def check_symbol2(matrix, pos):
    i, j = pos
    m = len(matrix)
    n = len(matrix[0])
    if i < 0 or j < 0:
        return False
    if i >= m or j >= n:
        return False

    return (i, j) if matrix[i][j] == "*" else None


def check_surroading2(matrix, pos):
    i, j = pos
    m = len(matrix)
    n = len(matrix[0])
    if i < 0 or j < 0:
        return False
    if i >= m or j >= n:
        return False

    return (
        check_symbol2(matrix, (i + 1, j))
        or check_symbol2(matrix, (i - 1, j))
        or check_symbol2(matrix, (i + 1, j))
        or check_symbol2(matrix, (i, j + 1))
        or check_symbol2(matrix, (i, j - 1))
        or check_symbol2(matrix, (i + 1, j + 1))
        or check_symbol2(matrix, (i + 1, j - 1))
        or check_symbol2(matrix, (i - 1, j + 1))
        or check_symbol2(matrix, (i - 1, j - 1))
    )


def check_valid_number2(end_pos, len_number, matrix):
    i, j = end_pos
    for k in range(len_number):
        star_pos = check_surroading2(matrix, (i, j - k))
        if star_pos:
            return star_pos
    return None


def process_matrix2(matrix):
    mapping = defaultdict(list)
    buffer = ""
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j].isdigit():
                buffer += matrix[i][j]
            if (not matrix[i][j].isdigit() or j == n - 1) and buffer:
                star_pos = check_valid_number2((i, j - 1), len(buffer), matrix)
                if star_pos:
                    mapping[tuple(star_pos)].append(int(buffer))
                buffer = ""
    return mapping


with open("input.txt", "r") as f:
    matrix = []
    lines = [line.rstrip() for line in f]
    for line in lines:
        matrix.append(list(line))
    # print(process_matrix(matrix))
    ans2_mapping = process_matrix2(matrix)
    ans2 = 0
    for value in ans2_mapping.values():
        tmp = 1
        if len(value) == 2:
            for v in value:
                tmp *= v
            ans2 += tmp
    print(ans2)
