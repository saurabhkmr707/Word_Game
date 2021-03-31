import tkinter as tk

class Example():
    def __init__(self):
        self.root = tk.Tk()
        # self.table = tk.Frame(self.root)
        # self.table.pack(fill="both", expand=True)
        self.entry_vals = [[0 for i in range(4)] for i in range(10)]

        self.rows = []
        for row in range(10):
            row_entries = []
            self.rows.append(row_entries)
            for column in range(4):
                entry = tk.Entry(self.root)
                entry.grid(row=row, column=column)
                row_entries.append(entry)

                entry.bind("<Return>", self.handle_enter)

    def handle_enter(self, event):
        # get the row and column of the entry that got the event
        entry = event.widget
        row = int(entry.grid_info()['row'])
        column = int(entry.grid_info()['column'])

        self.entry_vals[row][column] = entry.get()
        entry = self.rows[row][column]
        entry.config(state = 'disabled')
        # compute the new row; either the next row or circle
        # back around to the first row
        new_row = row+1 if row+1 < len(self.rows) else 0

        # get the entry for the new row, and set focus to it
        entry = self.rows[new_row][column]
        entry.focus_set()

example = Example()
tk.mainloop()
list = example.entry_vals
for row in list:
    for val in row:
        print (val, end = " ")
    print ("")