
num1=int(input("Enter value 1:"))
num2=int(input("Enter value 2:"))
opr=input("Enter the opr...(+,-,*,/,%)")

if opr=="+":
   print(num1+num2)
if opr=="-":
   print(num1-num2)
if opr=="*":
  print(num1*num2)
if opr=="/":
  print(num1/num2)
if opr=="%":
  print(num1%num2)

else:
  print("invalid opr...")