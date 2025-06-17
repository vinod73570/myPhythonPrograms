# name ='vinod'
# where = 'india'
# whattosay='vinod "you are good"'
# print(whattosay)
# print(name[0])  # prints the first character



# sentence = """hello dear my name is vinod
# i am from india
# i am a software engineer
# i love coding and i am learning python
# i am a good person"""

# print(sentence)








# import sys

# s = "hello"
# print("Address:", id(s))
# print("Size:", sys.getsizeof(s))













# import sys

# for text in ["a", "ab", "abc", "hello", "hello world", "a" * 100]:
#     print(f"{text!r}: {sys.getsizeof(text)} bytes")






# ------------------------------------- method  of string------------------------------------------
# import sys
# a="viNoD is A VeRY      good   gOod good  %^^&*^*& person #*&%^&%^  23534534  #*&%^&%^"
# print(f"{a!r} length : {len(a)}")

# print(f"converting string {a!r} int upperlatter : {a.upper() }")

# print(f"converting string {a!r} int lowerlatter : {a.lower() }")

# print(a.rstrip("*&^%$#") )
# print(a.replace("good","bad"))


# # split convert string to a list 
# print(a.split("good"))
# print(a.capitalize())
# print(a.center(500))
# print(len(a.center(50)))


a="hello hello my name is vinod hello he hello"
list=a.split(" ")
count=0
for i in range(0,len(list)):
    if(list[i]=="hello"):
        count+=1

print(count)

