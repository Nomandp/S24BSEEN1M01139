def check_first_last_same(numbers):
  if len(numbers) < 1:
      print("List is empty")
  elif numbers[0] == numbers[-1]:
      print("First and Last Numbers are same")
  else:
      print("Not Same")

numbers = [1, 2, 3, 4, 5, 6, 1]
check_first_last_same(numbers)













