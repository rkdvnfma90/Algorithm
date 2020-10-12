def binary_search(arr,target,start,end):
  # 시작점이 끝점보다 커지면 return
  if start > end:
    return None
  
  mid = int((start + end) / 2)

  # 찾고자하는 값이 중간값과 같으면 바로 return
  if arr[mid] == target:
    return mid

  # 찾고자 하는 값이 중간값 보다 크다면 오른쪽을 대상으로만 찾는다.
  elif target > arr[mid]:
    return binary_search(arr,target,mid+1,end)
  
  # 찾고자 하는 값이 중간값 보다 작다면 왼쪽을 대상으로만 찾는다.
  else :
    return binary_search(arr,target,start,mid-1)
  
# 원소의 갯수와 찾고자하는 값을 입력받음
n, target = list(map(int, input().split()))
arr = list(map(int, input().split()))

result = binary_search(arr,target,0,n-1)

if result == None:
  print('원소가 존재하지 않습니다.')
else:
  print('해당원소는 ', str(result+1) , '번째에 위치합니다.') 
