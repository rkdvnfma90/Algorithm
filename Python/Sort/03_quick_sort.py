arr = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(arr,start,end):
  # 원소가 1개인 경우 종료
  if start >= end:
    return
  
  # 피벗은 맨처음 시작하는 값을 넣는다
  pivot = start
  # 왼쪽과 오른쪽의 인덱스 값. 왼쪽은 피벗값 보다 큰 값을 선택하고 오른쪽은 작은 값을 선택한다.
  left = start + 1
  right = end

  while left <= right:
    # 피벗보다 큰 데이터를 찾을때까지 반복한다 (left)
    while left <= end and arr[left] <= arr[pivot]:
      left += 1
    
    # 피벗보다 작은 데이터를 찾을때까지 반복한다 (right)
    while right > start  and arr[right] >= arr[pivot]:
      right -= 1
    
    # left 와 right가 엇갈렸다면 피벗과 작은값을 스왑
    if left > right:
      arr[pivot], arr[right] = arr[right], arr[pivot]
    # 엇갈리지 않았다면 작은값과 큰 값을 스왑
    else:
      arr[left], arr[right] = arr[right], arr[left]
  
  # 스왑이 된 이후(분할), 피벗보다 작은 값은 왼쪽, 큰값은 오른쪽에 오기 때문에 재귀적으로 다시 호출한다.
  quick_sort(arr,start,right - 1) # 왼쪽
  quick_sort(arr,right + 1, end) # 오른쪽


quick_sort(arr, 0, len(arr) - 1)
print(arr)