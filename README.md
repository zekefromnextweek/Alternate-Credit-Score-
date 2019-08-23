# Alternate-Credit-Score-
  This program will create and run an alternate credit score on various indivduals to see if they are 'risky' clients or not.<br />
I will create the data needed in an sqlite database and use tkinter for the GUI. The alternative credit score that I will be<br />
implementing will range from 100-800. 800 being excellent and 100 being terrible. 

  The factors that are making up the credit score will be: <br />
    -bank overdrafts<br />
    -insurance payments<br />
    -child support and or alimony<br />
    -household utility payments<br />
    -cell phone payments<br />
    -rent payments<br />
    
  Each late payment will resort in subtracting points from their score and, on-time payments will add to their score. <br />
    To make the scoring system a bit more simple, I will only be using two months worth of payments.<br />
# Instructions-
First thing is to make sure that the database and the python file are in the same folder or the program won't run.<br />
I also put the complete directory when connecting to the database in my code so change this to mirror the filepath that you have for your database. <br />
After that run thr program in the terminal.(cd.... to get to the directory you put the file) To run it just type scoreCreator.py <br />
after you are in the proper directory. Then a window will appear prompting you to push a button. Press the button and a person from the<br /> databse will get their score calculated.
