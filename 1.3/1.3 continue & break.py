# absent = [2, 5] # 결석
# for student in range(1, 11): # 1,2,3,4,5,6,7,8,9,10
#     if student in absent: 
#         continue # 아래에있는 문장을 실행시키지 않고 다음 반복으로 skip
#     print("{0}, 책을 읽어봐".format(student))

absent = [2, 5] # 결석
no_book = [7]
for student in range(1, 11): # 1,2,3,4,5,6,7,8,9,10
    if student in absent: 
        continue # 아래에있는 문장을 실행시키지 않고 다음 반복으로 skip
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(no_book))
        break
    print("{0}, 책을 읽어봐".format(student))