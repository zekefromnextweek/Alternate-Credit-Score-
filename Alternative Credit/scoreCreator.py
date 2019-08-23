import tkinter
import random
import sqlite3
window=tkinter.Tk()
title=tkinter.Label(window,text='Welcome to the Alaternate Credit Score Generator')
title.pack()
conn = sqlite3.connect('D:\\Alternate-Credit-Score-\\Alt_Credit.db')
c=conn.cursor()
def latePayments(id):
    c.execute('''select p_lateCount
    from indvidual,payments
    where i_id= p_key and
    p_rentDate between '2019-07-01'and '2019-07-31'
    and p_key={}'''.format(id))
    phist1=c.fetchone()
    #creates tuple but i want an int
    str1=int(phist1[0])
    print(str1)
    c.execute('''select p_lateCount
    from indvidual,payments
    where i_id= p_key and
    p_rentDate between '2019-08-01'and '2019-08-31'
    and p_key={}'''.format(id))
    phist2=c.fetchone()
    str2=int(phist2[0])
    print(str2)
    c.execute('''select count(distinct b_OverdraftDate)
    from indvidual,payments,bankstatement
    where i_id=p_key and
    p_key=b_id and b_id ={}'''.format(id))
    overDraftcount = c.fetchone()
    str3=int(overDraftcount[0])
    print(str3)
    return str1,str2,str3
def calculateScore(id,paymentHistory1,paymentHistory2,bankHistory):
    ##This will calculate the credit Score
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
#rename this

def practice():
    id=random.randint(1,6)
    str1,str2,str3=latePayments(id)
    c.execute('''select *
    from indvidual,payments,bankstatement
    where i_id=p_key and
    p_key=b_id and b_id ={}'''.format(id))
    rows = c.fetchall()
    for row in rows:
        str.configure(text=row)
        print(row)
    #latePayments(id)
    calculateScore(id,str1,str2,str3)
##will come back to this later this is gui stuff
button=tkinter.Button(window,text='Display Individual and Info',command=practice)
button.pack()
str=tkinter.Label(window)
str.pack()
window.mainloop()
practice()
conn.close()
