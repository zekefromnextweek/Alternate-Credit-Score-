import tkinter
import random
import sqlite3
window=tkinter.Tk()
def practice():
    conn = sqlite3.connect('D:\\Alternate-Credit-Score-\\Alt_Credit.db')
    c=conn.cursor()
    c.execute('''select i_name, count(distinct b_OverdraftDate)
    from indvidual,payments,bankstatement
    where i_id= p_key and
    p_key=b_id
    group by i_name
    ''')
    rows = c.fetchall()
    for row in rows:
        print('ji')
    conn.close()
