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

def check_all_words(row,col,words_list,entry_vals):

    def get_words(mid, full_word):
        n = len(full_word)
        res = []

        for l in range(0,mid+1):
            for r in range(mid,n):
                cur = full_word[l:r+1]
                if cur+"\n" in words_list: #todo remove the \n part from the data file
                    if (len(cur) > 1):
                        res.append(cur)
        return res

    found_words = []
    up = down = row
    left = right = col

    # processing all words vertically
    while(up>=0 and entry_vals[up][col] != 0): #todo check logic here
        up -= 1
    up+=1
    while(down<=9 and entry_vals[down][col] != 0): #todo remove the hard-coded part
        down += 1
    down -= 1
    vertical_word = ""
    for i in range(up,down+1):
        vertical_word += entry_vals[i][col]
    # print (vertical_word)
    found_words += get_words(row-up, vertical_word)

    while(left>=0 and entry_vals[row][left] != 0):
        left -= 1
    left += 1
    while(right <=9 and entry_vals[row][right] != 0):
        right += 1
    right -= 1

    horizontal_word = ""
    for i in range(left,right+1):
        horizontal_word += entry_vals[row][i]
    # print (horizontal_word)

    found_words += get_words(col-left, horizontal_word)
    print (found_words)
    return found_words


if __name__ == '__main__':
    path = 'data/20k.txt'
    words_list = read_file(path)
    word = "asd"
    word = word.lower()
    # print (word)
    print (search_word(word+"\n",words_list))


