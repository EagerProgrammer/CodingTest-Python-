# 상위 K 빈도 추출
from collections import Counter
def solution(nums,k):
    set1 = set(nums)
    a = Counter(nums)
    list1 = []
    for i in set1:
        if a[i] < k:
            continue
        else:
            list1.append(i)
    return list1.sort()
