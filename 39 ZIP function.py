# zipping lists

first = ['Aman', 'Aanchal', 'Agam', 'Arun']
last = ['Malhotra', 'Malhotra', 'DeepSingh', 'Sharma']

name = zip(first, last)

del first
del last

for n, m in name:
    print(n, m)
# first and last deleted
# for n in first:
#     print(n)
# for n in last:
#     print(n)