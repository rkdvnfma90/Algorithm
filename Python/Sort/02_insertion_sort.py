"""
삽입정렬
- 특정한 데이터를 적절한 위치에 삽입 한다는 의미에서 삽입정렬 이라고 한다.
- 특정한 데이터가 위치에 들어가기 이전에 그 앞까지의 데이터는 이미 정렬되어 있다고 가정 한다.
- 이러한 규칙을 미뤄보았을때, 맨 끝에서부터 앞으로 이동하면서 자신보다 작은 값을 만나면 그 자리에서 멈추면된다.

"""
arr = [7,5,9,0,3,1,6,2,4,8]

# 맨 첫번째 요소는 정렬되어 있다고 가정
for i in range(1,len(arr)):
  for j in range(i, 0, -1):
    # 배열의 끝에서부터 탐색하여 자기보다 큰 값이면 스왑
    if arr[j] < arr[j-1]:
      arr[j], arr[j-1] = arr[j-1], arr[j]
    # 자기보다 작은 값이면 그 자리에서 멈춤
    else:
      break
      
print(arr)