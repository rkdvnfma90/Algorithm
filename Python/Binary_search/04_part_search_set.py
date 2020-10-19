"""
part_search 를 set(집합)을 사용하여 푸는법
특정한 수가 한번이라도 등장했는지 검사하면 되므로 set 을 이용하여도 된다.
소스가 간결하다는 장점이 있다.
"""
# 가게의 부품수
n = int(input())
# 가게에 있는 전체 부품 번호를 입력받아서 set 자료형에 기록
na = set(map(int,input().split()))

# 손님이 원하는 부품수
m = int(input())
# 손님이 원하는 부품 번호를 입력받아서 list 자료형에 기록
ma = list(map(int,input().split()))


for i in ma:
    if i in na:
        print('yes', end=' ')
    else:
        print('no' , end=' ')