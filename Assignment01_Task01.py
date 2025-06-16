#TASK 1

print("Instructions : Please enter 2 numbers. Decimal Numbers are allowed. "
      "\nDo not enter 0 as a number in input or else the script will give validation error.")
number1 = float(input("Please Enter your First Number : "))
number2 = float(input("Please Enter your Second Number : "))

print("The result of Addition for",number1, "and", number2, "is : ", round(number1 + number2,2))
print("The result of Subtraction for",number1, "and", number2, "is : ", round(number1 - number2,2))
print("The result of Multiplication for",number1, "and", number2, "is : ", round(number1 * number2,2))
print("The result of Division for",number1, "and", number2, "is : ", round(number1 / number2,2))