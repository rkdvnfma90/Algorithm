"""

"""

n,k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# a는 오름차순으로, b는 내림차순으로 정렬한다.
a = sorted(a)
b = sorted(b, reverse=True)


# 바꿔치기를 k 번 진행 한다.
for i in range(k):
  # b의 원소가 a의 원소보다 크면 스왑한다.
  if a[i] < b[i]:
    a[i] , b[i] = b[i], a[i]
  # a의 원소가 b의 원소보다 크거나 같으면 반복문 탈출한다.
  else:
    break

print(sum(a))
