# for i in range(1,6):
 
#     for k in range(1,6):
#         if(k==5 or i==1 or i==k):
#             print("*",end=" ")
#         else:
#             print("-",end=" ")
#     print()


rows = 4
ch = 65  # ASCII for 'A'

for i in range(1, rows + 1):
    for j in range(i):
        print(f"{chr(ch)}({ch})", end=" ")
        ch += 1
    print()
