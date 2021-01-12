# print("Python", "Java", "JavaScript", sep="vs") # sep이 없을때는 , 이후 띄어쓰기가 되늗네 sep가 있으면 사이에 들어가게된다.
# print("Python", "Java", sep="vs", end="?") # end가 추가되면 두문장이 같이 출력된다.
# # print("무엇이 더 재밌을까요?")
# import sys
# print("Python", "Java", file=sys.stdout) # 표준 출력
# print("Python", "Java", file=sys.stderr) # 표준 에러

# # 시험 성적
# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items(): # scores.item 식으로하면 키 와 벨류를 쌍으로 튜플형식으로 출력할수있다.
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":") # ljust(8) 은 왼쪽에서 8칸떨어진 곳에서 왼쪽정렬을 해달라 

# 은행 대기 순번표
# # 001, 002, 003, .....
# for num in range(1,21):
#     print("대기번호 : " + str(num).zfill(3)) # zfill은 3의 공간을 확보를하고 나머지 빈공간은 0으로 채운다.

answer = input("아무 값이나 입력하세요 : ") # 항상 문자열 형태로 값을 받게 된다.
print(type(answer))
# print("입력하신 값은" + answer + "입니다." )