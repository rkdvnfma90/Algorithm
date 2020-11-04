"""
볼링공 고르기
A,B 두사람이 볼링을 치고 있다. 두 사람은 서로 무게가 다른 볼링공을 고르려 한다.
볼링공은 총 n개가 있으며, 볼링공마다 무게가 적혀 있고, 공의 번호는 1번부터 순서대로 부여된다.
또한 같은 무게의 공이 여러개 있을 수 있지만 서로 다른 공으로 간주한다.
볼링공의 무게는 1부터 m까지의 자연수로 존재한다.
예를 들어 n이 5이고, m이 3이며 각각 무게가 차례대로 1,3,2,3,2 일때 각 공의 번호가 차례대로
1번부터 5번까지 부여 된다. 이때 두사람이 고를 수 있는 볼링공 번호의 조합은 다음과 같다.
(1,2) (1,3) (1,4) (1,5) (2,3) (2,5) (3,4) (4,5)
결과적으로 두 사람이 공을 고르는 경우의 수는 8가지 이다. n개의 공의 무게가 각각 주어질 때
두 사람이 볼링공을 고르는 경우의 수를 구하는 프로그램을 작성하시오

입력조건
1. 첫째줄에 볼링공의 개수 n, 공의 최대무게 m이 공백으로 구분되어 자연수 형태로 주어진다.
(1 <= n <= 1,000 , 1 <= m <= 10)
2. 둘째줄에 각 볼링공의 무게 k가 공백으로 구분되어 순서대로 자연수 형태로 주어진다.

출력조건
1. 첫째 줄에 두 사람이 볼링공을 고르는 경우의 수를 출력한다.

해결방안

"""

# n : 볼링공의 수, m : 공의 최대 무게
n, m = map(int, input().split())
# ball : 볼링공의 무게
ball = list(map(int, input().split()))

# 무게에 따른 공의 갯수를 저장하는 리스트 초기화 (공의 최대 무게는 10까지 이므로 11개의 리스트)
arr = [0] * 11 

for data in ball:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    arr[data] += 1

# 결과값 초기 세팅
result = 0

# 1부터 m까지 각 무게에 대해서 처리한다.
for i in range(1, m + 1):
    # n에서 현재 무게의 볼링공의 수를 뺀다, 왜냐하면 자기 자신을 선택할 수 없기 때문
    n -= arr[i]
    # 현재 무게의 볼링공 * 경우의수 n 을 곱하여 result 에 값을 갱신한다.
    result += arr[i] * n

print(result)

"""
combinations 사용
import sys
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())
ball = list(map(int, input().split()))
pick = list(combinations(ball, 2))
count = len(pick)

for a, b in pick:
    if a == b:
        count -= 1
print(count)

"""

