"""
개선된 다익스트라 알고리즘을 사용하기에 앞서 필요한 최소힙의 사용법을 알아본다.
파이썬같은 경우 heapq 라이브러리는 기본적으로 최소 힙으로 되어있다.
Java도 마찬가지로 최소 힙으로 되어있고, C++ 같은 경우는 최대 힙으로 되어 있다.
만약 파이썬에서 최대힙을 사용하고 싶다면 우선순위에 -1를 곱하여 음수로 넣었다가 꺼낼때 다시 -1를 곱하여 원래의 수로 돌린다.
"""

import heapq

# 오름차순 힙정렬(Heap sort)
def heap_sort(iterable):
    h = []
    result = []

    # 모든 원소를 차례대로 힙에 삽입
    for val in iterable:
        heapq.heappush(h, val)
    
    # 힙에 삽입된 원소를 차례대로 꺼내어 담는다.
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heap_sort([1,3,5,7,9,2,4,6,8,10])

print(result)
    
