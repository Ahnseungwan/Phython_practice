# score_file = open("score.txt","w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt","a", encoding="utf8") # 뒤에더 추가할때는 w가 아니라 a 를쓴다
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100") # print 와는 다르게 줄바꿈이 없어서 \n을 통해서 줄바꿈을 한다.
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline()) # 줄별로 읽기, 한 줄로 읽고 커서는 다음 줄로 이동
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# # score_file.close()
# print(score_file.readline(), end="") # 줄바꿈 하기 싫으면
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# # 만약 파일이 몇줄인지 모를때
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line, end="")

score_file.close()