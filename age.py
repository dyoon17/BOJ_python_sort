#10814. 나이순 정렬

n = int(input())  # 회원 수 입력
user_list = [input().split() for _ in range(n)]  # 나이와 이름 입력하는 리스트 생성

# 나이를 정수로 변환하고 리스트에 저장
user_list = [(int(age), name) for age, name in user_list]

# 나이 기준으로 정렬 (가입 순서를 유지)
user_list.sort(key=lambda x: x[0])

# 결과 출력
for age, name in user_list:
    print(age, name)
