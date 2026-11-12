# for i in range(5):

#     for k in range(5):
#         if k < 5-i:
#             print(" ", end=" ")
#         if 5-i <= k:
#             print("*", end=" ")
       
#     print("*",end=" ")
    
    
#     for j in range(0,i):
#         print("*", end=" ")
#     print( )




# for i in range(-5,1):
   
#     for m in range(5):
#         if m>= -i:
#             print(" ", end=" ")

#     for k in range(0,-i):
#             print("*", end=" ")
       
       
#     print("*",end=" ")  

#     for j in range(0,-i):
#         print("*", end=" ")
#     print( )      
  

# n = 5

# for i in range(0, n + 1):
#     print(" "* (n-i) + "* " * (i+1) )
# for j in range(n-1,-1,-1):      
#     print(" "* (n-j) + "* " * (j+1) )


def naturalNum(n):
    total = 0
    for i in range(1,n+1):
        
        if i <= 0:
            print('invaide number',i)
        else: 
            total += i
    return total

print(naturalNum(-10))