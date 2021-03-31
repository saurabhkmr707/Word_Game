from tkinter import *
from word_search import *

class Table:

    def __init__(self, root, n_rows, n_cols):

        # code for creating table
        self.entry_list = []  # list of lists containing rows and columns
        self.entry_vals = [[0 for i in range(n_cols)] for i in range(n_rows)]

        for i in range(n_rows):
            rows = []
            for j in range(n_cols):
                e = Entry(root,  width=2, fg='blue',
                               font=('Arial', 16, 'bold'))

                e.grid(row=i, column=j)
                # e.insert(END, lst[i][j])
                e.bind("<Return>", self.on_change)
                # root.bind("<Return>", lambda eff: rand_func(eff, a=10, b=20, c=30))
                rows.append(e)
            self.entry_list.append(rows)

    def on_change(self, event):
        # self.entry_vals[i][j] = func.widget.get()
        # print(func.widget.get())
        entry = event.widget
        row = int(entry.grid_info()['row'])
        column = int(entry.grid_info()['column'])
        small_alpha = 'abcdefghijklmnopqrstuvwxyz'
        small_alpha = [char for char in small_alpha]
        capital_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        capital_alpha = [char for char in capital_alpha]

        inp = entry.get()
        if len(inp) != 1:
            return
        if not ((inp in small_alpha) | (inp in capital_alpha)) :
            # print (inp not in small_alpha)
            return


        self.entry_vals[row][column] = inp

        entry = self.entry_list[row][column]
        entry.config(state='disabled')
        found_words = []
        found_words += check_all_words(row,column, words_list, self.entry_vals)
        # print (found_words)


if __name__ == "__main__":
    # find total number of rows and
    # columns in list
    path = 'data/20k.txt'
    words_list = read_file(path) # todo choose a better data source with minimal and very frequent words
    total_rows = 10
    total_columns = 10

    # create root window
    window = Tk()
    window.title('GUI')
    window.geometry('350x350')

    # Code to set the window in the middle of the screen
    # Gets the requested values of the height and widht.
    windowWidth = window.winfo_reqwidth()
    windowHeight = window.winfo_reqheight()
    # print("Width", windowWidth, "Height", windowHeight)

    # Gets both half the screen width/height and window width/height
    positionRight = int(window.winfo_screenwidth() / 2 - windowWidth / 2)
    positionDown = int(window.winfo_screenheight() / 2 - windowHeight / 2)

    # Positions the window in the center of the page.
    window.geometry("+{}+{}".format(positionRight, positionDown))


    t = Table(window, total_rows, total_columns)

    window.mainloop()
    for i in range(total_rows):
        for j in range(total_columns):
            print (t.entry_vals[i][j], end = " ")
        print ("")
