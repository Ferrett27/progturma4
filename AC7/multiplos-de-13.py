a = int(input())
b = int(input())

def mult_13(a, b):
    nums = []
    for i in range(a, b+1):
        if i % 13 != 0:
            nums.append(i)
    total = sum(nums)
    return total

resul = mult_13(a, b)

print(resul)
