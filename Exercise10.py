def extract_digits_reverse(num):
    return list(map(int, str(num)))[::-1]

num = 987654321
digits = extract_digits_reverse(num)
print(digits)









