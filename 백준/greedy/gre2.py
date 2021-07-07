# https://www.acmicpc.net/problem/1931

a = int(input())

lst = []
gap = []
cur = 0
result = 0

for i in range(a):
    x, y = map(int, input().split())

    lst.append((x, y))

# ---------------------------------
# sorted() 인자 없이 사용하면 각 요소 순서대로 정렬 한다.
# 
# 인자에 함수를 넘겨주면 해당 함수의 반환값을 비교하여 순서대로 정렬한다. 
# 
# lst = sorted(lst, key=lambda time: time[0])
# 해당 코드는 lambda 익명함수를 정의하여 time이라는 반환값을 통해서 비교할 아이템을 기준으로 정렬해주는 코드이다 
# time이라는 반환값에 time[0] 요소를 오름차순으로 정렬하는 코드이다
#
# ---------------------------------

# 시작시간 오름차순으로 정렬
lst = sorted(lst, key=lambda time: time[0])

# 종료시간 오름차순으로 정렬
lst = sorted(lst, key=lambda time: time[1])

for i in range(len(lst)):
    if i == 0:
        cur = lst[i][1]
        result += 1
    elif lst[i][0] >= cur:
        cur = lst[i][1]
        result += 1

print(result)
