if __name__ == '__main__':
    n = int(input())
    x = list(map(int, input().split()))
    w = list(map(int, input().split()))

    suma = .0
    for _ in range(n):
        suma += x[_]*w[_]

    media_variable = suma / sum(w)
    print("{0:.1f}".format(media_variable))
