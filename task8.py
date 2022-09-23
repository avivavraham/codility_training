def solution(A):
    B = [0] * len(A)
    for item in A:
        if ((item < 1) or (item > len(A))):
            return 0
        B[item - 1] = 1
    for item in B:
        if item == 0:
            return 0
    return 1