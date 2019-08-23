import tkinter
import random
import sqlite3
from tkinter import *
from tkinter import ttk
#creates tkinter window
window=tkinter.Tk()
title=tkinter.Label(window,text='Welcome to the Alaternative Credit Score Generator')
title.pack(fill=BOTH, expand=True)
#connects to sqlite database
conn = sqlite3.connect('D:\\Alternate-Credit-Score-\\Alt_Credit.db')
c=conn.cursor()
#this will retrieve the number of late payments and convert them into ints

def latePayments(id):
    c.execute('''select p_lateCount
    from indvidual,payments
    where i_id= p_key and
    p_rentDate between '2019-07-01'and '2019-07-31'
    and p_key={}'''.format(id))
    phist1=c.fetchone()
    #creates tuple but i want an int
    #missed payments of month 1
    newInt1=int(phist1[0])
    c.execute('''select p_lateCount
    from indvidual,payments
    where i_id= p_key and
    p_rentDate between '2019-08-01'and '2019-08-31'
    and p_key={}'''.format(id))
    phist2=c.fetchone()
    #misspayments of month 2
    newInt2=int(phist2[0])
    c.execute('''select count(distinct b_OverdraftDate)
    from indvidual,payments,bankstatement
    where i_id=p_key and
    p_key=b_id and b_id ={}'''.format(id))
    overDraftcount = c.fetchone()
    #number of overdrafts
    newInt3=int(overDraftcount[0])
    return newInt1,newInt2,newInt3
def calculateScore(id,paymentHistory1,paymentHistory2,bankHistory):
    ##This will calculate the credit Score
    score=650
    if(paymentHistory1==0 or paymentHistory2==0):
        score=score+25
    elif(paymentHistory1==0 and paymentHistory2==0):
        score=score+75
    elif(paymentHistory1>0 or paymentHistory2>0):
        score=score-(25*(paymentHistory1+paymentHistory2))
    elif(bankHistory>1):
        score=score-10
    if(score>=550):
        print('Good news! he/she is not a risky client. His/Her score is ', score)
        strscore=str(score)
        message2=tkinter.Label(window,text='Good news! he/she is not a risky client. His/Her score is '+strscore)
        message2.pack(fill=BOTH, expand=True)

    else:
        strscore=str(score)
        print('I am sorry to inform you that he/she is a risky client. His/Her score is ',score)
        message2=tkinter.Label(window,text='I am sorry to inform you that he/she is a risky client. His/Her score is '+strscore)
        message2.pack(fill=BOTH, expand=True)



def mainFunction():
    #i want to get a random id each time the program executes
    id=random.randint(1,6)
    #passed in variables from previous function
    newInt1,newInt2,newInt3=latePayments(id)
    c.execute('''select i_name as name, sum(distinct p_lateCount) as latePayments, count(distinct b_OverdraftDate) as numofOverDrafts
    from indvidual,payments,bankstatement
    where i_id=p_key and
    p_key=b_id and b_id ={}'''.format(id))
    rows = c.fetchall()

    for row in rows:
        #each variable is displayed as a tuple when retrieving from database so they are converted into strings
        name=str(row[0])
        latePayment=str(row[1])
        numofOverDrafts=str(row[2])
        label1.configure(text='Name: '+name)
        label2.configure(text='Num of late payments: '+latePayment)
        label3.configure(text='Num of bank overdrafts: '+numofOverDrafts)
        message.configure(text='The individual named '+name+' has '+latePayment+' late payments and '+numofOverDrafts+' overdrafts over the past 2 months.')
        print('The individual named ',name,'has',latePayment,'late payments and',numofOverDrafts,'overdrafts over the past 2 months.')
    calculateScore(id,newInt1,newInt2,newInt3)

buttonDisplay=tkinter.Button(window,text='Display Individual and their Information',command=mainFunction)
buttonDisplay.pack(fill=BOTH, expand=True)
message=tkinter.Label(window)
message.pack(fill=BOTH, expand=True)
#button to exit prgram
buttonQuit=tkinter.Button(window,text='leave program',command=quit)
buttonQuit.pack(side=BOTTOM,fill=BOTH, expand=True)

label1=tkinter.Label(window)
label2=tkinter.Label(window)
label3=tkinter.Label(window)
label1.pack(fill=BOTH, expand=True)
label2.pack(fill=BOTH, expand=True)
label3.pack(fill=BOTH, expand=True)


window.mainloop()
#exit database connection
conn.close()
