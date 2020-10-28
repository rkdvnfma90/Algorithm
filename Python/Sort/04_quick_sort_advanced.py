arr = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(arr):
    # 리스트가 1개 이하의 요소를 가지고 있으면 그 리스트를 리턴함
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0] # 피벗
    tail = arr[1:] # 피벗을 제외한 나머지 리스트

    # 분할된 왼쪽부분
    left_side = [x for x in tail if x <= pivot]

    # 분할된 오른쪽부분
    right_side = [x for x in tail if x > pivot]

    # 분할 이후 왼쪽부분과 오른쪽 부분에서 각각 정렬을 수행하고 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(arr))