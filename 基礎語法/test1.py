#print("Hello, World!")
#print("Hello, Leo!")
#print('Hello, World!s')

#item_one=1
# item_two=3
# item_three=4

# total = item_one +item_two +item_three

# total = item_one + \
#         item_two + \
#         item_three
str='123456789'

print("str[0] = ",str[0])
print("str[1] = ",str[1])
print("str[2] = ",str[2])
print("str[3] = ",str[3])
print("str[4] = ",str[4])
print("str[5] = ",str[5])
print("str[6] = ",str[6])
print("str[7] = ",str[7])
print("str[8] = ",str[8])
 
print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第六个的字符（不包含）
print(str[2:])             # 输出从第三个开始后的所有字符
print(str[1:5:2])          # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(str * 2)             # 输出字符串两次
print(str + '你好')        # 连接字符串

 
print('------------------------------')
 
print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义