"""
피보나치수열 반복문 (보텀업)
반복문을 사용하여 오버헤드를 줄일수 있다.
보텀업 방식에서 사용되는 결과 저장용 리스트는 DP테이블 이라고 부르며
메모이제이션은 탑다운 방식(재귀) 방식에 국한되어 사용되는 표현이다. -> 결과를 어디에 담아놓고 활용하지 않을 수도 있음
"""

# 한번 계산된 결과를 저장하기 위한 dp 테이블 초기화
d = [0] * 100

# 첫번째, 두번째 수는 1
d[1] = 1
d[2] = 1

# 피보나치 수를 구할 값
n = 99

# 1,2 는 있으므로
for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n]) 
