python = "Python is Amazing"
print(python.lower()) # 소문자로 출력
print(python.upper()) # 대문자로 출력
print(python[0].isupper()) #첫번째가 대문자가 맞으면 true
print(len(python)) #길이가 얼마인지 반환
print(python. replace("Python","Java")) #원하는 문자 바꾸기

index = python.index("n")
print(index) # 파이썬 안에서 n이 몇번째에 있는지 확인 
index = python.index("n", index + 1) #앞에서 찾은 위치이후부터 찾는것 +1은 index start위치 
print(index)

print(python.find("Java")) # 원하는 값이 없을 경우 -1을 출력
# print(python.index("Java")) # index로 찾을경우 원하는 값이 없으면 바로 error을 내보낸다

print(python.count("n")) # 몇개가 들어갔는지 확인하기