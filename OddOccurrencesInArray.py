def solution(A):
    d = {}
    for item in A:
        d[item] = d.get(item,0) + 1
    for index,count in d.items():
        if (count % 2 == 1):
            return index