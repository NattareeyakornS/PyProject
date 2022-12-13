from tkinter import *
import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd
import csv
import matplotlib.pyplot as plt


#for Excel on history frame4
df = pd.read_csv(r'C:\Users\User\OneDrive\Desktop\PyProject\PyProject\Realject\Book2.csv')




#for multi frame
def show_frame(frame):
    frame.tkraise()

# for keep data in frame 3
def keepdata(x, y, z):
    print(x, y, z)
    row=[x, y, z]
    # Keep data in csv file 
    with open('Book2.csv', 'a', newline='') as f:
        cw = csv.writer(f)
        cw.writerow(row)
    f.close()

#for first frame
def login():
    username = "65011396"
    password = "bb"
    if username_entry.get()==username and password_entry.get()==password:
        show_frame(frame2)
    else:
        messagebox.showerror(title="Error", message="Invalid login.")

# for frame 5
def guidance():
    IN = df.loc[df["Type"] =="Income"].sum().Value
    OC = df.loc[df["Type"] =="Outcome"].sum().Value
    if IN*0.6 <= OC:
        messagebox.showinfo(title="You using too much!", message="You using over 60% of your Monthly income! \n!Save more!")
    else:
        messagebox.showinfo(title="Looking good!", message="You expenditure is lower than 60% of your Monthly income! \n!Still Good!")

#for pie chart
def pie():
      t = df.loc[df["Type"] =="Outcome"].groupby('Category')['Value'].sum()
      mylabels =  ["Food", "Daily goods", "Rent", "Transport","Travel"]
      explode = [0, 0, 0, 0, 0]
      colors =['#A7D2CB','#F2D388','#C98474','#874C62','#C58940']
      plt.title("Statement")
      plt.pie(t, labels = mylabels, autopct='%0.2f%%',startangle = 180 ,explode=explode,colors=colors)
      plt.legend(title = "Category:",loc='upper right')
      plt.show()

def pie2():
      f = df.loc[df["Type"] =="Income"].groupby('Category')['Value'].sum()
      mylabels =  ["Income"]
      explode = [0]
      colors =['#A7D2CB']
      plt.title("Statement")
      plt.pie(f, labels = mylabels, autopct='%0.2f%%',startangle = 180 ,explode=explode,colors=colors)
      plt.legend(title = "Category:",loc='upper right')
      plt.show()
      

window = tk.Tk()
window.title("Login form")
window.geometry('700x700')
window.configure(bg='#333333')
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)


frame1 = tk.Frame(window, bg='#333333') #Login
frame2 = tk.Frame(window) #Main Menu
frame3 = tk.Frame(window) #Today Account
frame4 = tk.Frame(window) #History
frame5 = tk.Frame(window) # Guidance
for frame in (frame1, frame2, frame3, frame4, frame5):
    frame.grid(row=0,column=0,sticky='nsew')

#==================Frame 1 code creating

login_label = tk.Label(frame1, text="Login", bg='#333333', fg="#FF3399", font=("Arial", 30))
username_label = tk.Label(frame1, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
username_entry = tk.Entry(frame1, font=("Arial", 16))
password_entry = tk.Entry(frame1, show="*", font=("Arial", 16))
password_label = tk.Label(frame1, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
login_button = tk.Button(frame1, text="Login", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=login)

#==================Frame 1 code placing

login_label.pack(padx = 20, pady =20)
username_label.pack(padx = 20, pady =20)
username_entry.pack(padx = 20, pady =20)
password_label.pack(padx = 20, pady =20)
password_entry.pack(padx = 20, pady =20)
login_button.pack(padx = 20, pady =20)



#==================Frame 2 code creating

frame2_title=  tk.Label(frame2, text='Welcome Nattareeyakorn Sethakit', font='times 20', bg='Black', fg='White')
frame3_button = tk.Button(frame2, text='Today account',command=lambda:show_frame(frame3))
frame4_button = tk.Button(frame2, text='History',command=lambda:show_frame(frame4))
frame5_button = tk.Button(frame2, text='Guidance',command=lambda:show_frame(frame5))
logut_button = tk.Button(frame2, text='Logout',command=lambda:show_frame(frame1))

#==================Frame 2 code placing

frame2_title.pack(fill='x', expand=False, side = TOP)
frame3_button.pack(padx = 20,ipady=15)
frame4_button.pack(padx = 20,ipady=15)
frame5_button.pack(padx = 20,ipady=15)
logut_button.pack(fill='x',ipady=15,side = BOTTOM)



#==================Frame 3 code creating

frame3_title=  tk.Label(frame3, text='Monthly Account',font='times 15', bg='Pink',fg='White')
date_label = tk.Label(frame3, text="Month", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
data_entry = ttk.Combobox(frame3, value= ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],font='times 15')
statement_label = tk.Label(frame3, text="Statement", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
statement_ttk = ttk.Combobox(frame3, value= ['Income','Expense'],font='times 15')
value_label = tk.Label(frame3, text="Value", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
statement_entry = tk.Entry(frame3, font=("Arial", 16))
catagory_label = tk.Label(frame3, text="Catagory", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
catagory_ttk = ttk.Combobox(frame3, value= ['Food','Transport','Travel','Daily Good','Rent','Income'],font='times 15')
test_button = tk.Button(frame3, text='Add',command=lambda:keepdata(data_entry.get(), catagory_ttk.get(), statement_entry.get()))
backtomenu_button = tk.Button(frame3, text='Back to Main menu',command=lambda:show_frame(frame2))

#==================Frame 3 code placing

frame3_title.pack(fill='x', expand=False)
date_label.pack(fill='x', expand=False)
data_entry.pack(fill='x', expand=False)
statement_label.pack(fill='x', expand=False)
statement_ttk.pack(fill='x', expand=False)
value_label.pack(fill='x', expand=False)
statement_entry.pack(fill='x', expand=False)
catagory_label.pack(fill='x', expand=False)
catagory_ttk.pack(fill='x', expand=False)
test_button.pack(fill='x', expand=False)
backtomenu_button.pack(fill='x',ipady=15,side = BOTTOM)

#==================Frame 4 code

test_Label= tk.Label(frame4, text = df, wraplength = 500, justify = LEFT)
test_Label.pack(anchor=W)
test1_button = tk.Button(frame4, text='Expense Pie Chart',command=pie)
test1_button.pack(fill='x', expand=False)
test2_button = tk.Button(frame4, text='Income Pie Chart',command=pie2)
test2_button.pack(fill='x', expand=False)
backtomenu_button = tk.Button(frame4, text='Back to Main menu',command=lambda:show_frame(frame2))
backtomenu_button.pack(fill='x',ipady=15,side = BOTTOM)



#==================Frame 5 code creaing
frame2_title = tk.Label(frame5, text='Need a guidance?', font='times 20', bg='Black', fg='White')
suggests_button = tk.Button(frame5, text='yes', bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=guidance)
backtomenu_button = tk.Button(frame5, text='Back to Main menu',command=lambda:show_frame(frame2))



#==================Frame 5 code placing
frame2_title.pack(fill='x', expand=False, side = TOP)
suggests_button.pack(padx = 40 ,pady = 20,ipady=15)
backtomenu_button.pack(fill='x',ipady=15,side = BOTTOM)





show_frame(frame1)
window.mainloop()