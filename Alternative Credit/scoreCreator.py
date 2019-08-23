import tkinter
import random
import sqlite3
window=tkinter.Tk()
title=tkinter.Label(window,text='Welcome to the Alaternate Credit Score Generator')
title.pack()
conn = sqlite3.connect('D:\\Alternate-Credit-Score-\\Alt_Credit.db')
c=conn.cursor()

def calculateScore(randomId,paymentHistory1,paymentHistory2,bankHistory):
    ##This will calculate the credit Score
    randomId=random.randint(1,6)
    score=650
    if(paymentHistory1==0 or paymentHistory2==0):
        score=score+25
    elif(paymentHistory1==0 and paymentHistory2==0):
        score=score+75
    elif(paymentHistory1>0 or paymentHistory2>0):
        score=score-(50*(paymentHistory1+paymentHistory2))
    elif(bankHistory>1):
        score=score-15
    if(score>550):
        print('Good news! You are not a risky client. Your score is ', score)
    else:
        print('I am sorry to inform you that you are a risky client. Your score is ',score)
def sumPayments():
    sq1=('''p_lateCount
    from indvidual,payments
    where i_id= p_key and p_key=2 and
    p_rentDate between '2019-07-01'and '2019-07-31'
    group by i_name
    ''')
    c.execute(sq1)
    phist1=int(p_lateCount)
    print(phist1)
    print('hi')
def practice():
    c.execute('''select i_name, count(distinct b_OverdraftDate)
    from indvidual,payments,bankstatement
    where i_id=p_key and
    p_key=b_id
    group by i_name''')
    rows = c.fetchall()
    for row in rows:
        #str.configure(text=row)
        print(row)
#calculateScore(1,1,1,1)
##will come back to this later this is gui stuff
'''button=tkinter.Button(window,text='Display names',command=practice)
button.pack()
str=tkinter.Label(window)
str.pack()
window.mainloop()
'''
conn.close()
