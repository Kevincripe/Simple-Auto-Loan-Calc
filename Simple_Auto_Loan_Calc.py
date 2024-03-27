# SDEV-140 Final Project
# author: Kevin Cripe
# started: 2024-02-12
# Auto Loan Comparison Calculator


# Takes popular TKinter loan cal function and 
# modifies the functions to do months instead of years
# dealerships allow you to pick number of months exactly
# I myself pick odd month counts to get certain numbers


from tkinter import *
from tkinter.ttk import *
import webbrowser
from PIL import Image, ImageTk
from tkinter import messagebox 


# def function to open the second window
def open_window1():
    top = Toplevel()
    top.title("ScratchPad")
    top.geometry("400x400")
    top.config(bg='#F0F0F0')
    # creating extra label and close button
    lbl = Label(top, text="Scratchpad").pack()
    btn2 = Button(top, text="Close Window", command=top.destroy).pack()
    # Text box for just taking notes as companion to main widget
    scratchpad = Text(top, height=200, width=200).pack()

# def function to open the third window
def open_window2():
    top = Toplevel()
    top.title("Links")
    top.geometry("400x400")
    top.config(bg='#F0F0F0')
    #Define a callback function to use browser in window
    def callback(url):
        webbrowser.open_new_tab(url)
    # creating extra label and close button
    lbl = Label(top, text="Links").pack()
    btn2 = Button(top, text="Close Window", command=top.destroy).pack()
    #Create a Label to display the link bind link to url
    link = Label(top, text="www.autotrader.com",font=('Helveticabold', 15), cursor="hand2")
    link.pack()
    link.bind("<Button-1>", lambda e:
    callback("http://www.autotrader.com"))
    #Create a 2nd Label to display the 2nd link bind link to url
    link2 = Label(top, text="www.cars.com",font=('Helveticabold', 15), cursor="hand2")
    link2.pack()
    link2.bind("<Button-1>", lambda e:
    callback("http://www.cars.com"))
  
# create class
class LoanCalculator:
    # init  class
    def __init__(self):

        # Create a root
        root = Tk() 

        # Set title and windows size default
        root.title("Auto Loan Comparison Calculator") 
        root.geometry("700x400")
        root.config(bg='#F0F0F0')

        # Instance 1 of calc LEFT Pane
        # create the input text boxes and their alignment 
        Label(root, text = "Annual Interest Rate").grid(row = 2, column = 1, sticky = W)
        Label(root, text = "Number of Months").grid(row = 3, column = 1, sticky = W)
        Label(root, text = "Loan Amount").grid(row = 4, column = 1, sticky = W)
        Label(root, text = "Monthly Payment").grid(row = 5, column = 1, sticky = W)
        Label(root, text = "Total Paid").grid(row = 6, column = 1, sticky = W)

        # Instance 2 of calc RIGHT Pane
        # create the input text boxes and their alignment 
        Label(root, text = "Annual Interest Rate").grid(row = 2, column = 11, sticky = W)
        Label(root, text = "Number of Months").grid(row = 3, column = 11, sticky = W)
        Label(root, text = "Loan Amount").grid(row = 4, column = 11, sticky = W)
        Label(root, text = "Monthly Payment").grid(row = 5, column = 11, sticky = W)
        Label(root, text = "Total Paid").grid(row = 6, column = 11, sticky = W)
 
        # for taking inputs On LEFT Pane Calc  all loan variables
        self.annualInterestRateVarL = StringVar() 
        Entry(root, textvariable = self.annualInterestRateVarL, justify = RIGHT).grid(row = 2, column = 2)
        self.numberOfMonthsVarL = StringVar()
        Entry(root, textvariable = self.numberOfMonthsVarL, justify = RIGHT).grid(row = 3, column = 2)
        self.loanAmountVarL = StringVar()
        Entry(root, textvariable = self.loanAmountVarL, justify = RIGHT).grid(row = 4, column = 2)
        self.monthlyPaymentVarL = StringVar()
        lblMonthlyPaymentL = Label(root, textvariable = self.monthlyPaymentVarL).grid(row = 5,column = 2, sticky = E)
        self.totalPaymentVarL = StringVar()
        lblTotalPaymentL = Label(root, textvariable = self.totalPaymentVarL).grid(row = 6, column = 2, sticky = E)

        # for taking inputs On RIGHT Pane Calc all loan variables
        self.annualInterestRateVarR = StringVar() 
        Entry(root, textvariable = self.annualInterestRateVarR, justify = RIGHT).grid(row = 2, column = 12)
        self.numberOfMonthsVarR = StringVar()
        Entry(root, textvariable = self.numberOfMonthsVarR, justify = RIGHT).grid(row = 3, column = 12)
        self.loanAmountVarR = StringVar()
        Entry(root, textvariable = self.loanAmountVarR, justify = RIGHT).grid(row = 4, column = 12)
        self.monthlyPaymentVarR = StringVar()
        lblMonthlyPayment = Label(root, textvariable = self.monthlyPaymentVarR).grid(row = 5,column = 12, sticky = E)
        self.totalPaymentVarR = StringVar()
        lblTotalPayment = Label(root, textvariable = self.totalPaymentVarR).grid(row = 6, column = 12, sticky = E)
         
        # create the calculate payment button on LEFT Pane Calc
        btCalculatePaymentL = Button(root, text = "Calculate Payment", command = self.calculatePaymentL).grid(row = 7, column = 2, sticky = E) 

        # create the calculate payment button on RIGHT Pane Calc
        btCalculatePaymentR = Button(root, text = "Calculate Payment", command = self.calculatePaymentR).grid(row = 7, column = 12, sticky = E) 

        # buttons for manipulating additional windows
        btn = Button(root, text="Open Scratch Pad", command=open_window1).grid(row = 8, column = 2, sticky = E) 
        # button to Links window
        btn_links = Button(root, text="Open Links", command=open_window2).grid(row = 8, column = 12, sticky = E) 

        # button to close the window
        main_close_btn = Button(root, text="Close Window", command=root.destroy).grid(row = 9, column = 2, sticky = E) 

        # Load and display an image 
        image = Image.open('happy_car.jpg')
        image = ImageTk.PhotoImage(image)

        # Create a label to display the image
        image_label = Label(root, image=image)
        image_label.grid(row = 15, column = 2, sticky = W)

        # Create an event loop
        root.mainloop() 
 
    # Define functions for calc payment both calcs are seperate
        # lEFT pane
    def calculatePaymentL(self):
        # Error catching by try-except 
        try:
            monthlyPaymentL = self.getMonthlyPaymentL(
            float(self.loanAmountVarL.get()),
            float(self.annualInterestRateVarL.get()) / 1200,
            int(self.numberOfMonthsVarL.get()))
            # put outputs into the LEFT output lanes
            self.monthlyPaymentVarL.set(format(monthlyPaymentL, '10.2f'))
            totalPaymentL = float(self.monthlyPaymentVarL.get()) * int(self.numberOfMonthsVarL.get())
            self.totalPaymentVarL.set(format(totalPaymentL, '10.2f'))
        # if non num entered except will trigger and show alert box    
        except ValueError: messagebox.showerror("showerror", "Invalid Input, use only Numbers")

        # RIGHT pane
    def calculatePaymentR(self):
        # Error catching by try-except 
        try:
            monthlyPaymentR = self.getMonthlyPaymentR(
            float(self.loanAmountVarR.get()),
            float(self.annualInterestRateVarR.get()) / 1200,
            int(self.numberOfMonthsVarR.get()))
            # put outputs into the RIGHT output lanes
            self.monthlyPaymentVarR.set(format(monthlyPaymentR, '10.2f'))
            totalPaymentR = float(self.monthlyPaymentVarR.get()) * int(self.numberOfMonthsVarR.get())
            self.totalPaymentVarR.set(format(totalPaymentR, '10.2f'))
        # if non num entered except will trigger and show alert box    
        except ValueError: messagebox.showerror("showerror", "Invalid Input, use only Numbers")
    
        # calculate the monthly payment LEFT Pane.
    def getMonthlyPaymentL(self, loanAmountL, monthlyInterestRateL, numberOfMonthsL): 
        # If block to catch zero Interest Rate
        if monthlyInterestRateL == 0:
            monthlyPaymentL = (loanAmountL/numberOfMonthsL)
            return monthlyPaymentL;
    
        else:
            # If there is an interest rate this proceeds
            monthlyPaymentL = loanAmountL * monthlyInterestRateL / (1- 1 / (1 + monthlyInterestRateL) ** (numberOfMonthsL))

            # return the needed variable
            return monthlyPaymentL;
                    
     # calculate the monthly payment RIGHT Pane.
    def getMonthlyPaymentR(self, loanAmountR, monthlyInterestRateR, numberOfMonthsR): 
        # If block to catch zero Interest Rate
        if monthlyInterestRateR == 0:
            monthlyPaymentR = (loanAmountR/numberOfMonthsR)
            return monthlyPaymentR;
    
        else:
            # If there is an interest rate this proceeds
            monthlyPaymentR = loanAmountR * monthlyInterestRateR / (1- 1 / (1 + monthlyInterestRateR) ** (numberOfMonthsR))

            # return the needed variable
            return monthlyPaymentR;
    
# call the class to run the program.
LoanCalculator()
