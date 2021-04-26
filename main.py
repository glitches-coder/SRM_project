######## GLOBAL DECLARATION ##########
from tkinter import *
from tkinter import ttk
import sqlite3 as sq

############## Databse INTEGRATION #####################
cnect_db = sq.connect('database.db')
cur = cnect_db.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS DATA
(
    FirstName TEXT,
    LastName TEXT,
    Email TEXT,
    Mobile TEXT,
    Country TEXT,
    City TEXT,
    State TEXT,
    PinCode TEXT,
    ClassX_Board TEXT,
    ClassX_year of passing TEXT, 
    ClassX_Percentage TEXT
)''')
cur.close()
cnect_db.commit()
cnect_db.close()


def fetchdets():
    global cnect_db
    global cur
    print("\n")
    print("Registration Information")
    print("\n")

    print("First Name:", first_ent.get())
    print("Last Name", last_ent.get())
    print("Email:", email_ent.get())
    print("Mobile:", num_ent.get())
    print("Country:", country_ent.get())
    print("City:", city_ent.get())
    print("State:", state_ent.get())
    print("Pin Code:", pincode_ent.get())
    print("Class X_Board:", brdl1.get())
    print("Class X_Percentage:", perc1.get())
    print("Class X_year of passing:", yrpass1.get())

    cnect_db = sq.connect('database.db')
    cur = cnect_db.cursor()
    cur.execute("Insert into DATA values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
                % (first_ent.get(), last_ent.get(), email_ent.get(),
                   num_ent.get(), country_ent.get(), city_ent.get(),
                   state_ent.get(), pincode_ent.get(), brdl1.get(),
                   perc1.get(), yrpass1.get()))
    cur.close()
    cnect_db.commit()
    cur.close()
#    Address TEXT,
# , text.get()
    # print("Address:", text.get())
########## Main Events ########
PURPLE = '#695bca'
window = Tk()
window.config(width=570, height=750, bg=PURPLE)
frame = Frame(window, bg=PURPLE)
frame.grid(column=1, row=3, sticky='W')
frame1 = Frame(window)
frame1.grid(column=1, row=6, sticky='W')
frame2 = Frame(window)
frame2.grid(column=1, row=13, sticky='W')
frame3 = Frame(window)
frame3.grid(column=1, row=14, sticky='W')
frame4 = Frame(window)
frame4.grid(column=1, row=15, sticky='W')
frame4 = Frame(window)
frame4.grid(column=1, row=16, sticky='W')
frame5 = Frame(window, bg=PURPLE)
frame5.grid(column=0, row=24, sticky='W')
frame6 = Frame(window, bg=PURPLE)
frame6.grid(column=2, row=26, sticky='W')
frame7 = Frame(window, bg=PURPLE)
frame7.grid(column=1, row=24, sticky='W')

####################FUNCTIONS and Variables###########################
v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
v4 = IntVar()
v5 = IntVar()
v6 = IntVar()
v7 = IntVar()

################ HEADER #######################

heading = Label(window, text='STUDENT REGISTRATION FORM', fg=PURPLE, font=("Ubuntu Mono", 15))
heading.grid(column=2, row=0, padx=10, pady=10, sticky='W')

##################### Label Section ####################

firstname = Label(window, text='FIRST NAME', fg='white', bg=PURPLE, font=("Ubuntu Mono", 12))
firstname.grid(column=0, row=1, padx=(10, 30), pady=5, sticky='W')
first_ent = Entry(window)
first_ent.grid(column=1, row=1, sticky='W')
firstname_2 = Label(window, text=' (max 30 characters a-z and A-z)', fg='white', bg=PURPLE, font=("Ubuntu Mono", 12))
firstname_2.grid(column=2, row=1, sticky='W')

lastname = Label(window, text='LAST NAME', fg='white', bg=PURPLE, font=("Ubuntu Mono", 12))
lastname.grid(column=0, row=2, padx=(10, 30), pady=5, sticky='W')
last_ent = Entry(window)
last_ent.grid(column=1, row=2, sticky='W')
lastname_2 = Label(window, text=' (max 30 characters a-z and A-z)', fg='white', bg=PURPLE, font=("Ubuntu Mono", 12))
lastname_2.grid(column=2, row=2, sticky='W')

dob = Label(window, text='DATE OF BIRTH', fg='white', bg=PURPLE, font=("Ubuntu Mono", 12))
dob.grid(column=0, row=3, padx=(10, 30), pady=5, sticky='W')
dlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
         31]

Combo = ttk.Combobox(frame, values=dlist, width=4)
Combo.set("Day")
Combo.pack(side=LEFT, padx=2)

mlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

Combo1 = ttk.Combobox(frame, values=mlist, width=4)
Combo1.set("Month")
Combo1.pack(side=LEFT, padx=2)

ylist = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007,
         2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]

Combo2 = ttk.Combobox(frame, values=ylist, width=4)
Combo2.set("Year")
Combo2.pack(side=LEFT, padx=2)

emailname = Label(window, text='EMAIL ID', fg='white', bg=PURPLE, font=("Ubuntu Mono", 12))
emailname.grid(column=0, row=4, padx=(10, 30), pady=5, sticky='W')
email_ent = Entry(window)
email_ent.grid(column=1, row=4, sticky='W')

mobile_num = Label(window, text='MOBILE NUMBER', fg='white', bg=PURPLE, font=("Ubuntu Mono", 12))
mobile_num.grid(column=0, row=5, padx=(10, 30), pady=5, sticky='W')
num_ent = Entry(window)
num_ent.grid(column=1, row=5, sticky='W')
num_2 = Label(window, text='(10 digit number)', fg='white', bg=PURPLE, font=("Ubuntu Mono", 13))
num_2.grid(column=2, row=5, sticky='W')

gender = Label(window, text='GENDER', fg='white', bg=PURPLE, font=("Ubuntu Mono", 13))
gender.grid(column=0, row=6, padx=(10, 30), pady=5, sticky='W')

R1 = Radiobutton(frame1, variable=v5, value=1, bg=PURPLE, activebackground=PURPLE, cursor='dot', highlightthickness=0)
R1.pack(side=LEFT)

btn1 = Label(frame1, text='MALE', fg='white', bg=PURPLE, font=("Ubuntu Mono", 13))
btn1.pack(side=LEFT)

R2 = Radiobutton(frame1, variable=v5, value=2, bg=PURPLE, activebackground=PURPLE, cursor='dot', highlightthickness=0)
R2.pack(side=LEFT)

btn2 = Label(frame1, text='FEMALE', fg='white', bg=PURPLE, font=("Ubuntu Mono", 13))
btn2.pack(side=LEFT)

address = Label(window, text='ADDRESS', fg='white', bg=PURPLE, font=("Ubuntu Mono", 12))
address.grid(column=0, row=7, padx=(10, 30), pady=5, sticky='W')

text = Text(window, height=4, width=26)
text.grid(column=1, row=7, pady=10, sticky='W')

city = Label(window, text='CITY', fg='white', bg=PURPLE, font=("Ubuntu Mono", 12))
city.grid(column=0, row=8, padx=(10, 30), pady=5, sticky='W')
city_ent = Entry(window)
city_ent.grid(column=1, row=8, sticky='W')
city_2 = Label(window, text=' (max 30 characters a-z and A-z)', fg='white', bg=PURPLE, font=("Ubuntu Mono", 12))
city_2.grid(column=2, row=8, sticky='W')

pincode = Label(window, text='PIN CODE', fg='white', bg=PURPLE, font=("Ubuntu Mono", 12))
pincode.grid(column=0, row=9, padx=(10, 30), pady=5, sticky='W')
pincode_ent = Entry(window)
pincode_ent.grid(column=1, row=9, sticky='W')
pincode_2 = Label(window, text=' (6 digit number)', fg='white', bg=PURPLE, font=("Ubuntu Mono", 12))
pincode_2.grid(column=2, row=9, sticky='W')

state = Label(window, text='STATE', fg='white', bg=PURPLE, font=("Ubuntu Mono", 12))
state.grid(column=0, row=10, padx=(10, 30), pady=5, sticky='W')
state_ent = Entry(window)
state_ent.grid(column=1, row=10, sticky='W')
state_2 = Label(window, text=' (max 30 characters a-z and A-z)', fg='white', bg=PURPLE, font=("Ubuntu Mono", 12))
state_2.grid(column=2, row=10, sticky='W')

country = Label(window, text='COUNTRY', fg='white', bg=PURPLE, font=("Ubuntu Mono", 12))
country.grid(column=0, row=12, padx=(10, 30), pady=5, sticky='W')
country_ent = Entry(window)
country_ent.insert(0, "India")
country_ent.grid(column=1, row=12, sticky='W')

hobbies = Label(window, text='Hobbies', fg='white', bg=PURPLE, font=("Ubuntu Mono", 12))
hobbies.grid(column=0, row=13, padx=(10, 30), pady=5, sticky='W')

H1 = Checkbutton(frame2, variable=v1, bg=PURPLE, activebackground=PURPLE, cursor='dot', highlightthickness=0)
H1.pack(side=LEFT)

btnh1 = Label(frame2, text='Drawing', fg='white', bg=PURPLE, font=("Ubuntu Mono", 13), highlightthickness=0)
btnh1.pack(side=LEFT)

H2 = Checkbutton(frame2, variable=v2, bg=PURPLE, activebackground=PURPLE, cursor='dot', highlightthickness=0)
H2.pack(side=LEFT)

btnh2 = Label(frame2, text='Singing', fg='white', bg=PURPLE, font=("Ubuntu Mono", 13), highlightthickness=0)
btnh2.pack(side=LEFT)

H3 = Checkbutton(frame3, variable=v3, bg=PURPLE, activebackground=PURPLE, cursor='dot', highlightthickness=0)
H3.pack(side=LEFT)

btnh3 = Label(frame3, text='Dancing', fg='white', bg=PURPLE, font=("Ubuntu Mono", 13), highlightthickness=0)
btnh3.pack(side=LEFT)

H4 = Checkbutton(frame3, variable=v4, bg=PURPLE, activebackground=PURPLE, cursor='dot', highlightthickness=0)
H4.pack(side=LEFT)

btnh4 = Label(frame3, text='Sketching', fg='white', bg=PURPLE, font=("Ubuntu Mono", 13), highlightthickness=0)
btnh4.pack(side=LEFT)

btnh5 = Label(frame4, text='Others', fg='white', bg=PURPLE, font=("Ubuntu Mono", 13), highlightthickness=0)
btnh5.pack(side=LEFT)

H5 = Checkbutton(frame4, variable=v6, bg=PURPLE, activebackground=PURPLE, cursor='dot', highlightthickness=0)
H5.pack(side=LEFT)

btnhe = Entry(frame4, font=("Ubuntu Mono", 13), width=13)
btnhe.pack(side=LEFT)

qual = Label(window, text='QUALIFICATION', fg='white', bg=PURPLE, font=("Ubuntu Mono", 12))
qual.grid(column=0, row=17, padx=(10, 20), pady=5, sticky='W')

s_num = Label(window, text='Sl.No', fg='white', bg=PURPLE, font=("Ubuntu Mono", 12))
s_num.grid(column=1, row=17, pady=5, sticky='W')

no1 = Label(window, text='1', fg='white', bg=PURPLE, font=("Ubuntu Mono", 12))
no1.grid(column=1, row=18, pady=5, sticky='W')

no2 = Label(window, text='2', fg='white', bg=PURPLE, font=("Ubuntu Mono", 12))
no2.grid(column=1, row=19, pady=5, sticky='W')

no3 = Label(window, text='3', fg='white', bg=PURPLE, font=("Ubuntu Mono", 12))
no3.grid(column=1, row=20, pady=5, sticky='W')

no4 = Label(window, text='4', fg='white', bg=PURPLE, font=("Ubuntu Mono", 12))
no4.grid(column=1, row=21, pady=5, sticky='W')

Exam = Label(window, text='Examination', fg='white', bg=PURPLE, font=("Ubuntu Mono", 12))
Exam.grid(column=2, row=17, pady=5, sticky='W')

no1_e = Label(window, text='Class X', fg='white', bg=PURPLE, font=("Ubuntu Mono", 12))
no1_e.grid(column=2, row=18, pady=5, sticky='W')

no2_e = Label(window, text='Class XII', fg='white', bg=PURPLE, font=("Ubuntu Mono", 12))
no2_e.grid(column=2, row=19, pady=5, sticky='W')

no3_e = Label(window, text='Graduation', fg='white', bg=PURPLE, font=("Ubuntu Mono", 12))
no3_e.grid(column=2, row=20, pady=5, sticky='W')

no4_e = Label(window, text='Masters', fg='white', bg=PURPLE, font=("Ubuntu Mono", 12))
no4_e.grid(column=2, row=21, pady=5, sticky='W')

board = Label(window, text='Board', fg='white', bg=PURPLE, font=("Ubuntu Mono", 12))
board.grid(column=3, row=17, padx=(10, 30), pady=5, sticky='W')

brdl1 = Entry(window)
brdl1.grid(column=3, row=18, sticky='W')

brdl2 = Entry(window)
brdl2.grid(column=3, row=19, sticky='W')

brdl3 = Entry(window)
brdl3.grid(column=3, row=20, sticky='W')

brdl4 = Entry(window)
brdl4.grid(column=3, row=21, sticky='W')

percent = Label(window, text='Percentage', fg='white', bg=PURPLE, font=("Ubuntu Mono", 12))
percent.grid(column=4, row=17, padx=(10, 30), pady=5, sticky='W')

perc1 = Entry(window)
perc1.grid(column=4, row=18, sticky='W', padx=9)

perc2 = Entry(window)
perc2.grid(column=4, row=19, sticky='W', padx=9)

perc3 = Entry(window)
perc3.grid(column=4, row=20, sticky='W', padx=9)

perc4 = Entry(window)
perc4.grid(column=4, row=21, sticky='W', padx=9)

yr_pass = Label(window, text='Year of Passing', fg='white', bg=PURPLE, font=("Ubuntu Mono", 12))
yr_pass.grid(column=5, row=17, padx=(10, 30), pady=5, sticky='W')

yrpass1 = Entry(window)
yrpass1.grid(column=5, row=18, sticky='W')

yrpass2 = Entry(window)
yrpass2.grid(column=5, row=19, sticky='W')

yrpass3 = Entry(window)
yrpass3.grid(column=5, row=20, sticky='W')

yrpass4 = Entry(window)
yrpass4.grid(column=5, row=21, sticky='W')

crs = Label(frame5, text='COURSES', fg='white', bg=PURPLE, font=("Ubuntu Mono", 12))
crs.pack()

appl_f = Label(frame5, text='APPLIED FOR', fg='white', bg=PURPLE, font=("Ubuntu Mono", 12))
appl_f.pack(side=BOTTOM, padx=(10, 20))

button_s = Button(frame6, text='Submit', font=("Ubuntu Mono", 10), command=fetchdets)
button_s.pack(side=LEFT, pady=(0, 10), padx=8)

button_r = Button(frame6, text='Reset', font=("Ubuntu Mono", 10))
button_r.pack(side=LEFT, pady=(0, 10))

co1 = Radiobutton(frame7, variable=v7, value=8, bg=PURPLE, activebackground=PURPLE, cursor='dot')
co1.pack(side=LEFT)

bc1 = Label(frame7, text='BCA', fg='white', bg=PURPLE, font=("Ubuntu Mono", 13))
bc1.pack(side=LEFT)

co2 = Radiobutton(frame7, variable=v7, value=9, bg=PURPLE, activebackground=PURPLE, cursor='dot')
co2.pack(side=LEFT)

bc2 = Label(frame7, text='B.Com', fg='white', bg=PURPLE, font=("Ubuntu Mono", 13))
bc2.pack(side=LEFT)

co3 = Radiobutton(frame7, variable=v7, value=10, bg=PURPLE, activebackground=PURPLE, cursor='dot')
co3.pack(side=LEFT)

c3 = Label(frame7, text='B.Sc', fg='white', bg=PURPLE, font=("Ubuntu Mono", 13))
c3.pack(side=LEFT)
co4 = Radiobutton(frame7, variable=v7, value=11, bg=PURPLE, activebackground=PURPLE, cursor='dot')
co4.pack(side=LEFT)

c4 = Label(frame7, text='B.A', fg='white', bg=PURPLE, font=("Ubuntu Mono", 13))
c4.pack(side=LEFT)

mainloop()
