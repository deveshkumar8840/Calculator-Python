print(" simple calculator")
num1=float(input("enter first number:"))
op=input("enter operator(+ , _ , * , / ):")
num2= float(input("enter second number:"))
if op == "+":
    print("Result = " ,num1+num2)
elif op == "-":
    print("Result=",num1-num2)
elif op =="*":
    print("Result=",num1*num2)
elif op =="/":
    print("Result=",num1/num2)
else:
    print("Invalid operator")