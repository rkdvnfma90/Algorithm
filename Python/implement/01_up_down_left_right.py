"""
여행가 A는 n * n 크기의 정사각형 공간위에 서있다. 가장 왼쪽 위 좌표는 (1,1)이고 가장 오른쪽 아래 좌표는 (n,n)이다.
여행 계획서에는 L R U D 중 하나의 문자가 반복적으로 적혀있다.
L : 왼쪽이동
R : 오른쪽이동
U : 위이동
D : 아래이동

n * n 크기의 정사각형 공간을 벗어나는 움직임은 무시된다.
계획서가 주어졌을때 여행가가 최종 도착할 지점의 좌표를 출력하는 프로그램을 작성하시오.
"""

n = int(input())
x, y = 1, 1;
moving = input().split()
move_types = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for move in moving:
  for i in range(len(move_types)):
    if move == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]

  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue
  
  x, y = nx, ny

print(x,y)
  