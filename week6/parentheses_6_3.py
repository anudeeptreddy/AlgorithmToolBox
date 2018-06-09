# Uses python3


def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def get_min_and_max(i, j, op, m, M):
    min_value = float("inf")
    max_value = float("-inf")
    for k in range(i, j):
        a = evalt(M[i][k], M[k+1][j], op[k])
        b = evalt(M[i][k], m[k+1][j], op[k])
        c = evalt(m[i][k], M[k+1][j], op[k])
        d = evalt(m[i][k], m[k+1][j], op[k])
        min_value = min(min_value, a, b, c, d)
        max_value = max(max_value, a, b, c, d)
    return min_value, max_value


def get_maximum_value(dataset):
    # Algorithm to compute maximum value by parenthesising a given expression
    op = dataset[1:len(dataset):2]
    digit = dataset[0:len(dataset)+1:2]
    n = len(digit)
    min_matrix = [[0 for i in range(n)] for j in range(n)]
    max_matrix = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        min_matrix[i][i] = int(digit[i])
        max_matrix[i][i] = int(digit[i])
    for s in range(1, n):
        for i in range(n-s):
            j = i + s
            min_matrix[i][j], max_matrix[i][j] = get_min_and_max(i, j, op, min_matrix, max_matrix)
    return max_matrix[0][n-1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
