# # for i in range(1,6):
 
# #     for k in range(1,6):
# #         if(k==5 or i==1 or i==k):
# #             print("*",end=" ")
# #         else:
# #             print("-",end=" ")
# #     print()





# # # Pyramid of Numbers 
# # rows = 5
# # num = 1

# # for i in range(1, rows + 1):
# #     print(" " * (rows - i), end="")
# #     for j in range(i):
# #         print(num, end=" ")
# #         num += 1
# #     print()






# # # Right-Angled Triangle with Characters
# # rows = 4
# # ch = 65  

# # for i in range(1, rows + 1):
# #     for j in range(i):
# #         print(chr(ch), end=" ")
# #         ch += 1
# #     print()



# # # Inverted Triangle with Characters


# # rows = 5
# # ch = 65

# # for i in range(rows, 0, -1):
# #     for j in range(i):
# #         print(chr(ch), end=" ")
# #         ch += 1
# #     print()




# # # Hollow Right-Angled Triangle with Characters
# # rows = 5

# # for i in range(1, rows + 1):
# #     for j in range(1, i + 1):
# #         if j == 1 or j == i or i == rows:
# #             print(chr(64 + j), end=" ")  
# #         else:
# #             print(" ", end=" ")
# #     print()






# # ----------------------------------------------------------------date 29 may 2025--------------------------------------------------  






# # quetion -1.
# num=1
# for i in range (1,5):
#     for j in range(i,5):
#         print(num ,end=" ")
#         num+=1
#     print()





# #  quetion -2.
# ch=65
# for i in range (1,5):
#     for j in range(i):
#         print(chr(ch) ,end=" ")
#         ch+=1
#     print()




# # quetion -3

# for i in range (1,5):
#     num=1
#     for j in range(1,6-i):
#         print(num ,end=" ")
#         num+=1
#     print()






# #  quetion -4.

# for i in range (1,4):
#     ch=66
#     for j in range(1,5-i):
#         print(ch ,end=" ")
#         ch+=1
#     print()




# #  quetion -5.

# for i in range (1,5):
#     num=1
#     for j in range(i):
#         print("?" ,end=" ")
#         ch+=1
#     for j in range(1,5-i):
#         print(num ,end=" ")
#         num+=1
#     print()


# #  quetion -5.

# for i in range (1,5):
#     num=1
#     for j in range(1,6-i):
#         print(num ,end=" ")
#         num+=1
#     for j in range(i-1):
#         print("*" ,end=" ")
#         ch+=1
    
#     print()


# quetion -6.
# num=1
# value=10
# for i in range (1,value):
   
#     if i<=value//2 :
#          for j in range(1,6-i+1):
#             print("*" ,end="")
#     else:
#         for j in range(value//2,i+1):
#             print("*" ,end="")

        
   
       
#     num+=1
    
    
#     print()



# quetion -7.

num=1
value=10
for i in range (1,value):
   
    if i<=value//2 :
         for j in range(i-1):
            print(" " ,end="")
         
         for j in range(1,value//2-i+2):
            print("*" ,end="")
    else:

        for j in range(i,value-1):
            print(" " ,end="")
        for j in range(value//2-1,i):
            print("*" ,end="")

        
   
       
    num+=1
    
    
    print()
