try:
    a=int(input('enter your first number :'))
    b=int(input('enter your second number :'))

    result = a/b
    print('result : ',result)

except ZeroDivisionError:
    if a == 0:
        print('first value is 0')
    else:
        print('second value is 0')    

       
except ValueError:

    print('invald value given') 

except Exception as e:
    print('error occur ::',e)  

else:
    print('program excuted successfully') 

finally:

    print('program excution completed !')          