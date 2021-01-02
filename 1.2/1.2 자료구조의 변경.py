# 자료구조의 변경
# 커피숍
menu = {"커피", "우유", "주스"} #{}여서 set(집합) 형태이다
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))