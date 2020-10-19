"""
부품찾기
n개의 부품이 있다. 각 부품은 정수 형태의 고유한 번호가 있다.
어느날 손님이 m개 종류의 부품을 대량으로 구매하겠다며 당일 날 견적서를 요청했다. 
손님이 문의한 부품 m개 종류를 모두 확인해서 해당 부품이 모두 있는지 확인하는 프로그램을 작성하시오.

입력조건
1. 첫째 줄에 정수 n이 주어진다 (1 <= n <= 1,000,000)
2. 둘째 줄에는 공백으로 구분하여 n개의 정수가 주어진다. 정수는 1보다 크고 1,000,000 이하이다.
3. 셋째 줄에는 정수 m이 주어진다 (1 <= m <= 100,000)
4. 넷째 줄에는 공백으로 구분하여 m개의 정수가 주어진다. 정수는 1보다 크고 10억 이하이다.

출력조건
1. 첫째줄에 공백으로 구분하여 각 부품이 존재하면 yes, 없으면 no를 출력
"""

def binary_search(a, target, start, end):

    if start > end:
      return None

    mid = int((start + end) / 2)

    # 타겟이 중간값이면 리턴
    if a[mid] == target:
        return mid
    # 타겟이 중간값 보다 작을때 
    elif a[mid] > target:
        return binary_search(a, target, start, mid -1)
    # 타겟이 중간값 보다 크면
    else:
        return binary_search(a, target, mid + 1, end)



# 가게의 부품 갯수
n = int(input())

# 가게의 부품 번호를 공백으로 구분하여 입력
na = list(map(int, input().split()))
# 이진 탐색을 진행하기 위해 먼저 부품의 배열을 정렬한다.
na.sort()
# 손님이 원하는 부품 갯수
m = int(input())

# 손님이 원하는 부품 번호를 공백으로 구분하여 입력
ma = list(map(int, input().split()))

for i in ma:
    result = binary_search(na, i, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end= ' ')
