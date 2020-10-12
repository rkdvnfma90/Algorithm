"""
입력조건
1. 첫째 줄에 수열에 속해 있는 수의 개수 n이 주어진다 (1 <= n <= 500)
2. 둘째줄부터 n+1 번째 줄까지 n개의 수가 입력된다 수의 범위는 1이상 100,00 이하의 자연수

출력조건
입력으로 주어진 수열이 내림차순으로 정렬된 결과를 공백으로 구분하여 출력한다.
"""
# n 을 입력 받는다
n = int(input())

arr = []

# n 만큼의 정수를 입력한다.
for i in range(n):
  arr.append(int(input()))

print(sorted(arr, reverse=True))


