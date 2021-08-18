def findPair(A, target):
    for i in range(len(A) - 1):
        for j in range(i + 1, len(A)):
            if A[i] + A[j] == target:
                print("Pair found", (A[i], A[j]))
    return


A = [8, 7, 2, 5, 3, 1]
target = 10
findPair(A, target)