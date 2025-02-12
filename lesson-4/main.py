# Python strings
s = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

#print(s)


b = 'Hello World'
# cắt chuỗi - str[start:stop:step]
#print(b[0:5]) # Hello
#print(b[:5]) # Do start không chuyền mặc định sẽ là 0 nên kết quả sẽ là: Hello
#print(b[0::2]) # Do step = 2 thì khi cắt sẽ loại bỏ 2 kí tự mỗi lần. Kết quả là: HloWrd
#print(b[-5:]) # -5 Kí tự sẽ là W, stop ko nhập sẽ mặc định là lấy hết chuỗi kết quả: World
# -1 là kí tự d | -2 là kí tự l | ... -5 là kí tự W
#print(b[-1])
#print(b[-2])
#print(b[-5])

# Modify Strings
# print(b.upper())
# print(b.lower())
# print(b.split()) # ['Hello', 'World']
#print(b.replace('d', 'q')) # Hello Worlq
# print(" xxx ".strip()) # xxx
#print('Hello ' + 'Python') # Hello Python
#print(1 + '2') # TypeError
# print(1 + int('2')) # 3

# Format strings

name = 'John'
age = 18
txt = f"My name is {name}, I am {age}"
# print(txt) # My name is John, I am 18

price = 59
txt = f"The price is {price:.3f} dollars"
# print(txt) #The price is 59.000 dollars

# Escape Characte
'''
    \\
    \'
    \n
    \t
    \b
    ...
'''

# print('Hello\tWorld\nI\'m Quoc')

txt = 'xyz'
# print(len(txt))

# Url string methods: https://www.w3schools.com/python/python_strings_methods.asp
