#type csating

# a = "1" - this is a integers number
# b= 2 this is a string number

# so agar hame num ko add karana hai to to num string form me honea chahiye 

a = "1"
b = "2"
print(a+b)
# ye 1+2 = 12 ho jyega 
a = 1
b = 2
print(a+b)
# ye 1+2 = 3 hoaga 
# ese codisons me hame string ko integer me convert krna hoga tabhi work karega 

a = "1"
b = "2"
print(int(a) + int(b))

string = "15"
number = 7
string_number = int(string) 
# THROWS AN ERROE IF THE STRING IS NOT A VALID INTEGER
sum = number + string_number
print("the sum num of both numbers is :" ,sum )

# implicit typecasting
c = 1.9 
d = 8

print(c+d)