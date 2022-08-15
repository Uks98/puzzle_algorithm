
# # 평균은 넘겠지 
# #대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.
# #첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
# #둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

# n = int(input())
# for i in range(n):
#     newscore = 0
#     cnt = 0
#     student = input()
#     score = list(map(int,input().split(" ")))
#     newscore = sum(score) // int(student)
#     for index in score:
#         if index > newscore:
#             cnt += 1
#         rate = cnt / int(student) * 100
#     print(f'{rate:.3f}%')

#세준이는 기말고사를 망쳤다. 세준이는 점수를 조작해서 집에 가져가기로 했다. 일단 세준이는 자기 점수 중에 최댓값을 골랐다. 이 값을 M이라고 한다. 그리고 나서 모든 점수를 점수/M*100으로 고쳤다.
#예를 들어, 세준이의 최고점이 70이고, 수학점수가 50이었으면 수학점수는 50/70*100이 되어 71.43점이 된다.
#세준이의 성적을 위의 방법대로 새로 계산했을 때, 새로운 평균을 구하는 프로그램을 작성하시오.

# number = int(input())
# n = list(map(int,input().split()))
# score_list = []

# for i in range(number):
#     for index in n:
#         avg = index / max(n) * 100
#         score_list.append(avg)
#         result = sum(score_list)/number
#     print(result) 

# n = int(input())  # 과목 수
# test_list = list(map(int, input().split()))
# max_score = max(test_list)

# new_list = []
# for score in test_list :
#     new_list.append(score/max_score *100)  # 새로운 점수 생성
# test_avg = sum(new_list)/n
# print(test_avg)

#두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다. 
#수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

# arr = []
# for i in range(3):
#     x = int(input())
#     arr.append(x % 42)
# arr = set(arr)
# print(len(arr))

#Python 2, Python 3, PyPy, PyPy3: def solve(a: list) -> int
#a: 합을 구해야 하는 정수 n개가 저장되어 있는 리스트 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)
#리턴값: a에 포함되어 있는 정수 n개의 합 (정수)

# x = list(map(int,input().split(" ")))
# def solve(lists):
#     return sum(lists)