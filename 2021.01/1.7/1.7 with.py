# import pickle

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file)) # 따로 close를 할 필요가 없다.

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬 공부를 열심히 하고 있어요.")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())
