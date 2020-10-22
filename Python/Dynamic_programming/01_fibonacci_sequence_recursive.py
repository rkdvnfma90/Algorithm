"""
피보나치수열 재귀적
"""

# 한번 계산된 값을 메모이제이션 하기 위한 리스트 초기화
d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    
    # 이미 계산된 적이 있으면 그 값을 바로 리턴한다.
    if d[x] != 0:
        return d[x]
    
    # 아직 계산하지 않은 값이라면 점화식에 의해 재귀적으로 피보나치 함수를 호출한다.
    d[x] = fibo(x - 1) + fibo(x - 2)

    return d[x]

print(fibo(99))
    
