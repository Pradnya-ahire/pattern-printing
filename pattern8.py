n=6
# for i in range(1,n)
#     for k in range(1,i):
#         print(" ",end = " ")
#     for j in range(1,2*(n-i)):
#         print("*",end=" ")
#     print()

n=6

for i in range(n-1,0,-1):
    for k in range(1,n-i):
        print(" ",end = " ")
    for j in range(1,i*2):
        print("*",end=" ")
    print()


