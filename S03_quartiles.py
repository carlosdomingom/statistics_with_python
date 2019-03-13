if __name__ == "__main__":
    n = int(input())
    mylist = list(map(int, input().split()))
    mylist.sort()
    lower_half = mylist[0:n//2]
    upper_half = mylist[((n+1)//2):]


    q1 = lower_half[((n//2)-1)//2:(n//2)//2+1]
    print("{:d}".format(int(sum(q1) / len(q1))))
    q2 = mylist[(n-1)//2:n//2+1]
    print("{:d}".format(int(sum(q2) / len(q2))))
    q3 = upper_half[((n//2)-1)//2:(n//2)//2+1]
    print("{:d}".format(int(sum(q3) / len(q3))))
