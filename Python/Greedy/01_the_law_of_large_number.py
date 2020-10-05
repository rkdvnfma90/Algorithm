"""
N 개의 다양한 자연수로 이루어진 배열이 있을 때 주어진 수 들을 총 M 번 더하여 가장 큰수를 만드는 법칙
단 배열의 특정한 인덱스에 해당하는 수가 연속해서 K 번을 초과하여 더해질 수 없다.

- 입력 예시
5 8 3
2 4 5 4 6

- 출력 예시
46
"""

# n = 자연수 배열의 길이
# m = 총 더할 수
# k = 연속해서 더할 횟수
# count = 가장 큰수가 더해지는 횟수
n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

result = 0

first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두번째로 큰 수

# m / (k + 1) = 반복되는 수열의 수
# k는 연속해서 더할수있는 횟수인데, 연속해서 더하는 수는 가장 큰 수이다. 즉, 반복되는 수열의 수 * k = 가장 큰수가 더해지는 횟수이다.
count = int(m / (k + 1)) * k 

# m 이 (k + 1)로 나누어 떨어지지않을 경우도 있기 때문에 더해준다.
count += m % (k + 1)

result = 0
result += (count) * first
result += (m - count) * second

print(result)