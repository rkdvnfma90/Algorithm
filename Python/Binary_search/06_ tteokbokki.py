"""
떡볶이 떡 만들기
절단기에 높이 h 를 지정하면 줄지어진 떡을 한번에 절단한다.
떡의길이가 h 보다 긴떡은 윗부분이 잘릴것이고 낮은떡은 잘리지 않는다
예를들어 19, 14, 10, 17 길이의 떡 4개가 있고 절단기의 높이가 15라면 
자른뒤의 떡 길이는 15, 14, 10, 15 이고 
잘린떡의 길이는 4, 0, 0, 2 이다. 손님은 6만큼의 길이를 가져간다.

손님이 왔을때 요청한 총 길이가 m 일때 적어도 m 만큼의 떡을 얻기위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오

입력조건
1. 첫째 줄에 떡의 갯수 n과 요청한 떡의길이 m이 주어진다 (1 <= n <= 1,000,000, 1 <= m <= 2,000,000,000)
2. 둘째 줄에는 떡의 개별 높이가 주어진다. 떡 높이의 총합은 항상 m 이므로 손님은 필요한 양만큼 떡을 사갈 수 있다. 길이는 10억보다 작거나 같은 양의 정수 or 0 이다.

출력조건
1. 적어도 m 만큼의 떡을 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.
"""

"""
전형적인 이진탐색 문제이자 파라메트릭 서치 유형의 문제이다.
파라메트릭 서치는 최적화 문제를 결정 문제로 바꾸어 해결하는 기법이다. (원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제)
예를 들어 범위 내에서 조건을 만족하는 가장 큰 값을 찾으라는 최적화 문제라면 이진 탐색으로 결정 문제를 해결하면서 범위를 좁혀갈 수 있다.
보통 파라메트릭 서치 유형은 이진 탐색을 이용하여 해결한다.
파라메트릭 서치 문제는 이진 탐색을 재귀적으로 구현하지 않고 반복문으로 구현하면 더 간결하게 구현 할 수 있다.

절단기의 높이는 1부터 10억까지의 정수인데 이처럼 큰 수를 봤을 때엔 이진탐색을 떠올려야 한다.

절단기의 높이 h는 0부터 가장 긴 떡의 길이 안에 있어야 한다 (시작점 : 0, 종료점 : 긴 떡의 길이 -> 이것을 이진탐색으로!)  
"""


# n : 떡의 갯수 , m : 손님이 원하는 떡의 길이
n,m = list(map(int, input().split()))

# 각 개별의 떡 높이
array = list(map(int, input().split()))

# 시작값 
start = 0
# 종료값은 개별의 떡 높이중 가장 높은 길이
end = max(array)
# 결과값 (최적화된 높이)
result = 0

# 시작 값이 종료값보다 커지면 반복문 종료
while start <= end:
  total = 0
  mid = (start + end) // 2

  for x in array:
    # 잘랐을때 떡의 양 계산. 중간값보다 작으면 자르지 않음
    if x > mid:
      total += x - mid
  
  # 잘린 떡의 양이 손님이 원하는 떡의 길이보다 작을 경우 더 많이 잘라야 하기 때문에 왼쪽 (작은부분)을 탐색한다.
  if total < m:
    end = mid - 1
  
  # 잘린 떡의 양이 충분할 경우 덜 자르기 위해 오른쪽 (큰부분)을 탐색한다.
  else:
    # 최대한 덜 잘렸을때가 원하는 값이므로 이때 result 값을 mid로 넣는다.
    result = mid
    start = mid + 1

print(result)