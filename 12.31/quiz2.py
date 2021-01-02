# 퀴즈 - 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

#예) http://naver.com
# 규칙1 : http:// 부분은 제외
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
# 예) 생성된 비밀번호 : nave 51!

#내가 푼 답
# name = "http://naver.com" 
# print("생성된 비밀번호 :"+ name[7:10]+ str(len(name[7:-4]))+str(name[7:-4].count("e"))+"!")

#url = "http://youtube.com"
url = "http://google.com"
my_str = url.replace("http://","") # 규칙 1
my_str = my_str[:my_str.index(".")] # 0~5 직전까지. 규칙 2
# print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다".format(url,password))