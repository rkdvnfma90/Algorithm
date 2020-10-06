"""
게임 캐릭터가 맵안에서 움직이는 시스탬을 개발중이다.
캐릭터가 있는 장소는 1 x 1 크기의 정사각형으로 이루어진 n x m 크기의 직사각형으로, 각각 칸은 육지이거나 바다 이다.
캐릭터는 동서남북중 한곳을 바라보고 있다.
맵의 각 칸은 (a,b)로 나타낼수 있고 A는 북쪽으로부터 떨어진 칸의 갯수, B는 서쪽으로부터 떨어진 칸의 갯수를 의미한다.
맵의 외곽은 항상 바다로 되어 있다. (육지 : 0 , 바다 : 1)
캐릭터는 상하좌우로 움직일 수 있으며, 바다로는 갈 수 없다. 캐릭터 움직임 매뉴얼은 아래와 같다.

1. 현재 위치에서 현재 방향을 기준으로 반시계 방향부터 차례대로 갈 곳을 정한다.
2. 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면 왼쪽 방향으로 회전한 다음 한칸 전진한다. 가보지 않은 칸이 없다면 회전만 수행하고 1단계로 돌아간다
3. 네 방향 모두 가본곳이거나 바다일 경우 방향을 유지한채로 뒤로 한칸 가고 1단계로 돌아간다. 만약 뒤쪽 방향이 바다라면 움직임을 멈춘다.

- 입력예시
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1

- 출력예시
"""

# 맵 크기 초기화
n, m = map(int, input().split())

# 2차원 배열 같은 경우 컴프리핸션을 이용한다.
# visit 방문한 장소를 저장하기 위한 초기맵 세팅. 0 : 미방문, 1 : 방문
visit = [[0] * m for _ in range(n)]

# 현재 캐릭터의 초기좌표와 방향을 지정
x, y, direction = map(int, input().split())

# 초기위치는 방문한것으로 표시
visit[x][y] = 1

# 맵 입력받기
array = []
for i in range(n):
  # 맵을 2차원 배열로 만드는 동작
  array.append(list(map(int, input().split()))) 

# 일반적으로 방향을 설정하는 문제같은 경우 dx, dy를 따로 리스트로 관리하는것이 좋다.
# 북 동 남 서
dx = [-1, 0, 1, 0];
dy = [0, 1, 0, -1];

def turn_left():
    # 함수 바깥에서 선언된 변수이기 때문에 global 사용
    global direction
    # 왼쪽으로만 회전하기 때문에 1씩 감소한다. 
    direction -= 1

    if direction == -1:
        direction = 3


# 로직시작
# count : 방문횟수
count = 1
# 회전횟수, 회전횟수가 4번인 경우 근처가 모두 가본곳 이기 때문에 멈춰야 한다.
turn_time = 0

while True:
    # 최초 왼쪽으로 한번 회전
    # nx, ny는 현재 위치에서 해당 방향으로 이동한 후의 위치이다.
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 이동한 위치가 바다거나 이미 방문한적이 있으면 다시 회전한다.
    if array[nx][ny] == 1 or visit[nx][ny] == 1:
        turn_time += 1
    # 방문해본적이 없거나 바다가 아닐경우 이동한다. 이때 회전 횟수는 다시 0으로 초기화 해준다.
    else:
        visit[nx][ny] = 1
        x = nx
        y = ny
        turn_time = 0
        count += 1
        continue

    # 4방향 모두 갈수 없을 경우 방향유지한채로 한칸 뒤로 간다
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        # 뒤로 갔을때 바다일 경우 멈춘다.
        if array[nx][ny] == 1:
            break
        else:
            x = nx
            y = ny
        # 회전 횟수는 다시 초기화
        turn_time = 0

print(count)

