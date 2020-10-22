"""
(내가 생각한 방법 : 탐색범위는 1부터 10억까지인데 이 경우 이진탐색을 떠올려야 한다. 하지만)
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

# n : 떡의 갯수 , m : 손님이 원하는 떡의 길이
n,m = list(map(int, input().split()))

# 각 개별의 떡 높이
array = list(map(int, input().split()))


def func(array, target):
  # 기계의 초기 높이
  h = 0
  # 자르고 남은 떡들의 길이 총 합
  h_sum = 0
  # 손님이 원하는 떡의 길이보다 크거나 같게 자를수 있는 기계의 높이 h를 저장하고 있는 배열
  arr = []

  while True:
    # 기계의 높이를 1씩 증가시킨다.
    h += 1
    new_array = list(map(lambda x : x - h if x - h >= 0 else 0  , array))
    h_sum = sum(new_array)
    arr.append(h)
    # 손님이 원하는 길이보다 짧아지면 반복문 종료
    if h_sum <= target:
      break
  return max(arr)
    
print(func(array, m))