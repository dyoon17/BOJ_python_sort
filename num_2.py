# 2751. 수 정렬하기 2 

import sys  
input = sys.stdin.read  # input() 함수 대신 sys.stdin.read를 사용하여 한번에 처리

# 공백과 개행 문자로 분리해 리스트로 변환
data = input().split()  # split()을 사용하여 공백을 기준으로 나눔
N = int(data[0])  # 리스트의 첫 번째 요소 N을 정수형으로 변환하여 저장
numbers = list(map(int, data[1:]))  # 나머지 데이터는 정수형으로 변환하여 리스트로 저장

numbers.sort()  # 내장 함수를 사용하여 정렬

print("\n".join(map(str, numbers)))		# 정렬된 숫자 리스트를 문자열로 변환하고 각 숫자를 한 줄에 하나씩 출력
