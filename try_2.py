try :
  n =int(input("enter a number"))
  a=10/n
except ZeroDivisionError:
    print("number is zero")
else :
    print("number is non zero")
finally:
  print("it is test for a number if zero or not")
