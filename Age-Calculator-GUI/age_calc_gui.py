# import libraries

import tkinter as tk
from datetime import date

# GUI App class


class App:
    def __init__(self):
        # initialized window
        self.master = tk.Tk()
        self.master.geometry('280x300')
        self.master.configure(bg="lightblue")
        self.master.resizable(0, 0)
        self.master.title('Age Calculator')
        self.statement = tk.Label(self.master)

    def run(self):
        self.l1 = tk.Label(text="Name: ", font="courier 10", bg="lightblue")
        self.l1.grid(row=1, column=0)
        nameValue = tk.StringVar()
        self.nameEntry = tk.Entry(self.master, textvariable=nameValue, relief="solid")
        self.nameEntry.grid(row=1, column=1, padx=10, pady=10)

        self.l2 = tk.Label(text="Year: ", font="courier 10", bg="lightblue")
        self.l2.grid(row=2, column=0)
        yearValue = tk.StringVar()
        self.yearEntry = tk.Entry(self.master, textvariable=yearValue, relief="solid")
        self.yearEntry.grid(row=2, column=1, padx=10, pady=10)

        self.l3 = tk.Label(text="Month: ", font="courier 10", bg="lightblue")
        self.l3.grid(row=3, column=0)
        monthValue = tk.StringVar()
        self.monthEntry = tk.Entry(self.master, textvariable=monthValue, relief="solid")
        self.monthEntry.grid(row=3, column=1, padx=10, pady=10)

        self.l4 = tk.Label(text="Day: ", font="courier 10", bg="lightblue")
        self.l4.grid(row=4, column=0)
        dayValue = tk.StringVar()
        self.dayEntry = tk.Entry(self.master, textvariable=dayValue, relief="solid")
        self.dayEntry.grid(row=4, column=1, padx=10, pady=10)

        self.master.mainloop()


if __name__ == '__main__':
    age_calc = App()
    age_calc.run()
