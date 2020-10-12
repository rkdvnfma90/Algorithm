"""
계수정렬은 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을때만 사용한다.
일반적으로 가장 큰 데이터와 작은 데이터의 차이가 1,000,000을 넘지 않을때 효과적이다.
그 이유는 모든 범위를 담을 수 있는 크기의 리스트를 선언해야한다.
예를들어 가장 큰 데이터와 가장 작은 데이터의 차이가 1,000,000 이라면 1,000,001 개의 데이터가 들어갈 수 있는 리스트를 초기화 해야한다.
1,000,001 이 된 이유는 0부터 1,000,000 까지는 총 1,000,001 개의 수가 존재하기 때문

동일한 값을 가지는 데이터가 여러개 존재할때 효과적이다.
"""
# 모든 원소의 값이 0보다 크거나 같다고 가정
arr = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

# 0이 존재하기 때문에 최대값보다 1 큰 갯수만큼 배열을 0으로 초기화 한다.
count = [0] * (max(arr) + 1)

# 각 데이터에 해당하는 인덱스의 값을 증가시킨다
for i in range(len(arr)):
  count[arr[i]] += 1

# 리스트에 있는 정렬 정보를 확인하여 출력한다.
for i in range(len(count)):
  for j in range(count[i]):
    print(i, end = ' ')