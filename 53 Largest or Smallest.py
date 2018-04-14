import heapq

grades = [32, 43, 100, 354, 20, 5]

print(heapq.nlargest(3, grades))
print(heapq.nsmallest(3, grades))


