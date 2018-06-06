# Uses python3
def edit_distance(s, t):
    # Algorithm to compute the edit distance of two strings
    n = len(s)   # rows
    m = len(t)   # columns

    # create a matrix of size n+1 * m+1
    d_matrix = [[0 for x in range(m+1)] for y in range(n+1)]

    for i in range(n+1):
        d_matrix[i][0] = i   # Edit distance in comparison to a blank string
    for i in range(m+1):
        d_matrix[0][i] = i   # Edit distance in comparison to a blank string

    # compute all the possible edit distances between the strings
    for j in range(1, m+1):
        for i in range(1, n+1):
            insertion_cost = d_matrix[i][j-1] + 1     # insertion
            deletion_cost = d_matrix[i-1][j] + 1      # deletion
            match_cost = d_matrix[i-1][j-1]           # match
            mismatch_cost = d_matrix[i-1][j-1] + 1    # mismatch

            # s[i-1] & t[j-1]: because strings start at index 0 where as strings in d_matrix start at position 1
            d_matrix[i][j] = min(insertion_cost, deletion_cost, match_cost) if s[i-1] == t[j-1] \
                else min(insertion_cost, deletion_cost, mismatch_cost)

    return d_matrix[n][m]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
