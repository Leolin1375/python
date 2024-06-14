# #!/usr/bin/python3

# list = ['red', 'green', 'blue', 'yellow', 'white', 'black']
# print( list[0] )
# print( list[1] )
# print( list[2] )

# #!/usr/bin/python3

# list = ['red', 'green', 'blue', 'yellow', 'white', 'black']
# print( list[-1] )
# print( list[-2] )
# print( list[-3] )

#!/usr/bin/python3

nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(nums[0])
print(nums[1])
print(nums[2])

print(nums[0:4])


print("=" * 24)


index_to_print = 2555
if index_to_print < len(nums):
    print(nums[index_to_print])
else:
    print(f"索引 {index_to_print} 超出範圍")
