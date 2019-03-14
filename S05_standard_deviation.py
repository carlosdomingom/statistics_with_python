if __name__ == '__main__':

    import math
    n = int(input())
    x = list(map(int, input().split()))

    mean = sum(x) / len(x)
    sum_of_sq_distance = 0
    for _ in range(n):
        sum_of_sq_distance += (x[_]-mean)**2

    stddev = math.sqrt(sum_of_sq_distance/n)
    print("{0:.1f}".format(stddev))
