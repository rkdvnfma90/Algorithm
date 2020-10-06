"""
왕실정원은 체스판과 같은 8 x 8 좌표 평면이다.
나이트는 충성스러운 신하로서 매일 무술을 연마한다.
이동은 L 자 형태로만 이동할 수 있으며 정원 밖으로는 나갈 수 없다. 이동할 수 있는 경우는 다음과 같다.
1. 수평으로 2칸 이동 후 수직으로 1칸 이동
2. 수직으로 2칸 이동 후 수평으로 1칸 이동

나이트의 위치가 주어졌을때 나이트가 이동할 수 있는 경우의 수를 구하는 프로그램을 작성하시오.
"""

# 현재 위치 입력
pos = input()
n = 8
result = 0

# 움직일 수 있는 모든 경우의 수
steps = [(-2, 1), (-2, -1), (2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

column = int(pos[0])
row = int(ord(pos[1])) - int(ord('a')) + 1

for step in steps:
  next_col = column + step[0]
  next_row = row + step[1]

  if next_col < 1 or next_row < 1 or next_col > n or next_row > n:
    continue
  
  result += 1

print(result)
