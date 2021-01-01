cabinet = {3:"유재석", 100:"김태호"} # key는 3이고 value는 유재석 이라는 뜻
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet[5]) # 5라는 키가 없으면 바로 errro가 나오고 종료된다.
print(cabinet.get(5)) #이것은 종료가 되지않고 none이라는 것이 출력된다.
print(cabinet.get(5,"사용 가능"))

print(3 in cabinet) # True
print(5 in cabinet) # Flase

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())
print(cabinet.values())

# key, values 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)

 

