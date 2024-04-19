nums = []
a = int(input())
b = int(input())

for i in range(a, b+1):
  if i % 13 != 0:
    nums.append(i)

resul = sum(nums)

print(resul)
