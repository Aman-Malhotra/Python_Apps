from collections import Counter

text = "Hello I am aman and i want to be a computer programmer. Code And i love to code " \
       "and i want to be the best programmer like the best ones out " \
       "there "

words = text.split()

counter = Counter(words)

top_three = counter.most_common(3)
print(top_three)