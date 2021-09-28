arrSize = input()
stringArr = input()
arr = stringArr.split(' ')

portion = 1.0/float(arrSize)
neg = 0
zero = 0
positive = 0
for num in arr:
    num = int(num)
    if num > 0:
        positive += portion
    elif num < 0: 
        neg += portion
    else:
        zero += portion

print('%.6f'%positive)
print('%.6f'%neg)
print('%.6f'%zero)

