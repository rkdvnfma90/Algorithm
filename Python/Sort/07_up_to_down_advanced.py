"""
n명의 학생정보가 있고 학생정보는 이름과 성적으로 구분 된다 (튜플이용)
성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성하시오

입력조건
1. 첫번째 줄에 학생의 수 n이 입력된다 (1 <= n <= 100,000)
2. 두번째 줄부터 n + 1 번째 줄에는 학생의 이름을 나타내는 문자열과 성적을 나타내는 정수가 공백으로 구분되어 입력 된다.

출력조건
모든 학생의 이름을 성적이 낮은 순서대로 출력한다.
"""
n = int(input())

arr = []

for i in range(n):
  data = input().split()
  arr.append((data[0], int(data[1])))

# lambda x : -x[1] -> 내림차순 
arr = sorted(arr, key = lambda x : x[1] )

for i in arr:
  print(i[0], end = ' ')