def waiter(number, q):
  #2D list to store the iterations 
    A = [[] for i in range(q+1)]
    B = [[] for j in range(q+1)]
    A[0] = number
    #Initialize the prime number list
    lower = 2
    upper = 10000
    prime = [i for i in range(lower, upper + 1) if all(i % j != 0 for j in range(2, i))]
    # pick up plates from A stack
    for i in range(q):
        for j in range(len(A[i])):
            n = A[i].pop()
            if n % prime[i] == 0:
                B[i].append(n)
            else :
                A[i+1].append(n)
    b = []
    a = []
    for i in range(len(B)):
        while B[i] != []:
            b.append(B[i].pop())
    for i in range(len(A)):
        while A[i] != []:
            a.append(A[i].pop())
    return b + a if b and a else b
