# weather = input("오늘 날씨는 어때요? ") # input은 예를 들어 오늘 날씨는 어떄요? 다음커서에서 기다리고있다.
# if weather == "비" or weather == "눈": # 변수를 추가한다 or 로
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요")

temp = int(input("기온은 어때요? ")) # int를 쓰는이유는 정수를 입력해서 temp라는 값에 저장하기 위해
if 30 <=temp:
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요")
elif 0 <= temp and temp < 10: # 0 <= temp <10 으로 해도 상관 없음
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요")