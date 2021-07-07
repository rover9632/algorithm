import random


def dfs(a):
    for i in range(9):
        for j in range(9):
            if a[i][j] != "0":
                continue
            s = set(map(str, range(1, 10)))
            s = s - set(a[i]) - set(x[j] for x in a)
            m, n = i // 3 * 3, j // 3 * 3
            s = list(s - set(y for x in a[m:m + 3] for y in x[n:n + 3]))
            for x in s:
                a[i][j] = x
                if dfs(a):
                    return True
            a[i][j] = "0"
            return False
    return True


def main(args):
    s = """0 0 0 0 0 0 0 0 0
           0 0 0 0 0 0 0 0 0
           8 6 7 3 5 0 0 0 0
           6 2 4 1 9 5 3 7 0
           7 5 9 8 0 3 0 0 0
           1 3 8 6 2 7 5 9 0
           2 7 0 5 0 8 6 4 0
           3 8 6 9 1 4 2 5 0
           0 4 5 2 7 6 8 3 0"""
    a = []
    for line in s.splitlines():
        a.append(line.split())

    dfs(a)

    for x in a:
        print(" ".join(x))
