#Exception is an abnormal condition that 
#distrupts the normal flow of the program.

#try block contains a block of program statements
#within which an exception might occure

#the corresponding except block executes if an exception 
#of a perticular type occurs within the try block

#Ex 1

print("start")
x=0
try:
  res=10/x
  print(res)
except ZeroDivisionError:
    print("can't div by Zero")
    
print("end")


#Ex 2 : nested try

print("start")

x=0
list1=[1,2,3,4]

try:
  res=10/x
  try:
     print(list1[2])
  except IndexError as ex:
      print(ex)
  print(res)
  
except ZeroDivisionError as ex:
    print(ex)
    
print("end")

#Ex 3 multiple except block


print("start")
x=2
list1=[1,2,3,4]

try:
  res=10/x
  print(list1[4])
  print(res)
  
except ZeroDivisionError as ex:
    print(ex)
    
except IndexError as ex:
      print(ex)
print("end")

#Ex 4


print("start")

x=2
list1=[1,2,3,4]

try:
  res=10/x
  print(list1[4])
  print(res)
  
except (ZeroDivisionError, IndexError) as ex:
    print(ex)
print("end")

#Ex 5 using Exception class

print("start")
x=0
list1=[1,2,3,4]

try:
  res=10/x
  print(list1[4])
  print(res)
  
except Exception as a:
    print(a)
    
print("end")    

#Ex 6 Finally block

#the finally block always executes immediately after try-except block exits.
#the main use   ge of finally block is to do clean up jobs.

print("start")

x=0
list1=[1,2,3,4]

try:
  res=10/x
  print(list1[2])
  print(res)
  
except IndexError as ex :
    print(ex)
    
finally:
    print("finally execute")
    
print("end")


#Ex 7 else bloack

#else is executed after try when there's no exception

print("start")

x=2
list1=[1,2,3,4]

try:
  res=10/x
  print(list1[2])
  print(res)
  
except Exception as ex :
    print(ex)
else:
    print("else block")
finally:
    print("finally execute")
    
print("end")

#Ex 8 raise exception

#raise allows you to throw an exception at any time.

class InvalideAgeError(Exception):
    '''define our own exception'''
    pass

def checkAge(age):
    if type(age)!=int:
        raise InvalideAgeError(f"age must be in int not {type(age)}")

    if age>=18:
        print("valid")
    else:
        print("not valid")


#calling of function

try:
  module2.checkAge('23')
except module2.InvalideAgeError as ex:
   print(ex)



   

        






