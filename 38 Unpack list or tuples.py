# unpacking list
date, item, price = ['December 23 ,2015', 'Bread Gloves', 851]


# tuples
def drop_first_last(grades):
    first, *middle, last = grades
    avg = sum(middle)/len(middle)
    print(avg)


drop_first_last([65, 76, 98, 54, 21])

