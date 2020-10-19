from bisect import bisect_left, bisect_right

a = [1,2,4,4,4,4,4,4,4,8,9,10,11]
x = 4

# 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
print(bisect_left(a,x)) # 2
# 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환
print(bisect_right(a,x)) # 9 

# 이러한 특징을 통하여 값이 특정 범위에 속하는 데이터 갯수 구하기를 할 수 있다.
# left value와 right value 사이에 있는 값의 갯수를 반환 (이미 정렬 되어 있음)
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# 값이 4인 데이터 갯수 출력
print(count_by_range(a, 4, 4))

# 값이 -1 ~ 3 범위에 있는 데이터 갯수 출력
print(count_by_range(a, -1, 3))

"""
이진 탐색 문제는 입력 데이터가 많거나 탐색범위가 매우 넓다.
데이터의 갯수가 1000만개 넘어가거나 탐색 범위 크기가 1000억 이상이라면 이진탐색 알고리즘을 의심해보자.
하지만 입력 데이터의 갯수가 많은 문제에 input() 함수를 사용하면 동작 속도가 느려 시간 초과로 오답판정 받을 수 있다.
sys 라이브러리의 readline() 을 사용하자
"""

import sys

# readline() 을 호출하고나서는 꼭 rstrip() 함수를 사용하자
# 엔터가 줄바꿈 기호로 입력되기 때문에 이 공백을 제거해주어야 한다.
input_data = sys.stdin.readline().rstrip()

print(input_data)