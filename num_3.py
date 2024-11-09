#10989. 수 정렬하기 3

import sys
input = sys.stdin.readline

counts = [0] * 10001  # 1부터 10000까지의 자연수 배열 생성

N = int(input().strip())  # 첫째 줄에 수의 개수 N을 입력받아 정수로 변환
for _ in range(N):
    num = int(input().strip())  # 한 줄에 하나씩 숫자를 입력
    counts[num] += 1  	# 입력받은 숫자를 인덱스로 하여 해당 위치의 값을 1 증가

for num in range(1, 10001):		# 숫자 1부터 10,000까지 차례로 반복
    if counts[num] > 0:		# 해당 숫자의 빈도가 0보다 클 경우
        for _ in range(counts[num]):
            print(num)  # 숫자 num을 빈도만큼 한 줄에 하나씩 출력
