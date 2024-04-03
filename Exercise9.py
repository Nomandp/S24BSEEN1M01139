def create_new_list(list1, list2):
  return [num for num in list1 if num % 2 != 0] + [num for num in list2 if num % 2 == 0]

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

new_list = create_new_list(list1, list2)
print(new_list)
















