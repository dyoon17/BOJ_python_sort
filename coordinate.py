#11650. 좌표 정렬하기

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]  # N개의 좌표를 입력받아 [x, y] 형태로 arr 리스트에 저장
# 변수를 쓰지 않기 때문에 _로 표기해 단순히 N번 반복함을 의미
arr.sort()  # x 좌표를 기준으로 오름차순 정렬 + x 좌표가 같다면 두 번째 요소인 y 좌표로 오름차순 정렬

for point in arr:	# point 리스트의 요소를 출력하는데
    print(point[0], point[1])  # 정렬된 좌표 출력
