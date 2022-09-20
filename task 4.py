import math
def solution(X, Y, D):
    i = 0
    j = 0
    while(X + D * pow(2,i) <= Y): #binary search for jump
        i += 1
        j = pow(2,i)  # Now we know 2^(i-1) < jump < 2^i
    left = int(pow(2, (i-1))) #so we search jump in that interval
    right = j
    j = left + (right - left) // 2
    while(j != left and j != right): #binary search in an interval
        if(X + D * j < Y):
            left = j
        else: right = j
        j = left + (right - left) // 2
    if(X + D * j < Y):
        j += 1
    return j

print(solution(257546415, 2587564627, 999))