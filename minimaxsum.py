import sys
arr = input().rstrip().split()
runningSum = 0
runningSum = 0
min = -1
max = 0
for num in arr:
    num = int(num)
    if num < min or min == -1:
        min = num
    if num > max: 
        max = num
    runningSum += num
print((runningSum - max),(runningSum - min))

