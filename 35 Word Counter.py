import requests
from bs4 import BeautifulSoup
import operator


def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, "html.parser")
    for post_text in soup.findAll('a', {'class': 'title'}):
        content = post_text.string
        words = content.lower().split()
        for each_word in words:
            word_list.append(each_word)
    clean_up_list(word_list)


def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        symbols = "~!@#$%^&*()_+`-={}|:\"?<>[]\;'.,/"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
            if len(word) > 0:
                # print(word)
                clean_word_list.append(word)
    # count_words(clean_word_list)
    create_dictionary(clean_word_list)


# def count_words(final_word_list):
#     count = 0
#     fw = open('final word list with counter value .txt', 'w')
#     for i in range(len(final_word_list)-1):
#         if len(final_word_list[i]) > 0:
#             for j in range(1, len(final_word_list)):
#                 if final_word_list[j] is final_word_list[i]:
#                     # final_word_list.remove(final_word_list[j])
#                     count += 1
#                     # final_word_list[j] = ""
#                     # print(final_word_list[i])
#             fw.write(final_word_list[i] + "    count = " + str(count) + "\n")
#             count = 0


def create_dictionary(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for key, value in sorted(word_count.items(), key= operator.itemgetter(0)):
        print(key , value)



start(r'https://thenewboston.com/forum/')
