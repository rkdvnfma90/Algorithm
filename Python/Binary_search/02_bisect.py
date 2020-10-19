"""
파이썬 이진탐색 라이브러리
bisect
"""

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