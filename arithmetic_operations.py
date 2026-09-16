# Angelina Del Vicario
# CMP131
# Week 4
# Lab 2
# Basic Arithmetic Operations
# 9/16/26


print (" Basic Arithmetic Calculatior!")
print ("=======================================")
#ask user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

#calculate the results
add = num1 + num2
sub = num1 - num2
multiply = num1 * num2
power = (num1 ** num2)
average = (num1 + num2) /2

#print all six results
print("__Results__")
print ("Addition: ", add )
print ("Subtraction: " , sub)
print ("Multiplication: " ,multiply)

if num2 != 0:
    division = num1 / num2 
    print( "Division:" , division)

else:
    print ("Error: Cannot Divide By Zero")

print ("Power: " , power )
print ("Average: " , average)

