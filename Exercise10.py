def extract_digits_reverse(num):
  return [int(d) for d in str(num)][::-1]

num = 12345
digits = extract_digits_reverse(num)
print(digits)

















