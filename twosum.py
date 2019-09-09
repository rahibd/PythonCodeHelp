array_length = int(input("Array length = "))
target_numbers = int(input("Target = "))
a_numbers = []
# x = len(a_numbers)
# print(a_numbers[1])
# print(x)
for x in range(array_length):
    a = int(input("array number = "))
    a_numbers.insert(x + 1, a)
#  print(x)
# print(a_numbers)
# list.insert(index, elem)

i = 0
j = len(a_numbers) - 1
while i < j:
  two_sum = a_numbers[i] + a_numbers[j]
  if two_sum == target_numbers:
    break
  if two_sum > target_numbers:
    j -= 1
  else:
    i += 1
print(i, j)
