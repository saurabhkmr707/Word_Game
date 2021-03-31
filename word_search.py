def read_file(path):
    file = open(path,"r")
    words_list = file.readlines()
    words_list = set(words_list)
    file.close()
    return words_list

def search_word(word, words_list):
    if word in words_list:
        return "Found"
    return "Not Found"

# def check_all_words(row,col,words_list):
#     found_words = []
#     up = down = i
#     left = right = j
#
#     # processing all words vertically
#     while()
    




# def func(x):
#     x = x + " where"
#     return
#
# x = "hello"
# func(x)
# print (x)

if __name__ == '__main__':
    path = 'data/20k.txt'
    words_list = read_file(path)
    word = "zebra"
    word = word.lower()
    # print (word)
    print (search_word(word+"\n",words_list))

