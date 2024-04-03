def is_palindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]

num = 12323
if is_palindrome(num):
    print("Palindrome")
else:
    print("Not a Palindrome")
















