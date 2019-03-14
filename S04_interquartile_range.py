if __name__ == '__main__':
    n = int(input())
    x = list(map(int, input().split()))
    f = list(map(int, input().split()))
    for _ in range(n):
        # Add f-1 (one is already in list) times the element of the list
        x.extend(x[_] for i in range(f[_]-1))

    # Recalculate length
    n = len(x)
    x.sort()
    lower_half = x[0:n//2]
    upper_half = x[((n+1)//2):]

    q1 = lower_half[((n//2)-1)//2:(n//2)//2+1]

    q3 = upper_half[((n//2)-1)//2:(n//2)//2+1]

    print("{0:.1f}".format( (sum(q3)/len(q3)) - (sum(q1)/len(q1)) ))
