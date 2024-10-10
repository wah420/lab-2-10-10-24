# Question 1
a = 11
a += 5
type_a = type(a)
print(f"a = {a} and its data type is {type_a}")

#Question 2
a = 11
b = 5
result = a < b
type_result = type(result)
print(f"The result is {result} and the data type is {type_result}")

#Question 3
unit_name = "Level 4 Programming"
print("This unit is", unit_name)
print("The 1st character is", unit_name[0])
print("The 4th charcater is", unit_name[3])
print("The 8th character is", unit_name[7])

#Question 4
greeting_string = ("Welcome to Programming unit! This is level 4 :)")
print(greeting_string)
print("The 1st character of the string is", greeting_string[0] ,"and the 5th character is", greeting_string[4])
print("These are the first 5 characters of the string" , greeting_string[0:5])
print("This is the last character of the string", greeting_string[-1])
print("These are the last 4 characters of the string", greeting_string[-4:])

#Question 5
a = 11.0
print(type(a))
b = "11"
print(type(b))
c = "11" + "11"
print(type(c))
d = "d"
print(type(d))
e = True
print(type(e))
f = "False"
print(type(f))

#Question 6
x = 10.5
x = int(x)
print(type(x))

#Quesiton 7
x = "Look! I will become the best Python programmer"
y = 10
z = 5.5
print(type(x))
print(type(y))
print(type(z))
print("The result is", (y + z), type(y + z))
print("The result is", (y + int(z), type(y + (int(z)))))
print("The result is", (z +float(y), type(z + float(y))))
print(type(str(z)))
print("The result is", x + str(y) + str(z), type(x + str(y) + str (z)))


