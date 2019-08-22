import tkinter
import random
import sqlite3
window=tkinter.Tk()
title=tkinter.Label(window,text='Welcome to the Alaternate Credit Score Generator')
title.pack()
conn = sqlite3.connect('D:\\Alternate-Credit-Score-\\Alt_Credit.db')
c=conn.cursor()
def practice():

    c.execute('''select i_name, count(distinct b_OverdraftDate)
    from indvidual,payments,bankstatement
    where i_id= p_key and
    p_key=b_id
    group by i_name
    ''')
    rows = c.fetchall()
    for row in rows:
        str.configure(text=rows)
    conn.close()

button=tkinter.Button(window,text='Display names',command=practice)
button.pack()
str=tkinter.Label(window)
str.pack()
window.mainloop()
def calculateScore(randomId,paymentHistory,bankHistory):
    ##This will calculate the credit Score
    randomId=random.randint(1,6)
    score=800
    if():
