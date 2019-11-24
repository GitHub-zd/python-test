num = [1,3,5,6,7,8,13,14,15,17,18,24,30,43,56]
num_input = int(input("请输入要查找的数字:"))
head = 0
tail = len(num)
mid = 0

while tail - head > 1:
    mid = (tail + head)//2
    if num[mid] > num_input:
        tail = mid - 1
    elif num[mid]< num_input:
        head = mid + 1
    else:
        num[mid] == num_input
        break
else:
    if num_input == num[head]:
        mid = head
    else:
        mid = -1
print(mid)
