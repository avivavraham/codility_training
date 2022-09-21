def solution5(A):
    B = [0] * (len(A)+1)
    for num in A:
        B[num-1] = 1
    for i in range(len(B)):
        if B[i] == 0:
            return i + 1


print(solution5([2,3,1,5]))