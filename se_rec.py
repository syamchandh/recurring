import subprocess
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import pandas as pd
from tkinter.messagebox import showinfo
import tkinter.scrolledtext as scrolledtext
from tkinter.filedialog import askopenfilename
import os
import webbrowser
from tkcalendar import Calendar
from tkcalendar import DateEntry
from datetime import date
import mysql.connector
from tkinter import filedialog
import json
import shutil
from math import *
from datetime import timedelta
from datetime import date
import datetime

fbilldb = mysql.connector.connect(
    host="localhost", user="root", password="", database="f_billingsintgrtd", port="3306"
)
fbcursor = fbilldb.cursor()


def reset():
  global root
  root.destroy()


# root.title("F-Billing Revolution 2022(FREE version) | Company database:fbillingdb | User:Administrator")
def log():
    global user_name1
    user_name1=username1.get()
    passwd1=password1.get()
    if user_name1=="" or passwd1=="":
        Label(text='Plz enter both username and password',fg='red').place(x=85,y=260)
    else:
        sql='SELECT * FROM users WHERE username=%s AND password=%s'
        val=(user_name1,passwd1,)
        fbcursor.execute(sql,val)
        if fbcursor.fetchone()is not None:
            # mainpage()
            if user_name1 != "adminstator":
              tab06.destroy()
            else:
              pass
            root.iconify()
        else:
            messagebox.showinfo('Acess denied','Username Or Password Wrong')

  
sql = "select * from users"
fbcursor.execute(sql)
user_log = fbcursor.fetchall()
if not user_log:
  def lo():
    # mainpage()
    root=Tk()
    root.geometry("500x250")
    root.resizable(False, False)
    root.eval('tk::PlaceWindow . center')
    Label(text='Wellocome to F-Billing Revolution 2022',font='arial 13 bold').place(x=100,y=40)
    submitbtn1=Button(text='OPEN NOW', width=20,height=2,command=lo,activeforeground="white",activebackground="black",font='arial 8 bold').place(x=165,y=100)             
else:
    root=Tk()
    root.geometry("500x200")
    root.resizable(False, False)
    root.eval('tk::PlaceWindow . center')
    root.title("F-Billing Revolution 2022")
    p1 = PhotoImage(file = 'images/fbicon.png')
    root.iconphoto(False,p1)
    username1=StringVar()
    password1=StringVar()

    Label(text='Login F-Billing Revolution 2022',font='arial 13 bold').place(x=120,y=15)
    
  
    sql = "select username from users"
    fbcursor.execute(sql)
    user_log_name = fbcursor.fetchall()
    uss1=Label(text='Username').place(x=120,y=65)
    usname_comb = ttk.Combobox(textvariable=username1)
    usname_comb.place(x=220,y=65)
    usname_comb["values"] = user_log_name

    pss1=Label(text='Password').place(x=120,y=105)
    ee2=Entry(textvariable=password1,show='*',width=23).place(x=220,y=105)
    
    submitbtn1=Button(text='Login', width=15,command=log,activeforeground="white",
                   activebackground="black").place(x=250,y=150)


def main_page():
  root.iconify()
  main = Toplevel()
root=Tk()
root.geometry("1360x730")
root.title("F-Billing Revolution 2022(FREE version) | Company database:fbillingdb | User:Administrator")
p1 = PhotoImage(file = 'images/fbicon.png')
root.iconphoto(False, p1)

s = ttk.Style()
s.theme_use('default')
s.configure('TNotebook.Tab', background="#999999", width=20, padding=10)
invoices= PhotoImage(file="images/invoice.png")
orders = PhotoImage(file="images/order.png")
estimates = PhotoImage(file="images/estimate.png")
recurring = PhotoImage(file="images/recurring.png")
purchase = PhotoImage(file="images/purchase.png")
expenses = PhotoImage(file="images/expense.png")
customer = PhotoImage(file="images/customer.png")
product = PhotoImage(file="images/package.png")
reports = PhotoImage(file="images/report.png")
setting = PhotoImage(file="images/setting.png")
tick = PhotoImage(file="images/check.png")
warnin = PhotoImage(file="images/sign_warning.png")
cancel = PhotoImage(file="images/close.png")
saves = PhotoImage(file="images/save.png")
folder = PhotoImage(file="images/folder-black.png")
photo11 = PhotoImage(file = "images/invoice-pvt.png")
customer = PhotoImage(file="images/customer.png")
smslog = PhotoImage(file = "images/smslog.png")
video = PhotoImage(file = "images/video.png")
mark1 = PhotoImage(file="images/mark.png")
mark2 = PhotoImage(file="images/mark2.png")
photo10 = PhotoImage(file = "images/text-message.png")
addnew = PhotoImage(file="images/plus.png")
delete = PhotoImage(file="images/delete_E.png")
tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3=  ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tab5 = ttk.Frame(tabControl)
tab6=  ttk.Frame(tabControl)
tab7 = ttk.Frame(tabControl)
tab8 = ttk.Frame(tabControl)
tab9 =  ttk.Frame(tabControl)
tab10=  ttk.Frame(tabControl)
tabControl.add(tab1,image=invoices,compound = LEFT, text ='Invoices',)
tabControl.add(tab2,image=orders,compound = LEFT, text ='Orders')
tabControl.add(tab3,image=estimates,compound = LEFT, text ='Estimates')
tabControl.add(tab4,image=recurring,compound = LEFT, text ='Recurring')
tabControl.add(tab5,image=purchase,compound = LEFT, text ='Purchase Orders') 
tabControl.add(tab6,image=expenses,compound = LEFT, text ='Expenses')
tabControl.add(tab7,image=customer,compound = LEFT, text ='Customers')
tabControl.add(tab8,image=product,compound = LEFT, text ='Product/Services')
tabControl.add(tab9,image=reports,compound = LEFT, text ='Report')
tabControl.add(tab10,image=setting,compound = LEFT, text ='Settings')
tabControl.pack(expand = 1, fill ="both")




selectall = PhotoImage(file="images/table_select_all.png")
cut = PhotoImage(file="images/cut.png")
copy = PhotoImage(file="images/copy.png")
paste = PhotoImage(file="images/paste.png")

undo = PhotoImage(file="images/undo.png")
redo = PhotoImage(file="images/redo.png")
bold = PhotoImage(file="images/bold.png")

italics = PhotoImage(file="images/italics.png")
underline = PhotoImage(file="images/underline.png")
left = PhotoImage(file="images/left.png")

right = PhotoImage(file="images/right.png")
center = PhotoImage(file="images/center.png")
hyperlink = PhotoImage(file="images/hyperlink.png")
remove = PhotoImage(file="images/eraser.png")


photo = PhotoImage(file = "images/plus.png")
photo1 = PhotoImage(file = "images/edit.png")
photo2 = PhotoImage(file = "images/delete_E.png")
photo3 = PhotoImage(file = "images/export-file.png")
photo4 = PhotoImage(file = "images/seo.png")
photo5 = PhotoImage(file = "images/printer.png")
photo6 = PhotoImage(file = "images/gmail.png")
photo7 = PhotoImage(file = "images/priewok.png")
photo8 = PhotoImage(file = "images/refresh_E.png")
photo9 = PhotoImage(file = "images/sum.png")
photo10 = PhotoImage(file = "images/text-message.png")
recalc = PhotoImage(file="images/recalculate.png")
plus_1 = PhotoImage(file="images/plus_1.png")
minus = PhotoImage(file="images/minus.png")
#generate recurring invoice popups
def generate_recurring_noinvoice(): 
  
  messagebox.showinfo("F-Billing Revolution 2022", "No recurring invoices are ready today")

def generate_recurring_invoice_success(): 
  sql = "select * from invoice where (recurring_period_month =%s OR recurring_period_month =%s)AND status!=%s"
  val = ('month(s)', 'day(s)', 'void')
  fbcursor.execute(sql,val)
  pdata = fbcursor.fetchall()
  # rectotalinput=0

  j = 0
  for i in pdata:
      main_rec_tree.insert(parent='', index='end', iid=i, text='', values=('',i[0], i[26], i[25], i[29], i[20], i[10]))
      j += 1
  #  if result=='ok':  
  messagebox.showinfo("F-Billing Revolution 2022", "Recurring invoices successfully generated.")
 




#print invoice
  
def print_invoice_recurring():

  def property1():
    propert=Toplevel()
    propert.title("Microsoft Print To PDF Advanced Document Settings")
    propert.geometry("670x500+240+150")

    def property2():
      propert1=Toplevel()
      propert1.title("Microsoft Print To PDF Advanced Document Settings")
      propert1.geometry("670x500+240+150")

      name=Label(propert1, text="Microsoft Print To PDF Advanced Document Settings").place(x=10, y=5)
      paper=Label(propert1, text="Paper/Output").place(x=30, y=35)
      size=Label(propert1, text="Paper size").place(x=55, y=65)
      n = StringVar()
      search = ttk.Combobox(propert1, width = 28, textvariable = n )
      search['values'] = ('letter')
      search.place(x=150,y=65)
      search.current(0)
      copy=Label(propert1, text="Copy Count:").place(x=55, y=95)
      nocopy = Spinbox(propert1,from_=0,to=100000000, width=28).place(x=150, y=95)    

      btn=Button(propert1,text="OK", width=10,).place(x=390, y=425)
      btn=Button(propert1,text="Cancel", width=10,).place(x=490, y=425) 




      okbtn=Button(propert1,text="OK", width=10,).place(x=390, y=425)
      canbtn=Button(propert1,text="Cancel", width=10,).place(x=490, y=425)  
      
      
   
    style = ttk.Style()
    style.theme_use('default')
    style.configure('TNotebook.Tab', background="#999999", padding=5)
    property_Notebook = ttk.Notebook(propert)
    property_Frame = Frame(property_Notebook, height=500, width=670)
    property_Notebook.add(property_Frame, text="Layout")
    property_Notebook.place(x=0, y=0)

    name=Label(property_Frame, text="Orientation:").place(x=10, y=5)
    n = StringVar()
    search = ttk.Combobox(property_Frame, width = 23, textvariable = n )
    search['values'] = ('Portrait')
    search.place(x=10,y=25)
    search.current(0)

    text=Text(property_Frame,width=50).place(x=250, y=5,height=350)

    btn=Button(property_Frame, text="Advanced",command=property2).place(x=450, y=370)
    btn=Button(property_Frame,text="OK", width=10,).place(x=390, y=410)
    btn=Button(property_Frame, text="Cancel", width=10,).place(x=490, y=410)  


    
  if(False):
      messagebox.showwarning("FBilling Revelution 2020", "Customer is required, Please select customer for this invoice\nbefore printing")
  elif(False):
      messagebox.showinfo("FBilling Revelution 2020", "Print job has been completed.")
  else:
      print1=Toplevel()
      print1.title("Print")
      print1.geometry("670x400+240+150")
      
      printerframe=LabelFrame(print1, text="Printer", height=80, width=650)
      printerframe.place(x=7, y=5)      
      name=Label(printerframe, text="Name:").place(x=10, y=5)
      e1= ttk.Combobox(printerframe, width=40).place(x=70, y=5)
      where=Label(printerframe, text="Where:").place(x=10, y=30)
      printocheckvar=IntVar()
      printochkbtn=Checkbutton(printerframe,text="Print to file",variable=printocheckvar,onvalue=1,offvalue=0,height=1,width=10)
      printochkbtn.place(x=450, y=30)
      btn=Button(printerframe, text="Properties", width=10,command=property1).place(x=540, y=5)

      pageslblframe=LabelFrame(print1, text="Pages", height=140, width=320)
      pageslblframe.place(x=10, y=90)
      radvar=IntVar()
      radioall=Radiobutton(pageslblframe, text="All", variable=radvar, value="1").place(x=10, y=5)
      radiocpage=Radiobutton(pageslblframe, text="Current Page", variable=radvar, value="2").place(x=10, y=25)
      radiopages=Radiobutton(pageslblframe, text="Pages: ", variable=radvar, value="3").place(x=10, y=45)
      pagecountentry = Entry(pageslblframe, width=23).place(x=80, y=47)
      pageinfolabl=Label(pageslblframe, text="Enter page numbers and/or page ranges\nseperated by commas. For example:1,3,5-12")
      pageinfolabl.place(x=5, y=75)

      copylblframe=LabelFrame(print1, text="Copies", height=140, width=320)
      copylblframe.place(x=335, y=90)
      nolabl=Label(copylblframe, text="Number of copies").place(x=5, y=5)      
      noentry = Entry(copylblframe, width=18).place(x=130, y=5)      
      one=Frame(copylblframe, width=30, height=40, bg="black").place(x=20, y=40)     
      two=Frame(copylblframe, width=30, height=40, bg="grey").place(x=15, y=45)     
      three=Frame(copylblframe, width=30, height=40, bg="white").place(x=10, y=50)      
      four=Frame(copylblframe, width=30, height=40, bg="black").place(x=80, y=40)      
      fiv=Frame(copylblframe, width=30, height=40, bg="grey").place(x=75, y=45)      
      six=Frame(copylblframe, width=30, height=40, bg="white").place(x=70, y=50)      
      collatecheckvar=IntVar()
      collatechkbtn=Checkbutton(copylblframe,text="Collate",variable=collatecheckvar,onvalue=1,offvalue=0,height=1,width=10)
      collatechkbtn.place(x=130, y=70)

      othrlblframe=LabelFrame(print1, text="Other", height=120, width=320)
      othrlblframe.place(x=10, y=235)
      printlb=Label(othrlblframe, text="Print").place(x=5, y=0)
      dropprint = ttk.Combobox(othrlblframe, width=23).place(x=80, y=0)
      orderlb=Label(othrlblframe, text="Order").place(x=5, y=25)
      dropord = ttk.Combobox(othrlblframe, width=23).place(x=80, y=25)
      duplexlb=Label(othrlblframe, text="Duplex").place(x=5, y=50)
      droplex = ttk.Combobox(othrlblframe, width=23).place(x=80, y=50)

      prmodelblframe=LabelFrame(print1, text="Print mode", height=120, width=320)
      prmodelblframe.place(x=335, y=235)
      dropscal = ttk.Combobox(prmodelblframe, width=30).place(x=5, y=5)
      poslb=Label(prmodelblframe, text="Print on sheet").place(x=5, y=35)
      droppos = ttk.Combobox(prmodelblframe, width=10).place(x=155, y=35)

      okbtn=Button(print1, text="Ok", width=10).place(x=460, y=370)
      canbtn=Button(print1, text="Cancel", width=10).place(x=560, y=370)
      


#email
      
def email_invoice_recurring():
  mailDetail=Toplevel()
  mailDetail.title("Invoice E-Mail")
  mailDetail.geometry("1080x550")
  mailDetail.resizable(False, False)
  def my_SMTP():
      if True:
          em_ser_conbtn.destroy()
          mysmtpservercon=LabelFrame(account_Frame,text="SMTP server connection(ask your ISP for your SMTP settings)", height=165, width=380)
          mysmtpservercon.place(x=610, y=110)
          lbl_hostn=Label(mysmtpservercon, text="Hostname").place(x=5, y=10)
          hostnent=Entry(mysmtpservercon, width=30).place(x=80, y=10)
          lbl_portn=Label(mysmtpservercon, text="Port").place(x=5, y=35)
          portent=Entry(mysmtpservercon, width=30).place(x=80, y=35)
          lbl_usn=Label(mysmtpservercon, text="Username").place(x=5, y=60)
          unament=Entry(mysmtpservercon, width=30).place(x=80, y=60)
          lbl_pasn=Label(mysmtpservercon, text="Password").place(x=5, y=85)
          pwdent=Entry(mysmtpservercon, width=30).place(x=80, y=85)
          ssl_chkvar=IntVar()
          ssl_chkbtn=Checkbutton(mysmtpservercon, variable=ssl_chkvar, text="This server requires a secure connection(SSL)", onvalue=1, offvalue=0)
          ssl_chkbtn.place(x=50, y=110)
          em_ser_conbtn1=Button(account_Frame, text="Test E-mail Server Connection").place(x=610, y=285)
      else:
          pass
    
  style = ttk.Style()
  style.theme_use('default')
  style.configure('TNotebook.Tab', background="#999999", padding=5)
  email_Notebook = ttk.Notebook(mailDetail)
  email_Frame = Frame(email_Notebook, height=500, width=1080)
  account_Frame = Frame(email_Notebook, height=550, width=1080)
  email_Notebook.add(email_Frame, text="E-mail")
  email_Notebook.add(account_Frame, text="Account")
  email_Notebook.place(x=0, y=0)

  messagelbframe=LabelFrame(email_Frame,text="Message", height=500, width=730)
  messagelbframe.place(x=5, y=5)
  lbl_emailtoaddr=Label(messagelbframe, text="Email to address").place(x=5, y=5)
  emailtoent=Entry(messagelbframe, width=50).place(x=120, y=5)
  sendemail_btn=Button(messagelbframe, text="Send Email", width=10, height=1,command=addacnt).place(x=600, y=10)
  lbl_carcopyto=Label(messagelbframe, text="Carbon copy to").place(x=5, y=32)
  carcopyent=Entry(messagelbframe, width=50).place(x=120, y=32)
  stopemail_btn=Button(messagelbframe, text="Stop sending", width=10, height=1).place(x=600, y=40)
  lbl_subject=Label(messagelbframe, text="Subject").place(x=5, y=59)
  subent=Entry(messagelbframe, width=50).place(x=120, y=59)

  
  style = ttk.Style()
  style.theme_use('default')
  style.configure('TNotebook.Tab', background="#999999", width=20, padding=5)
  mess_Notebook = ttk.Notebook(messagelbframe)
  emailmessage_Frame = Frame(mess_Notebook, height=350, width=710)
  htmlsourse_Frame = Frame(mess_Notebook, height=350, width=710)
  mess_Notebook.add(emailmessage_Frame, text="E-mail message")
  mess_Notebook.add(htmlsourse_Frame, text="Html sourse code")
  mess_Notebook.place(x=5, y=90)

  btn1=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)

  
  btn2=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
  btn3=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
  btn4=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
  btn5=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=undo).place(x=140, y=1)
  btn6=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=redo).place(x=175, y=1)
  btn7=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=bold).place(x=210, y=1)
  btn8=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=italics).place(x=245, y=1)
  btn9=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=underline).place(x=280, y=1)
  btn10=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=left).place(x=315, y=1)
  btn11=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=right).place(x=350, y=1)
  btn12=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=center).place(x=385, y=1)
  btn13=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=hyperlink).place(x=420, y=1)
  
  btn14=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=remove).place(x=455, y=1)


  dropcomp = ttk.Combobox(emailmessage_Frame, width=12, height=3).place(x=500, y=5)
  dropcompo = ttk.Combobox(emailmessage_Frame, width=6, height=3).place(x=600, y=5)
  mframe=Frame(emailmessage_Frame, height=350, width=710, bg="white")
  mframe.place(x=0, y=28)



  btn1=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)

  
  btn2=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
  btn3=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
  btn4=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
  mframe=Frame(htmlsourse_Frame, height=350, width=710, bg="white")
  mframe.place(x=0, y=28)

  attachlbframe=LabelFrame(email_Frame,text="Attachment(s)", height=350, width=280)
  attachlbframe.place(x=740, y=5)
  htcodeframe=Frame(attachlbframe, height=220, width=265, bg="white").place(x=5, y=5)
  lbl_btn_info=Label(attachlbframe, text="Double click on attachment to view").place(x=30, y=230)
  btn17=Button(attachlbframe, width=20, text="Add attacment file...").place(x=60, y=260)
  btn18=Button(attachlbframe, width=20, text="Remove attacment").place(x=60, y=295)
  lbl_tt_info=Label(email_Frame, text="You can create predefined invoice, order, estimate\nand payment receipt email templates under Main\nmenu/Settings/E-Mail templates tab")
  lbl_tt_info.place(x=740, y=370)

  ready_frame=Frame(mailDetail, height=20, width=1080, bg="#b3b3b3").place(x=0,y=530)
  
  sendatalbframe=LabelFrame(account_Frame,text="E-Mail(Sender data)",height=270, width=600)
  sendatalbframe.place(x=5, y=5)
  lbl_sendermail=Label(sendatalbframe, text="Your company email address").place(x=5, y=30)
  sentent=Entry(sendatalbframe, width=40).place(x=195, y=30)
  lbl_orcompanyname=Label(sendatalbframe, text="Your name or company name").place(x=5, y=60)
  nament=Entry(sendatalbframe, width=40).place(x=195, y=60)
  lbl_reply=Label(sendatalbframe, text="Reply to email address").place(x=5, y=90)
  replyent=Entry(sendatalbframe, width=40).place(x=195, y=90)
  lbl_sign=Label(sendatalbframe, text="Signature").place(x=5, y=120)
  signent=Entry(sendatalbframe,width=50).place(x=100, y=120,height=75)
  confirm_chkvar=IntVar()
  confirm_chkbtn=Checkbutton(sendatalbframe, variable=confirm_chkvar, text="Confirmation reading", onvalue=1, offvalue=0)
  confirm_chkbtn.place(x=200, y=215)
  btn18=Button(account_Frame, width=15, text="Save settings",command=savesettings).place(x=25, y=285)

  sendatalbframe=LabelFrame(account_Frame,text="SMTP Server",height=100, width=380)
  sendatalbframe.place(x=610, y=5)
  servar=IntVar()
  SMTP_rbtn=Radiobutton(sendatalbframe, text="Use the Built-In SMTP Server Settings", variable=servar, value=1)
  SMTP_rbtn.place(x=10, y=10)
  MySMTP_rbtn=Radiobutton(sendatalbframe, text="Use My Own SMTP Server Settings(Recommended)", variable=servar, value=2, command=my_SMTP)
  MySMTP_rbtn.place(x=10, y=40)
  em_ser_conbtn=Button(account_Frame, text="Test E-mail Server Connection")
  em_ser_conbtn.place(x=710, y=110)


def addacnt():  
   messagebox.showinfo("F-Billing Revolution 2022", "No sender email address.\nPlease fill Your company email address textfield under the Account tab.")

def savesettings():  
   messagebox.showinfo("F-Billing Revolution 2022", "Your E-mail configuration settings has been saved.")



#print preview invoice-recurring
# def printpreview():
  #messagebox.showerror("F-Billing Revolution","Customer is required,please select customer for this order before printing.")
  # win= Tk()
#Set the Geometry
  # win.geometry("750x450")
  # win.title("F-Billing Revolution 2022 - Invoice")
  # text= Text(win,width= 80,height=30)
  # text.pack(pady=20)


def printpreviewinvoice_recurring():
  preview = Toplevel()
  preview.title("F-Billing Revolution Invoice Report ")
  p2= PhotoImage(file = "images/fbicon.png")
  preview.iconphoto(False, p1)
  preview.geometry("1800x1800+0+0")
  canvas = Canvas(preview)
  canvas.place(relwidth=1, relheight=1,x=250,y=10) 
  paperheigth = preview.winfo_fpixels('1m') * 297
  paperwidth = preview.winfo_fpixels('1m') * 210
  canvas.create_rectangle(20, 20, 20+paperwidth, 20+paperheigth, outline='', fill='white')  



#convert to invoice
def convert():
  if messagebox.askyesno("Make invoice from Orders", "Are you sure to make invoice from this Orders ") == True:
        messagebox.askyesno("Make invoice from Estimate", "Invoice Creation was Successfull.\n New Invoice is \n Would you like to open this invoice ")
  else:
      messagebox.destroy()
  

#search in invoice 
def search_invoice_recurring():  
    top = Toplevel()     
    top.title("Find Text")   
    top.geometry("600x250+390+250")
    findwhat1=Label(top,text="Find What:",pady=5,padx=10).place(x=5,y=20)
    n = StringVar()
    findwhat = ttk.Combobox(top, width = 40, textvariable = n ).place(x=90,y=25)
   
    findin1=Label(top,text="Find in:",pady=5,padx=10).place(x=5,y=47)
    n = StringVar()
    findIN = ttk.Combobox(top, width = 30, textvariable = n )
    findIN['values'] = ('Product/Service id', ' Category', ' Active',' name',' stock',' location', ' image',' <<All>>')                       
    findIN.place(x=90,y=54)
    findIN.current(0)

    findButton = Button(top, text ="Find next",width=10).place(x=480,y=22)
    closeButton = Button(top,text ="Close",width=10).place(x=480,y=52)
    
    match1=Label(top,text="Match:",pady=5,padx=10).place(x=5,y=74)
    n = StringVar()
    match = ttk.Combobox(top, width = 23, textvariable = n )   
    match['values'] = ('From Any part',' Whole Field',' From the beginning of the field')                                    
    match.place(x=90,y=83)
    match.current(0)

    search1=Label(top,text="Search:",pady=5,padx=10).place(x=5,y=102)
    n = StringVar()
    search = ttk.Combobox(top, width = 23, textvariable = n )
    search['values'] = ('All', 'up',' Down')
    search.place(x=90,y=112)
    search.current(0)
    checkvarStatus4=IntVar()  
    Button4 = Checkbutton(top,variable = checkvarStatus4,text="Match Case",onvalue =0 ,offvalue = 1,height=3,width = 15)
    Button4.place(x=90,y=141)
    checkvarStatus5=IntVar()   
    Button5 = Checkbutton(top,variable = checkvarStatus5,text="Match Format",onvalue =0 ,offvalue = 1,height=3,width = 15)
    Button5.place(x=300,y=141)

#-------------------------view/edit invoice---------------------------

#--------------------------calculator-recurring----------------------






 
  


#edit/view invoice in recurring 

def view_invoice_recurring():
  # try:
  #   itemid =self.main_rec_tree.item(self.main_rec_tree.focus())["values"][1]
    # print(itemid)
    # MyApp1object=MyApp1(tab4)
    # MyApp1object.main_rec_tree
    # itemid =MyApp1object.main_rec_tree.item(MyApp1object.main_rec_tree.focus())["values"][2]
    # itemid = MyApp1object.main_rec_tree.item(MyApp1object.main_rec_tree.focus())["values"][1]
    # print(itemid)
    # for child in MyApp1object.main_rec_tree.get_children():
    #   print(MyApp1object.main_rec_tree.item(child)["values"])
    global ee1,ee2,ee3,ee4,ee5,ee6
    global rec_edit_inv_data
    pop=Toplevel(recurring_midFrame)
    pop.title("Invoice")
    pop.geometry("950x690+150+0")

    edit_inv_fetch = main_rec_tree.item(main_rec_tree.focus())["values"][1]
    print(edit_inv_fetch)
    sql_edit = "SELECT * FROM Invoice WHERE invoiceid=%s"
    val_edit = (edit_inv_fetch,)
    fbcursor.execute(sql_edit,val_edit)
    rec_edit_inv_data = fbcursor.fetchone()
    
    print(rec_edit_inv_data)
    

    
      
  

         


  
    def customer_invoice_recurring():
      cuselection=Toplevel()
      cuselection.title("Select Customer")
      cuselection.geometry("930x650+240+10")
      cuselection.resizable(False, False)


      #add new customer
      def create_newcustomer_recurring():
        ven=Toplevel(recurring_midFrame)
        ven.title("Add new vendor")
        ven.geometry("930x650+240+10")
        checkvar1=IntVar()
        checkvar2=IntVar()
        radio=IntVar()
        createFrame=Frame(ven, bg="#f5f3f2", height=650)
        createFrame.pack(side="top", fill="both")
        labelframe1 = LabelFrame(createFrame,text="Customer",bg="#f5f3f2",font=("arial",15))
        labelframe1.place(x=10,y=5,width=910,height=600)
        text1=Label(labelframe1, text="Customer ID:",bg="#f5f3f2",fg="blue").place(x=5 ,y=10)
        e1=Entry(labelframe1,width=25).place(x=150,y=10)
        text2=Label(labelframe1, text="Category:",bg="#f5f3f2").place(x=390 ,y=10)
        e2=ttk.Combobox(labelframe1,width=25,value="Default").place(x=460 ,y=10)
        text3=Label(labelframe1, text="Status:",bg="#f5f3f2").place(x=710 ,y=10)
        Checkbutton(labelframe1,text="Active",variable=checkvar1,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=760 ,y=10)
        
        labelframe2 = LabelFrame(labelframe1,text="Invoice to (appears on invoices)",bg="#f5f3f2")
        labelframe2.place(x=5,y=40,width=420,height=150)
        name = Label(labelframe2, text="Business name:",bg="#f5f3f2",fg="blue").place(x=5,y=5)
        e1 = Entry(labelframe2,width=28).place(x=130,y=5)
        addr = Label(labelframe2, text="Address:",bg="#f5f3f2",fg="blue").place(x=5,y=40)
        e2 = Entry(labelframe2,width=28).place(x=130,y=40,height=80)
        
        btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=440, y=90)

        labelframe3 = LabelFrame(labelframe1,text="Ship to (appears on invoices)",bg="#f5f3f2")
        labelframe3.place(x=480,y=40,width=420,height=150)
        name = Label(labelframe3, text="Ship to name:",bg="#f5f3f2").place(x=5,y=5)
        e1 = Entry(labelframe3,width=28).place(x=130,y=5)
        addr = Label(labelframe3, text="Address:",bg="#f5f3f2").place(x=5,y=40)
        e2 = Entry(labelframe3,width=28).place(x=130,y=40,height=80)
        
        labelframe4 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
        labelframe4.place(x=5,y=195,width=420,height=150)
        name = Label(labelframe4, text="Contact person:",bg="#f5f3f2").place(x=5,y=5)
        e1 = Entry(labelframe4,width=28).place(x=130,y=5)
        email = Label(labelframe4, text="E-mail address:",bg="#f5f3f2",fg="blue").place(x=5,y=35)
        e2 = Entry(labelframe4,width=28).place(x=130,y=35)
        tel = Label(labelframe4, text="Tel.number:",bg="#f5f3f2").place(x=5,y=65)
        e3 = Entry(labelframe4,width=11).place(x=130,y=65)
        fax = Label(labelframe4, text="Fax:",bg="#f5f3f2").place(x=240,y=65)
        e4 = Entry(labelframe4,width=11).place(x=280,y=65)
        sms = Label(labelframe4, text="Mobile number for SMS notifications:",bg="#f5f3f2").place(x=5,y=95)
        e5 = Entry(labelframe4,width=15).place(x=248,y=95)      

        btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=440, y=250)

        
        labelframe5 = LabelFrame(labelframe1,text="Ship to contact",bg="#f5f3f2")
        labelframe5.place(x=480,y=195,width=420,height=125)
        name = Label(labelframe5, text="Contact person:",bg="#f5f3f2").place(x=5,y=5)
        e1 = Entry(labelframe5,width=28).place(x=130,y=5)
        email = Label(labelframe5, text="E-mail address:",bg="#f5f3f2").place(x=5,y=35)
        e2 = Entry(labelframe5,width=28).place(x=130,y=35)
        tel = Label(labelframe5, text="Tel.number:",bg="#f5f3f2").place(x=5,y=65)
        e3 = Entry(labelframe5,width=11).place(x=130,y=65)
        fax = Label(labelframe5, text="Fax:",bg="#f5f3f2").place(x=240,y=65)
        e4 = Entry(labelframe5,width=11).place(x=280,y=65)

        labelframe6 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
        labelframe6.place(x=5,y=350,width=420,height=100)
        Checkbutton(labelframe6,text="Tax Exempt",variable=checkvar2,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=5 ,y=5)
        tax = Label(labelframe6, text="Specific Tax1 %:",bg="#f5f3f2").place(x=180,y=5)
        e1 = Entry(labelframe6,width=10).place(x=290,y=5)
        discount = Label(labelframe6, text="Discount%:",bg="#f5f3f2").place(x=5,y=35)
        e2 = Entry(labelframe6,width=10).place(x=100,y=35)

        labelframe7 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
        labelframe7.place(x=480,y=330,width=420,height=100)
        country = Label(labelframe7, text="country:",bg="#f5f3f2").place(x=5,y=5)
        e1 = Entry(labelframe7,width=28).place(x=130,y=5)
        city = Label(labelframe7, text="City:",bg="#f5f3f2").place(x=5,y=35)
        e2 = Entry(labelframe7,width=28).place(x=130,y=35)

        labelframe8 = LabelFrame(labelframe1,text="Customer Type",bg="#f5f3f2")
        labelframe8.place(x=5,y=460,width=420,height=100)
        R1=Radiobutton(labelframe8,text=" Client ",variable=radio,value=1,bg="#f5f3f2").place(x=5,y=15)
        R2=Radiobutton(labelframe8,text=" Vendor ",variable=radio,value=2,bg="#f5f3f2").place(x=150,y=15)
        R3=Radiobutton(labelframe8,text=" Both(client/vendor)",variable=radio,value=3,bg="#f5f3f2").place(x=250,y=15)
        

        labelframe9 = LabelFrame(labelframe1,text="Notes",bg="#f5f3f2")
        labelframe9.place(x=480,y=430,width=420,height=150)
        e1 = Entry(labelframe9).place(x=10,y=10,height=100,width=390)

        btn1=Button(ven,width=60,height=10,bg="#f5f3f2",compound = LEFT,image=tick ,text="OK").place(x=20, y=615)
        btn2=Button(ven,width=60,height=10,bg="#f5f3f2",compound = LEFT,image=cancel,text="Cancel").place(x=800, y=615)
          
                

      def fetch_details():
        cust_tree_item = cusventtree.item(cusventtree.focus())["values"][0]
        sql = "SELECT * FROM Customer WHERE customerid=%s"
        val = (cust_tree_item,)
        fbcursor.execute(sql,val)
        sel_cust_str = fbcursor.fetchone()
        ee1.delete(0, END)
        ee1.insert(0,sel_cust_str[4])
        ee2.delete('1.0',END)
        ee2.insert('1.0',sel_cust_str[5])
        ee3.delete(0, END)
        ee3.insert(0, sel_cust_str[6])
        ee4.delete('1.0',END)
        ee4.insert('1.0',sel_cust_str[7])
        ee5.delete(0,END)
        ee5.insert(0,sel_cust_str[9])
        ee6.delete(0,END)
        ee6.insert(0,sel_cust_str[12])

        cuselection.destroy()  

    # def inv_newline():
    # #fetch new line item
    #   def product_tree_fetch():
    #     product_tree_item = product_sel_tree.item(product_sel_tree.focus())["values"][0]
    #     sql = "SELECT * FROM Productservice WHERE Productserviceid=%s"
    #     val = (product_tree_item,)
    #     fbcursor.execute(sql,val)
    #     sel_pro_str = fbcursor.fetchone()
    #     sub_rec_tree.insert(parent='',index='end',iid=sel_pro_str,text='',values=(sel_pro_str[0],sel_pro_str[4],sel_pro_str[5],sel_pro_str[7],sel_pro_str[18]))
    #     inv_newline_sel.destroy()
    #   show_newline = ee1.get()
    #   if show_newline == '':
    #     messagebox.showinfo('F-Billing Revolution','Customer is required, please select customer before adding line item to invoice')
    #   else:
    #     inv_newline_sel=Toplevel()
    #     inv_newline_sel.title("Product/Services")
    #     inv_newline_sel.geometry("930x650+240+10")
    #     inv_newline_sel.resizable(False, False)

    #     global product_sel_tree

    #     product_sel_tree=ttk.Treeview(inv_newline_sel, height=27)
    #     product_sel_tree["columns"]=["1","2","3", "4","5"]
    #     product_sel_tree.column("#0", width=35)
    #     product_sel_tree.column("1", width=160)
    #     product_sel_tree.column("2", width=160)
    #     product_sel_tree.column("3", width=140)
    #     product_sel_tree.column("4", width=70)
    #     product_sel_tree.column("5", width=70)
    #     product_sel_tree.heading("#0",text="")
    #     product_sel_tree.heading("1",text="ID/SKU")
    #     product_sel_tree.heading("2",text="Product/Service Name")
    #     product_sel_tree.heading("3",text="Unit price")
    #     product_sel_tree.heading("4",text="Service")
    #     product_sel_tree.heading("5",text="Stock")
    #     product_sel_tree.place(x=5, y=45)

    #     sql = "SELECT * FROM Productservice"
    #     fbcursor.execute(sql)
    #     product_details = fbcursor.fetchall()

    #     count = 0
    #     for p in product_details:
    #       if True:
    #         product_sel_tree.insert(parent='',index='end',iid=p,text='',values=(p[0],p[4],p[7],p[12],p[13]))
    #       else:
    #         pass
    #     count += 1
    

      def filter_customer():
        
        if cust_entry.get() == '':
          sql = "SELECT * FROM Customer"
          fbcursor.execute(sql,)
          customer_details = fbcursor.fetchall()
          
          for record in cusventtree.get_children():
            cusventtree.delete(record)

          count = 0
          for i in customer_details:
            if True:
              cusventtree.insert(parent='',index='end',iid=i,text='',values=(i[0],i[4],i[10],i[8]))
            else:
              pass
          count += 1
        else:
          filter = cust_entry.get()
          for record in cusventtree.get_children():
            cusventtree.delete(record)

          sql = "SELECT * FROM Customer WHERE businessname=%s"
          val = (filter, )
          fbcursor.execute(sql, val)
          customer_details = fbcursor.fetchall()

      
          count=0
          for i in customer_details:
            if True:
              cusventtree.insert(parent='', index='end', iid=i, text='', values=(i[0],i[4],i[10],i[8]))  
            else:
              pass
          count += 1
      enter=Label(cuselection, text="Enter filter text").place(x=5, y=10)
      cust_filter_button=Button(cuselection, text='ok',command=filter_customer)
      cust_filter_button.place(x=240, y=9,height=20,width=60)
      cust_entry=Entry(cuselection, width=20)
      cust_entry.place(x=110, y=10)
      text=Label(cuselection, text="Filtered column").place(x=340, y=10)
      e2=Entry(cuselection, width=20).place(x=450, y=10)

      global cusventtree

      cusventtree=ttk.Treeview(cuselection, height=27)
      cusventtree["columns"]=["1","2","3", "4"]
      cusventtree.column("#0", width=35)
      cusventtree.column("1", width=160)
      cusventtree.column("2", width=160)
      cusventtree.column("3", width=140)
      cusventtree.column("4", width=140)
      cusventtree.heading("#0",text="")
      cusventtree.heading("1",text="Customer/Ventor ID")
      cusventtree.heading("2",text="Customer/Ventor Name")
      cusventtree.heading("3",text="Tel.")
      cusventtree.heading("4",text="Contact Person")
      cusventtree.place(x=5, y=45)

      sql_sel_cust = "SELECT * FROM Customer"
      fbcursor.execute(sql_sel_cust)
      customer_details = fbcursor.fetchall()

      count=0
      for i in customer_details:
        if True:
          cusventtree.insert(parent='',index='end',iid=i,text='',values=(i[0],i[4],i[10],i[8]))
        else:
          pass
      count += 1
     



      rec_cus_ctegorytree=ttk.Treeview(cuselection, height=27)
      rec_cus_ctegorytree["columns"]=["1"]
      rec_cus_ctegorytree.column("#0", width=35, minwidth=20)
      rec_cus_ctegorytree.column("1", width=205, minwidth=25, anchor=CENTER)    
      rec_cus_ctegorytree.heading("#0",text="", anchor=W)
      rec_cus_ctegorytree.heading("1",text="View filter by category", anchor=CENTER)
      rec_cus_ctegorytree.place(x=660, y=45)

      def recur_list_filter_customer(event):
        selected_cust_indices = recur_cust_fil_cat_list.curselection()
        selected_cust_filter = ",".join([recur_cust_fil_cat_list.get(i) for i in selected_cust_indices])

        if selected_cust_filter == "               View all records" or selected_cust_filter == "               View only Client/Vendor" or selected_cust_filter == "               Default":
          cust_all_sql = "SELECT * FROM Customer"
          fbcursor.execute(cust_all_sql)
          cust_all_data = fbcursor.fetchall()
          for record in cusventtree.get_children():
            cusventtree.delete(record)
          count_all = 0
          for i in cust_all_data:
            cusventtree.insert(parent='',index='end',iid=i,text='',values=(i[0],i[4],i[10],i[8]))
          count_all += 1
        elif selected_cust_filter == "               View only Client type":
          client_sql = "SELECT * FROM Customer WHERE customertype=%s"
          client_val = ('Client',)
          fbcursor.execute(client_sql,client_val)
          client_data = fbcursor.fetchall()
          for record in cusventtree.get_children():
            cusventtree.delete(record)
          count_c = 0
          for i in client_data:
            cusventtree.insert(parent='',index='end',iid=i,text='',values=(i[0],i[4],i[10],i[8]))
          count_c += 1
        else:
          vendor_sql = "SELECT * FROM Customer WHERE customertype=%s"
          vendor_val = ('Vendor',)
          fbcursor.execute(vendor_sql,vendor_val)
          vendor_data = fbcursor.fetchall()
          for record in cusventtree.get_children():
            cusventtree.delete(record)
          count_v = 0
          for i in vendor_data:
            cusventtree.insert(parent='',index='end',iid=i,text='',values=(i[0],i[4],i[10],i[8]))
          count_v += 1

      recur_cust_fil_cat_list = Listbox(cuselection,height=34,width=40,bg="white",activestyle="dotbox",fg="black",highlightbackground="white")
      recur_cust_fil_cat_list.insert(0,"               View all records")
      recur_cust_fil_cat_list.insert(1,"               View only Client/Vendor")
      recur_cust_fil_cat_list.insert(2,"               View only Client type")
      recur_cust_fil_cat_list.insert(3,"               View only Vendor type")
      recur_cust_fil_cat_list.insert(4,"               Default")
      recur_cust_fil_cat_list.place(x=660,y=63)
      recur_cust_fil_cat_list.bind('<<ListboxSelect>>',recur_list_filter_customer)


      scrollbar = Scrollbar(cuselection)
      scrollbar.place(x=640, y=45, height=560)
      scrollbar.config( command=sub_rec_tree.yview )

      btn1=Button(cuselection,compound = LEFT,image=tick ,text="ok", width=60,command=fetch_details).place(x=15, y=610)
      btn1=Button(cuselection,compound = LEFT,image=tick,text="Edit selected customer", width=150,command=create_newcustomer_recurring).place(x=250, y=610)
      btn1=Button(cuselection,compound = LEFT,image=tick, text="Add new customer", width=150,command=create_newcustomer_recurring).place(x=435, y=610)
      btn1=Button(cuselection,compound = LEFT,image=cancel ,text="Cancel", width=60).place(x=740, y=615)   



      

    #add new line item
    def recur_inv_newline():
    #fetch new line item
      def recur_product_tree_fetch():
        product_tree_item = recur_product_sel_tree.item(recur_product_sel_tree.focus())["values"][0]
        sql = "SELECT * FROM Productservice WHERE Productserviceid=%s"
        val = (product_tree_item,)
        fbcursor.execute(sql,val)
        sel_pro_str = fbcursor.fetchone()
        sub_rec_tree.insert(parent='',index='end',iid=sel_pro_str,text='',values=(sel_pro_str[0],sel_pro_str[4],sel_pro_str[5],sel_pro_str[7],sel_pro_str[18]))
        recur_inv_newline_sel.destroy()
      show_newline = ee1.get()
      if show_newline == '':
        messagebox.showinfo('F-Billing Revolution','Customer is required, please select customer before adding line item to invoice')
      else:
        recur_inv_newline_sel=Toplevel()
        recur_inv_newline_sel.title("Product/Services")
        recur_inv_newline_sel.geometry("930x650+240+10")
        recur_inv_newline_sel.resizable(False, False)

        global recur_product_sel_tree

        recur_product_sel_tree=ttk.Treeview(recur_inv_newline_sel, height=27)
        recur_product_sel_tree["columns"]=["1","2","3", "4","5"]
        recur_product_sel_tree.column("#0", width=35)
        recur_product_sel_tree.column("1", width=160)
        recur_product_sel_tree.column("2", width=160)
        recur_product_sel_tree.column("3", width=140)
        recur_product_sel_tree.column("4", width=70)
        recur_product_sel_tree.column("5", width=70)
        recur_product_sel_tree.heading("#0",text="")
        recur_product_sel_tree.heading("1",text="ID/SKU")
        recur_product_sel_tree.heading("2",text="Product/Service Name")
        recur_product_sel_tree.heading("3",text="Unit price")
        recur_product_sel_tree.heading("4",text="Service")
        recur_product_sel_tree.heading("5",text="Stock")
        recur_product_sel_tree.place(x=5, y=45)

        sql = "SELECT * FROM Productservice"
        fbcursor.execute(sql)
        product_details = fbcursor.fetchall()
        print(product_details)

        count = 0
        for p in product_details:
          if True:
            recur_product_sel_tree.insert(parent='',index='end',iid=p,text='',values=(p[0],p[4],p[7],p[12],p[13]))
          else:
            pass
        count += 1

        enter=Label(recur_inv_newline_sel, text="Enter filter text").place(x=5, y=10)
        pro_filter_entry_e1=Entry(recur_inv_newline_sel, width=20)
        pro_filter_entry_e1.place(x=110, y=10)

        #filtering product
        def filter_product():
          # pro_filter_entry_e1=0
          if pro_filter_entry_e1.get() == '':
            sql = "SELECT * FROM Productservice"
            fbcursor.execute(sql)
            product_details = fbcursor.fetchall()
            for record in recur_product_sel_tree.get_children():
              recur_product_sel_tree.delete(record)
              
            count = 0
            for p in product_details:
              if True:
                recur_product_sel_tree.insert(parent='',index='end',iid=p,text='',values=(p[0],p[4],p[7],p[12],p[13]))
              else:
                pass
            count += 1

          else:
            filter = pro_filter_entry_e1.get()
            for record in recur_product_sel_tree.get_children():
              recur_product_sel_tree.delete(record)
            
            sql = "SELECT * FROM Productservice WHERE name=%s"
            val = (filter, )
            fbcursor.execute(sql, val)
            records = fbcursor.fetchall()
      
        
            count=0
            for i in records:
              if True:
                recur_product_sel_tree.insert(parent='', index='end', iid=i, text='', values=(i[0],i[4],i[10],i[8]))  
              else:
                pass
            count += 1
        pro_filter_button=Button(recur_inv_newline_sel, text='ok',command=filter_product)
        pro_filter_button.place(x=240, y=9,height=20,width=60)
        
        btn1=Button(recur_inv_newline_sel,compound = LEFT,image=tick ,text="ok",command=recur_product_tree_fetch, width=60).place(x=15, y=610)
        

        def new_product():  
          top = Toplevel()  
          top.title("Add a new Product/Service")
          p2 = PhotoImage(file = 'images/fbicon.png')
          top.iconphoto(False, p2)
          top.geometry("700x550+390+15")
          tabControl = ttk.Notebook(top)
          s = ttk.Style()
          s.theme_use('default')
          s.configure('TNotebook.Tab', background="#999999",padding=10,bd=0)
              

          tab1 = ttk.Frame(tabControl)
          tab2 = ttk.Frame(tabControl)
        
          tabControl.add(tab1,compound = LEFT, text ='Product/Service')
          tabControl.add(tab2,compound = LEFT, text ='Product Image')
        
          tabControl.pack(expand = 1, fill ="both")
        
          innerFrame = Frame(tab1,bg="#f5f3f2", relief=GROOVE)
          innerFrame.pack(side="top",fill=BOTH)

          Customerlabelframe = LabelFrame(innerFrame,text="Product/Service",width=580,height=485)
          Customerlabelframe.pack(side="top",fill=BOTH,padx=10)

          add_pro_code_label=Label(Customerlabelframe,text="Code or SKU:",fg="blue",pady=10,padx=10)
          add_pro_code_label.place(x=20,y=0)
          add_pro_code_entry = Entry(Customerlabelframe,width=35)
          add_pro_code_entry.place(x=120,y=8)

          checkvarStatus=IntVar()
          add_pro_status=Label(Customerlabelframe,text="Status:")
          add_pro_status.place(x=500,y=8)
          add_pro_checkbtn_active = Checkbutton(Customerlabelframe,
                            variable = checkvarStatus,text="Active",compound="right",
                            onvalue =0 ,
                            offvalue = 1,
                          
                            width = 10)

          add_pro_checkbtn_active.place(x=550,y=5)

          add_pro_cat=Label(Customerlabelframe,text="Category:",pady=5,padx=10)
          add_pro_cat.place(x=20,y=40)
          n = StringVar()
          add_pro_country = ttk.Combobox(Customerlabelframe, width = 40, textvariable = n )
          
          add_pro_country['values'] = ('Default',' India',' China',' Australia',' Nigeria',' Malaysia',' Italy',' Turkey',)
          
          add_pro_country.place(x=120,y=45)
          add_pro_country.current(0)


          add_pro_name_label=Label(Customerlabelframe,text="Name :",fg="blue",pady=5,padx=10)
          add_pro_name_label.place(x=20,y=70)
          add_pro_name_entry = Entry(Customerlabelframe,width=60)
          add_pro_name_entry.place(x=120,y=75)

          add_pro_des_label=Label(Customerlabelframe,text="Description :",pady=5,padx=10)
          add_pro_des_label.place(x=20,y=100)
          add_pro_des_entry = Entry(Customerlabelframe,width=60)
          add_pro_des_entry.place(x=120,y=105)

          uval = IntVar(Customerlabelframe, value='$0.00')
          add_pro_unit_label=Label(Customerlabelframe,text="Unit Price:",fg="blue",pady=5,padx=10)
          add_pro_unit_label.place(x=20,y=130)
          add_pro_unit_entry = Entry(Customerlabelframe,width=20,textvariable=uval)
          add_pro_unit_entry.place(x=120,y=135)

          pcsval = IntVar(Customerlabelframe, value='$0.00')
          add_pro_pcs_label=Label(Customerlabelframe,text="Pcs/Weight:",fg="blue",pady=5,padx=10)
          add_pro_pcs_label.place(x=320,y=140)
          add_pro_pcs_entry = Entry(Customerlabelframe,width=20,textvariable=pcsval)
          add_pro_pcs_entry.place(x=410,y=140)

          costval = IntVar(Customerlabelframe, value='$0.00')
          add_pro_cost_label=Label(Customerlabelframe,text="Cost:",pady=5,padx=10)
          add_pro_cost_label.place(x=20,y=160)
          add_pro_cost_entry = Entry(Customerlabelframe,width=20,textvariable=costval)
          add_pro_cost_entry.place(x=120,y=165)

          priceval = IntVar(Customerlabelframe, value='$0.00')
          add_pro_price_label=Label(Customerlabelframe,text="(Price Cost):",pady=5,padx=10)
          add_pro_price_label.place(x=20,y=190)
          add_pro_price_entry = Entry(Customerlabelframe,width=20,textvariable=priceval)
          add_pro_price_entry.place(x=120,y=195)

          checkvarStatus2=IntVar()
        
          add_pro_checkbtn_tax = Checkbutton(Customerlabelframe,variable = checkvarStatus2,
                            text="Taxable Tax1rate",compound="right",
                            onvalue =0 ,
                            offvalue = 1,
                            height=2,
                            width = 12)

          add_pro_checkbtn_tax.place(x=415,y=170)


          checkvarStatus3=IntVar()
        
          add_pro_checkbtn_no = Checkbutton(Customerlabelframe,variable = checkvarStatus3,
                            text="No stock Control",
                            onvalue =1 ,
                            offvalue = 0,
                            height=3,
                            width = 15)

          add_pro_checkbtn_no.place(x=40,y=220)


          stockval = IntVar(Customerlabelframe)
          add_pro_stock_label=Label(Customerlabelframe,text="Stock:",pady=5,padx=10)
          add_pro_stock_label.place(x=90,y=260)
          add_pro_stock_entry = Entry(Customerlabelframe,width=15,textvariable=stockval)
          add_pro_stock_entry.place(x=150,y=265)

          lowval = IntVar(Customerlabelframe)
          add_pro_low_label=Label(Customerlabelframe,text="Low Stock Warning Limit:",pady=5,padx=10)
          add_pro_low_label.place(x=300,y=260)
          add_pro_low_entry = Entry(Customerlabelframe,width=10,textvariable=lowval)
          add_pro_low_entry.place(x=495,y=265)

        
          add_pro_ware_label=Label(Customerlabelframe,text="Warehouse:",pady=5,padx=10)
          add_pro_ware_label.place(x=60,y=290)
          add_pro_ware_entry = Entry(Customerlabelframe,width=50)
          add_pro_ware_entry.place(x=150,y=295)

          add_pro_pnote_label=Label(Customerlabelframe,text="Private notes(not appears on invoice):",pady=5,padx=10)
          add_pro_pnote_label.place(x=20,y=330)

          add_pro_pnote_scroll = scrolledtext.ScrolledText(Customerlabelframe, undo=True,width=62,height=4)
          add_pro_pnote_scroll.place(x=32,y=358)

          def add_new_product():
            sku = add_pro_code_entry.get()
            category = add_pro_country.get()
            name = add_pro_name_entry.get()
            description = add_pro_des_entry.get()
            unitprice = add_pro_unit_entry.get()
            peices = add_pro_pcs_entry.get()
            cost = add_pro_cost_entry.get()
            priceminuscost = add_pro_price_entry.get()
            stock = add_pro_stock_entry.get()
            stocklimit = add_pro_low_entry.get()
            warehouse = add_pro_ware_entry.get()
            privatenote = add_pro_pnote_scroll.get("1.0",'end-1c')
            status = checkvarStatus.get()
            taxable = checkvarStatus2.get()
            serviceornot = checkvarStatus3.get()
            sql='INSERT INTO Productservice (sku,category,name,description,unitprice,peices,cost,priceminuscost,stock,stocklimit,warehouse,privatenote,status,taxable,serviceornot) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' #adding values into db
            val=(sku,category,name,description,unitprice,peices,cost,priceminuscost,stock,stocklimit,warehouse,privatenote,status,taxable,serviceornot)
            fbcursor.execute(sql,val)
            fbilldb.commit()
            top.destroy()
            messagebox.showinfo("F-Billing Revolution","Product registered successfully")

          # Cancel add new product
          def cancel_add():
            top.destroy()

          add_pro_ok_btn = Button(innerFrame,compound = LEFT,image=tick , text ="Ok",width=60,command=add_new_product)
          add_pro_ok_btn.pack(side=LEFT)

          def cancel_add():
            top.destroy()

          add_pro_cancel_btn = Button(innerFrame,compound = LEFT,image=cancel ,text="Cancel",width=60,command=cancel_add)
          add_pro_cancel_btn.pack(side=RIGHT)

          imageFrame = Frame(tab2, relief=GROOVE,height=580)
          imageFrame.pack(side="top",fill=BOTH)

          browseimg=Label(imageFrame,text=" Browse for product image file(recommended image type:JPG,size 480x320 pixels) ",bg='#f5f3f2')
          browseimg.place(x=15,y=35)

          browsebutton=Button(imageFrame,text = 'Browse')
          browsebutton.place(x=580,y=30,height=30,width=50)
          
          removeButton = Button(imageFrame,compound = LEFT,image=cancel, text ="Remove Product Image",width=150)
          removeButton.place(x=400,y=450)
        btn3=Button(recur_inv_newline_sel,compound = LEFT,image=tick , text="Add product/Service",command=new_product, width=150).place(x=435, y=610)
        btn2=Button(recur_inv_newline_sel,compound = LEFT,image=tick , text="Edit product/Service",command=new_product, width=150).place(x=250, y=610)
        def cancel_pro_dis_page():
          recur_inv_newline_sel.destroy()

        btn4=Button(recur_inv_newline_sel,compound = LEFT,image=cancel ,text="Cancel",command=cancel_pro_dis_page, width=60).place(x=740, y=610)
        ctegorytree=ttk.Treeview(recur_inv_newline_sel, height=27)
        ctegorytree["columns"]=["1"]
        ctegorytree.column("#0", width=35, minwidth=20)
        ctegorytree.column("1", width=205, minwidth=25, anchor=CENTER)    
        ctegorytree.heading("#0",text="", anchor=W)
        ctegorytree.heading("1",text="View filter by category", anchor=CENTER)
        ctegorytree.place(x=660, y=45)
            #filter customer
        def recur_list_filter_product(evet):
          selected_indices = ctegorytree_list.curselection()
          selected_filter = ",".join([ctegorytree_list.get(i) for i in selected_indices])

          if selected_filter == "               View all Products/Services" or selected_filter == "               Default":
            pro_ser_sql = "SELECT * FROM Productservice"
            fbcursor.execute(pro_ser_sql)
            pro_ser_data = fbcursor.fetchall()
            for record in recur_product_sel_tree.get_children():
              recur_product_sel_tree.delete(record)
            count_ps = 0
            for i in pro_ser_data:
              recur_product_sel_tree.insert(parent='',index='end',iid=i,text='',values=(i[2],i[4],i[7],i[12],i[13]))
            count_ps += 1
          elif selected_filter == "               View all Products":
            pro_sql = "SELECT * FROM Productservice WHERE serviceornot=%s"
            pro_val = ('0',)
            fbcursor.execute(pro_sql,pro_val)
            pro_data = fbcursor.fetchall()
            for record in recur_product_sel_tree.get_children():
              recur_product_sel_tree.delete(record)
            count_p = 0
            for i in pro_data:
              recur_product_sel_tree.insert(parent='', index='end', iid=i, text='', values=(i[2],i[4],i[7],i[12],i[13]))
            count_p += 1
          elif selected_filter == "               View all Services":
            ser_sql = "SELECT * FROM Productservice WHERE serviceornot=%s"
            ser_val = ('1',)
            fbcursor.execute(ser_sql,ser_val)
            ser_data = fbcursor.fetchall()
            for record in recur_product_sel_tree.get_children():
              recur_product_sel_tree.delete(record)
            count_s = 0
            for i in ser_data:
              recur_product_sel_tree.insert(parent='', index='end', iid=i, text='', values=(i[2],i[4],i[7],i[12],i[13]))
            count_s += 1


        ctegorytree_list = Listbox(recur_inv_newline_sel,height=34,width=40,bg="white",activestyle="dotbox",fg="black",highlightbackground="white")
        ctegorytree_list.insert(0,"               View all Products/Services")
        ctegorytree_list.insert(1,"               View all Products")
        ctegorytree_list.insert(2,"               View all Services")
        ctegorytree_list.insert(3,"               Default")
        ctegorytree_list.place(x=660,y=63)
        ctegorytree_list.bind('<<ListboxSelect>>',recur_list_filter_product)
        

      
    
     

      



      
                 
    

      # cusventtree=ttk.Treeview(inv_newline_sel, height=27)
      # cusventtree["columns"]=["1","2","3", "4","5"]
      # cusventtree.column("#0", width=35)
      # cusventtree.column("1", width=160)
      # cusventtree.column("2", width=160)
      # cusventtree.column("3", width=140)
      # cusventtree.column("4", width=70)
      # cusventtree.column("5", width=70)
      # cusventtree.heading("#0",text="")
      # cusventtree.heading("1",text="ID/SKU")
      # cusventtree.heading("2",text="Product/Service Name")
      # cusventtree.heading("3",text="Unit price")
      # cusventtree.heading("4",text="Service")
      # cusventtree.heading("5",text="Stock")
      # cusventtree.place(x=5, y=45)


      
      # scrollbar = Scrollbar(inv_newline_sel)
      # scrollbar.place(x=640, y=45, height=560)
      # scrollbar.config( command=sub_rec_tree.yview )
    

     


  # #preview message if customer  is not
  # def previewline():
  #   messagebox.showerror("F-Billing Revolution","line is required,please select customer for this order before printing.")


  
  #sms notification
    def sms_recurring():
      send_SMS=Toplevel()
      send_SMS.geometry("700x480+240+150")
      send_SMS.title("Send SMS notification")

      style = ttk.Style()
      style.theme_use('default')
      style.configure('TNotebook.Tab', background="#999999", padding=5)
      sms_Notebook = ttk.Notebook(send_SMS)
      SMS_Notification = Frame(sms_Notebook, height=470, width=700)
      SMS_Service_Account = Frame(sms_Notebook, height=470, width=700)
      sms_Notebook.add(SMS_Notification, text="SMS Notification")
      sms_Notebook.add(SMS_Service_Account, text="SMS Service Account")
      sms_Notebook.place(x=0, y=0)

      numlbel=Label(SMS_Notification, text="SMS number or comma seperated SMS number list(Please start each SMS number with the country code)")
      numlbel.place(x=10, y=10)
      numentry=Entry(SMS_Notification, width=92).place(x=10, y=30)
      stexbel=Label(SMS_Notification, text="SMS Text").place(x=10, y=60)
      stex=Entry(SMS_Notification, width=40).place(x=10, y=85,height=120)
      
      dclbel=Label(SMS_Notification, text="Double click to insert into text")
      dclbel.place(x=410, y=60)
      dcl=Entry(SMS_Notification, width=30)
      dcl.place(x=400, y=85,height=200)
      
      smstype=LabelFrame(SMS_Notification, text="SMS message type", width=377, height=60)
      smstype.place(x=10, y=223)
      snuvar=IntVar()
      normal_rbtn=Radiobutton(smstype, text="Normal SMS(160 chars)", variable=snuvar, value=1)
      normal_rbtn.place(x=5, y=5)
      unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)", variable=snuvar, value=2)
      unicode_rbtn.place(x=190, y=5)
      tiplbf=LabelFrame(SMS_Notification, text="Tips", width=680, height=120)
      tiplbf.place(x=10, y=290)
      tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="Always start the SMS nymber with the country code. Do not use the + sign at the beginning(example\nUS number:8455807546). Do not use any special characters in your normal SMS text. Please use the\nstndard SMS characters or the English alphabet and numbers only. Otherwise the SMS will be\nunreadable or undeliverable. If you need to enter international characters, accents,email address, or\nspecial characters to the SMS text field then choose the Unicode SMS format.")
      tiplabl.place(x=5, y=5)

      btn1=Button(SMS_Notification, width=20, text="Send SMS notification").place(x=10, y=420)
      btn2=Button(SMS_Notification, width=25, text="Confirm SMS cost before sending").place(x=280, y=420)
      btn3=Button(SMS_Notification, width=15, text="Cancel").place(x=550, y=420)
      

      smstype=LabelFrame(SMS_Service_Account, text="Select the notification service provider", width=670, height=65)
      smstype.place(x=10, y=5)
      snumvar=IntVar()
      normal_rbtn=Radiobutton(smstype,text="BULKSMS(www.bulksms.com)",variable=snumvar,value=1,)
      normal_rbtn.place(x=5, y=5)
      unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)-Recommended", variable=snumvar, value=2)
      unicode_rbtn.place(x=290, y=5)

      sms1type=LabelFrame(SMS_Service_Account, text="Your BULKSMS.COM Account", width=670, height=100)
      sms1type.place(x=10, y=80)
      name=Label(sms1type, text="Username").place(x=10, y=5)
      na=Entry(sms1type, width=20).place(x=100, y=5)
      password=Label(sms1type, text="Password").place(x=10, y=45)
      pas=Entry(sms1type, width=20).place(x=100, y=45)
      combo=Label(sms1type, text="Route").place(x=400, y=5)
      n = StringVar()
      combo1 = ttk.Combobox(sms1type, width = 20, textvariable = n ).place(x=450,y=5)
      btn1=Button(sms1type, width=10, text="Save settings").place(x=550, y=45)

      
      tiplbf=LabelFrame(SMS_Service_Account, text="Terms of service", width=680, height=250)
      tiplbf.place(x=10, y=190)
      tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="The SMS notification service is not free.This service costs you creadit.You must have your own account\nat BULKSMS.COM and you need to have sufficient creadit and an active internet connection to use\nthis feature.Please review all fields in this form for accuracy")
      tiplabl.place(x=0, y=5)
      tiplabl1=Label(tiplbf,justify=LEFT,fg="black",  text="visit www.bulksms.com website to create your own account.please make sure the BULKSMS .COM\n service works well in your country before you busy creadit")
      tiplabl1.place(x=0, y=60)
      tiplabl2=Label(tiplbf,justify=LEFT,fg="black",  text="Our SMS notification tool comes without any warranty.our software only forwards your SMS message\nthe BULKSMS API server .The BULKSMS API server will try to sent SMS message your recipient")
      tiplabl2.place(x=0, y=100)
      tiplabl3=Label(tiplbf,justify=LEFT,fg="red",  text="Please note that you access and use the SMS notification tool your own risk.F-Billing software is not\nresponsible for any type of loss or damage or undelivered SMS massage which you may as a result\nof accessing and using the SMS notification service.")
      tiplabl3.place(x=0, y=140)
      checkvar1=IntVar()
      chkbtn1=Checkbutton(tiplbf,text="I have read and agree to the terms of service above",variable=checkvar1,onvalue=1,offvalue=0).place(x=70, y=200) 

    #mark invoice
    def markinvoice_recurring():
      mark_inv=Toplevel()
      mark_inv.geometry("700x480+240+150")
      mark_inv.title("Record Payement for Invoice")
      checkvar=IntVar()
      checkvar1=IntVar()
      checkvar2=IntVar()

      style = ttk.Style()
      style.theme_use('default')
      style.configure('TNotebook.Tab', background="#999999", padding=5)
      mark_Notebook = ttk.Notebook(mark_inv)
      Mark_Invoice = Frame(mark_Notebook, height=470, width=750)
      mark_Notebook.add(Mark_Invoice, text="Mark Invoice")
      mark_Notebook.place(x=0, y=0)

      involbel=Label(Mark_Invoice, text="Invoice Balance")
      involbel.place(x=10, y=10)
      numentry=Entry(Mark_Invoice, width=45).place(x=130, y=10)

      labelframe5 = LabelFrame(Mark_Invoice,text="Payement Record Details",bg="#f5f3f2")
      labelframe5.place(x=10,y=60,width=670,height=250)
      e1 = Entry(labelframe5,width=28).place(x=30,y=45)
      pdate = Label(labelframe5, text="Payement Date:",bg="#f5f3f2").place(x=250,y=20)
      e2 = Entry(labelframe5,width=28).place(x=220,y=45)
      payd = Label(labelframe5, text="Paid By:",bg="#f5f3f2").place(x=450,y=20)
      drop = ttk.Combobox(labelframe5, value="Hello")
      drop.place(x=450,y=45)
      involbel=Label(labelframe5, text="Description")
      involbel.place(x=30, y=80)
      numentry=Entry(labelframe5, width=100).place(x=30, y=120)
      Checkbutton(labelframe5,text="Paid in full and close invoice",variable=checkvar,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=30 ,y=150)
      pl = Label(labelframe5,text="Payement Reciepts",bg="#f5f3f2")
      pl.place(x=300,y=145)
      Checkbutton(labelframe5,text="Send Payement Reciept",variable=checkvar1,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=320 ,y=170)
      Checkbutton(labelframe5,text="Attach updated invoice",variable=checkvar2,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=320 ,y=200)

      okbtn=Button(Mark_Invoice,compound = LEFT,image=tick , text="Save payement", width=100).place(x=10, y=350)
      canbtn=Button(Mark_Invoice,compound = LEFT,image=cancel, text="Cancel", width=100).place(x=500, y=350)
    
   
#from tkinter import*

# win=Tk()
# win.title("Calculator")
# win.geometry('315x510')
# win.configure(background='grey')

# def  btnclick(num):
#     global operator
#     operator=operator + str(num)
#     _input.set(operator)

# def clear():
#     global operator
#     operator=""
#     _input.set("")

# def answer():
#     global operator
#     ans=str(eval(operator))
#     _input.set(ans)
#     operator = ""

# label=Label(win,font=('ariel' ,20,'bold'),text='Calculator',bg='grey',fg='black')
# label.grid(columnspan=4)

# _input=StringVar()
# operator=""

# display = Entry(win,font=('ariel' ,20,'bold'), textvariable=_input ,insertwidth=7 , bd=5 ,bg="white",justify='right')
# display.grid(columnspan=4)

# #------------------Row-1-------------------------------------------------------------------------------------------------------

# b7=Button(win,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="7",bg="grey", command=lambda: btnclick(7) )
# b7.grid(row=2,column=0)

# b8=Button(win,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="8",bg="grey", command=lambda: btnclick(8) )
# b8.grid(row=2,column=1)

# b9=Button(win,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="9",bg="grey", command=lambda: btnclick(9) )
# b9.grid(row=2,column=2)

# Add=Button(win,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="+",bg="grey", command=lambda: btnclick("+") )
# Add.grid(row=2,column=3)

# #----------------Row-2---------------------------------------------------------------------------------------------------------------

# b4=Button(win,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="4",bg="grey", command=lambda: btnclick(4) )
# b4.grid(row=3,column=0)

# b5=Button(win,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="5",bg="grey", command=lambda: btnclick(5) )
# b5.grid(row=3,column=1)

# b6=Button(win,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="6",bg="grey", command=lambda: btnclick(6) )
# b6.grid(row=3,column=2)

# Sub=Button(win,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="-",bg="grey", command=lambda: btnclick("-") )
# Sub.grid(row=3,column=3)

# #-------------Row-3------------------------------------------------------------------------------------------------------------------

# b1=Button(win,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="1",bg="grey", command=lambda: btnclick(1) )
# b1.grid(row=4,column=0)

# b2=Button(win,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="2",bg="grey", command=lambda: btnclick(2) )
# b2.grid(row=4,column=1)

# b3=Button(win,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="3",bg="grey", command=lambda: btnclick(3) )
# b3.grid(row=4,column=2)

# mul=Button(win,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="*",bg="grey", command=lambda: btnclick("*") )
# mul.grid(row=4,column=3)

# #-----------------Row-4--------------------------------------------------------------------------------------------------------

# b0=Button(win,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="0",bg="grey", command=lambda: btnclick(0) )
# b0.grid(row=5,column=0)

# bc=Button(win,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="c",bg="grey", command=clear)
# bc.grid(row=5,column=1)

# Decimal=Button(win,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text=".",bg="grey", command=lambda: btnclick(".") )
# Decimal.grid(row=5,column=2)

# Div=Button(win,padx=16,pady=16,bd=4, fg="black", font=('ariel', 20 ,'bold'),text="/",bg="grey", command=lambda: btnclick("/") )
# Div.grid(row=5,column=3)

# #-----------------Row-6------------------------------------------------------------------------------------------------------------------

# bequal=Button(win,padx=16,pady=16,bd=4,width = 16, fg="black", font=('ariel', 20 ,'bold'),text="=",bg="grey",command=answer)
# bequal.grid(columnspan=4)

# win.mainloop()
    #voidinvoice
    def voidinvoice_recurring():
      messagebox.askyesno("F-Billing Revolution","Are you sure to avoid this invoice?\nAll products will be placed back into stock and all payemnts will be voided.")
    
    #delete line item  
    def delete_recurring_line_item():
      
      selected_line_item = sub_rec_tree.selection()[0]
      sub_rec_tree.delete(selected_line_item)
      

    firFrame=Frame(pop, bg="#f5f3f2", height=60)
    firFrame.pack(side="top", fill=X)

    w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="left", padx=5)

    create = Button(firFrame,compound="top", text="Select\nCustomer",relief=RAISED, image=customer,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=customer_invoice_recurring)
    create.pack(side="left", pady=3, ipadx=4)


    w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="left", padx=5)

    add= Button(firFrame,compound="top", text="Add new\nline item",relief=RAISED, image=addnew,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=recur_inv_newline)
    add.pack(side="left", pady=3, ipadx=4)

    dele= Button(firFrame,compound="top", text="Delete line\nitem",relief=RAISED, image=delete,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=delete_recurring_line_item)
    dele.pack(side="left", pady=3, ipadx=4)

    w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="left", padx=5)

    prev= Button(firFrame,compound="top", text="Preview\nInvoice",relief=RAISED, image=photo4,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=printpreviewinvoice_recurring)
    prev.pack(side="left", pady=3, ipadx=4)

    prin= Button(firFrame,compound="top", text="Print \nInvoice",relief=RAISED, image=photo5,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=print_invoice_recurring)
    prin.pack(side="left", pady=3, ipadx=4)

    w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="left", padx=5)
            
    def emailorder():
      mailDetail=Toplevel()
      mailDetail.title("E-Mail Invoice List")
      p2 = PhotoImage(file = "images/fbicon.png")
      mailDetail.iconphoto(False, p2)
      mailDetail.geometry("1030x550+150+120")
    
      def my_SMTP():
          if True:
              em_ser_conbtn.destroy()
              mysmtpservercon=LabelFrame(account_Frame,text="SMTP server connection(ask your ISP for your SMTP settings)", height=165, width=380)
              mysmtpservercon.place(x=610, y=110)
              lbl_hostn=Label(mysmtpservercon, text="Hostname").place(x=5, y=10)
              hostnent=Entry(mysmtpservercon, width=30).place(x=80, y=10)
              lbl_portn=Label(mysmtpservercon, text="Port").place(x=5, y=35)
              portent=Entry(mysmtpservercon, width=30).place(x=80, y=35)
              lbl_usn=Label(mysmtpservercon, text="Username").place(x=5, y=60)
              unament=Entry(mysmtpservercon, width=30).place(x=80, y=60)
              lbl_pasn=Label(mysmtpservercon, text="Password").place(x=5, y=85)
              pwdent=Entry(mysmtpservercon, width=30).place(x=80, y=85)
              ssl_chkvar=IntVar()
              ssl_chkbtn=Checkbutton(mysmtpservercon, variable=ssl_chkvar, text="This server requires a secure connection(SSL)", onvalue=1, offvalue=0)
              ssl_chkbtn.place(x=50, y=110)
              em_ser_conbtn1=Button(account_Frame, text="Test E-mail Server Connection").place(x=610, y=285)
          else:
              pass
        
      style = ttk.Style()
      style.theme_use('default')
      style.configure('TNotebook.Tab', background="#999999", padding=5)
      email_Notebook = ttk.Notebook(mailDetail)
      email_Frame = Frame(email_Notebook, height=500, width=1080)
      account_Frame = Frame(email_Notebook, height=550, width=1080)
      email_Notebook.add(email_Frame, text="E-mail")
      email_Notebook.add(account_Frame, text="Account")
      email_Notebook.place(x=0, y=0)
      messagelbframe=LabelFrame(email_Frame,text="Message", height=495, width=730)
      messagelbframe.place(x=5, y=5)
      lbl_emailtoaddr=Label(messagelbframe, text="Email to address").place(x=5, y=5)
      emailtoent=Entry(messagelbframe, width=50).place(x=120, y=5)
      sendemail_btn=Button(messagelbframe, text="Send Email", width=10, height=1).place(x=600, y=10)
      lbl_carcopyto=Label(messagelbframe, text="Carbon copy to").place(x=5, y=32)
      carcopyent=Entry(messagelbframe, width=50).place(x=120, y=32)
      stopemail_btn=Button(messagelbframe, text="Stop sending", width=10, height=1).place(x=600, y=40)
      lbl_subject=Label(messagelbframe, text="Subject").place(x=5, y=59)
      subent=Entry(messagelbframe, width=50).place(x=120, y=59)
    mail= Button(firFrame,compound="top", text="Email\nInvoice",relief=RAISED, image=photo6,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=email_invoice_recurring)
    mail.pack(side="left", pady=3, ipadx=4)

    sms1= Button(firFrame,compound="top", text="Send SMS\nnotification",relief=RAISED, image=photo10,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=sms_recurring)
    sms1.pack(side="left", pady=3, ipadx=4)

    w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="left", padx=5)

    mark= Button(firFrame,compound="top", text="Mark invoice\nas 'Paid'",relief=RAISED, image=mark1,bg="#f5f3f2", fg="black", height=55, bd=1, width=57,command=markinvoice_recurring)
    mark.pack(side="left", pady=3, ipadx=4)

    void= Button(firFrame,compound="top", text="Void\ninvoice",relief=RAISED, image=mark2,bg="#f5f3f2", fg="black", height=55, bd=1, width=56,command=voidinvoice_recurring)
    void.pack(side="left", pady=3, ipadx=4)


    w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
    w.pack(side="left", padx=5)
    def calculator_recurring():
      subprocess.Popen('C:\Windows\\System32\\calc.exe')


    calc= Button(firFrame,compound="top", text="Open\nCalculator",relief=RAISED, image=photo9,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=calculator_recurring)
    calc.pack(side="left", pady=3, ipadx=4)

    fir1Frame=Frame(pop, height=180,bg="#f5f3f2")
    fir1Frame.pack(side="top", fill=X)
    labelframe1 = LabelFrame(fir1Frame,text="Customers",font=("arial",15))
    labelframe1.place(x=10,y=5,width=640,height=160)
    def recur_inv_to_combo(event):
      inv_to_str = inv_to.get()
      sql = "SELECT * FROM Customer WHERE businessname=%s"
      val = (inv_to_str,)
      fbcursor.execute(sql,val)
      inv_sel_combo = fbcursor.fetchone()
      print(inv_sel_combo)
      ee2.delete('1.0',END)
      ee2.insert('1.0',inv_sel_combo[5])
      ee3.delete(0, END)
      ee3.insert(0, inv_sel_combo[9])
      ee4.delete('1.0',END)
      ee4.insert('1.0',inv_sel_combo[6])
      ee5.delete(0,END)
      ee5.insert(0,inv_sel_combo[7])
      ee6.delete(0,END)
      ee6.insert(0,inv_sel_combo[12])


    sql = "select businessname from Customer"
    fbcursor.execute(sql,)
    global pdata
    pdata = fbcursor.fetchall()
    print(pdata)
    # global ee1,ee2,ee3,ee4,ee5,ee6
   
    invoice_to = Label(labelframe1, text="Order to").place(x=10,y=5)
    inv_to = StringVar()
    ee1 = ttk.Combobox(labelframe1,width=28,textvariable=inv_to)
    ee1.place(x=80,y=5)
    ee1.place(x=80,y=5)
    ee1['values'] = pdata
    ee1.bind("<<ComboboxSelected>>", recur_inv_to_combo)
    
    address=Label(labelframe1,text="Address").place(x=10,y=30)
    ee2=scrolledtext.Text(labelframe1, undo=True,width=23)
    ee2.place(x=80,y=30,height=70)
    ship=Label(labelframe1,text="Ship to").place(x=342,y=5)
    ee3=Entry(labelframe1,width=30)
    ee3.place(x=402,y=3)
    address1=Label(labelframe1,text="Address").place(x=340,y=30)
    ee4=scrolledtext.Text(labelframe1, undo=True,width=23)
    ee4.place(x=402,y=30,height=70)

    btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=280, y=50)
    
    labelframe2 = LabelFrame(fir1Frame,text="")
    labelframe2.place(x=10,y=130,width=640,height=42)
    email=Label(labelframe2,text="Email").place(x=10,y=5)
    ee5=Entry(labelframe2,width=30)
    ee5.place(x=80,y=5)
    sms=Label(labelframe2,text="SMS Number").place(x=328,y=5)
    ee6=Entry(labelframe2,width=30)
    ee6.place(x=402,y=5)
      
    labelframe = LabelFrame(fir1Frame,text="Invoice",font=("arial",15))
    labelframe.place(x=652,y=5,width=290,height=170)
    order=Label(labelframe,text="Invoice#").place(x=5,y=5)
    invoice_number_entry=Entry(labelframe,width=25)
    invoice_number_entry.place(x=100,y=5,)
    orderdate=Label(labelframe,text="Invoice date").place(x=5,y=33)
    invoice_date_entry=DateEntry(labelframe,width=20)
    invoice_date_entry.place(x=150,y=33)
    checkvarStatus5=IntVar()
    duedate=Checkbutton(labelframe,variable = checkvarStatus5,text="Due date",onvalue =0 ,offvalue = 1).place(x=5,y=62)
    due_date_entry=Entry(labelframe,width=20)
    due_date_entry.place(x=150,y=62)
    terms=Label(labelframe,text="Terms").place(x=5,y=92)
    terms_entry=ttk.Combobox(labelframe, value="",width=25)
    terms_entry.place(x=100,y=92)
    ref=Label(labelframe,text="Order ref#").place(x=5,y=118)
    orderref_entry=Entry(labelframe,width=27)
    orderref_entry.place(x=100,y=118)
    invoice_number_entry.delete(0, END)
    invoice_number_entry.insert(0,rec_edit_inv_data[1])
    invoice_date_entry.delete(0, END)
    invoice_date_entry.insert(0,rec_edit_inv_data[2])
    due_date_entry.delete(0, END)
    due_date_entry.insert(0,rec_edit_inv_data[3])
    orderref_entry.delete(0, END)
    orderref_entry.insert(0,rec_edit_inv_data[5])
    
    term_sql = "SELECT terms_of_payment FROM terms_of_payment"
    fbcursor.execute(term_sql,)
    term_data = fbcursor.fetchall()
    tdata = []
    for i in term_data:
      tdata.append(i[0])
    
    
    # inv_terms_label=Label(labelframe,text="Terms").place(x=5,y=92)
    # inv_terms_combo=ttk.Combobox(labelframe, value="",width=23)
    # inv_terms_combo.place(x=100,y=92)
    terms_entry['values'] = tdata
    terms_entry.bind("<<ComboboxSelected>>")
    ee1.delete(0, END)#buisiness name
    ee1.insert(0,rec_edit_inv_data[18])
    ee2.delete('1.0',END)#address
    ee2.insert('1.0',rec_edit_inv_data[19])
    ee3.delete(0, END)#ship to customer name
    ee3.insert(0, rec_edit_inv_data[20])
    ee4.delete('1.0',END)#ship address
    ee4.insert('1.0',rec_edit_inv_data[21])
    ee5.delete(0,END)#email
    ee5.insert(0,rec_edit_inv_data[22])
    ee6.delete(0,END)#smsnumber
    ee6.insert(0,rec_edit_inv_data[23])


    fir2Frame=Frame(pop, height=150,width=100,bg="#f5f3f2")
    fir2Frame.pack(side="top", fill=X)
    listFrame = Frame(fir2Frame, bg="white", height=140,borderwidth=5,  relief=RIDGE)
    
    sub_rec_tree=ttk.Treeview(listFrame)
    sub_rec_tree["columns"]=["1","2","3","4","5","6","7","8"]

    sub_rec_tree.column("#0", width=40)
    sub_rec_tree.column("1", width=80)
    sub_rec_tree.column("2", width=190)
    sub_rec_tree.column("3", width=190)
    sub_rec_tree.column("4", width=80)
    sub_rec_tree.column("5", width=60)
    sub_rec_tree.column("6", width=60)
    sub_rec_tree.column("7", width=60)
    sub_rec_tree.column("8", width=80)
    
    sub_rec_tree.heading("#0")
    sub_rec_tree.heading("1",text="ID/SKU")
    sub_rec_tree.heading("2",text="Product/Service")
    sub_rec_tree.heading("3",text="Description")
    sub_rec_tree.heading("4",text="Unit Price")
    sub_rec_tree.heading("5",text="Quality")
    sub_rec_tree.heading("6",text="Pcs/Weight")
    sub_rec_tree.heading("7",text="Tax1")
    sub_rec_tree.heading("8",text="Price")
    
    sub_rec_tree.pack(fill="both", expand=1)
    listFrame.pack(side="top", fill="both", padx=5, pady=3, expand=1)

    fir3Frame=Frame(pop,height=200,width=700,bg="#f5f3f2")
    fir3Frame.place(x=0,y=490)

    tabStyle = ttk.Style()
    tabStyle.theme_use('default')
    tabStyle.configure('TNotebook.Tab', background="#999999", width=12, padding=5)
    myNotebook=ttk.Notebook(fir3Frame)
    invoiceFrame = Frame(myNotebook, height=200, width=800)
    recurFrame = Frame(myNotebook, height=200, width=800)
    payementFrame = Frame(myNotebook, height=200, width=800)
    headerFrame = Frame(myNotebook, height=200, width=800)
    commentFrame = Frame(myNotebook, height=200, width=800)
    termsFrame = Frame(myNotebook, height=200, width=800)
    noteFrame = Frame(myNotebook, height=200, width=800)
    documentFrame = Frame(myNotebook, height=200, width=800)
    
    myNotebook.add(invoiceFrame,compound="left", text="Invoice")
    myNotebook.add(recurFrame,compound="left", text="Recurring")
    myNotebook.add(payementFrame,compound="left", text="Payements")
    myNotebook.add(headerFrame,compound="left",  text="Header/Footer")
    myNotebook.add(commentFrame,compound="left",  text="Comments")
    myNotebook.add(termsFrame,compound="left", text="Terms")
    myNotebook.add(noteFrame,compound="left",  text="Private notes")
    myNotebook.add(documentFrame,compound="left",  text="Documents")
    myNotebook.pack(expand = 1, fill ="both")  


    
    recurring_labelframe = LabelFrame(recurFrame,text="",font=("arial",15))
    recurring_labelframe.place(x=1,y=1,width=735,height=170)

    # def inv_stop_check_1():
    #   if checkstopStatus_1.get() == 0:
    #     recur_stop_date_1['state'] = NORMAL
    #   else:
    #     recur_stop_date_1['state'] = DISABLED
    def recur_check():
      if recurring_status_check.get() == 0:
        recurring_period_entry['state'] = DISABLED
        recurring_month_combo['state'] = DISABLED
        recurring_next_invoice_date['state'] = DISABLED
        recurring_stop_check['state'] = DISABLED
        recurring_stop_date['state'] = DISABLED
        recurring_recalc['state'] = DISABLED
      else:
        recurring_status_check.set(1)
        recurring_period_entry['state'] = NORMAL
        recurring_month_combo['state'] = NORMAL
        recurring_next_invoice_date['state'] = NORMAL
        recurring_stop_check['state'] = NORMAL
        recurring_stop_date['state'] = NORMAL
        recurring_recalc['state'] = NORMAL 

    mdata_1 = ["Month(s)","Day(s)"]
    
    recurring_status_check=IntVar()
    recurring_status_check.set(1)
    recurring_check_button = Checkbutton(recurring_labelframe,command=recur_check,variable=recurring_status_check,text="Recurring",onvalue= 1,offvalue=0)
    recurring_check_button.place(x=25,y=20)
    recurring_period_label = Label(recurring_labelframe,text="Recurring period (interval)").place(x=130,y=45)
    recurring_period_entry = Spinbox(recurring_labelframe,width=10,from_=1,to=10)
    recurring_period_entry.place(x=280,y=45)
    recurring_month_combo = ttk.Combobox(recurring_labelframe,values="",width=15)
    recurring_month_combo.place(x=360,y=45)
    recurring_month_combo['values'] = mdata_1
    recurring_next_inv_label = Label(recurring_labelframe,text="Next Invoice").place(x=280,y=70)
    recurring_next_invoice_date = DateEntry(recurring_labelframe,width=20)
    recurring_next_invoice_date.place(x=360,y=70)
    checkstopStatus_1 = IntVar()
    recurring_stop_check = Checkbutton(recurring_labelframe,variable=checkstopStatus_1,text="Stop recurring after",onvalue=1,offvalue=0)
    recurring_stop_check.place(x=225,y=95)
    recurring_stop_date = DateEntry(recurring_labelframe,width=20)
    recurring_stop_date.place(x=360,y=95)
    # def recalculator():  
    #   # date_1 = invoice_date_entry.get()
    #   # print(date_1)
    #   # print(recurring_period_entry.get())
      
    #   if recurring_month_combo.get() == "Month(s)":
    #     # end_date = date_1 + str(datetime.timedelta(int(recurring_period_entry.get())*365/12))
    #     date_1 = datetime.datetime(str(invoice_date_entry.get()))
    #     print(date_1)
    #     end_date = date_1 + datetime.timedelta(days=int(recurring_period_entry.get()))

    #   elif recurring_month_combo.get() == "Day(s)":
    #     end_date = date_1 + str(datetime.timedelta(days=int(recurring_period_entry.get())))
        
          
          
    #   print(end_date)
    #   recurring_next_invoice_date.delete(0,'end')
    #   recurring_next_invoice_date.insert(0, end_date.strftime('%m/%d/%y'))
    # def recalculatorr():
    #   date_1 = str(datetime.datetime(invoice_date_entry.get_date(), "%m/%d/%y"))
 
    #   end_date = date_1 + datetime.timedelta(days=int(recurring_period_entry.get()))
    #   print(end_date)
 
      # converted_date.config(text=f"Date: {end_date.strftime('%m/%d/%Y')}")

    recurring_recalc = Button(recurring_labelframe,compound=LEFT,image=recalc,text="Recalculate",width=80,height=12)
    recurring_recalc.place(x=540,y=70)


    recurring_period_entry.delete(0, END)
    recurring_period_entry.insert(0, rec_edit_inv_data[24])
    recurring_month_combo.delete(0,END)
    recurring_month_combo.insert(0,rec_edit_inv_data[25])
    recurring_next_invoice_date.delete(0,END)
    recurring_next_invoice_date.insert(0,rec_edit_inv_data[26])
    recurring_stop_date.delete(0,END)
    recurring_stop_date.insert(0,rec_edit_inv_data[27])

    
    pay_labelframe_1 = LabelFrame(payementFrame,text="",font=("arial",15))
    pay_labelframe_1.place(x=1,y=1,width=735,height=170)
    pay_tree_1 = ttk.Treeview(payementFrame,height=6)
    pay_tree_1["columns"] = ["1","2","3","4","5"]
    pay_tree_1.column("#0", width=10)
    pay_tree_1.column("1", width=130)
    pay_tree_1.column("2", width=130)
    pay_tree_1.column("3", width=130)
    pay_tree_1.column("4", width=130)
    pay_tree_1.column("5", width=130)
    pay_tree_1.heading("#0", text="",anchor=W)
    pay_tree_1.heading("1",text="Payment ID")
    pay_tree_1.heading("2",text="Payment date")
    pay_tree_1.heading("3",text="Paid by")
    pay_tree_1.heading("4",text="Description")
    pay_tree_1.heading("5",text="Amount")
    pay_tree_1.place(x=45,y=20)

    def add_plus_invo():
      get_pay_sql = "SELECT * FROM payments WHERE invoice_number=%s"
      get_pay_val = (rec_edit_inv_data[1],)
      fbcursor.execute(get_pay_sql,get_pay_val)
      get_pay_data = fbcursor.fetchall()

      # len_pay = []
      # for gpay in get_pay_data:
      #   if gpay[2] == '':
      #     pass
      #   else:
      #     len_pay.append(gpay[2])
      
      check_newline = sub_rec_tree.get_children()
      if ee1.get() == '':
        messagebox.showwarning("F-Billing Revolution","Customer required, please select customer first.")
      elif len(check_newline) == 0:
        messagebox.showwarning("F-Billing Revolution","This invoice has no line items. \nPlease add line item(s) first.")
      else:
        mark_inv=Toplevel()
        mark_inv.geometry("700x480+240+150")
        mark_inv.title("Record Payement for Invoice")

        # if tax_radio == 1:
        #   if sel_pro_str[10] == "0" and sel_pro_str[19] == "0":
        #     for i in add_newline_tree.get_children():
        #       price = float(add_newline_tree.item(i,'values')[3])
        #     total_cost = 0.0
        #     t = 0.0
        #     dis_rate = float(dis_rate_entry.get())
        #     if dis_rate == "0":
        #       t = price
        #     else:
        #       discount_rate = (price*dis_rate)/100
        #       t = price-discount_rate
        #     total_cost += t
        # elif tax_radio == 2:
        #   if sel_pro_str[10] == "1":
        #     for i in add_newline_tree.get_children():
        #       price = float(add_newline_tree.item(i,'values')[3])
        #     tax1 = float(sectab[16])
        #     tax1_rate = (price*tax1)/100
        #     total_cost = 0.0
        #     t = 0.0
        #     dis_rate = float(dis_rate_entry.get())
        #     if dis_rate == "0":
        #       t = (price + tax1_rate)
        #     else:
        #       discount_rate = ((price + tax1_rate)*dis_rate)/100
        #       t = (price + tax1_rate)-discount_rate
        #     total_cost += t
        #   else:
        #     for i in add_newline_tree.get_children():
        #       price = float(add_newline_tree.item(i,'values')[3])
        #     total_cost = 0.0
        #     t = 0.0
        #     dis_rate = float(dis_rate_entry.get())
        #     if dis_rate == "0":
        #       t = price
        #     else:
        #       discount_rate = (price*dis_rate)/100
        #       t = price-discount_rate
        #     total_cost += t
        # elif tax_radio == 3:
        #   if sel_pro_str[10] == "1" and sel_pro_str[19] == "1":
        #     for i in add_newline_tree.get_children():
        #       price = float(add_newline_tree.item(i,'values')[3])
        #     tax1 = float(sectab[16])
        #     tax2 = float(sectab[19])
        #     tax1_rate = (price*tax1)/100
        #     tax2_rate = ((price + tax1_rate)*tax2)/100
        #     total_cost = 0.0
        #     t = 0.0
        #     dis_rate = float(dis_rate_entry.get())
        #     if dis_rate == "0":
        #       t = (price + tax1_rate + tax2_rate)
        #     else:
        #       discount_rate = ((price + tax1_rate + tax2_rate)*dis_rate)/100
        #       t = (price + tax1_rate + tax2_rate)-discount_rate
        #     total_cost += t
        #   elif sel_pro_str[10] == "1" and sel_pro_str[19] == "0":
        #     for i in add_newline_tree.get_children():
        #       price = float(add_newline_tree.item(i,'values')[3])
        #     tax1 = float(sectab[16])
        #     tax1_rate = (price*tax1)/100
        #     total_cost = 0.0
        #     t = 0.0
        #     dis_rate = float(dis_rate_entry.get())
        #     if dis_rate == "0":
        #       t = (price + tax1_rate)
        #     else:
        #       discount_rate = ((price + tax1_rate)*dis_rate)/100
        #       t = (price + tax1_rate)-discount_rate
        #     total_cost += t
        #   elif sel_pro_str[10] == "0" and sel_pro_str[19] == "1":
        #     for i in add_newline_tree.get_children():
        #       price = float(add_newline_tree.item(i,'values')[3])
        #     tax2 = float(sectab[19])
        #     tax2_rate = (price *tax2)/100
        #     total_cost = 0.0
        #     t = 0.0
        #     dis_rate = float(dis_rate_entry.get())
        #     if dis_rate == "0":
        #       t = (price + tax2_rate)
        #     else:
        #       discount_rate = ((price + tax2_rate)*dis_rate)/100
        #       t = (price + tax1_rate)-discount_rate
        #     total_cost += t
        #   else:
        #     for i in add_newline_tree.get_children():
        #       price = float(add_newline_tree.item(i,'values')[3])
        #     total_cost = 0.0
        #     t = 0.0
        #     dis_rate = float(dis_rate_entry.get())
        #     if dis_rate == "0":
        #       t = price
        #     else:
        #       discount_rate = (price*dis_rate)/100
        #       t = price-discount_rate
        #     total_cost += t

      def add_newline_pay():
        pay_amnt = inv_amnt_entry_1.get()
        pay_date = inv_pdate_entry_1.get()
        pay_by = inv_pby_combo_1.get()
        pay_desc = inv_des_entry_1.get()
        pay_inv_number = inv_number_entry.get()
        pay_sql = "INSERT INTO payments(payment_date,paid_by,description,amount,invoice_number) VALUES(%s,%s,%s,%s,%s)"
        pay_val = (pay_date,pay_by,pay_desc,pay_amnt,pay_inv_number,)
        fbcursor.execute(pay_sql,pay_val)
        fbilldb.commit()


        pay_get_sql = "SELECT * FROM payments WHERE invoice_number=%s"
        payy_get_val = (pay_inv_number,)
        fbcursor.execute(pay_get_sql,payy_get_val)
        pay_data = fbcursor.fetchone()
        pay_tree_1.insert(parent='',index='end',iid=pay_data[0],text='',values=(pay_data[4],pay_data[0],pay_data[1],pay_data[2],pay_data[3]))
        mark_inv.destroy()

        if checkvar1.get() == 1:
          send_precp = Toplevel()
          p2 = PhotoImage(file = "images/fbicon.png")
          send_precp.iconphoto(False, p2)
          send_precp.geometry("1030x490+150+120")
          send_precp.title("Payment reciept E-mail")

          style = ttk.Style()
          style.theme_use('default')
          style.configure('TNotebook.Tab', background="#999999", padding=5)
          email_Notebook = ttk.Notebook(send_precp)
          email_Frame = Frame(email_Notebook, height=500, width=1080)
          account_Frame = Frame(email_Notebook, height=550, width=1080)
          email_Notebook.add(email_Frame, text="E-mail")
          email_Notebook.add(account_Frame, text="Account")
          email_Notebook.place(x=0, y=0)
          messagelbframe=LabelFrame(email_Frame,text="Message", height=450, width=730)
          messagelbframe.place(x=5, y=5)
          email_to_addr_label=Label(messagelbframe, text="Email to address").place(x=5, y=5)
          email_to_addr_entry=Entry(messagelbframe, width=50)
          email_to_addr_entry.place(x=120, y=5)
          email_addr = ee5.get()
          email_to_addr_entry.delete(0,END)
          email_to_addr_entry.insert(0,email_addr)
          send_email_btn=Button(messagelbframe, text="Send Email", width=10, height=1).place(x=600, y=10)
          carbon_label=Label(messagelbframe, text="Carbon copy to").place(x=5, y=32)
          carbon_entry=Entry(messagelbframe, width=50).place(x=120, y=32)
          stop_email_btn=Button(messagelbframe, text="Stop sending", width=10, height=1,state=DISABLED)
          stop_email_btn.place(x=600, y=40)
          subject_label=Label(messagelbframe, text="Subject").place(x=5, y=59)
          subject_entry=Entry(messagelbframe, width=50)
          subject_entry.place(x=120, y=59)
          subject = inv_number_entry.get()
          subject_entry.delete(0,END)
          subject_entry.insert(0,"Payment reciept for Invoice" + " " + "(" + subject + ")")

                  


  #email


          style = ttk.Style()
          style.theme_use('default')
          style.configure('TNotebook.Tab', background="#999999", width=20, padding=5)
          mess_Notebook = ttk.Notebook(messagelbframe)
          emailmessage_Frame = Frame(mess_Notebook,height=305, width=710)
          htmlsourse_Frame = Frame(mess_Notebook, height=305, width=710)
          mess_Notebook.add(emailmessage_Frame, text="E-mail message")
          mess_Notebook.add(htmlsourse_Frame, text="Html sourse code")
          mess_Notebook.place(x=5, y=90)

          btn1=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)  
          btn2=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
          btn3=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
          btn4=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
          btn5=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=undo).place(x=140, y=1)
          btn6=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=redo).place(x=175, y=1)
          btn7=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=bold).place(x=210, y=1)
          btn8=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=italics).place(x=245, y=1)
          btn9=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=underline).place(x=280, y=1)
          btn10=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=left).place(x=315, y=1)
          btn11=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=right).place(x=350, y=1)
          btn12=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=center).place(x=385, y=1)
          btn13=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=hyperlink).place(x=420, y=1)
          btn14=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=remove).place(x=455, y=1)

          dropcomp = ttk.Combobox(emailmessage_Frame, width=12, height=3).place(x=500, y=5)
          dropcompo = ttk.Combobox(emailmessage_Frame, width=6, height=3).place(x=600, y=5)
          mframe=scrolledtext.ScrolledText(emailmessage_Frame, height=17, width=86, bg="white")
          mframe.place(x=0, y=28)
          btn1=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)
          btn2=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
          btn3=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
          btn4=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
          mframe=Frame(htmlsourse_Frame, height=350, width=710, bg="white")
          mframe.place(x=0, y=28)
          attachlbframe=LabelFrame(email_Frame,text="Attachment(s)", height=350, width=280)
          attachlbframe.place(x=740, y=5)
          htcodeframe=Frame(attachlbframe, height=220, width=265, bg="white").place(x=5, y=5)
          lbl_btn_info=Label(attachlbframe, text="Double click on attachment to view").place(x=30, y=230)
          btn17=Button(attachlbframe, width=20, text="Add attacment file...").place(x=60, y=260)
          btn18=Button(attachlbframe, width=20, text="Remove attacment").place(x=60, y=295)
          lbl_tt_info=Label(email_Frame, text="You can create predefined invoice, order, estimate\nand payment receipt email templates under Main\nmenu/Settings/E-Mail templates tab")
          lbl_tt_info.place(x=740, y=370)

          ready_frame=Frame(send_precp, height=20, width=1080, bg="#b3b3b3").place(x=0,y=530)
          
          sendatalbframe = LabelFrame(account_Frame,text="E-Mail(Sender data)",height=270, width=600)
          sendatalbframe.place(x=5, y=5)
          your_cemail_label = Label(sendatalbframe, text="Your company email address").place(x=5, y=30)
          your_cemail_entry = Entry(sendatalbframe, width=40)
          your_cemail_entry.place(x=195, y=30)
          your_cemail_entry.delete(0,END)
          your_cemail_entry.insert(0,email_addr)

          your_cname_label = Label(sendatalbframe, text="Your name or company name").place(x=5, y=60)
          your_cname_entry = Entry(sendatalbframe, width=40)
          your_cname_entry.place(x=195, y=60)
          company_name = ee1.get()
          your_cname_entry.delete(0,END)
          your_cname_entry.insert(0,company_name)
          replay_email_label = Label(sendatalbframe, text="Reply to email address").place(x=5, y=90)
          replay_email_entry = Entry(sendatalbframe, width=40)
          replay_email_entry.place(x=195, y=90)
          replay_email_entry.delete(0,END)
          replay_email_entry.insert(0,email_addr)
          lbl_sign=Label(sendatalbframe, text="Signature").place(x=5, y=120)
          signent=Entry(sendatalbframe,width=50).place(x=100, y=120,height=75)
          confirm_chkvar=IntVar()
          confirm_chkbtn=Checkbutton(sendatalbframe, variable=confirm_chkvar, text="Confirmation reading", onvalue=1, offvalue=0)
          confirm_chkbtn.place(x=200, y=215)
          btn18=Button(account_Frame, width=15, text="Save settings").place(x=25, y=285)

          sendatalbframe=LabelFrame(account_Frame,text="SMTP Server",height=100, width=380)
          sendatalbframe.place(x=610, y=5)
          servar=IntVar()
          SMTP_rbtn=Radiobutton(sendatalbframe, text="Use the Built-In SMTP Server Settings", variable=servar, value=1)
          SMTP_rbtn.place(x=10, y=10)
          MySMTP_rbtn=Radiobutton(sendatalbframe, text="Use My Own SMTP Server Settings(Recommended)", variable=servar, value=2)#, command=my_SMTP
          MySMTP_rbtn.place(x=10, y=40)
          em_ser_conbtn=Button(account_Frame, text="Test E-mail Server Connection")
          em_ser_conbtn.place(x=710, y=110)
        else:
          pass

      # def new_payment():

      checkvar=IntVar()
      checkvar1=IntVar()
      checkvar2=IntVar()

      style = ttk.Style()
      style.theme_use('default')
      style.configure('TNotebook.Tab', background="#999999", padding=5)
      mark_Notebook = ttk.Notebook(mark_inv)
      Mark_Invoice = Frame(mark_Notebook, height=470, width=750)
      mark_Notebook.add(Mark_Invoice, text="Mark Invoice")
      mark_Notebook.place(x=0, y=0)

      inv_number=Label(Mark_Invoice, text="Invoice number").place(x=10, y=10)
      inv_number_entry=Entry(Mark_Invoice, width=45)
      inv_number_entry.place(x=130, y=10)

      labelframe5 = LabelFrame(Mark_Invoice,text="Payement Record Details",bg="#f5f3f2")
      labelframe5.place(x=10,y=60,width=670,height=250)
      inv_amnt_label=Label(labelframe5, text="Payement Amount",bg="#f5f3f2").place(x=50,y=20)
      inv_amnt_entry_1 = Entry(labelframe5,width=28)
      inv_amnt_entry_1.place(x=30,y=45)
      inv_pdate_label_1 = Label(labelframe5, text="Payement Date:",bg="#f5f3f2").place(x=250,y=20)
      inv_pdate_entry_1 = Entry(labelframe5,width=28)
      inv_pdate_entry_1.place(x=220,y=45)
      inv_pby_label_1 = Label(labelframe5, text="Paid By:",bg="#f5f3f2").place(x=450,y=20)
      inv_pby_combo_1 = ttk.Combobox(labelframe5, value="Hello")
      inv_pby_combo_1.place(x=450,y=45)
      inv_des_label_1=Label(labelframe5, text="Description").place(x=30, y=80)
      inv_des_entry_1=Entry(labelframe5, width=100)
      inv_des_entry_1.place(x=30, y=120)
      inv_pfull_check_1 = Checkbutton(labelframe5,text="Paid in full and close invoice",variable=checkvar,onvalue=1,offvalue=0,bg="#f5f3f2")
      inv_pfull_check_1.place(x=30 ,y=150)
      inv_precp_label_1 = Label(labelframe5,text="Payement Reciepts",bg="#f5f3f2").place(x=300,y=145)
      inv_send_precp_1 = Checkbutton(labelframe5,text="Send Payement Reciept",variable=checkvar1,onvalue=1,offvalue=0,bg="#f5f3f2")
      inv_send_precp_1.place(x=320 ,y=170)
      inv_att_upinv_1 = Checkbutton(labelframe5,text="Attach updated invoice",variable=checkvar2,onvalue=1,offvalue=0,bg="#f5f3f2")
      inv_att_upinv_1.place(x=320 ,y=200)

      inv_pok_btn_1 =Button(Mark_Invoice,compound = LEFT,image=tick , text="Save payment", command=add_newline_pay, width=100).place(x=10, y=350)
      inv_pcan_btn_1 =Button(Mark_Invoice,compound = LEFT,image=cancel, text="Cancel", width=100).place(x=500, y=350)

    pay_plus_1 = Button(payementFrame,image=plus_1,text="",width=20,height=25,command=add_plus_invo)
    pay_plus_1.place(x=10,y=20)
    pay_minus_1 = Button(payementFrame,image=minus,text="",width=20,height=25)
    pay_minus_1.place(x=10,y=55)
    pay_srch_1 = Button(payementFrame,image=photo4,text="",width=20,height=25)
    pay_srch_1.place(x=10,y=90)
    pay_msg_1 = Button(payementFrame,image=photo6,text="",width=20,height=25)
    pay_msg_1.place(x=10,y=125)

    print("data20   " + rec_edit_inv_data[20] +"   data20" )
    pay_sql = "SELECT * FROM markinvoice WHERE paid_by=%s"
    pay_val = (rec_edit_inv_data[20],)
    fbcursor.execute(pay_sql,pay_val)
    pay_data = fbcursor.fetchone()
    # pay_tree_1.insert(parent='',index='end',iid=i,text='',values=(pay_data[0],pay_data[3],pay_data[4],pay_data[5],pay_data[6]))



    # sql = "select extracostname from invoice"
    # fbcursor.execute(sql,)
    # exdata = fbcursor.fetchall()  
  ##
  #   itemid = main_rec_tree.items(main_rec_tree.focus())["values"][1]
  #   sql = "select * from invoice where invoiceid = %s"
  #   val = (itemid, )
  #   fbcursor.execute(sql, val)
  #   orbtdata = fbcursor.fetchone()
  # ##



    sql_exn = "SELECT extra_cost_name FROM extra_cost_name"
    fbcursor.execute(sql_exn)
    ex_data = fbcursor.fetchall()
    print(ex_data)
    
    labelframe1 = LabelFrame(invoiceFrame,text="",font=("arial",15))
    labelframe1.place(x=1,y=1,width=800,height=170)

    
 
    cost1=Label(labelframe1,text="Extra cost name").place(x=2,y=5)
    extracost_entry=ttk.Combobox(labelframe1, value="",width=20)
    extracost_entry.place(x=115,y=5)
    extracost_entry['values'] = ex_data
    extracost_entry.bind("<<ComboboxSelected>>")
    extracost_entry.delete(0, END)
    print(rec_edit_inv_data[13])
    extracost_entry.insert(0, rec_edit_inv_data[13])
  #   extra4['values']= ["Shipping and handling", "Postage and handling", "Delivery cost"] 
  #   extra4.delete(0,'end')
  #   extra4.insert(0, orbtdata[11])

    e1=ttk.Combobox(labelframe1, value="",width=20).place(x=115,y=5)
    rate=Label(labelframe1,text="Discount rate").place(x=370,y=5)

    discount_rate_entry=Entry(labelframe1,width=6)
    discount_rate_entry.place(x=460,y=5)
    discount_rate_entry.delete(0, END)
    discount_rate_entry.insert(0, rec_edit_inv_data[15])
    print(rec_edit_inv_data[13])
    print("discount rate entry above")

    cost2=Label(labelframe1,text="Extra cost").place(x=35,y=35)
    extraname_entry=Entry(labelframe1,width=10)
    extraname_entry.place(x=115,y=35)
    extraname_entry.delete(0, END)
    extraname_entry.insert(0, rec_edit_inv_data[12])
    tax=Label(labelframe1,text="Tax1").place(x=420,y=35)
    tax_entry=Entry(labelframe1,width=7)
    tax_entry.place(x=460,y=35)
    tax_entry.delete(0, END)
    tax_entry.insert(0, rec_edit_inv_data[16])
    template=Label(labelframe1,text="Template").place(x=37,y=70)

    template_entry=ttk.Combobox(labelframe1, value="",width=25)
    template_entry.place(x=115,y=70)
    template_entry.delete(0, END)
    template_entry.insert(0, rec_edit_inv_data[13])

    sales=Label(labelframe1,text="Sales Person").place(x=25,y=100)
    sales_entry=Entry(labelframe1,width=18)
    sales_entry.place(x=115,y=100)
    sales_entry.delete(0, END)
    sales_entry.insert(0, rec_edit_inv_data[14])
    category=Label(labelframe1,text="Category").place(x=300,y=100)
    category_entry=Entry(labelframe1,width=22)
    category_entry.place(x=370,y=100)
    category_entry.delete(0, END)
    category_entry.insert(0, rec_edit_inv_data[17])
    
    statusfrme = LabelFrame(labelframe1,text="Status",font=("arial",15))
    statusfrme.place(x=540,y=0,width=160,height=160)
    draft_label=Label(statusfrme, text="Draft",font=("arial", 15, "bold"), fg="grey")
    draft_label.place(x=50, y=3)
    on1=Label(statusfrme, text="Emailed on:").place( y=50)
    nev1=Label(statusfrme, text="Never").place(x=100,y=50)
    on2=Label(statusfrme, text="Printed on:").place( y=90)
    nev2=Label(statusfrme, text="Never").place(x=100,y=90)
        #here it goes
    head_sql = "SELECT headerandfooter FROM header_and_footer"
    fbcursor.execute(head_sql,)
    header_data = fbcursor.fetchall()
    head_data = []
    for i in header_data:
      head_data.append(i[0])

    text1=Label(headerFrame,text="Title text").place(x=50,y=5)
    title_combo=ttk.Combobox(headerFrame, value="",width=60)
    title_combo.place(x=125,y=5)
    title_combo['values'] = head_data
    title_combo.bind("<<ComboboxSelected>>")
    text2=Label(headerFrame,text="Page header text").place(x=2,y=45)
    header_combo=ttk.Combobox(headerFrame, value=head_data,width=60)
    header_combo.place(x=125,y=45)
    header_combo.bind("<<ComboboxSelected>>")
    text3=Label(headerFrame,text="Footer text").place(x=35,y=85)
    footer_combo=ttk.Combobox(headerFrame, value=head_data,width=60)
    footer_combo.place(x=125,y=85)
    footer_combo.bind("<<ComboboxSelected>>")

    title_combo.delete(0,END)
    title_combo.insert(0,rec_edit_inv_data[39])
    header_combo.delete(0,END)
    header_combo.insert(0,rec_edit_inv_data[40])
    footer_combo.delete(0,END)
    footer_combo.insert(0,rec_edit_inv_data[41])

    text=Label(noteFrame,text="Private notes(not shown on invoice/order/estemates)").place(x=10,y=10)
    private_note_entry=Text(noteFrame,width=100,height=7)
    private_note_entry.place(x=10,y=32)
    private_note_entry.delete("1.0",END)
    private_note_entry.insert("1.0",rec_edit_inv_data[45])

    terms_entry=Text(termsFrame,width=100,height=9)
    terms_entry.place(x=10,y=10)
    terms_entry.delete("1.0",END)
    terms_entry.insert("1.0",rec_edit_inv_data[35])


    comments_entry=Text(commentFrame,width=100,height=9)
    comments_entry.place(x=10,y=22)
    comments_entry.delete("1.0",END)
    comments_entry.insert("1.0",rec_edit_inv_data[44])

    
    ################### attatch file ###########################
    def attaching_file():
      global files,file_types
      file_types = [('png files','*.png'),('jpg files','*.jpg'),('all files','*.*')]
      files = filedialog.askopenfilename(initialdir="/",filetypes=file_types)
      shutil.copyfile(files, os.getcwd()+'/images/'+files.split('/')[-1])
      file_size_1 = converting(os.path.getsize(files))
      cusventtree.insert(parent='',index='end',iid=files.split('/')[-1],text='',values=('',files.split('/')[-1],file_size_1))
      

    #################### size convertion of files############################
    def converting(B):
      BYTE = float(B)
      KB = float(1024)
      MB = float(KB**2)

      if BYTE < KB:
        return '{0} {1}'.format(BYTE,'Bytes' if 0 == B > 1 else 'Byte')
      elif KB <= BYTE < MB:
        return '{0:.2f} KB'.format(BYTE / KB)
      elif MB <= BYTE:
        return '{0:.2f} MB'.format(BYTE / MB)
    ############### delete file #################
    def deleting_file():
      selected_doc_item_1 = cusventtree.selection()[0]
      cusventtree.delete(selected_doc_item_1)


    ############## show file ###############

    def show_file(event):
      selected_file_1 = cusventtree.item(cusventtree.focus())["values"][1]
      show = Toplevel()
      show.geometry("700x500")
      show.title("View Files")
      if selected_file_1.lower().endswith(('.png','.jpg')):
        open_image_1 = Image.open("images/"+selected_file_1)
        resize_img_1 = open_image_1.resize((700,500))
        img_1 = ImageTk.PhotoImage(resize_img_1)
        image_1 = Label(show,image=img_1)
        image_1.photo = img_1
        image_1.pack()
      else:
        with open("images/"+selected_file_1,mode='r',encoding="utf-8",errors="ignore") as none_img_1:
          data_1 = none_img_1.read()
          image_1 = Label(show,text=data_1)
          image_1.pack()



    plus_button=Button(documentFrame,height=2,width=3,text="+",command=attaching_file)
    plus_button.place(x=5,y=10)
    minus_button=Button(documentFrame,height=2,width=3,text="-",command=deleting_file)
    minus_button.place(x=5,y=50)
    text=Label(documentFrame,text="Attached documents or image files.If you attach large email then email taken long time to send").place(x=50,y=10)
    cusventtree=ttk.Treeview(documentFrame, height=5)
    cusventtree["columns"]=["1","2","3"]
    cusventtree.column("#0", width=20)
    cusventtree.column("1", width=250)
    cusventtree.column("2", width=250)
    cusventtree.column("2", width=200)
    cusventtree.heading("#0",text="", anchor=W)
    cusventtree.heading("1",text="Attach to Email")
    cusventtree.heading("2",text="Filename")
    cusventtree.heading("3",text="Filesize")  
    cusventtree.place(x=50, y=45)
    cusventtree.bind('<Double-Button-1>',show_file)
    

    fir4Frame=Frame(pop,height=190,width=210,bg="#f5f3f2")
    fir4Frame.place(x=740,y=520)
    summaryfrme = LabelFrame(fir4Frame,text="Summary",font=("arial",15))
    summaryfrme.place(x=0,y=0,width=200,height=170)
    discount=Label(summaryfrme, text=str(rec_edit_inv_data[15]) + "" + "% Discount").place(x=0 ,y=0)
    discount1=Label(summaryfrme, text=rec_edit_inv_data[31]).place(x=130 ,y=0)
    sub=Label(summaryfrme, text="Subtotal").place(x=0 ,y=21)

    company_sql = "SELECT * FROM company"
    fbcursor.execute(company_sql,)
    company_data = fbcursor.fetchone()

    if company_data[12] == "1":
      sub_data = 0.0
      for record in sub_rec_tree.get_children():
        sub_data += float(sub_rec_tree.item(record,'values')[6])
      sub1_1=Label(summaryfrme, text=sub_data - rec_edit_inv_data[31])
    elif company_data[12] == "2":
      sub_data = 0.0
      for record in sub_rec_tree.get_children():
        sub_data += float(sub_rec_tree.item(record,'values')[7])
      sub1_1=Label(summaryfrme, text=sub_data - rec_edit_inv_data[31])
    elif company_data[12] == "3":
      sub_data = 0.0
      for record in sub_rec_tree.get_children():
        sub_data += float(sub_rec_tree.item(record,'values')[8])

      #calcrrr

     if company_data[12] == "1":
          add_newline_tree_1.insert(parent='',index='end',text='',values=(sel_pro_str[2],sel_pro_str[4],sel_pro_str[5],sel_pro_str[7],sel_pro_str[18],'',sel_pro_str[7]))
          price = 0.0
          total_cost = 0.0
          exc = float(ex_cost_entry_1.get())
          dis_rate = float(dis_rate_entry_1.get())
          for i in add_newline_tree_1.get_children():
            price += float(add_newline_tree_1.item(i,'values')[3])
          discount_rate = (price*dis_rate)/100
          total_cost += (price - discount_rate) + exc
          discount_1.config(text= str(dis_rate) + "" +"% Discount")
          discount1_1.config(text=round(discount_rate,2))
          sub_tot = round((price - discount_rate),2)
          sub1_1.config(text=sub_tot)
          cost1_1.config(text=round(exc,2))
          invoicetot1_1.config(text=round(total_cost,2))
          tot_paid = 0.0
          for tp in pay_tree_1.get_children():
            tot_paid += float(pay_tree_1.item(tp,'values')[4])
          total1_1.config(text=round(tot_paid,2))
          bal = round((total_cost - tot_paid),2)
          balance1_1.config(text=bal)
        elif comp_data[12] == "2":
          if sel_pro_str[10] == "1":
            add_newline_tree_1.insert(parent='',index='end',text='',values=(sel_pro_str[2],sel_pro_str[4],sel_pro_str[5],sel_pro_str[7],sel_pro_str[18],'','Yes',sel_pro_str[7]))
          else:
            add_newline_tree_1.insert(parent='',index='end',text='',values=(sel_pro_str[2],sel_pro_str[4],sel_pro_str[5],sel_pro_str[7],sel_pro_str[18],'','No',sel_pro_str[7]))
          price = 0.0
          p = 0.0
          total_cost = 0.0
          exc = float(ex_cost_entry_1.get())
          dis_rate = float(dis_rate_entry_1.get())
          tx1 = float(tax1_entry_1.get())
          for i in add_newline_tree_1.get_children():
            if add_newline_tree_1.item(i,'values')[6] == "No":
              p += float(add_newline_tree_1.item(i,'values')[3])
            else:
              price += float(add_newline_tree_1.item(i,'values')[3])
          discount_rate = ((price + p) * dis_rate)/100
          dis_price = (price * dis_rate)/100
          dis_p = (p * dis_rate)/100
          tax1_rate = ((price - dis_price)*tx1)/100
          tx_calc = (price - dis_price) + tax1_rate
          tx_calc1 = p - dis_p
          total_cost += (tx_calc + tx_calc1) + exc 
          discount_1.config(text= str(dis_rate) + "" +"% Discount")
          discount1_1.config(text=round(discount_rate,2))
          sub_tot = round(((price + p) - discount_rate),2)
          sub1_1.config(text=sub_tot)
          tax1_1.config(text=round(tax1_rate,2))
          cost1_1.config(text=round(exc,2))
          invoicetot1_1.config(text=round(total_cost,2))
          tot_paid = 0.0
          for tp in pay_tree_1.get_children():
            tot_paid += float(pay_tree_1.item(tp,'values')[4])
          total1_1.config(text=round(tot_paid,2))
          bal = round((total_cost - tot_paid),2)
          balance1_1.config(text=bal)
        elif comp_data[12] == "3":
          if sel_pro_str[10] == "1" and sel_pro_str[19] == "1":
            add_newline_tree_1.insert(parent='',index='end',text='',values=(sel_pro_str[2],sel_pro_str[4],sel_pro_str[5],sel_pro_str[7],sel_pro_str[18],'','Yes','Yes',sel_pro_str[7]))
          elif sel_pro_str[10] == "1" and sel_pro_str[19] == "0":
            add_newline_tree_1.insert(parent='',index='end',text='',values=(sel_pro_str[2],sel_pro_str[4],sel_pro_str[5],sel_pro_str[7],sel_pro_str[18],'','Yes','No',sel_pro_str[7]))
          elif sel_pro_str[10] == "0" and sel_pro_str[19] == "1":
            add_newline_tree_1.insert(parent='',index='end',text='',values=(sel_pro_str[2],sel_pro_str[4],sel_pro_str[5],sel_pro_str[7],sel_pro_str[18],'','No','Yes',sel_pro_str[7]))
          else:
            add_newline_tree_1.insert(parent='',index='end',text='',values=(sel_pro_str[2],sel_pro_str[4],sel_pro_str[5],sel_pro_str[7],sel_pro_str[18],'','No','No',sel_pro_str[7]))
          price = 0.0
          p1 = 0.0
          p2 = 0.0
          p3 = 0.0
          total_cost = 0.0
          tx1 = float(tax1_entry_1.get())
          tx2 = float(tax2_entry_1.get())
          exc = float(ex_cost_entry_1.get())
          dis_rate = float(dis_rate_entry_1.get())
          for i in add_newline_tree_1.get_children():
            if add_newline_tree_1.item(i,'values')[6] == "No" and add_newline_tree_1.item(i,'values')[7] == "No":
              p1 += float(add_newline_tree_1.item(i,'values')[3])
            elif add_newline_tree_1.item(i,'values')[6] == "Yes" and add_newline_tree_1.item(i,'values')[7] == "No":
              p2 += float(add_newline_tree_1.item(i,'values')[3])
            elif add_newline_tree_1.item(i,'values')[6] == "No" and add_newline_tree_1.item(i,'values')[7] == "Yes":
              p3 += float(add_newline_tree_1.item(i,'values')[3])
            else:
              price += float(add_newline_tree_1.item(i,'values')[3])
          discount_rate = ((p1 + p2 + p3 + price) * dis_rate)/100
          dis_p2 = (p2 * dis_rate)/100
          tax1_rate = ((p2 - dis_p2) * tx1)/100
          dis_price = (price * dis_rate)/100
          tax2_rate = ((price - dis_price) * tx1)/100
          tax3_rate = ((price - dis_price) * tx2)/100
          dis_p3= (p3 * dis_rate)/100
          tax4_rate = ((p3 - dis_p3) * tx2)/100
          dis_p4 = (p1 * dis_rate)/100
          tx_calc1 = (p2 - dis_p2) + tax1_rate
          tx_calc2 = (price - dis_price) + tax2_rate + tax3_rate
          tx_calc3 = (p3 - dis_p3) + tax4_rate
          tx_calc4 = (p1 - dis_p4)
          total_cost += (tx_calc1 + tx_calc2 + tx_calc3 + tx_calc4) + exc
          discount_1.config(text= str(dis_rate) + "" +"% Discount")
          discount1_1.config(text=round(discount_rate,2))
          sub_tot = round(((price + p1 + p2 + p3) - discount_rate),2)
          sub1_1.config(text=sub_tot)
          tax1_1.config(text=round((tax1_rate + tax2_rate),2))
          tax2_1.config(text=round((tax3_rate + tax4_rate),2))
          cost1_1.config(text=round(exc,2))
          invoicetot1_1.config(text=round(total_cost,2))
          tot_paid = 0.0
          for tp in pay_tree_1.get_children():
            tot_paid += float(pay_tree_1.item(tp,'values')[4]) 
          total1_1.config(text=round(tot_paid,2))
          bal = round((total_cost - tot_paid),2)
          balance1_1.config(text=bal)
        inv_newline_sel_1.destroy()
      show_newline_1 = inv_combo_e1_1.get()

    sub1=Label(summaryfrme, text=sub_data - rec_edit_inv_data[31]).place(x=130 ,y=21)
    tax=Label(summaryfrme, text="Tax1").place(x=0 ,y=42)
    tax1=Label(summaryfrme, text=rec_edit_inv_data[16]).place(x=130 ,y=42)
    cost=Label(summaryfrme, text="Extra cost").place(x=0 ,y=63)
    costt1=Label(summaryfrme, text=rec_edit_inv_data[12]).place(x=130 ,y=63)
    order=Label(summaryfrme, text="Order total").place(x=0 ,y=84)
    order1=Label(summaryfrme, text=rec_edit_inv_data[8]).place(x=130 ,y=84)
    total=Label(summaryfrme, text="Total paid").place(x=0 ,y=105)
    total1=Label(summaryfrme, text=rec_edit_inv_data[9]).place(x=130 ,y=105)
    balance=Label(summaryfrme, text="Balance").place(x=0 ,y=126)
    balance1=Label(summaryfrme, text=rec_edit_inv_data[10]).place(x=130 ,y=126)

    fir5Frame=Frame(pop,height=38,width=210)
    fir5Frame.place(x=735,y=485)
    btndown=Button(fir5Frame, compound="left", text="Line Down").place(x=75, y=0)
    btnup=Button(fir5Frame, compound="left", text="Line Up").place(x=150, y=0)
    if draft_label['text'] == "Void":
      recurring_check_button['state'] = DISABLED
      recurring_period_entry['state'] = DISABLED
      recurring_month_combo['state'] = DISABLED
      recurring_next_invoice_date['state'] = DISABLED
      recurring_stop_check['state'] = DISABLED
      recurring_stop_date['state'] = DISABLED
      recurring_recalc['state'] = DISABLED
    else:
      recurring_status_check.set(1)
      recurring_period_entry['state'] = NORMAL
      recurring_month_combo['state'] = NORMAL
      recurring_next_invoice_date['state'] = NORMAL
      recurring_stop_check['state'] = NORMAL
      recurring_stop_date['state'] = NORMAL
      recurring_recalc['state'] = NORMAL

  # except:
  #   try:
  #     # pop.destroy()
  #     messagebox.showerror('F-Billing Revolution', 'Select a record to edit.') 
  #   except:
  #     pass
  #     messagebox.showerror('F-Billing Revolution', 'Select a record to edit.') 




#---------------------------- Buttons--------------------------------------

recurring_mainFrame=Frame(tab4, relief=GROOVE, bg="#f8f8f2")
recurring_mainFrame.pack(side="top", fill=BOTH)

recurring_midFrame=Frame(recurring_mainFrame, bg="#f5f3f2", height=60)
recurring_midFrame.pack(side="top", fill=X)

w = Canvas(recurring_midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=(5, 2))
w = Canvas(recurring_midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=(0, 5))

invoiceLabel = Button(recurring_midFrame,compound="top", text="Generate recurring\n invoices",relief=RAISED, image=video,bg="#f8f8f2", fg="black", height=55, bd=1, width=95,command=generate_recurring_invoice_success)
invoiceLabel.pack(side="left", pady=3, ipadx=4)


w = Canvas(recurring_midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

orderLabel = Button(recurring_midFrame,compound="top", text="View/Edit\nInvoice",relief=RAISED, image=photo1,bg="#f8f8f2", fg="black", height=55, bd=1, width=75,command=view_invoice_recurring) 
orderLabel.pack(side="left")


w = Canvas(recurring_midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

previewLabel = Button(recurring_midFrame,compound="top", text="Print Preview",relief=RAISED, image=photo4,bg="#f8f8f2", fg="black", height=55, bd=1, width=75,command=printpreviewinvoice_recurring)
previewLabel.pack(side="left")

purchaseLabel = Button(recurring_midFrame,compound="top", text="Print Invoice",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=75,command=print_invoice_recurring)
purchaseLabel.pack(side="left")

w = Canvas(recurring_midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

expenseLabel = Button(recurring_midFrame,compound="top", text=" E-mail \nInvoice",relief=RAISED, image=photo6,bg="#f8f8f2", fg="black", height=55, bd=1, width=75,command=email_invoice_recurring)
expenseLabel.pack(side="left")


w = Canvas(recurring_midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

productLabel = Button(recurring_midFrame,compound="top", text="Search in\nInvoices",relief=RAISED, image=photo7,bg="#f8f8f2", fg="black", height=55, bd=1, width=75,command=search_invoice_recurring)
productLabel.pack(side="left")

w = Canvas(recurring_midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

productLabel = Button(recurring_midFrame,compound="top", text="Refresh\nInvoices list",relief=RAISED, image=photo8,bg="#f8f8f2",fg="black", height=55, bd=1, width=75)
productLabel.pack(side="left")

w = Canvas(recurring_midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

productLabel = Button(recurring_midFrame,compound="top", text="Show totals\nSUM",relief=RAISED, image=photo9,bg="#f8f8f2", fg="black", height=55, bd=1, width=75,command=lambda: label.place())
productLabel.pack(side="left")

productLabel = Button(recurring_midFrame,compound="top", text="Hide totals\nSUM",relief=RAISED, image=photo9,bg="#f8f8f2", fg="black", height=55, bd=1, width=75,command=lambda: label.place_forget())
productLabel.pack(side="left")

label = Label(recurring_mainFrame, text = "$500")
label.place(x= 100 , y=120)


invoilabel = Label(recurring_mainFrame, text="Recurring invoices", font=("arial", 18), bg="#f8f8f2")
invoilabel.pack(side="left", padx=(20,0))



#------------------------------End Buttons-----------------------------------------------







# Recurring invoice table and scrollbars


class MyApp1:
  def __init__(self, parent):
    
    self.myParent = parent 

    self.myContainer1 = Frame(parent) 
    self.myContainer1.pack()
    
    self.top_frame = Frame(self.myContainer1) 
    self.top_frame.pack(side=TOP,
      fill=BOTH, 
      expand=YES,
      )  

    self.left_frame = Frame(self.top_frame, background="white",
      borderwidth=5,  relief=RIDGE,
      height=250, 
      width=2000, 
      )
    self.left_frame.pack(side=LEFT,
      fill=BOTH, 
      expand=YES,
      )

    global main_rec_tree
    main_rec_tree = ttk.Treeview(self.left_frame, columns = (1,2,3,4,5,6,7), height = 15, show = "headings")
    main_rec_tree.pack(side = 'top')
    main_rec_tree.heading(1)
    main_rec_tree.heading(2, text="Invoice#")
    main_rec_tree.heading(3, text="Next Invoice")
    main_rec_tree.heading(4, text="Recurring Period")
    main_rec_tree.heading(5, text="Stop After")
    main_rec_tree.heading(6, text="Customer Name")
    main_rec_tree.heading(7, text="Invoice Total")  
    main_rec_tree.column(1, width = 40)
    main_rec_tree.column(2, width = 200)
    main_rec_tree.column(3, width = 200)
    main_rec_tree.column(4, width = 200)
    main_rec_tree.column(5, width = 200)
    main_rec_tree.column(6, width = 340)
    main_rec_tree.column(7, width = 190)

    scrollbar = Scrollbar(self.left_frame)
    scrollbar.place(x=1008+300+25, y=0, height=300+20)
    scrollbar.config( command=main_rec_tree.yview )

    # def genrec():
    #   sql = "select * from invoice where (recurring_period_month =%s OR recurring_period_month =%s)AND status!=%s"
    #   val = ('month(s)', 'day(s)', 'void')
    #   fbcursor.execute(sql,val)
    #   pdata = fbcursor.fetchall()
    #   # rectotalinput=0
    #   j = 0
    #   for i in pdata:
    #       main_rec_tree.insert(parent='', index='end', iid=i, text='', values=('',i[0], i[28], i[27], i[29], i[20], i[10]))
    #       j += 1
    #     for line in main_rec_tree.get_children():
    #     recidsave1=main_rec_tree.item(line)['values'][6]
    #     rectotalinput += recidsave1
    #     j += 1
    # rectotalrowcol.config(text=rectotalinput)



    tabControl = ttk.Notebook(self.left_frame,width=1)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3=  ttk.Frame(tabControl)
    tab4 = ttk.Frame(tabControl)
    tabControl.add(tab1,image=invoices,compound = LEFT, text ='Invoice Items')
    tabControl.add(tab2,image=photo11,compound = LEFT, text ='Invoice Private Notes')
    tabControl.add(tab3,image=smslog,compound = LEFT, text ='SMS log')
    tabControl.add(tab4,image=photo11,compound = LEFT, text ='Documents')
    tabControl.pack(expand = 1, fill ="both")
    
    sub_rec_tree = ttk.Treeview(tab1, columns = (1,2,3,4,5,6,7,8,), height = 15, show = "headings")
    sub_rec_tree.pack(side = 'top')
    sub_rec_tree.heading(1)
    sub_rec_tree.heading(2, text="Product/Service ID",)
    sub_rec_tree.heading(3, text="Name")
    sub_rec_tree.heading(4, text="Description")
    sub_rec_tree.heading(5, text="Price")
    sub_rec_tree.heading(6, text="QTY")
    sub_rec_tree.heading(7, text="Tax1")
    sub_rec_tree.heading(8, text="Line Total")   
    sub_rec_tree.column(1, width = 40)
    sub_rec_tree.column(2, width = 250)
    sub_rec_tree.column(3, width = 270)
    sub_rec_tree.column(4, width = 300)
    sub_rec_tree.column(5, width = 130)
    sub_rec_tree.column(6, width = 100)
    sub_rec_tree.column(7, width = 100)
    sub_rec_tree.column(8, width = 190)

    note1=Text(tab2, width=170,height=10).place(x=10, y=10)

    note1=Text(tab3, width=170,height=10).place(x=10, y=10)

    mail_rec_tree = ttk.Treeview(tab4, columns = (1,2,3), height = 15, show = "headings")
    mail_rec_tree.pack(side = 'top')
    mail_rec_tree.heading(1)
    mail_rec_tree.heading(2, text="Attach to Email",)
    mail_rec_tree.heading(3, text="Filename")
    mail_rec_tree.column(1, width = 30)
    mail_rec_tree.column(2, width = 310)
    mail_rec_tree.column(3, width = 1000)

    scrollbar = Scrollbar(self.left_frame)
    scrollbar.place(x=1004+300+25, y=360, height=195)
    scrollbar.config( command=main_rec_tree.yview )
       
myapp = MyApp1(tab4)



#-----------------Settings tab-----------------------


settingsframe=Frame(tab10, relief=GROOVE, bg="#f8f8f2")
settingsframe.pack(side="top", fill=BOTH)

settframe=Frame(settingsframe, bg="#f5f3f2", height=60)
settframe.pack(side="top", fill=X)

pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=(5, 2))
pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=(0, 5))
# def upload_filelogo():
#   global imglogo,filename
#   f_types =[('Png files','*.png'),('Jpg Files', '*.jpg')]
#   filena = filedialog.askopenfilename(filetypes=f_types)
#   shutil.copyfile(filena, os.getcwd()+'/images/'+filena.split('/')[-1])
#   print(filena.split('/')[-1])
#   image = Image.open(filena)
#   resize_image = image.resize((280, 160))
#   imglogo = ImageTk.PhotoImage(resize_image)
  # b2 = Button(secondtab,image=img)
  # b2.place(x=130, y=80)

  # btlogo = Button(secondtab,width=280,height=160,image=imglogo)
  # btlogo.place(x=580,y=280)
global filename
filename = ""
def save_company():
  company_name = comname.get()
  company_address = caddent.get(1.0,END)
  company_mail = comemail.get()
  company_salestax =comsalestax.get()
  currency = comcur.get()
  currencysign = comcursign.get()
  currencysign_placement = comcursignpla.get()
  decimal_sepator = comdecsep.get()
  currency_example = comex.get()
  date_format = comdaf.get()
  example_dateformat = exd.get_date()
  tax = radtax.get()
  tax1name = tax1namee.get()
  tax1rate = tax1ratee.get()
  printtax1 = comptax1.get()
  tax2name = tax2namee.get()
  tax2rate = tax2ratee.get()
  printtax2 = comptax2.get()
  printimage = compimg.get()
  win_menu_colour = win_menu.get()
  radiobut = radema.get()
  cbut1 = checkb1.get()
  cbut2 = checkb2.get()
  cbut3 = checkb3.get()
  cbut4 = checkb4.get()
  cbut5 = checkb5.get()
  cbut6 = checkb6.get()
  est_prefix = est_str.get()
  est_header = win_menu1.get()
  est_text1 = est_str1.get()
  est_text2 = est_str2.get()
  est_text3 = est_str3.get()
  est_text4 = est_str4.get()
  est_text5 = est_str5.get()
  est_text6 = est_str6.get()
  est_predefined = est_str7.get(1.0,END)
  est_default = win_menu2.get()
  est_spin1 = spin1.get()
  adv_default = adv_win_menu8.get()

  child = exctree.get_children()
  var = json.dumps(child)
  sql = "select image from company"
  fbcursor.execute(sql)
  im = fbcursor.fetchone()
  sql = "select * from company"
  fbcursor.execute(sql)
  i = fbcursor.fetchall()
  if not i:
    if filename == "":
      print(12)
      sql = 'insert into company(name, address, email,salestaxno,currency,currencysign,currsignplace,  decimalseperator,excurrency,dateformat,exdate,taxtype,printimageornot,tax1name,tax1rate,printtax1,  tax2name,tax2rate,printtax2,attachment_file_type,miscellanoustab_cbutton1,miscellanoustab_cbutton2,miscellanoustab_cbutton3,miscellanoustab_cbutton4,miscellanoustab_cbutton5,miscellanoustab_cbutton6,Estimate_prefix,Customizeestimatetextlabels,Customizeestimatetextlabels1,Customizeestimatetextlabels2,Customizeestimatetextlabels3,Customizeestimatetextlabels4,Customizeestimatetextlabels5,Defaultestimatetemplate,Startingestimatenumber,Predefinedtextforestimates,adv_Selectedtemplatepreview,est_Headerboxbackgroundcolor) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
      val = (company_name,company_address,company_mail,company_salestax,currency,currencysign,  currencysign_placement,decimal_sepator,currency_example,date_format,example_dateformat,tax,printimage,  tax1name,tax1rate,printtax1,tax2name,tax2rate,printtax2,radiobut,cbut1,cbut2,cbut3,cbut4,cbut5,cbut6,est_prefix,est_text1,est_text2,est_text3,est_text4,est_text5,est_text6,est_default,est_spin1,est_predefined,adv_default,est_header)
      fbcursor.execute(sql, val)
      fbilldb.commit()
    else:
      shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
      sql = 'insert into company(name, address, email,salestaxno,currency,currencysign,currsignplace,  decimalseperator,excurrency,dateformat,exdate,taxtype,printimageornot,tax1name,tax1rate,printtax1,  tax2name,tax2rate,printtax2,image,attachment_file_type,miscellanoustab_cbutton1,miscellanoustab_cbutton2,miscellanoustab_cbutton3,miscellanoustab_cbutton4,miscellanoustab_cbutton5,miscellanoustab_cbutton6,Estimate_prefix,Customizeestimatetextlabels,Customizeestimatetextlabels1,Customizeestimatetextlabels2,Customizeestimatetextlabels3,Customizeestimatetextlabels4,Customizeestimatetextlabels5,Defaultestimatetemplate,Startingestimatenumber,Predefinedtextforestimates,adv_Selectedtemplatepreview,est_Headerboxbackgroundcolor) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
      val = (company_name,company_address,company_mail,company_salestax,currency,currencysign,  currencysign_placement,decimal_sepator,currency_example,date_format,example_dateformat,tax,printimage,  tax1name,tax1rate,printtax1,tax2name,tax2rate,printtax2,filename.split('/')[-1],radiobut,cbut1,cbut2,cbut3,cbut4,cbut5,cbut6,est_prefix,est_text1,est_text2,est_text3,est_text4,est_text5,est_text6,est_default,est_spin1,est_predefined,adv_default,est_header)
      fbcursor.execute(sql, val)
      fbilldb.commit()
  else:
    if filename == "":
      sql = "update company set name=%s, address=%s, email=%s,salestaxno=%s,currency=%s,currencysign=%s,  currsignplace=%s,decimalseperator=%s,excurrency=%s,dateformat=%s,exdate=%s,taxtype=%s,  printimageornot=%s,tax1name=%s,tax1rate=%s,printtax1=%s,tax2name=%s,tax2rate=%s,printtax2=%s,attachment_file_type=%s,miscellanoustab_cbutton1=%s,miscellanoustab_cbutton2=%s,miscellanoustab_cbutton3=%s,miscellanoustab_cbutton4=%s,miscellanoustab_cbutton5=%s,miscellanoustab_cbutton6=%s,Estimate_prefix=%s,Customizeestimatetextlabels=%s,Customizeestimatetextlabels1=%s,Customizeestimatetextlabels2=%s,Customizeestimatetextlabels3=%s,Customizeestimatetextlabels4=%s,Customizeestimatetextlabels5=%s,Defaultestimatetemplate=%s,Startingestimatenumber=%s,Predefinedtextforestimates=%s,adv_Selectedtemplatepreview=%s,est_Headerboxbackgroundcolor=%s"
      val = (company_name,company_address,company_mail,company_salestax,currency,currencysign,  currencysign_placement,decimal_sepator,currency_example,date_format,example_dateformat,tax,printimage,  tax1name,tax1rate,printtax1,tax2name,tax2rate,printtax2,radiobut,cbut1,cbut2,cbut3,cbut4,cbut5,cbut6,est_prefix,est_text1,est_text2,est_text3,est_text4,est_text5,est_text6,est_default,est_spin1,est_predefined,adv_default,est_header)
      fbcursor.execute(sql, val)
      fbilldb.commit()
    else:
      shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
      sql = "update company set name=%s, address=%s, email=%s,salestaxno=%s,currency=%s,currencysign=%s,  currsignplace=%s,decimalseperator=%s,excurrency=%s,dateformat=%s,exdate=%s,taxtype=%s,  printimageornot=%s,tax1name=%s,tax1rate=%s,printtax1=%s,tax2name=%s,tax2rate=%s,printtax2=%s,image=%s,attachment_file_type=%s,miscellanoustab_cbutton1=%s,miscellanoustab_cbutton2=%s,miscellanoustab_cbutton3=%s,miscellanoustab_cbutton4=%s,miscellanoustab_cbutton5=%s,miscellanoustab_cbutton6=%s,Estimate_prefix=%s,Customizeestimatetextlabels=%s,Customizeestimatetextlabels1=%s,Customizeestimatetextlabels2=%s,Customizeestimatetextlabels3=%s,Customizeestimatetextlabels4=%s,Customizeestimatetextlabels5=%s,Defaultestimatetemplate=%s,Startingestimatenumber=%s,Predefinedtextforestimates=%s,adv_Selectedtemplatepreview=%s,est_Headerboxbackgroundcolor=%s"
      val = (company_name,company_address,company_mail,company_salestax,currency,currencysign,  currencysign_placement,decimal_sepator,currency_example,date_format,example_dateformat,tax,printimage,  tax1name,tax1rate,printtax1,tax2name,tax2rate,printtax2,filename.split('/')[-1],radiobut,cbut1,cbut2,cbut3,cbut4,cbut5,cbut6,est_prefix,est_text1,est_text2,est_text3,est_text4,est_text5,est_text6,est_default,est_spin1,est_predefined,adv_default,est_header)
      fbcursor.execute(sql, val)
      fbilldb.commit()
    
    

addcustomerIcon = ImageTk.PhotoImage(Image.open("images/user_add.png"))
save_setting = Button(settframe,compound="top", text="Save\nSettings",relief=RAISED,    command=save_company, image=saves, font=("arial", 8),bg="#f5f3f2", fg="black", height=55, bd=1, width=55)
save_setting.pack(side="left", pady=3, ipadx=4)
pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=(0, 5))

def wiz_page():
  global filname
  filname = ""
  def upload_cfilelogo():
    global filname
    f_types =[('Png files','*.png'),('Jpg Files', '*.jpg')]
    filname = filedialog.askopenfilename(filetypes=f_types)
    shutil.copyfile(filname, os.getcwd()+'/images/'+filname.split('/')[-1])
    image = Image.open(filname)
    resize_image = image.resize((280, 140))
    imgclogo = ImageTk.PhotoImage(resize_image)
    btclogo = Button(wiz,width=280,height=140,image=imgclogo)
    btclogo.place(x=30,y=240)
    btclogo.photo = imgclogo
  def csave():
    company_name = company_namee.get()
    company_address = company_addresse.get('1.0', 'end-1c')
    company_email = company_emaile.get()
    salestaxregno = salestaxregnoe.get()
    cprint_logopic = cplogopic.get()
    sql = "select image from company"
    fbcursor.execute(sql)
    im = fbcursor.fetchone()
    sql = "select * from company"
    fbcursor.execute(sql)
    i = fbcursor.fetchall()
    if not i:
      if filname == "":
        sql = 'insert into company(name, address, email,salestaxno,printimageornot) values(%s, %s, %s, %s, %s)'
        val = (company_name,company_address,company_email,salestaxregno,cprint_logopic)
        fbcursor.execute(sql, val)
        fbilldb.commit()
      else:
        shutil.copyfile(filname, os.getcwd()+'/images/'+filname.split('/')[-1])
        sql = 'insert into company(name, address, email,salestaxno,printimageornot,image) values(%s, %s, %s, %s, %s, %s)'
        val = (company_name,company_address,company_email,salestaxregno,cprint_logopic,filname.split('/')[-1],)
        fbcursor.execute(sql, val)
        fbilldb.commit()
    else:
      if filname == "":
        sql = "update company set name=%s, address=%s, email=%s,salestaxno=%s,printimageornot=%s"
        val = (company_name,company_address,company_email,salestaxregno,cprint_logopic)
        fbcursor.execute(sql, val)
        fbilldb.commit()
      else:
        shutil.copyfile(filname, os.getcwd()+'/images/'+filname.split('/')[-1])
        sql = "update company set name=%s, address=%s, email=%s,salestaxno=%s,printimageornot=%s,image=%s"
        val = (company_name,company_address,company_email,salestaxregno,cprint_logopic,filname.split('/')[-1])
        fbcursor.execute(sql, val)
        fbilldb.commit()
    centry.delete(0, END)
    centry.insert(0, company_name)
    caddent.delete('1.0', END)
    caddent.insert('1.0', company_address)
    cemailentry.delete(0, END)
    cemailentry.insert(0, company_email)
    ste.delete(0, END)
    ste.insert(0, salestaxregno)
    if cprint_logopic == 1:
      primage.select()
    else:
      primage.deselect()
    try:
      image = Image.open("images/"+filname.split('/')[-1])
      resize_image = image.resize((280, 160))
      image = ImageTk.PhotoImage(resize_image)
      btlogo = Button(secondtab,width=280,height=160,image=image)
      btlogo.place(x=580,y=280)
      btlogo.photo = image
    except:
      pass
    wiz.destroy()


    
    

  
  wiz = Toplevel()
  wiz.geometry("500x449+400+167")
  wiz.title("Wellcome to Quick Start Wizard")
  sql = "select * from company"
  fbcursor.execute(sql)
  secctab = fbcursor.fetchone()
  comp_infor = Label(wiz,text="Enter Your Company Information",font='arial 13 bold',fg="blue")
  comp_infor.place(x=15,y=15)
  company_da_laframe = LabelFrame(wiz,text="Company data",height=180, width=460)
  company_da_laframe.place(x=15,y=40)
  company_name = Label(wiz,text="Company name")
  company_name.place(x=30,y=60)
  company_namee = Entry(wiz,width=50)
  company_namee.place(x=160,y=60)
  if  not secctab:
    pass
  else:
    company_namee.insert(0, secctab[1])

  company_address = Label(wiz,text="Company address")
  company_address.place(x=30,y=90)
  company_addresse = scrolledtext.ScrolledText(wiz,)
  company_addresse.place(x=160,y=90,width=250,height=60)
  if  not secctab:
    pass
  else:
    company_addresse.insert('1.0', secctab[2])

  company_email = Label(wiz,text="Email address")
  company_email.place(x=30,y=160)
  company_emaile = Entry(wiz,width=50)
  company_emaile.place(x=160,y=160)
  if  not secctab:
    pass
  else:
    company_emaile.insert(0, secctab[3])

  salestaxregno = Label(wiz,text="Sales Tax.Reg.No")
  salestaxregno.place(x=30,y=190)
  salestaxregnoe = Entry(wiz,width=50)
  salestaxregnoe.place(x=160,y=190)
  if  not secctab:
    pass
  else:
    salestaxregnoe.insert(0, secctab[4])
  
  
  company_da_laframe = LabelFrame(wiz,text="Company logo",height=190, width=460)
  company_da_laframe.place(x=15,y=220)
  try:
    image_wiz = Image.open("images/"+secctab[13])
    resize_image = image_wiz.resize((280, 140))
    image_wiza = ImageTk.PhotoImage(resize_image)
    btclogo = Button(wiz,width=280,height=140,image=image_wiza)
    btclogo.place(x=30,y=240)
    btclogo.photo = image_wiza
  except:
    pass
  cplogopic = BooleanVar()
  cprint_logopic = Checkbutton(wiz,text='Print logo picture',bg='white',onvalue =1,
                      offvalue = 0,variable=cplogopic)
  cprint_logopic.place(x=320,y=250)
  if  not secctab:
    pass
  else:
    if secctab[14] == 1:
      cprint_logopic.select()
    else:
      cprint_logopic.deselect()
    
  load_img = Button(wiz,text='Load logo image',command=upload_cfilelogo)
  load_img.place(x=320,y=360)
  save_com_wiz = Button(wiz,text='Save',width=10,command=csave)
  save_com_wiz.place(x=370,y=415)

quick_start_wiz = Button(settframe,compound="top", text="Quick\nStart Wizard ",relief=RAISED,    command=wiz_page, image=photo, font=("arial", 8),bg="#f5f3f2", fg="black", height=55, bd=1, width=55)
quick_start_wiz.pack(side="left", pady=3, ipadx=4)
pn = Canvas(settframe, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=(0, 5))



invoi1label = Label(settingsframe, text="Settings", font=("arial", 18), bg="#f8f8f2")
invoi1label.pack(side="left", padx=(20,0))

global tab06
m = ttk.Style()
m.theme_use('default')
m.configure('one.TNotebook.Tab', background="white", width=20, padding=10)
tabControl = ttk.Notebook(tab10,style='one.TNotebook.Tab')
tab01 = ttk.Frame(tabControl)
tab02 = ttk.Frame(tabControl)
tab03=  ttk.Frame(tabControl)
tab04 = ttk.Frame(tabControl)
tab05 = ttk.Frame(tabControl)
tab06=  ttk.Frame(tabControl)
tab07 = ttk.Frame(tabControl)
tab08 = ttk.Frame(tabControl)
tab09 =  ttk.Frame(tabControl)
tab010=  ttk.Frame(tabControl)
tabControl.add(tab01,image=invoices,compound = LEFT, text ='Miscellaneous',)
tabControl.add(tab02,image=orders,compound = LEFT, text ='Company settings')
tabControl.add(tab03,image=estimates,compound = LEFT, text ='Invoiced settings')
tabControl.add(tab04,image=recurring,compound = LEFT, text ='Order settings')
tabControl.add(tab05,image=purchase,compound = LEFT, text ='Estimate settings') 
tabControl.add(tab06,image=expenses,compound = LEFT, text ='Administrator panel')
tabControl.add(tab07,image=customer,compound = LEFT, text ='Advanced settings')
tabControl.add(tab08,image=product,compound = LEFT, text ='Email templates')
tabControl.add(tab09,image=reports,compound = LEFT, text ='Payments')
tabControl.add(tab010,image=setting,compound = LEFT, text ='Purchase Order')
tabControl.pack(expand = 1, fill ="both")

################### tab01 ###################################
sql = "select * from company"
fbcursor.execute(sql)
sectab = fbcursor.fetchone()

firsttab1=Frame(tab01, relief=GROOVE, bg="#f8f8f2")
firsttab1.pack(side="top", fill=BOTH)

firsttab=Frame(firsttab1, bg="#f5f3f2", height=700)
firsttab.pack(side="top", fill=BOTH)

messagelbframe=LabelFrame(firsttab,text="Menu and Window Color Style", height=60, width=180)
messagelbframe.place(x=5, y=15)

win_menu = StringVar()
winstyle = ttk.Combobox(firsttab,textvariable=win_menu)
winstyle.place(x=22 ,y=40)
winstyle['values'] = ('whidbey','windows XP','windows 7','windows 8','windows 10')
winstyle.current(0)
fbill = Label(firsttab,text="F-Billing Revolution 2022",font="arial 12 bold").place(x=220,y=20)

dbhost=LabelFrame(firsttab,text="Database Server Hostname", height=60, width=415)
dbhost.place(x=5, y=85)

db = Label(firsttab, text="DESKTOP-2K")
db.place(x=15,y=110)

exc=LabelFrame(firsttab,text="Extra cost name", height=180, width=415)
exc.place(x=5, y=155)



def insert_valueexc():
  i = varexc.get()
  if i == "":
    pass
  else:
    entryexc.delete(0, END)
    sql1 = "select * from company"
    fbcursor.execute(sql1)
    com = fbcursor.fetchone()
    if not com:
      messagebox.showinfo("Alert", "Create Company Settings.")
    else:
      companyid = com[0]
      sql = 'insert into extra_cost_name(companyid,extra_cost_name) values(%s,%s)'
      val = (companyid,i)
      fbcursor.execute(sql,val)
      fbilldb.commit()
      for record in exctree.get_children():
        exctree.delete(record)
      sql = 'select * from extra_cost_name'
      fbcursor.execute(sql)
      setexctree = fbcursor.fetchall()
      countp = 0
      for i in setexctree:
        immm = str(i[2])
        imn = str.replace(immm," ","_")
        exctree.insert(parent='', index='end', iid=countp, text='hello', values=(imn))
        countp += 1
# new_value = String
      
      

def edit_valueexc(event):
  selected_item = exctree.selection()[0]
  temp = list(exctree.item(selected_item , 'values'))
  entryexc.delete(0, END)
  entryexc.insert(0, temp)

def save_valueexc():
  i = entryexc.get()
  if i == "":
    pass
  else:
    selected0 = exctree.focus()
    valuz1= exctree.item(selected0)["values"]
    idgettingextracnid=valuz1[0]
    print(i,idgettingextracnid)
    sql1 = "select * from company"
    fbcursor.execute(sql1)
    com = fbcursor.fetchone()
    companyid = com[0]
    if not com:
      pass
    else:
      sql = 'update extra_cost_name set extra_cost_name=%s where extra_cost_name=%s'
      val = (i,idgettingextracnid)
      fbcursor.execute(sql,val)
      fbilldb.commit()
      entryexc.delete(0, END)
      for record in exctree.get_children():
          exctree.delete(record)
      fbcursor.execute("select *  from extra_cost_name")
      pandsdata = fbcursor.fetchall()
      countp = 0
      for i in pandsdata:
        immm = str(i[2])
        imn = str.replace(immm," ","_")
        exctree.insert('', index='end', iid=countp, text='', values=(imn))
        countp += 1
  
  

def del_valueexc():
  itemid = exctree.item(exctree.focus())["values"][0]
  sql = "delete from extra_cost_name where extra_cost_name = %s"
  val = (itemid, )
  fbcursor.execute(sql, val)
  fbilldb.commit()
  exctree.delete(exctree.selection()[0])
    
    

  
  
  



scrollbarx = Scrollbar(firsttab, orient=HORIZONTAL)
scrollbary = Scrollbar(firsttab, orient=VERTICAL)
exctree = ttk.Treeview(firsttab, columns=("1"),height=40,selectmode='browse', yscrollcommand=scrollbary.set,   xscrollcommand=scrollbarx.set)
# exctree["show"]='headings'
scrollbary.config(command=exctree.yview)
scrollbary.place(x=394,y=200,height=125)
scrollbarx.config(command=exctree.xview)
scrollbarx.place(x=15,y=310, width=380)
exctree.heading('1', text="Extra cost name",)
# exctree.column('#0', stretch=NO, minwidth=0, width=0)
exctree.column("#0",width=0,anchor='c', stretch=False)
exctree.column('1',width=378,anchor='c')
exctree.place(x=15,y=200,height=115,width=380)
exctree.bind('<Double-Button-1>' , edit_valueexc)
sql = 'select * from extra_cost_name'
fbcursor.execute(sql)
setexctree = fbcursor.fetchall()
countp = 0
for i in setexctree:
    print(i[2])
    immm = str(i[2])
    imn = str.replace(immm," ","_")
    exctree.insert(parent='', index='end', iid=countp, text='', values=(imn))
    countp += 1
# new_value = StringVar()

# def edit_window_box(val):
    
#     edit_window = Toplevel(root)
#     edit_window.title("Edit the value or cancel")
#     edit_window.geometry("1000x250")
#     label_edit = Label(edit_window , text='Enter value to edit or press cancel', 
#     font = ("Times New Roman", 10)).grid(column=0,row=1,padx=0, pady = 2)
#     #create edit box
#     edit_box = Entry(edit_window)
#     edit_box.insert(0,val)
#     edit_box.grid(column=1,row=1,padx=0,pady=2)
#     #auto select edit window 
#     edit_window.focus()
    
#     def value_assignment(event):
#         printing = edit_box.get()
#         new_value.set(printing)
#         #only destroy will not update the value (perhaps event keeps running in background)
#         #quit allows event to stop n update value in tree but does not close the window in single click 
#         #rather on dbl click shuts down entire app 
#         edit_window.quit()
#         edit_window.destroy()
    
#     edit_window.bind('<Return>', value_assignment )

#     B1 = Button(edit_window, text="Okay")
#     B1.bind('<Button-1>',value_assignment)
#     B1.grid(column=0,row=10,padx=0, pady = 20)
    
#     B2 = Button(edit_window, text="Cancel", command = edit_window.destroy).grid(column=1,row=10,padx=10,   pady = 20)
#     edit_window.mainloop()
    
# #will explain
# #variable to hold col value (col clicked)
# shape1 = IntVar()
# #tracks both col , row on mouse click
# def tree_click_handler(event):
#     cur_item = exctree.item(exctree.focus())
#     col = exctree.identify_column(event.x)[1:]
#     rowid = exctree.identify_row(event.y)[1:]
#     #updates list
#     shape1.set(col)
#     try:
#         x,y,w,h = exctree.bbox('I'+rowid,'#'+col)
#     except:pass
#     #tree.tag_configure("highlight", background="yellow")
#     return(col)
    
# #code linked to event    
# exctree.bind('<ButtonRelease-1>', tree_click_handler)

# def edit(event):
#     try:
#         selected_item = exctree.selection()[0]
#         temp = list(exctree.item(selected_item , 'values'))
#         tree_click_handler
#         col_selected = int(shape1.get())-1
#         edit_window_box(temp[col_selected])
#         #do not run if edit window is open
#         #use edit_window.mainloop() so value assign after window closes
#         temp[col_selected] = new_value.get()
#         exctree.item(selected_item, values= temp)
#     except: pass
    
    
# #binding allows to edit on screen double click
# exctree.bind('<Double-Button-1>' , edit)
varexc = StringVar()
entryexc = Entry(firsttab,width=25,textvariable=varexc)
entryexc.place(x=15,y=173)

btexcadd = Button(firsttab,text="Add new line",command=insert_valueexc)
btexcadd.place(x=175,y=171)

btexcedit = Button(firsttab,text="Edit line   ",command=save_valueexc)
btexcedit.place(x=260,y=171)
btexcadd = Button(firsttab,text=" Delete line  ",command=del_valueexc)
btexcadd.place(x=330,y=171)

exc=LabelFrame(firsttab,text="Predefined text records for header and footer", height=180, width=415)
exc.place(x=5, y=350)

def insert_valuepre():
  i = prestr.get()
  if i == "":
    pass
  else:
    entrypre.delete(0, END)
    sql1 = "select * from company"
    fbcursor.execute(sql1)
    com = fbcursor.fetchone()
    if not com:
      messagebox.showinfo("Alert", "Create Company Settings.")
    else:
      companyid = com[0]
      sql = 'insert into header_and_footer(companyid,headerandfooter) values(%s,%s)'
      val = (companyid,i)
      fbcursor.execute(sql,val)
      fbilldb.commit()
      for record in pretree.get_children():
        pretree.delete(record)
      sql = 'select * from header_and_footer'
      fbcursor.execute(sql)
      setexctree = fbcursor.fetchall()
      countp = 0
      for i in setexctree:
        pret = str(i[2])
        pre = str.replace(pret," ","_")
        pretree.insert(parent='', index='end', iid=countp, text='hello', values=(pre))
        countp += 1
# new_value = String
      
      

def edit_valuepre(event):
  selected_item = pretree.selection()[0]
  temp = list(pretree.item(selected_item , 'values'))
  entrypre.delete(0, END)
  entrypre.insert(0, temp)

def save_valuepre():
  i = prestr.get()
  if i == "":
    pass
  else:
    selected0 = pretree.focus()
    valuz1= pretree.item(selected0)["values"]
    idgettingextracnid=valuz1[0]
    print(i,idgettingextracnid)
    sql1 = "select * from company"
    fbcursor.execute(sql1)
    com = fbcursor.fetchone()
    companyid = com[0]
    if not com:
      pass
    else:
      sql = 'update header_and_footer set headerandfooter=%s where headerandfooter=%s'
      val = (i,idgettingextracnid)
      fbcursor.execute(sql,val)
      fbilldb.commit()
      entryexc.delete(0, END)
      for record in pretree.get_children():
          pretree.delete(record)
      fbcursor.execute("select *  from header_and_footer")
      pandsdata = fbcursor.fetchall()
      countp = 0
      for i in pandsdata:
        pret = str(i[2])
        pre = str.replace(pret," ","_")
        pretree.insert('', index='end', iid=countp, text='', values=(pre))
        countp += 1
  
  

def del_valuepre():
  itemid = pretree.item(pretree.focus())["values"][0]
  print(itemid)
  sql = "delete from header_and_footer where headerandfooter = %s"
  val = (itemid,)
  fbcursor.execute(sql, val)
  fbilldb.commit()
  for record in pretree.get_children():
    pretree.delete(record)
  fbcursor.execute("select *  from header_and_footer")
  pandsdata = fbcursor.fetchall()
  countp = 0
  for i in pandsdata:
    pret = str(i[2])
    pre = str.replace(pret," ","_")
    pretree.insert('', index='end', iid=countp, text='', values=(pre))
    countp += 1
  
    

scrollbarx = Scrollbar(firsttab, orient=HORIZONTAL)
scrollbary = Scrollbar(firsttab, orient=VERTICAL)
pretree = ttk.Treeview(firsttab, columns=("1"),height=400,     selectmode="extended",   yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
# exctree["show"]='headings'
scrollbary.config(command=pretree.yview)
scrollbary.place(x=395,y=400,height=115)
scrollbarx.config(command=pretree.xview)
scrollbarx.place(x=15,y=510, width=380)
pretree.heading('1', text="header and footer",)
pretree.column('#0', stretch=NO, minwidth=0, width=0)
pretree.column('1', stretch=NO, width=378)
pretree.place(x=15,y=400,height=115,width=380)
pretree.bind('<Double-Button-1>' , edit_valuepre)
sql = 'select * from header_and_footer'
fbcursor.execute(sql)
setexctree = fbcursor.fetchall()
countp = 0
for i in setexctree:
  pret = str(i[2])
  pre = str.replace(pret," ","_")
  pretree.insert(parent='', index='end', iid=countp, text='hello', values=(pre))
  countp += 1
prestr = StringVar()
entrypre = Entry(firsttab,width=25,textvariable=prestr)
entrypre.place(x=15,y=370)
btexcadd = Button(firsttab,text="Add new line",command=insert_valuepre)
btexcadd.place(x=175,y=370)
btpredit = Button(firsttab,text="Edit line   ",command=save_valuepre)
btpredit.place(x=260,y=370)
btexcadd = Button(firsttab,text=" Delete line   ",command=del_valuepre)
btexcadd.place(x=330,y=370)

ver = Label(firsttab,text="FREE version.Upgrade PRO version for all features and Ad free invoice")
ver.place(x=480,y=15)


chapass=LabelFrame(firsttab,text="Change Password", height=150, width=500)
chapass.place(x=480, y=40)

enterold = StringVar()
lenold = Label(firsttab,text="Enter your old password")
lenold.place(x=495,y=60)
enold = Entry(firsttab,textvariable=enterold)
enold.place(x=640,y=60)

enternew = StringVar()
ennew = Label(firsttab,text="New password")
ennew.place(x=495,y=90)
newpass = Entry(firsttab,textvariable=enternew)
newpass.place(x=640,y=90)


cnewpass = StringVar()
cnp = Label(firsttab,text="Confirm new password")
cnp.place(x=495,y=120)
cnewp = Entry(firsttab,textvariable=cnewpass)
cnewp.place(x=640,y=120)

def change_pass():
  old_pass = enterold.get()
  new_pass = enternew.get()
  cnew_pass = cnewpass.get()
  usna = username1.get()
  print(usna)
  sql='SELECT * FROM users WHERE username=%s'
  val=(usna,)
  fbcursor.execute(sql,val)
  chpass = fbcursor.fetchone()
  print(chpass)
  if old_pass == "" or new_pass == "" or cnew_pass == "":
      messagebox.showerror('Password Error','Plz enter password')
  elif old_pass == chpass[4]:
    if new_pass == cnew_pass:
      sqll='UPDATE users SET password=%s,confirm_password=%s WHERE userID=%s'
      vall=(new_pass,cnew_pass,chpass[0])
      fbcursor.execute(sqll,vall,)
      fbilldb.commit()
      messagebox.showinfo('Updated','Password updated successfully')
    else:
      messagebox.showerror('Password Error','password is not match')
  else:
    messagebox.showerror('Password Error','Old Password is Incorrect')
chabtn = Button(firsttab,text="Change password",command=change_pass)
chabtn.place(x=840,y=150)

termf=LabelFrame(firsttab,text="Terms of payment", height=150, width=500)
termf.place(x=480, y=190)


def insert_valueterm():
  first = entrytopstr.get()
  second = entrydsstr.get()
  if first == "" or second == "":
    pass
  else:
    entrytop.delete(0, END)
    entryds.delete(0, END)
    sql1 = "select * from company"
    fbcursor.execute(sql1)
    com = fbcursor.fetchone()
    if not com:
      messagebox.showinfo("Alert", "Create Company Settings.")
    else:
      companyid = com[0]
      sql = 'insert into terms_of_payment(companyid,terms_of_payment,Date_shift) values(%s,%s,%s)'
      val = (companyid,first,second)
      fbcursor.execute(sql,val)
      fbilldb.commit()
      for record in termtree.get_children():
        termtree.delete(record)
      sql = 'select * from terms_of_payment'
      fbcursor.execute(sql)
      setexctree = fbcursor.fetchall()
      countp = 0
      for i in setexctree:
        
        termtree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[3]))
        countp += 1
# new_value = String
      
      

def edit_valueterm(event):
  itemid = termtree.item(termtree.focus())["values"][0]
  sql = "select * from terms_of_payment where terms_of_payment = %s"
  val = (itemid,)
  fbcursor.execute(sql,val)
  editterm = fbcursor.fetchone()
  entrytop.delete(0, END)
  entryds.delete(0, END)
  entrytop.insert(0, editterm[2])
  entryds.insert(0, editterm[3])

def save_valueterm():
  first = entrytopstr.get()
  second = entrydsstr.get()
  if first == "" or second == "":
    pass
  else:
    itemid = termtree.item(termtree.focus())["values"][0]
    sql1 = "select * from company"
    fbcursor.execute(sql1)
    com = fbcursor.fetchone()
    if not com:
      pass
    else:
      sql = "select * from terms_of_payment where terms_of_payment=%s"
      val = (itemid,)
      fbcursor.execute(sql,val)
      payt = fbcursor.fetchone()
      sql2 = 'update terms_of_payment set terms_of_payment=%s,Date_shift=%s where terms_of_paymentID=%s'
      val2 = (first,second,payt[0])
      fbcursor.execute(sql2,val2)
      fbilldb.commit()
      entrytop.delete(0, END)
      entryds.delete(0, END)
      for record in termtree.get_children():
        termtree.delete(record)
      fbcursor.execute("select *  from terms_of_payment")
      pandsdata = fbcursor.fetchall()
      countp = 0
      for i in pandsdata:
        
        termtree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[3]))
        countp += 1
  
  

def del_valueterm():
  itemid = termtree.item(termtree.focus())["values"][0]
  print(itemid)
  sql = "delete from terms_of_payment where terms_of_payment = %s"
  val = (itemid,)
  fbcursor.execute(sql, val)
  fbilldb.commit()
  for record in termtree.get_children():
      termtree.delete(record)
  fbcursor.execute("select *  from terms_of_payment")
  pandsdata = fbcursor.fetchall()
  countp = 0
  for i in pandsdata:
    termtree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[3]))
    countp += 1



scrollbarx = Scrollbar(firsttab, orient=HORIZONTAL)
scrollbary = Scrollbar(firsttab, orient=VERTICAL)
termtree = ttk.Treeview(firsttab, columns=("1","2"),height=400,selectmode="extended",   yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
# exctree["show"]='headings'
scrollbary.config(command=termtree.yview)
scrollbary.place(x=870,y=228,height=100)
scrollbarx.config(command=termtree.xview)
scrollbarx.place(x=495,y=313, width=380)
termtree.heading('1', text="Terms of payment",)
termtree.heading('2', text="Date shift (days)",)
termtree.column('#0', stretch=NO, minwidth=0, width=0)
termtree.column('1', stretch=NO, minwidth=0, width=250)
termtree.column('2', stretch=NO, minwidth=0, width=128)
termtree.place(x=495,y=235,height=80,width=380)
termtree.bind('<Double-Button-1>' , edit_valueterm)

sql = 'select * from terms_of_payment'
fbcursor.execute(sql)
termt = fbcursor.fetchall()
countp = 0
for i in termt:
    termtree.insert(parent='', index='end', iid=countp, text='hello', values=(i[2],i[3]))
    countp += 1
entrytopstr = StringVar()
entrytop = Entry(firsttab,width=25,textvariable=entrytopstr)
entrytop.place(x=495,y=208)
entrydsstr = StringVar()
entryds = Entry(firsttab,textvariable=entrydsstr)
entryds.place(x=670,y=208)
bttermadd = Button(firsttab,text="Add new line",command=insert_valueterm)
bttermadd.place(x=800,y=205)
bttermedit = Button(firsttab,text="     Edit line  ",command=save_valueterm)
bttermedit.place(x=890,y=205)
bttermdel = Button(firsttab,text="  Delete line  ",command=del_valueterm)
bttermdel.place(x=890,y=240)

radem=LabelFrame(firsttab,text="Invoice/Oder/Estimate/P.order Email Attachment file type", height=60,   width=500)
radem.place(x=480, y=340)
radema = StringVar()
radpdf = Radiobutton(firsttab,variable=radema,value="PDF",text='PDF')
radpdf.place(x= 485, y= 360 )
radhtml = Radiobutton(firsttab,variable=radema,value="HTML",text='HTML')
radhtml.place(x= 660, y= 360 )
if  not sectab:
  pass
else:
  if sectab[22] == 'PDF':
    radpdf.select()
  elif sectab[22] == 'HTML':
    radhtml.select()
  else:
    pass

checkb1 = IntVar()
check1 = Checkbutton(firsttab,variable = checkb1, 
                      text="PDF attachment with Embedded Fonts (PDF file size will be larger,but readable on   all devices) ", 
                      onvalue =1 ,
                      offvalue = 0,
                      )

check1.place(x=480,y=400)
if  not sectab:
  pass
else:
  if sectab[23] == 1:
    check1.select()
  else:
    check1.deselect()

checkb2 = IntVar()
check2 = Checkbutton(firsttab,variable = checkb2, 
                      text="invoice numbering with leading zero and current year", 
                      onvalue =1 ,
                      offvalue = 0,
                      )

check2.place(x=480,y=420)
if  not sectab:
  pass
else:
  if sectab[24] == 1:
    check2.select()
  else:
    check2.deselect()

checkb3 = IntVar()
check3 = Checkbutton(firsttab,variable = checkb3, 
                      text="Order numbering with leading zero and current year", 
                      onvalue =1 ,
                      offvalue = 0,
                      )

check3.place(x=480,y=440)
if  not sectab:
  pass
else:
  if sectab[25] == 1:
    check3.select()
  else:
    check3.deselect()

checkb4 = IntVar()
check4 = Checkbutton(firsttab,variable = checkb4, 
                      text="Estimate numbering with leading zero and current year", 
                      onvalue =1 ,
                      offvalue = 0,
                      )

check4.place(x=480,y=460)
if  not sectab:
  pass
else:
  if sectab[26] == 1:
    check4.select()
  else:
    check4.deselect()

checkb5 = IntVar()
check5 = Checkbutton(firsttab,variable = checkb5, 
                      text="Purchsae order numbering with leading zero and current year", 
                      onvalue =1 ,
                      offvalue = 0,
                      )
check5.place(x=480,y=480)
if  not sectab:
  pass
else:
  if sectab[27] == 1:
    check5.select()
  else:
    check5.deselect()

checkb6 = IntVar()
check6 = Checkbutton(firsttab,variable = checkb6, 
                      text="Confirmation before closing F-billing Revolution", 
                      onvalue =1 ,
                      offvalue = 0,
                    )

check6.place(x=480,y=500)
if  not sectab:
  pass
else:
  if sectab[28] == 1:
    check6.select()
  else:
    check6.deselect()

################### tab02 ###################################
sql = "select * from company"
fbcursor.execute(sql)
sectab = fbcursor.fetchone()
print(sectab)


secondtab1=Frame(tab02, relief=GROOVE, bg="#f8f8f2")
secondtab1.pack(side="top", fill=BOTH)

secondtab=Frame(secondtab1, bg="#f5f3f2", height=700)
secondtab.pack(side="top", fill=BOTH)

comdata=LabelFrame(secondtab,text="Company data", height=200, width=500)
comdata.place(x=5, y=15)
cname = Label(secondtab,text="Company name")
cname.place(x=20, y =35)
comname = StringVar()
centry = Entry(secondtab,textvariable=comname)
if  not sectab:
  pass
else:
  centry.insert(0, sectab[1])
centry.place(x=160,y=35,width=280)


cadd = Label(secondtab,text="Company Address")
cadd.place(x=20, y =65)
caddent = scrolledtext.ScrolledText(secondtab)
if  not sectab:
  pass
else:
  caddent.insert('1.0', sectab[2])
caddent.place(x=160,y=65,height=80,width=280)

cemail = Label(secondtab,text="E-mail Address")
cemail.place(x=20, y =160)
comemail = StringVar()
cemailentry = Entry(secondtab,textvariable=comemail)
if  not sectab:
  pass
else:
  cemailentry.insert(0, sectab[3])
cemailentry.place(x=160,y=160,width=280)

stl = Label(secondtab,text="sales Tax.Reg.No.")
stl.place(x=20, y =185)
comsalestax = StringVar()
ste = Entry(secondtab,textvariable=comsalestax)
if  not sectab:
  pass
else:
  ste.insert(0, sectab[4])
ste.place(x=160,y=185,width=280)


curre=LabelFrame(secondtab,text="Currency", height=125, width=500)
curre.place(x=5, y=220)
currl = Label(secondtab,text="Currency")
currl.place(x=20,y= 240)
comcur = StringVar()
currbox = ttk.Combobox(secondtab,width=10,textvariable=comcur)
currbox['values'] =('ALL','AFN','ARS','AWG','AUD','AZN','BSD','BBD','BYN','BZD','BMD','BOB','BAM','BWP',  'BGN','BRL','BND','KHR','CAD','KYD','CLP','CNY','COP','CRC','HRK','CUP','CZK','DKK','DOP','XCD','EGP','SVC',  'EUR','FKP','FJD','GHS','GIP','GTQ','GGP','GYD','HNL','HKD','HUF','ISK','INR','IDR','IRR','IMP','ILS','JMD',  'JPY','JEP','KZT','KPW','KRW','KGS','LAK','LBP','LRD','MKD','MYR','MUR','MXN','MNT','MNT','MZN','NAD','NPR',  'ANG','NZD','NIO','NGN','NOK','OMR','PKR','PAB','PYG','PEN','PHP','PLN','QAR','RON','RUB','SHP','SAR','RSD',  'SCR','SGD','SBD','SOS','KRW','ZAR','LKR','SEK','CHF','SRD','SYP','TWD','THB','TTD','TRY','TVD','UAH','AED',  'GBP','USD','UYU','UZS','VEF','VND','YER','ZWD',)
if  not sectab:
  pass
elif sectab[5]:
  currbox.insert(0, sectab[5])
currbox.place(x=80,y=240)

def signpl(event):
  amsgpl = comcursignpla.get()
  currsign = comcursign.get()
  if amsgpl == "before amount":
    exbox.delete(0, END)
    exbox.insert(0, currsign+'8347.26')
  elif amsgpl == "after amount":
    exbox.delete(0, END)
    exbox.insert(0, '8347.26'+currsign)
  elif amsgpl == "before amount with space":
    exbox.delete(0, END)
    exbox.insert(0, currsign+'  8347.26')
  elif amsgpl == "after amount with space":
    exbox.delete(0, END)
    exbox.insert(0, '8347.26  '+currsign)


currsignl = Label(secondtab,text="Currency sign")
currsignl.place(x=180,y=240)
comcursign = StringVar()
currsignbox = ttk.Combobox(secondtab,width=10,textvariable=comcursign)
currsignbox.bind("<<ComboboxSelected>>", signpl)
currsignbox["values"] = ('Lek','؋','$','ƒ','$','₼','$','$','Br','BZ$','$','$b','KM','P','лв','R$','$','៛',  '$','$','$','¥','$','₡','kn','₱','Kč','kr','RD$','$','£','$','€','£','$','¢','£','Q','£','$','L','$','Ft',  'kr','₹','Rp','﷼','£','₪','J$','¥','£','лв','₩','₩','₭','£','$','ден','RM','₨','$','₮',' د.إ','MT','$','₨',  'ƒ','$','C$','₦','kr','﷼','₨','B/.','Gs','S/.','₱','zł','﷼','lei','₽','£','﷼','Дин.','₨','S','₩','R','₨',  'kr','CHF','£','NT$','฿','TT$','₺','$','₴','د.إ','$U','лв','Bs','₫','﷼','Z$')
if  not sectab:
  pass
elif sectab[6]:
  currsignbox.insert(0, sectab[6])
currsignbox.place(x=265,y=240)

cspl = Label(secondtab,text="Currency sign placement")
cspl.place(x=20,y=270)

def amountsignspace(event):
  amsgpl = comcursignpla.get()
  currsign = comcursign.get()
  if amsgpl == "before amount":
    exbox.delete(0, END)
    exbox.insert(0, currsign+'8347.26')
  elif amsgpl == "after amount":
    exbox.delete(0, END)
    exbox.insert(0, '8347.26'+currsign)
  elif amsgpl == "before amount with space":
    exbox.delete(0, END)
    exbox.insert(0, currsign+'  8347.26')
  elif amsgpl == "after amount with space":
    exbox.delete(0, END)
    exbox.insert(0, '8347.26  '+currsign)
  
    
    
comcursignpla = StringVar()
cspe = ttk.Combobox(secondtab,width=24,textvariable=comcursignpla,)
cspe.bind("<<ComboboxSelected>>", amountsignspace)
cspe["values"] = ("before amount","after amount",'before amount with space',"after amount with space")
if  not sectab:
  pass
elif sectab[7]:
  cspe.insert(0, sectab[7])
cspe.place(x=180,y=270)

def decpl(event):
  dec = comdecsep.get()
  ex = comex.get()
  if dec == ",":
    var = str.replace(ex,".",",")
    exbox.delete(0, END)
    exbox.insert(0, var)
  elif dec == ".":
    var1 = str.replace(ex,",",".")
    exbox.delete(0, END)
    exbox.insert(0, var1)
dsl = Label(secondtab,text="Decimal separator")
dsl.place(x=20,y=300)
comdecsep = StringVar()
currbox = ttk.Combobox(secondtab,width=5,textvariable=comdecsep)
currbox.bind("<<ComboboxSelected>>",decpl)
currbox['values'] = ('.',',')
if  not sectab:
  pass
elif sectab[8]:
  currbox.insert(0, sectab[8])
currbox.place(x=130,y=300)

exl = Label(secondtab,text="Example")
exl.place(x=185,y=300)
comex = StringVar()
exbox = Entry(secondtab,width=15,textvariable=comex)
if  not sectab:
  exbox.insert(0, 84367.26)
elif sectab[9]:
  exbox.insert(0, sectab[9])
exbox.place(x=245,y=300)

btred = Button(secondtab,text="Restore Default")
btred.place(x=400,y=270)
btsc = Button(secondtab,text="SET CURRENCY")
btsc.place(x=400,y=300)

datef=LabelFrame(secondtab,text="Date format", height=60, width=500)
datef.place(x=5, y=355)

def daffun(event):
  dafget = daf.get()
  if dafget == "mm-dd-yyyy":
    exd._set_text(exd._date.strftime('%m-%d-%Y'))
  elif dafget == "dd-mm-yyyy":
    exd._set_text(exd._date.strftime('%d-%m-%Y'))
  elif dafget == "yyy.mm.dd":
    exd._set_text(exd._date.strftime('%Y.%m.%d'))
  elif dafget == "mm/dd/yyyy":
    exd._set_text(exd._date.strftime('%m/%d/%Y'))
  elif dafget == "dd/mm/yyy":
    exd._set_text(exd._date.strftime('%d/%m/%Y'))
  elif dafget == "dd.mm.yyyy":
    exd._set_text(exd._date.strftime('%d.%m.%Y'))
  elif dafget == "yyyy/mm/dd":
    exd._set_text(exd._date.strftime('%Y/%m/%d'))
  

comdaf = StringVar()
daf = ttk.Combobox(secondtab,textvariable=comdaf)
daf["values"] = ("Default",'mm-dd-yyyy','dd-mm-yyyy','yyy.mm.dd','mm/dd/yyyy','dd/mm/yyy','dd.mm.yyyy','yyyy/  mm/dd')
daf.bind("<<ComboboxSelected>>",daffun)
if not sectab:
  pass
elif sectab[10]:
  daf.insert(0, sectab[10])
daf.place(x=60,y=380)


exd = DateEntry(secondtab,)
exd.place(x=280,y=380)
if  not sectab:
  pass
elif sectab[11]:
  exd.delete(0, END)
  exd.insert(0, sectab[11])

tnr=LabelFrame(secondtab,text="Tax name and rate", height=200, width=500)
tnr.place(x=560, y=15)

stt=LabelFrame(secondtab,text="Select tax type", height=120, width=180)
stt.place(x=580, y=30)
def rtax1():
  ch = radtax.get()
  if ch == 1:
    tax1namel.place_forget()
    tax1namee.place_forget()
    tax1ratel.place_forget()
    tax1ratee.place_forget()
    tax1ratee.place_forget()
    ptax1.place_forget()

    tax2namel.place_forget()
    tax2namee.place_forget()
    tax2ratel.place_forget()
    tax2ratee.place_forget()
    ptax2.place_forget()
  elif ch == 2:
    tax1namel.place(x=800, y=40)
    tax1namee.place(x=880,y=40)
    tax1ratel.place(x=800, y=70)
    tax1ratee.place(x=880,y=70)
    ptax1.place(x=580,y=160)
    tax2namel.place_forget()
    tax2namee.place_forget()
    tax2ratel.place_forget()
    tax2ratee.place_forget()
    ptax2.place_forget()
  elif ch == 3:
    tax1namel.place(x=800, y=40)
    tax1namee.place(x=880,y=40)
    tax1ratel.place(x=800, y=70)
    tax1ratee.place(x=880,y=70)
    ptax1.place(x=580,y=160)
    tax2namel.place(x=800, y=110)
    tax2namee.place(x=880,y=110)
    tax2ratel.place(x=800, y=140)
    tax2ratee.place(x=880,y=140)
    ptax2.place(x=580,y=185)
  
radtax = IntVar()
rdnotax = Radiobutton(secondtab,text="Do not use TAX",value="1",variable=radtax,command=rtax1)
rdnotax.place(x=590,y=50)


rdtax1 = Radiobutton(secondtab,text="1 level of Tax",value="2",variable=radtax,command=rtax1)
rdtax1.place(x=590,y=80)
ptax01 = IntVar()
tax1namel = Label(secondtab,text="Tax1 name")


tax1namee = Entry(secondtab)
if  not sectab:
  pass
elif sectab[15]:
  tax1namee.insert(0, sectab[15])
tax1namee.place(x=60,y=380)


tax1ratel = Label(secondtab,text="Tax1 rate")


tax1ratee = Entry(secondtab)
if  not sectab:
  pass
elif sectab[16]:
  tax1ratee.insert(0, sectab[16])

comptax1 = BooleanVar()
ptax1 = Checkbutton(secondtab,text="Print TAX1" ,onvalue =1 ,offvalue = 0,variable=comptax1)
if  not sectab:
  pass
elif sectab[17] == 1:
  ptax1.select()
else:
  ptax1.deselect()

rdtax2 = Radiobutton(secondtab,text="2 level of Tax",value="3",variable=radtax,command=rtax1)
rdtax2.place(x=590,y=110)


tax2namel = Label(secondtab,text="Tax2 name")


tax2namee = Entry(secondtab)
if  not sectab:
  pass
elif sectab[18]:
  tax2namee.insert(0, sectab[18])

tax2ratel = Label(secondtab,text="Tax2 rate")

tax2ratee = Entry(secondtab)
if  not sectab:
  pass
elif sectab[19]:
  tax2ratee.insert(0, sectab[19])

comptax2 = BooleanVar()
ptax2 = Checkbutton(secondtab,text="Print TAX2" ,onvalue =1 ,offvalue = 0,variable=comptax2)
if  not sectab:
  pass
else:
  if sectab[20] == 1:
    ptax2.select()
  else:
    ptax2.deselect()

if  not sectab:
  pass
else:
  if sectab[12] == "1":
    rdnotax.select()
    tax1namel.place_forget()
    tax1namee.place_forget()
    tax1ratel.place_forget()
    tax1ratee.place_forget()
    tax1ratee.place_forget()
    ptax1.place_forget()

    tax2namel.place_forget()
    tax2namee.place_forget()
    tax2ratel.place_forget()
    tax2ratee.place_forget()
    ptax2.place_forget()
  elif sectab[12] == "2":
    tax1namel.place(x=800, y=40)
    tax1namee.place(x=880,y=40)
    tax1ratel.place(x=800, y=70)
    tax1ratee.place(x=880,y=70)
    ptax1.place(x=580,y=160)
    tax2namel.place_forget()
    tax2namee.place_forget()
    tax2ratel.place_forget()
    tax2ratee.place_forget()
    ptax2.place_forget()
    rdtax1.select()
  elif sectab[12] == "3":
    rdtax2.select()
    tax1namel.place(x=800, y=40)
    tax1namee.place(x=880,y=40)
    tax1ratel.place(x=800, y=70)
    tax1ratee.place(x=880,y=70)
    ptax1.place(x=580,y=160)
    tax2namel.place(x=800, y=110)
    tax2namee.place(x=880,y=110)
    tax2ratel.place(x=800, y=140)
    tax2ratee.place(x=880,y=140)
    ptax2.place(x=580,y=185)
  else:
    pass


comlo=LabelFrame(secondtab,text="Comapny Logo", height=260, width=320)
comlo.place(x=560, y=240)

def upload_filelogo():
  global imglogo,filename
  f_types =[('Png files','*.png'),('Jpg Files', '*.jpg')]
  filename = filedialog.askopenfilename(filetypes=f_types)
  shutil.copyfile(filename, os.getcwd()+'/images/'+filename.split('/')[-1])
  image = Image.open(filename)
  resize_image = image.resize((280, 160))
  imglogo = ImageTk.PhotoImage(resize_image)
  # b2 = Button(secondtab,image=img)
  # b2.place(x=130, y=80)

  btlogo = Button(secondtab,width=280,height=160,image=imglogo)
  btlogo.place(x=580,y=280)

try:
  image = Image.open("images/"+sectab[13])
  resize_image = image.resize((280, 160))
  image = ImageTk.PhotoImage(resize_image)
  btlogo = Button(secondtab,width=280,height=160,image=image)
  btlogo.place(x=580,y=280)
  btlogo.photo = image
except:
  pass

  
btloadim = Button(secondtab,text="Load logo image",command=upload_filelogo)
btloadim.place(x=580,y=460)

compimg = BooleanVar()
primage = Checkbutton(secondtab,text="Print logo image",variable = compimg,onvalue =1 ,offvalue = 0)
primage.place(x=740,y=460)

################### tab06 ###################################

def user():
  display = displaystart.get()
  user_name = usernae.get()
  password = userpase.get()
  conformpassword = usercpase.get()
  
  create_inv = creinvbol.get()
  delete_inv = delinvbol.get()
  void_inv = voinvbol.get()
  mark_inv_as_paid = markinvbol.get()
  
  create_ord = creordbol.get()
  delete_ord = delordbol.get()
  turn_inv_ord = turninvbol.get()
  smsnofi = smsinvbol.get()
  
  create_est = creestimatebol.get()
  delete_est = delestimatebol.get()
  turn_est = turnestiinvbol.get()

  create_exp = creexpensebol.get()
  delete_exp = delexpensebol.get()
  rebill_exp = rebillexpebol.get()
  
  create_cus = crecusbol.get()
  delete_cus = delcusbol.get()
  imp_cus = impcusbol.get()

  create_pros = creprosbol.get()
  delete_pros = delprosbol.get()
  import_pros = impprosbol.get()

  runrep = runrepbol.get()
  gen_rec = genrecinvbol.get()

  create_pur = crepurbol.get()
  delete_pur = delpurbol.get()

  modify_inv = modifyinvbol.get()
  modify_ord = modifyordbol.get()
  modify_est = modifyestibol.get()

  if user_name=="" or password=="":
    messagebox.showerror('',"Please complete the form")
  else:
    sql='SELECT * FROM users WHERE username=%s'# selecting entire table from db,taking username , nd check   the existance
    val=(user_name,)
    fbcursor.execute(sql,val)
    if fbcursor.fetchone()is not None:
      sql='SELECT * FROM users WHERE username=%s'
      val=(user_name,)
      fbcursor.execute(sql,val)
      whuser = fbcursor.fetchone()
      print(whuser[0])
      if password == conformpassword:
      # messagebox.showerror('Warming','User name already exist!!')
        sqll= 'UPDATE users SET displayloginscreen=%s,username=%s,password=%s,confirm_password=%s,create_invoice=%s,delete_invoice=%s,void_invoice=%s,mark_invoice_as_paid=%s,create_order=%s,delete_order=%s,turn_order_into_invoice=%s,send_sms_nofitication=%s,create_estimate=%s,delete_estimate=%s,turn_oestimate_into_invoice=%s,create_expense=%s,delete_expense=%s,rebill_exprense=%s,create_customer=%s,delete_customer=%s,import_customer=%s,	create_product_service=%s,delete_product_service=%s,import_product_service=%s,run_reports=%s,generate_recurring_invoice=%s,create_purchase_order=%s,delete_purchase_order=%s,modify_invoice_settings=%s,modify_order_settings=%s,modify_estimate_settings=%s WHERE userID=%s'
        vall=(display,user_name,password,conformpassword,create_inv,delete_inv,void_inv,mark_inv_as_paid,  create_ord,delete_ord,turn_inv_ord,smsnofi,create_est,delete_est,turn_est,create_exp,delete_exp,  rebill_exp,create_cus,delete_cus,imp_cus,create_pros,delete_pros,import_pros,runrep,gen_rec,create_pur,  delete_pur,modify_inv,modify_ord,modify_est,whuser[0])
        fbcursor.execute(sqll,vall)
        fbilldb.commit()
      else:
        messagebox.showerror('Warming','Password not match!!')
    else:
      if password == conformpassword:
        sql="INSERT INTO users(displayloginscreen,username,password,confirm_password,create_invoice,  delete_invoice,void_invoice,mark_invoice_as_paid,create_order,delete_order,turn_order_into_invoice,  send_sms_nofitication,create_estimate,delete_estimate,turn_oestimate_into_invoice,	create_expense,	  delete_expense,rebill_exprense,create_customer,delete_customer,import_customer,	create_product_service,  delete_product_service,	import_product_service,run_reports,generate_recurring_invoice,  create_purchase_order,delete_purchase_order,modify_invoice_settings,modify_order_settings,  modify_estimate_settings) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,  %s,%s,%s,%s,%s,%s,%s,%s)" #adding values into db
        val=(display,user_name,password,conformpassword,create_inv,delete_inv,void_inv,mark_inv_as_paid,  create_ord,delete_ord,turn_inv_ord,smsnofi,create_est,delete_est,turn_est,create_exp,delete_exp,  rebill_exp,create_cus,delete_cus,imp_cus,create_pros,delete_pros,import_pros,runrep,gen_rec,create_pur,  delete_pur,modify_inv,modify_ord,modify_est)
        fbcursor.execute(sql,val)
        fbilldb.commit()
        for record in uactree.get_children():
          uactree.delete(record)
        sql = "select * from users"
        fbcursor.execute(sql)
        sixuactree = fbcursor.fetchall()
        coutset = 0
        for i in sixuactree:
          uactree.insert(parent='', index='end', iid=coutset, text='hello', values=(i[3]))
          coutset += 1
      else:
        messagebox.showerror('Warming','Password not match!!')
      

  
  




  

  
sixtab1=Frame(tab06, relief=GROOVE, bg="#f8f8f2")
sixtab1.pack(side="top", fill=BOTH)

sixtab=Frame(sixtab1, bg="#f5f3f2", height=700)
sixtab.pack(side="top", fill=BOTH)

displaystart = BooleanVar()
displaylocsc = Checkbutton(sixtab,text="Display Login screen startup",onvalue =1 ,offvalue = 0,  variable=displaystart)
displaylocsc.place(x=20,y=30)

userac=LabelFrame(sixtab,text="User Acounts", height=400, width=260)
userac.place(x=20, y=55)


selper = Label(sixtab,text="Select username to modify permissions")
selper.place(x=30,y=75)

def focususer(event):
  itemid = uactree.item(uactree.focus())["values"][0]
  sql = "select * from users where username = %s"
  val = (itemid,)
  fbcursor.execute(sql,val)
  sixtabdataback = fbcursor.fetchone()
  print(sixtabdataback)
  usernae.delete(0,END)
  usernae.insert(0,itemid)
  if itemid == "adminstator":
      usernae.delete(0,END)
      usernae.insert(0,itemid)
      usernae["state"] = DISABLED
      creinv["state"] = DISABLED
      delinv["state"] = DISABLED
      voinv["state"] = DISABLED
      markinv["state"] = DISABLED
      creord["state"] = DISABLED
      delord["state"] = DISABLED
      turninv["state"] = DISABLED
      smsinv["state"] = DISABLED
      creestimate["state"] = DISABLED
      delestimate["state"] = DISABLED
      turnestiinv["state"] = DISABLED
      creexpense["state"] = DISABLED
      delexpense["state"] = DISABLED
      rebillexpe["state"] = DISABLED
      crecus["state"] = DISABLED
      delcus["state"] = DISABLED
      impcus["state"] = DISABLED
      crepros["state"] = DISABLED
      delpros["state"] = DISABLED
      imppros["state"] = DISABLED
      runrep["state"] = DISABLED
      genrecinv["state"] = DISABLED
      crepur["state"] = DISABLED
      delpur["state"] = DISABLED
      modifyinv["state"] = DISABLED
      modifyord["state"] = DISABLED
      modifyesti["state"] = DISABLED
  else:
      userpase.delete(0, END)
      usercpase.delete(0, END)
      usernae.delete(0,END)
      usernae.insert(0,itemid)
      usernae["state"] = NORMAL
      creinv["state"] = NORMAL
      delinv["state"] = NORMAL
      voinv["state"] = NORMAL
      markinv["state"] = NORMAL
      creord["state"] = NORMAL
      delord["state"] = NORMAL
      turninv["state"] = NORMAL
      smsinv["state"] = NORMAL
      creestimate["state"] = NORMAL
      delestimate["state"] = NORMAL
      turnestiinv["state"] = NORMAL
      creexpense["state"] = NORMAL
      delexpense["state"] = NORMAL
      rebillexpe["state"] = NORMAL
      crecus["state"] = NORMAL
      delcus["state"] = NORMAL
      impcus["state"] = NORMAL
      crepros["state"] = NORMAL
      delpros["state"] = NORMAL
      imppros["state"] = NORMAL
      runrep["state"] = NORMAL
      genrecinv["state"] = NORMAL
      crepur["state"] = NORMAL
      delpur["state"] = NORMAL
      modifyinv["state"] = NORMAL
      modifyord["state"] = NORMAL
      modifyesti["state"] = NORMAL
  if not sixtabdataback:
    userpase.delete(0, END)
    usercpase.delete(0, END)
    creinv.deselect()
    delinv.deselect()
    voinv.deselect()
    markinv.deselect()
    creord.deselect()
    delord.deselect()
    turninv.deselect()
    smsinv.deselect()
    creestimate.deselect()
    delestimate.deselect()
    turnestiinv.deselect()
    creexpense.deselect()
    delexpense.deselect()
    rebillexpe.deselect()
    crecus.deselect()
    delcus.deselect()
    impcus.deselect()
    crepros.deselect()
    delpros.deselect()
    imppros.deselect()
    runrep.deselect()
    genrecinv.deselect()
    crepur.deselect()
    delpur.deselect()
    modifyinv.deselect()
    modifyord.deselect()
    modifyesti.deselect()
    if itemid == "adminstator":
      usernae.delete(0,END)
      usernae.insert(0,itemid)
      usernae["state"] = DISABLED
      creinv["state"] = DISABLED
      delinv["state"] = DISABLED
      voinv["state"] = DISABLED
      markinv["state"] = DISABLED
      creord["state"] = DISABLED
      delord["state"] = DISABLED
      turninv["state"] = DISABLED
      smsinv["state"] = DISABLED
      creestimate["state"] = DISABLED
      delestimate["state"] = DISABLED
      turnestiinv["state"] = DISABLED
      creexpense["state"] = DISABLED
      delexpense["state"] = DISABLED
      rebillexpe["state"] = DISABLED
      crecus["state"] = DISABLED
      delcus["state"] = DISABLED
      impcus["state"] = DISABLED
      crepros["state"] = DISABLED
      delpros["state"] = DISABLED
      imppros["state"] = DISABLED
      runrep["state"] = DISABLED
      genrecinv["state"] = DISABLED
      crepur["state"] = DISABLED
      delpur["state"] = DISABLED
      modifyinv["state"] = DISABLED
      modifyord["state"] = DISABLED
      modifyesti["state"] = DISABLED
    else:
      userpase.delete(0, END)
      usercpase.delete(0, END)
      usernae.delete(0,END)
      usernae.insert(0,itemid)
      usernae["state"] = NORMAL
      creinv["state"] = NORMAL
      delinv["state"] = NORMAL
      voinv["state"] = NORMAL
      markinv["state"] = NORMAL
      creord["state"] = NORMAL
      delord["state"] = NORMAL
      turninv["state"] = NORMAL
      smsinv["state"] = NORMAL
      creestimate["state"] = NORMAL
      delestimate["state"] = NORMAL
      turnestiinv["state"] = NORMAL
      creexpense["state"] = NORMAL
      delexpense["state"] = NORMAL
      rebillexpe["state"] = NORMAL
      crecus["state"] = NORMAL
      delcus["state"] = NORMAL
      impcus["state"] = NORMAL
      crepros["state"] = NORMAL
      delpros["state"] = NORMAL
      imppros["state"] = NORMAL
      runrep["state"] = NORMAL
      genrecinv["state"] = NORMAL
      crepur["state"] = NORMAL
      delpur["state"] = NORMAL
      modifyinv["state"] = NORMAL
      modifyord["state"] = NORMAL
      modifyesti["state"] = NORMAL
  else:
    userpase.delete(0, END)
    usercpase.delete(0, END)
    userpase.insert(0, sixtabdataback[4])
    usercpase.insert(0, sixtabdataback[5])
    if sixtabdataback[6] == 1:
      creinv.select()
    else:
      creinv.deselect()
    if sixtabdataback[7] == 1:
      delinv.select()
    else:
      delinv.deselect()
    if sixtabdataback[8] == 1:
      voinv.select()
    else:
      voinv.deselect()
    if sixtabdataback[9] == 1:
      markinv.select()
    else:
      markinv.deselect()
    if sixtabdataback[10] == 1:
      creord.select()
    else:
      creord.deselect()
    if sixtabdataback[11] == 1:
      delord.select()
    else:
      delord.deselect()
    if sixtabdataback[12] == 1:
      turninv.select()
    else:
      turninv.deselect()
    if sixtabdataback[13] == 1:
      smsinv.select()
    else:
      smsinv.deselect()
    if sixtabdataback[14] == 1:
      creestimate.select()
    else:
      creestimate.deselect()
    if sixtabdataback[15] == 1:
      delestimate.select()
    else:
      delestimate.deselect()
    if sixtabdataback[16] == 1:
      turnestiinv.select()
    else:
      turnestiinv.deselect()
    if sixtabdataback[17] == 1:
      creexpense.select()
    else:
      creexpense.deselect()
    if sixtabdataback[18] == 1:
      delexpense.select()
    else:
      delexpense.deselect()
    if sixtabdataback[19] == 1:
      rebillexpe.select()
    else:
      rebillexpe.deselect()
    if sixtabdataback[20] == 1:
      crecus.select()
    else:
      crecus.deselect()
    if sixtabdataback[21] == 1:
      delcus.select()
    else:
      delcus.deselect()
    if sixtabdataback[22] == 1:
      impcus.select()
    else:
      impcus.deselect()
    if sixtabdataback[23] == 1:
      crepros.select()
    else:
      crepros.deselect()
    if sixtabdataback[24] == 1:
      delpros.select()
    else:
      delpros.deselect()
    if sixtabdataback[25] == 1:
      imppros.select()
    else:
      imppros.deselect()
    if sixtabdataback[26] == 1:
      runrep.select()
    else:
      runrep.deselect()
    if sixtabdataback[27] == 1:
      genrecinv.select()
    else:
      genrecinv.deselect()
    if sixtabdataback[28] == 1:
      crepur.select()
    else:
      crepur.deselect()
    if sixtabdataback[29] == 1:
      delpur.select()
    else:
      delpur.deselect()
    if sixtabdataback[30] == 1:
      modifyinv.select()
    else:
      modifyinv.deselect()
    if sixtabdataback[31] == 1:
      modifyord.select()
    else:
      modifyord.deselect()
    if sixtabdataback[32] == 1:
      modifyesti.select()
    else:
      modifyesti.deselect()
        

scrollbarx = Scrollbar(sixtab, orient=HORIZONTAL)
scrollbary = Scrollbar(sixtab, orient=VERTICAL)
uactree = ttk.Treeview(sixtab, columns=("1"),height=400,selectmode="extended", yscrollcommand=scrollbary.  set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=uactree.yview)
scrollbary.place(x=245,y=100,height=300)
uactree.heading('1', text="Username",)
uactree.column('#0', stretch=NO, minwidth=0, width=0)
uactree.column('1', stretch=NO, minwidth=0, width=218)
uactree.place(x=30,y=100,height=300,width=220)
uactree.bind('<Double-Button-1>' , focususer)
sql = "select * from users"
fbcursor.execute(sql)
sixuactree = fbcursor.fetchall()
coutset = 0
if not sixuactree:
  uactree.insert('', index='end', text='hello', values=("adminstator"))
else:
  for i in sixuactree:
    uactree.insert(parent='', index='end', iid=coutset, text='hello', values=(i[3]))
    coutset += 1

def adduser():
  uactree.insert('', index='end', text='hello', values=("Rename User"))

btadd = Button(sixtab,text="Add new User",command=adduser)
btadd.place(x=30,y=415)

def users():
  itemid = uactree.item(uactree.focus())["values"][0]
  if itemid == "adminstator":
    messagebox.showerror('F-Billing Revolution', 'Cannot delete adminstator user.')
  else:
    delusermess = messagebox.askyesno("Delete user", "Are you sure to delete this user?")
    if delusermess == True:
      sql = "delete from users where username = %s"
      val = (itemid, )
      fbcursor.execute(sql, val)
      fbilldb.commit()
      for record in uactree.get_children():
        uactree.delete(record)
      sql = "select * from users"
      fbcursor.execute(sql)
      sixuactree = fbcursor.fetchall()
      coutset = 0
      for i in sixuactree:
        uactree.insert(parent='', index='end', iid=coutset, text='hello', values=(i[3]))
        coutset += 1
    else:
      pass
      

btdus = Button(sixtab,text="Delete User",command=users)
btdus.place(x=180,y=415)

userpro=LabelFrame(sixtab,text="User Profile", height=400, width=750)
userpro.place(x=300, y=55)


userna = Label(sixtab,text="Username")
userna.place(x=340,y=90)
usernae = Entry(sixtab,)
usernae.place(x=460,y=90)

userpas = Label(sixtab,text="Password")
userpas.place(x=340,y=120)
userpase = Entry(sixtab,)
userpase.place(x=460,y=120)

usercpas = Label(sixtab,text="Confirm Password")
usercpas.place(x=340,y=150)
usercpase = Entry(sixtab,)
usercpase.place(x=460,y=150)

saveuserprofile = Button(sixtab,text="save user profile",command=user)
saveuserprofile.place(x=650,y=120)

creinvbol = BooleanVar()
creinv = Checkbutton(sixtab,text="Create invoice",onvalue= 1 ,offvalue= 0,variable=creinvbol)
creinv.place(x=340,y=200)
delinvbol = BooleanVar()
delinv = Checkbutton(sixtab,text="Delete invoice",onvalue= 1 ,offvalue= 0,variable=delinvbol)
delinv.place(x=340,y=225)
voinvbol = BooleanVar()
voinv = Checkbutton(sixtab,text="Void invoice",onvalue= 1 ,offvalue= 0,variable=voinvbol)
voinv.place(x=340,y=250)
markinvbol = BooleanVar()
markinv = Checkbutton(sixtab,text="Mark invoice as Paid",onvalue= 1 ,offvalue= 0,variable=markinvbol)
markinv.place(x=340,y=275)

creordbol = BooleanVar()
creord = Checkbutton(sixtab,text="Create Order",onvalue= 1 ,offvalue= 0,variable=creordbol)
creord.place(x=500,y=200)
delordbol = BooleanVar()
delord = Checkbutton(sixtab,text="Delete Order",onvalue= 1 ,offvalue= 0,variable=delordbol)
delord.place(x=500,y=225)
turninvbol = BooleanVar()
turninv = Checkbutton(sixtab,text="Turn order into invoice",onvalue= 1 ,offvalue= 0,variable=turninvbol)
turninv.place(x=500,y=250)
smsinvbol = BooleanVar()
smsinv = Checkbutton(sixtab,text="Send sms nofitication",onvalue= 1 ,offvalue= 0,variable=smsinvbol)
smsinv.place(x=500,y=275)

creestimatebol = BooleanVar()
creestimate = Checkbutton(sixtab,text="Create estimate",onvalue= 1 ,offvalue= 0,variable=creestimatebol)
creestimate.place(x=680,y=200)
delestimatebol = BooleanVar()
delestimate = Checkbutton(sixtab,text="Delete estimate",onvalue= 1 ,offvalue= 0,variable=delestimatebol)
delestimate.place(x=680,y=225)
turnestiinvbol = BooleanVar()
turnestiinv = Checkbutton(sixtab,text="Turn estimates into invoice",onvalue= 1 ,offvalue= 0,  variable=turnestiinvbol)
turnestiinv.place(x=680,y=250)

creexpensebol = BooleanVar()
creexpense = Checkbutton(sixtab,text="Create expenses",onvalue= 1 ,offvalue= 0,variable=creexpensebol)
creexpense.place(x=880,y=200)
delexpensebol = BooleanVar()
delexpense = Checkbutton(sixtab,text="Delete expenses",onvalue= 1 ,offvalue= 0,variable=delexpensebol)
delexpense.place(x=880,y=225)
rebillexpebol = BooleanVar()
rebillexpe = Checkbutton(sixtab,text="Rebill expenses",onvalue= 1 ,offvalue= 0,variable=rebillexpebol)
rebillexpe.place(x=880,y=250)

crecusbol = BooleanVar()
crecus = Checkbutton(sixtab,text="Create customer",onvalue= 1 ,offvalue= 0,variable=crecusbol)
crecus.place(x=340,y=320)
delcusbol = BooleanVar()
delcus = Checkbutton(sixtab,text="Delete customer",onvalue= 1 ,offvalue= 0,variable=delcusbol)
delcus.place(x=340,y=340)
impcusbol = BooleanVar()
impcus = Checkbutton(sixtab,text="Import customer",onvalue= 1 ,offvalue= 0,variable=impcusbol)
impcus.place(x=340,y=360)

creprosbol = BooleanVar()
crepros = Checkbutton(sixtab,text="Create product\services",onvalue= 1 ,offvalue= 0,variable=creprosbol)
crepros.place(x=500,y=320)
delprosbol = BooleanVar()
delpros = Checkbutton(sixtab,text="Delete product\services",onvalue= 1 ,offvalue= 0,variable=delprosbol)
delpros.place(x=500,y=340)
impprosbol = BooleanVar()
imppros = Checkbutton(sixtab,text="Import product\services",onvalue= 1 ,offvalue= 0,variable=impprosbol)
imppros.place(x=500,y=360)

runrepbol = BooleanVar()
runrep = Checkbutton(sixtab,text="Run reports",onvalue= 1 ,offvalue= 0,variable=runrepbol)
runrep.place(x=680,y=320)
genrecinvbol = BooleanVar()
genrecinv = Checkbutton(sixtab,text="Generate recurring invoices",onvalue= 1 ,offvalue= 0,  variable=genrecinvbol)
genrecinv.place(x=680,y=340)

crepurbol = BooleanVar()
crepur = Checkbutton(sixtab,text="Create Purchase order",onvalue =1 ,offvalue = 0,variable=crepurbol)
crepur.place(x=880,y=320)
delpurbol = BooleanVar()
delpur = Checkbutton(sixtab,text="Delete Purchase order",onvalue =1 ,offvalue = 0,variable=delpurbol)
delpur.place(x=880,y=340)

undersetlab = Label(sixtab,text="Under Settings menu tab")
undersetlab.place(x=340,y=400)

modifyinvbol = BooleanVar()
modifyinv = Checkbutton(sixtab,text="Modify invoice settings",onvalue =1 ,offvalue = 0,variable=modifyinvbol)
modifyinv.place(x=340,y=425)

modifyordbol = BooleanVar()
modifyord = Checkbutton(sixtab,text="Modify order settings",onvalue =1 ,offvalue = 0,variable=modifyordbol)
modifyord.place(x=500,y=425)

modifyestibol = BooleanVar()
modifyesti = Checkbutton(sixtab,text="Modify estimate settings",onvalue =1 ,offvalue = 0,  variable=modifyestibol)
modifyesti.place(x=680,y=425)

################### tab05 ###################################
fifthtab1=Frame(tab05, relief=GROOVE, bg="#f8f8f2")
fifthtab1.pack(side="top", fill=BOTH)

fifthtab=Frame(fifthtab1, bg="#f5f3f2", height=700)
fifthtab.pack(side="top", fill=BOTH)

sql = "select * from company"
fbcursor.execute(sql)
estdata = fbcursor.fetchone()
print(estdata)



ver = Label(fifthtab,text="Estimate# prefix")
ver.place(x=5,y=40)

est_str = StringVar() 
est_entry = Entry(fifthtab, textvariable=est_str)
est_entry.place(x=100,y=40)
if not estdata:
  est_str.set('EST')
else:
  est_entry.insert(0, estdata[29])

ver = Label(fifthtab,text="Starting estimate number")
ver.place(x=25,y=80)

def callback(input):
    
  if input.isdigit():
      print(input)
      return True
                        
  elif input is "":
      print(input)
      return True

  else:
      print(input)
      return False

spin1 = Spinbox(fifthtab,from_=0,to=1000000,width=15)
reg = fifthtab.register(callback)

spin1.config(validate ="key", 
        validatecommand =(reg, '%S'))
if not estdata:
  pass
else:
  spin1.delete(0, END)
  spin1.insert(0,estdata[38])
spin1.place(x=50,y=100)

ver = Label(fifthtab,text="Header box background color")
ver.place(x=5,y=140)

win_menu1 = StringVar()
winstyle1 = ttk.Combobox(fifthtab,textvariable=win_menu1)
#est_win1 = win_menu1.get()
winstyle1['values'] = ('Default','Black','Maroon','Green','Olive','Navy','Purple','Teal','Gray','Silver','Red','Lime','Yellow','Blue','Fuchsia','Aqua','White','ScrollBar','Background','ActiveCaption','InactiveCaption','Menu','Window','WindowFrame','MenuText','WindowText','CaptionText','ActiveBorder','InactiveBorder','AppWorkSpace','Highlight','HighlightText','BtnFace','InactiveCaptionText','BtnHighlight','3DDkShadow','3DLight','InfoText','InfoBk','Custom')
if not estdata:
  winstyle1.current(0)
else:
  winstyle1.insert(0, estdata[30])
winstyle1.place(x=6 ,y=160)
#winstyle1.current(0)

ver = Label(fifthtab,text="Customize Estimate text labels")
ver.place(x=5,y=190)

est_str1 = StringVar() 
est_lbx1 = Entry(fifthtab, width=30,textvariable=est_str1)
# est_str1.set('Estimate')
if not estdata:
  est_str1.set('Estimate')
else:
  est_lbx1.insert(0, estdata[31])
est_lbx1.place(x=5,y=220)

est_str2 = StringVar() 
est_lbx2 = Entry(fifthtab, width=30,textvariable=est_str2)
if not estdata:
  est_str2.set('Estimate#')
else:
  est_lbx2.insert(0,estdata[33])
est_lbx2.place(x=5,y=240)


est_str3 = StringVar() 
est_lbx3 = Entry(fifthtab,width=30,textvariable=est_str3)
if not estdata:
  est_str3.set('Estimate date')
else:
  est_lbx3.insert(0, estdata[34])
est_lbx3.place(x=5,y=260) 

est_str4 = StringVar() 
est_lbx4 = Entry(fifthtab,width=30,textvariable=est_str4)
if not estdata:
  est_str4.set('Due date')
else:
  est_lbx4.insert(0, estdata[35])
est_lbx4.place(x=5,y=280)

est_str5 = StringVar() 
est_lbx5 = Entry(fifthtab,width=30,textvariable=est_str5)
if not estdata:
  est_str5.set('Estimate to')
else:
  est_lbx5.insert(0, estdata[36])
est_lbx5.place(x=5,y=300)

est_str6 = StringVar() 
est_lbx6 = Entry(fifthtab, width=30,textvariable=est_str6)
if not estdata:
  est_str6.set('Estimate total')
else:
  est_lbx6.insert(0, estdata[37])
est_lbx6.place(x=5,y=320)


ver = Label(fifthtab,text="Default Estimate template(example,click on preview for mouse scrolling)")
ver.place(x=248,y=55 )

ver = Label(fifthtab,text="Default Estimate template")
ver.place(x=619,y=40)



messagelbframe=LabelFrame(fifthtab,text="Predefined terms and conditions text for estimates", height=70, width=980)
messagelbframe.place(x=248, y=396)


# est_str7 = StringVar() 
# entry1=Entry(fifthtab, width=155,textvariable=est_str7)
# if not estdata:
#   pass
# else:
#   entry1.insert(0, estdata[39])
# entry1.place(x=260, y=415, height=36)

est_str7 = scrolledtext.ScrolledText(fifthtab)
if  not estdata:
  pass
else:
  est_str7.insert('1.0', estdata[39])
est_str7.place(x=260,y=415,height=38,width=950)


def restore_defaulttt1():
      est_lbx1.delete(0, 'end')
      est_lbx1.insert(0, 'Estimate')
      est_lbx2.delete(0, 'end')
      est_lbx2.insert(0,'Estimate#')
      est_lbx3.delete(0, 'end')
      est_lbx3.insert(0, 'Estimate date')
      est_lbx4.delete(0, 'end')
      est_lbx4.insert(0, 'Due date')
      est_lbx5.delete(0, 'end')
      est_lbx5.insert(0, 'Estimate to')
      est_lbx6.delete(0, 'end')
      est_lbx6.insert(0, 'Estimate total')

bttermadd_01 = Button(fifthtab,text="Restore defaults", command=restore_defaulttt1)
bttermadd_01.place(x=32,y=430)


#------------Professional 1 (logo on left side)-------------
def maindropmenu(event):
    menuvar=win_menu2.get()
    print(menuvar,"hello")
    sql = "select * from company"
    fbcursor.execute(sql)
    estdata1 = fbcursor.fetchone()

    if menuvar == 'Professional 1 (logo on left side)':
      frame = Frame(fifthtab, width=953, height=300)
      frame.pack(expand=True, fill=BOTH)
      frame.place(x=247,y=90)
      canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
            
      vertibar=Scrollbar(frame, orient=VERTICAL)
      vertibar.pack(side=RIGHT,fill=Y)
      vertibar.config(command=canvas.yview)
        
      canvas.config(width=953,height=300)
      canvas.config(yscrollcommand=vertibar.set)
      canvas.pack(expand=True,side=LEFT,fill=BOTH)
      canvas.create_rectangle(100, 8, 850, 687 , outline='yellow',fill='white')
      canvas.create_text(500, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
      try:
        est_image = Image.open("images/"+estdata1[13])
        est_resize_image = est_image.resize((200,100))
        est_image = ImageTk.PhotoImage(est_resize_image)

        est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
        window_image = canvas.create_window(175, 45, anchor="nw", window=est_btlogo)
        est_btlogo.photo = est_image
      except:
        pass  
      canvas.create_text(202, 160, text=""+est_str2.get(), fill="black", font=('Helvetica 11'))
      canvas.create_text(215, 180, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
      canvas.create_text(200, 200, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))
      canvas.create_text(191, 220, text="Terms", fill="black", font=('Helvetica 11'))
      canvas.create_text(205, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
      canvas.create_text(350, 160, text="EST1/2022", fill="black", font=('Helvetica 11'))
      canvas.create_text(350, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
      canvas.create_text(350, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
      canvas.create_text(340, 220, text="NET 15", fill="black", font=('Helvetica 11'))
        
      canvas.create_text(720, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
      # canvas.create_text(700, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'), width=125)
      T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
      T_address.tag_configure('tag_name',justify='right')
      T_address.insert('1.0', estdata1[2])
      T_address.tag_add('tag_name','1.0', 'end')
      T_address_window = canvas.create_window(520, 80, anchor="nw", window=T_address)
      canvas.create_text(695, 180, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
      canvas.create_text(700, 205, text=" "+est_str1.get(), fill="black", font=('Helvetica 14 bold'))
      canvas.create_text(706, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
        
      canvas.create_text(210, 260, text=""+est_str5.get(), fill="black", font=('Helvetica 10 underline'))
      canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
      canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
      canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
      canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
      canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
      canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
      canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
      canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
      canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))
    
      s = ttk.Style()
      s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

      tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_1.Treeview')

      tree.column("# 1", anchor=E, stretch=NO, width=100)
      tree.heading("# 1", text="ID/SKU")
      tree.column("# 2", anchor=E, stretch=NO, width=350)
      tree.heading("# 2", text="Product/Service - Description")
      tree.column("# 3", anchor=E, stretch=NO, width=80)
      tree.heading("# 3", text="Quantity")
      tree.column("# 4", anchor=E, stretch=NO, width=90)
      tree.heading("# 4", text="Unit Price")
      tree.column("# 5", anchor=E, stretch=NO, width=80)
      tree.heading("# 5", text="Price")
        
      window = canvas.create_window(120, 340, anchor="nw", window=tree)

      canvas.create_line(120, 390, 820, 390 )
      canvas.create_line(120, 340, 120, 365 )
      canvas.create_line(120, 365, 120, 390 )
      canvas.create_line(820, 340, 820, 540 )
      canvas.create_line(740, 340, 740, 540 )
      canvas.create_line(570, 340, 570, 540 )
      canvas.create_line(570, 415, 820, 415 )
      canvas.create_line(570, 440, 820, 440 )
      canvas.create_line(570, 465, 820, 465 )
      canvas.create_line(570, 490, 820, 490 )
      canvas.create_line(570, 515, 820, 515 )
      canvas.create_line(650, 340, 650, 390 )
      canvas.create_line(220, 340, 220, 390 )
      canvas.create_line(570, 540, 820, 540 )

      canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
      canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
      canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))
  
      if comcursignpla.get() == "before amount":
        canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

      elif comcursignpla.get() == "after amount":
        canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

      elif comcursignpla.get() == "before amount with space":
        canvas.create_text(704, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

      elif comcursignpla.get() == "after amount with space":
        canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))

      else:
        pass
      # canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      if comcursignpla.get() == "before amount":
        canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

      elif comcursignpla.get() == "after amount":
        canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

      elif comcursignpla.get() == "before amount with space":
        canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

      elif comcursignpla.get() == "after amount with space":
        canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      else:
        pass
      # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

      canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
      if comcursignpla.get() == "before amount":
        canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount":
        canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

      elif comcursignpla.get() == "before amount with space":
        canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount with space":
        canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      else:
        pass
      # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

      canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

      if comcursignpla.get() == "before amount":
        canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount":
        canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "before amount with space":
        canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount with space":
        canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      else:
        pass
      # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

      canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
      
      if comcursignpla.get() == "before amount":
        canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount":
        canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "before amount with space":
        canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount with space":
        canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      else:
        pass

      # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

      if comcursignpla.get() == "before amount":
        canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
      elif comcursignpla.get() == "after amount":
        canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
      elif comcursignpla.get() == "before amount with space":
        canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
      elif comcursignpla.get() == "after amount with space":
        canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
      else:
        pass

      # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
      canvas.create_text(650, 479, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))
      if comcursignpla.get() == "before amount":
        canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount":
        canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "before amount with space":
        canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount with space":
        canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      else:
        pass

      # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))
      
      if comcursignpla.get() == "before amount":
        canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount":
        canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "before amount with space":
        canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount with space":
        canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      else:
        pass
      # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

      canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
      canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
      canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
      canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
        
      canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
      canvas.create_line(150, 608, 795, 608)
      # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10')) 
      T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
      T.insert(END, estdata1[39])
      T_window = canvas.create_window(155, 612, anchor="nw", window=T)

      canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
      canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
        

#----------------Professional 2 (logo on right side)------------------
    elif menuvar == 'Professional 2 (logo on right side)':
      frame = Frame(fifthtab, width=953, height=300)
      frame.pack(expand=True, fill=BOTH)
      frame.place(x=247,y=90)
    
      canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
        
      vertibar=Scrollbar(frame, orient=VERTICAL)
      vertibar.pack(side=RIGHT,fill=Y)
      vertibar.config(command=canvas.yview)
      canvas.config(width=953,height=300)
        
      canvas.config(yscrollcommand=vertibar.set)
      canvas.pack(expand=True,side=LEFT,fill=BOTH)
      canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
      canvas.create_text(500, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
      try:
        est_image = Image.open("images/"+estdata1[13])
        est_resize_image = est_image.resize((200,100))
        est_image = ImageTk.PhotoImage(est_resize_image)

        est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
        window_image = canvas.create_window(500, 45, anchor="nw", window=est_btlogo)
        est_btlogo.photo = est_image
      except:
        pass  
      canvas.create_text(250, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
      # canvas.create_text(215, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
      T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
      T_address.tag_configure('tag_name',justify='right')
      T_address.insert('1.0', estdata1[2])
      T_address.tag_add('tag_name','1.0', 'end')
      T_address_window = canvas.create_window(100, 80, anchor="nw", window=T_address)
      #T_address_window = canvas.create_window(175, 80, anchor="nw", window=T_address)

      canvas.create_text(215, 180, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
      canvas.create_text(225, 205, text=""+est_str1.get(), fill="black", font=('Helvetica 14 bold'))
      canvas.create_text(232, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
        
      canvas.create_text(502, 160, text=""+est_str2.get(), fill="black", font=('Helvetica 11'))
      canvas.create_text(515, 180, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
      canvas.create_text(500, 200, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))
      canvas.create_text(491, 220, text="Terms", fill="black", font=('Helvetica 11'))
      canvas.create_text(505, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
      canvas.create_text(690, 160, text="EST1/2022", fill="black", font=('Helvetica 11'))
      canvas.create_text(690, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
      canvas.create_text(690, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
      canvas.create_text(680, 220, text="NET 15", fill="black", font=('Helvetica 11'))      
        
      canvas.create_text(210, 260, text=""+est_str5.get(), fill="black", font=('Helvetica 10 underline'))
      canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
      canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
      canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
      canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
      canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
      canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
      canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
      canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
      canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

      s = ttk.Style()
      s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

      tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_1.Treeview')
        
      tree.column("# 1", anchor=E, stretch=NO, width=100)
      tree.heading("# 1", text="ID/SKU")
      tree.column("# 2", anchor=E, stretch=NO, width=350)
      tree.heading("# 2", text="Product/Service - Description")
      tree.column("# 3", anchor=E, stretch=NO, width=80)
      tree.heading("# 3", text="Quantity")
      tree.column("# 4", anchor=E, stretch=NO, width=90)
      tree.heading("# 4", text="Unit Price")
      tree.column("# 5", anchor=E, stretch=NO, width=80)
      tree.heading("# 5", text="Price")
        
      window = canvas.create_window(120, 340, anchor="nw", window=tree)

      canvas.create_line(120, 390, 820, 390 )
      canvas.create_line(120, 340, 120, 365 )
      canvas.create_line(120, 365, 120, 390 )
      canvas.create_line(820, 340, 820, 540 )
      canvas.create_line(740, 340, 740, 540 )
      canvas.create_line(570, 340, 570, 540 )
      canvas.create_line(570, 415, 820, 415 )
      canvas.create_line(570, 440, 820, 440 )
      canvas.create_line(570, 465, 820, 465 )
      canvas.create_line(570, 490, 820, 490 )
      canvas.create_line(570, 515, 820, 515 )
      canvas.create_line(650, 340, 650, 390 )
      canvas.create_line(220, 340, 220, 390 )
      canvas.create_line(570, 540, 820, 540 )

      canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
      canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
      canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))

      if comcursignpla.get() == "before amount":
        canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount":
        canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "before amount with space":
        canvas.create_text(704, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount with space":
        canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      else:
        pass

      # canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

      if comcursignpla.get() == "before amount":
        canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount":
        canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "before amount with space":
        canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount with space":
        canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      else:
        pass

      # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

      canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))

      if comcursignpla.get() == "before amount":
        canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount":
        canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "before amount with space":
        canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount with space":
        canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      else:
        pass

      # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

      canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

      if comcursignpla.get() == "before amount":
        canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount":
        canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "before amount with space":
        canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount with space":
        canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      else:
        pass

      # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

      canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))

      if comcursignpla.get() == "before amount":
        canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount":
        canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "before amount with space":
        canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount with space":
        canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      else:
        pass

      # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

      if comcursignpla.get() == "before amount":
        canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
      elif comcursignpla.get() == "after amount":
        canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
      elif comcursignpla.get() == "before amount with space":
        canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
      elif comcursignpla.get() == "after amount with space":
        canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
      else:
        pass

      # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
      canvas.create_text(650, 479, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))

      if comcursignpla.get() == "before amount":
        canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount":
        canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "before amount with space":
        canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount with space":
        canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      else:
        pass

      # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))
      
      if comcursignpla.get() == "before amount":
        canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount":
        canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "before amount with space":
        canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount with space":
        canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      else:
        pass

      # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

      canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
      canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
      canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
      canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))

      canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
      canvas.create_line(150, 608, 795, 608)
      # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10'))
      T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
      T.insert(END, estdata1[39])
      T_window = canvas.create_window(155, 612, anchor="nw", window=T)
      canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
      canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
#----------------Simplified 1 (logo on left side)------------------ 
    elif menuvar == 'Simplified 1 (logo on left side)':
      print('hello')
      frame = Frame(fifthtab, width=953, height=300)
      frame.pack(expand=True, fill=BOTH)
      frame.place(x=247,y=90)
      canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))

      vertibar=Scrollbar(frame, orient=VERTICAL)
      vertibar.pack(side=RIGHT,fill=Y)
      vertibar.config(command=canvas.yview)
      canvas.config(width=953,height=300)

      canvas.config(yscrollcommand=vertibar.set)
      canvas.pack(expand=True,side=LEFT,fill=BOTH)
      canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
      canvas.create_text(500, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
      try:
        est_image = Image.open("images/"+estdata1[13])
        est_resize_image = est_image.resize((200,100))
        est_image = ImageTk.PhotoImage(est_resize_image)

        est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
        window_image = canvas.create_window(175, 45, anchor="nw", window=est_btlogo)
        est_btlogo.photo = est_image
      except:
        pass  
      canvas.create_text(202, 160, text=""+est_str2.get(), fill="black", font=('Helvetica 11'))
      canvas.create_text(215, 180, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
      canvas.create_text(200, 200, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))
      canvas.create_text(191, 220, text="Terms", fill="black", font=('Helvetica 11'))
      canvas.create_text(205, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
      canvas.create_text(350, 160, text="EST1/2022", fill="black", font=('Helvetica 11'))
      canvas.create_text(350, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
      canvas.create_text(350, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
      canvas.create_text(340, 220, text="NET 15", fill="black", font=('Helvetica 11'))      

      canvas.create_text(720, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
      #canvas.create_text(710, 200, text=caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
      T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
      T_address.tag_configure('tag_name',justify='right')
      T_address.insert('1.0', estdata1[2])
      T_address.tag_add('tag_name','1.0', 'end')
      T_address_window = canvas.create_window(520, 80, anchor="nw", window=T_address)

      canvas.create_text(708, 180, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
      canvas.create_text(710, 205, text=""+est_str1.get(), fill="black", font=('Helvetica 14 bold'))
        
      canvas.create_text(210, 260, text=""+est_str5.get(), fill="black", font=('Helvetica 10 underline'))
      canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
      canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
      canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
      canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
      canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
      canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
      canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
      canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
      canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

      s = ttk.Style()
      s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

      tree=ttk.Treeview(canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle_1.Treeview')
        
      tree.column("# 1", anchor=E, stretch=NO, width=530)
      tree.heading("# 1", text="Product/Service - Description")
      tree.column("# 2", anchor=E, stretch=NO, width=90)
      tree.heading("# 2", text="Quantity")
      tree.column("# 3", anchor=E, stretch=NO, width=80)
      tree.heading("# 3", text="Price")
        
      window = canvas.create_window(120, 340, anchor="nw", window=tree)

      canvas.create_line(120, 390, 820, 390 )
      canvas.create_line(120, 340, 120, 365 )
      canvas.create_line(120, 365, 120, 390 )
      canvas.create_line(820, 340, 820, 540 )
      canvas.create_line(740, 340, 740, 540 )
      canvas.create_line(570, 390, 570, 540 )
      canvas.create_line(570, 415, 820, 415 )
      canvas.create_line(570, 440, 820, 440 )
      canvas.create_line(570, 465, 820, 465 )
      canvas.create_line(570, 490, 820, 490 )
      canvas.create_line(570, 515, 820, 515 )
      canvas.create_line(650, 340, 650, 390 )
      canvas.create_line(570, 540, 820, 540 )

    
      canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
      canvas.create_text(710, 372, text="1", fill="black", font=('Helvetica 10'))

      if comcursignpla.get() == "before amount":
        canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount":
        canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "before amount with space":
        canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount with space":
        canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      else:
        pass

      # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

      canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))

      if comcursignpla.get() == "before amount":
        canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount":
        canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "before amount with space":
        canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount with space":
        canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      else:
        pass

      # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

      canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

      if comcursignpla.get() == "before amount":
        canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount":
        canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "before amount with space":
        canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount with space":
        canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      else:
        pass

      # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

      canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))

      if comcursignpla.get() == "before amount":
        canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount":
        canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "before amount with space":
        canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount with space":
        canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      else:
        pass

      # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

      if comcursignpla.get() == "before amount":
        canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount":
        canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "before amount with space":
        canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount with space":
        canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      else:
        pass

      # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
      canvas.create_text(650, 479, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))

      if comcursignpla.get() == "before amount":
        canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount":
        canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "before amount with space":
        canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount with space":
        canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      else:
        pass

      # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))

      if comcursignpla.get() == "before amount":
        canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount":
        canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "before amount with space":
        canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount with space":
        canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      else:
        pass

      # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

      canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
      canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
      canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
      canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))

      canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
      canvas.create_line(150, 608, 795, 608)
      # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10'))
      T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
      T.insert(END, estdata1[39])
      T_window = canvas.create_window(155, 612, anchor="nw", window=T)
      canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
      canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))

#----------------Simplified 2 (logo on right side)------------------ 
    elif menuvar == 'Simplified 2 (logo on right side)':
      frame = Frame(fifthtab, width=953, height=300)
      frame.pack(expand=True, fill=BOTH)
      frame.place(x=247,y=90)

      canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))

      vertibar=Scrollbar(frame, orient=VERTICAL)
      vertibar.pack(side=RIGHT,fill=Y)
      vertibar.config(command=canvas.yview)
      canvas.config(width=953,height=300)

      canvas.config(yscrollcommand=vertibar.set)
      canvas.pack(expand=True,side=LEFT,fill=BOTH)
      canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
      canvas.create_text(500, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
      try:
        est_image = Image.open("images/"+estdata1[13])
        est_resize_image = est_image.resize((200,100))
        est_image = ImageTk.PhotoImage(est_resize_image)

        est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
        window_image = canvas.create_window(500, 45, anchor="nw", window=est_btlogo)
        est_btlogo.photo = est_image
      except:
        pass  
      canvas.create_text(250, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
      # canvas.create_text(224, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
      T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
      T_address.tag_configure('tag_name',justify='right')
      T_address.insert('1.0', estdata1[2])
      T_address.tag_add('tag_name','1.0', 'end')
      T_address_window = canvas.create_window(100, 80, anchor="nw", window=T_address)

      canvas.create_text(224, 180, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
      canvas.create_text(225, 205, text=""+est_str1.get(), fill="black", font=('Helvetica 14 bold'))

      canvas.create_text(502, 160, text=""+est_str2.get(), fill="black", font=('Helvetica 11'))
      canvas.create_text(515, 180, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
      canvas.create_text(500, 200, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))
      canvas.create_text(491, 220, text="Terms", fill="black", font=('Helvetica 11'))
      canvas.create_text(505, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
      canvas.create_text(680, 160, text="EST1/2022", fill="black", font=('Helvetica 11'))
      canvas.create_text(680, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
      canvas.create_text(680, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
      canvas.create_text(670, 220, text="NET 15", fill="black", font=('Helvetica 11'))      

      canvas.create_text(210, 260, text=""+est_str5.get(), fill="black", font=('Helvetica 10 underline'))
      canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
      canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
      canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
      canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
      canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
      canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
      canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
      canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
      canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

      s = ttk.Style()
      s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

      tree=ttk.Treeview(canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle_1.Treeview')
        
      tree.column("# 1", anchor=E, stretch=NO, width=530)
      tree.heading("# 1", text="Product/Service - Description")
      tree.column("# 2", anchor=E, stretch=NO, width=90)
      tree.heading("# 2", text="Quantity")
      tree.column("# 3", anchor=E, stretch=NO, width=80)
      tree.heading("# 3", text="Price")
        
      window = canvas.create_window(120, 340, anchor="nw", window=tree)

      canvas.create_line(120, 390, 820, 390 )
      canvas.create_line(120, 340, 120, 365 )
      canvas.create_line(120, 365, 120, 390 )
      canvas.create_line(820, 340, 820, 540 )
      canvas.create_line(740, 340, 740, 540 )
      canvas.create_line(570, 390, 570, 540 )
      canvas.create_line(570, 415, 820, 415 )
      canvas.create_line(570, 440, 820, 440 )
      canvas.create_line(570, 465, 820, 465 )
      canvas.create_line(570, 490, 820, 490 )
      canvas.create_line(570, 515, 820, 515 )
      canvas.create_line(650, 340, 650, 390 )
      canvas.create_line(570, 540, 820, 540 )

        
      canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
      canvas.create_text(710, 372, text="1", fill="black", font=('Helvetica 10'))

      if comcursignpla.get() == "before amount":
        canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount":
        canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "before amount with space":
        canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount with space":
        canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      else:
        pass

      # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

      canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))

      if comcursignpla.get() == "before amount":
        canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount":
        canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "before amount with space":
        canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount with space":
        canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      else:
        pass

      # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

      canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

      if comcursignpla.get() == "before amount":
        canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount":
        canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "before amount with space":
        canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount with space":
        canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      else:
        pass

      # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

      canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))

      if comcursignpla.get() == "before amount":
        canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount":
        canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "before amount with space":
        canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount with space":
        canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      else:
        pass

      # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

      if comcursignpla.get() == "before amount":
        canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount":
        canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "before amount with space":
        canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount with space":
        canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      else:
        pass

      # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
      canvas.create_text(650, 479, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))

      if comcursignpla.get() == "before amount":
        canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount":
        canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "before amount with space":
        canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount with space":
        canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      else:
        pass

      # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))

      if comcursignpla.get() == "before amount":
        canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount":
        canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "before amount with space":
        canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount with space":
        canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      else:
        pass

      # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

      canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
      canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
      canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
      canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))

      canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
      canvas.create_line(150, 608, 795, 608)
      # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10'))
      T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
      T.insert(END, estdata1[39])
      T_window = canvas.create_window(155, 612, anchor="nw", window=T)
      canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
      canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))

#----------------Business Classic------------------ 
    elif menuvar == 'Business Classic':
      frame = Frame(fifthtab, width=953, height=300)
      frame.pack(expand=True, fill=BOTH)
      frame.place(x=247,y=90)
        
      canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
        
      vertibar=Scrollbar(frame, orient=VERTICAL)
      vertibar.pack(side=RIGHT,fill=Y)
      vertibar.config(command=canvas.yview)
      canvas.config(width=953,height=300)
        
      canvas.config(yscrollcommand=vertibar.set)
      canvas.pack(expand=True,side=LEFT,fill=BOTH)
      canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
      canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
      canvas.create_line(150, 70, 800, 70, fill='orange')
      
      try:
        est_image = Image.open("images/"+estdata1[13])
        est_resize_image = est_image.resize((200,100))
        est_image = ImageTk.PhotoImage(est_resize_image)

        est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
        window_image = canvas.create_window(140, 120, anchor="nw", window=est_btlogo)
        est_btlogo.photo = est_image
      except:
        pass  

      canvas.create_text(500, 90, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
      # canvas.create_text(485, 220, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
      T_address = Text(canvas, height=5, width=35, font=('Helvetica 10'),borderwidth=0)
      T_address.tag_configure('tag_name',justify='right')
      T_address.insert('1.0', estdata1[2])
      T_address.tag_add('tag_name','1.0', 'end')
      T_address_window = canvas.create_window(350, 100, anchor="nw", window=T_address)
      
      canvas.create_text(480, 210, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))

      canvas.create_text(655, 100, text="John Doe", fill="black", font=('Helvetica 10 '))
      canvas.create_text(696, 120, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
      canvas.create_text(706, 135, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
      canvas.create_text(665, 150, text="United States", fill="black", font=('Helvetica 10'))

      canvas.create_text(659, 180, text=""+est_str1.get(), fill="black", font=('Helvetica 11'))
      canvas.create_text(675, 210, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
      canvas.create_text(659, 240, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))

      canvas.create_text(776, 180, text="EST1/2022", fill="black", font=('Helvetica 11'))
      canvas.create_text(776, 210, text="05 May 2022", fill="black", font=('Helvetica 11'))
      canvas.create_text(776, 240, text="20-05-2022", fill="black", font=('Helvetica 11'))

      s = ttk.Style()
      s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

      tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_1.Treeview')
        
      tree.column("# 1", anchor=E, stretch=NO, width=200)
      tree.heading("# 1", text="Product/Service")
      tree.column("# 2", anchor=E, stretch=NO, width=250)
      tree.heading("# 2", text="Description")
      tree.column("# 3", anchor=E, stretch=NO, width=90)
      tree.heading("# 3", text="Unit Price")
      tree.column("# 4", anchor=E, stretch=NO, width=80)
      tree.heading("# 4", text="Quantity")
      tree.column("# 5", anchor=E, stretch=NO, width=80)
      tree.heading("# 5", text="Price")
    
      window = canvas.create_window(120, 255, anchor="nw", window=tree)

      canvas.create_line(120, 295, 820, 295 )
      canvas.create_line(120, 255, 120, 295 )
      canvas.create_line(320, 255, 320, 295 )
      canvas.create_line(570, 255, 570, 295 )
      canvas.create_line(660, 255, 660, 295 )
      canvas.create_line(740, 255, 740, 295 )
      canvas.create_line(820, 255, 820, 445 )
      canvas.create_line(570, 320, 820, 320 )
      canvas.create_line(570, 345, 820, 345 )
      canvas.create_line(570, 370, 820, 370 )
      canvas.create_line(570, 395, 820, 395 )
      canvas.create_line(570, 420, 820, 420 )
      canvas.create_line(570, 445, 820, 445 )
    
      canvas.create_text(160, 285, text="PROD-0001", fill="black", font=('Helvetica 10'))
      canvas.create_text(450, 285, text="Example product - Description text...", fill="black", font=('Helvetica 10'))

      if comcursignpla.get() == "before amount":
        canvas.create_text(624, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount":
        canvas.create_text(624, 285, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "before amount with space":
        canvas.create_text(624, 285, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount with space":
        canvas.create_text(624, 285, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      else:
        pass
      # canvas.create_text(624, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      canvas.create_text(700, 285, text="1", fill="black", font=('Helvetica 10'))
      if comcursignpla.get() == "before amount":
        canvas.create_text(784, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount":
        canvas.create_text(784, 285, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "before amount with space":
        canvas.create_text(784, 285, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount with space":
        canvas.create_text(784, 285, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      else:
        pass
      # canvas.create_text(784, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      if comcursignpla.get() == "before amount":
        canvas.create_text(784, 310, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount":
        canvas.create_text(784, 310, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "before amount with space":
        canvas.create_text(784, 310, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount with space":
        canvas.create_text(784, 310, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      else:
        pass
      # canvas.create_text(784, 310, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      if comcursignpla.get() == "before amount":
        canvas.create_text(789, 335, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount":
        canvas.create_text(789, 335, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "before amount with space":
        canvas.create_text(789, 335, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount with space":
        canvas.create_text(789, 335, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      else:
        pass
      # canvas.create_text(789, 335, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      if comcursignpla.get() == "before amount":
        canvas.create_text(789, 360, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount":
        canvas.create_text(789, 360, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "before amount with space":
        canvas.create_text(789, 360, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount with space":
        canvas.create_text(789, 360, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      else:
        pass
      # canvas.create_text(789, 360, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      if comcursignpla.get() == "before amount":
        canvas.create_text(784, 385, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount":
        canvas.create_text(784, 385, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "before amount with space":
        canvas.create_text(784, 385, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount with space":
        canvas.create_text(784, 385, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      else:
        pass
      # canvas.create_text(784, 385, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
      if comcursignpla.get() == "before amount":
        canvas.create_text(784, 410, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount":
        canvas.create_text(784, 410, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "before amount with space":
        canvas.create_text(784, 410, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount with space":
        canvas.create_text(784, 410, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      else:
        pass
      # canvas.create_text(784, 410, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      if comcursignpla.get() == "before amount":
        canvas.create_text(784, 435, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount":
        canvas.create_text(784, 435, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "before amount with space":
        canvas.create_text(784, 435, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
      elif comcursignpla.get() == "after amount with space":
        canvas.create_text(784, 435, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
      else:
        pass
      # canvas.create_text(784, 435, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

      canvas.create_text(595, 310, text="Subtotal", fill="black", font=('Helvetica 10'))
      canvas.create_text(585, 335, text="TAX1", fill="black", font=('Helvetica 10'))
      canvas.create_text(635, 360, text="Shipping and handling", fill="black", font=('Helvetica 10'))
      canvas.create_text(615, 385, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))
      canvas.create_text(600, 410, text="Total Paid", fill="black", font=('Helvetica 10'))
      canvas.create_text(595, 435, text="Balance", fill="black", font=('Helvetica 10'))

      canvas.create_line(150, 470, 800, 470, fill='orange')
      canvas.create_text(275, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
      canvas.create_text(182, 510, text="...", fill="black", font=('Helvetica 10'))
      canvas.create_text(182, 520, text="...", fill="black", font=('Helvetica 10'))
      canvas.create_text(182, 530, text="...", fill="black", font=('Helvetica 10'))
        
      canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
      canvas.create_line(150, 608, 795, 608, fill='orange')
      # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10'))
      T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
      T.insert(END, estdata1[39])
      T_window = canvas.create_window(155, 612, anchor="nw", window=T)
      canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
      canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
    else:
      pass

win_menu2 = StringVar()
winstyle2 = ttk.Combobox(fifthtab,textvariable=win_menu2)
winstyle2.bind("<<ComboboxSelected>>", maindropmenu)
winstyle2["values"] = ("Professional 1 (logo on left side)","Professional 2 (logo on right side)","Simplified 1 (logo on left side)","Simplified 2 (logo on right side)","Business Classic")
if not estdata:
  winstyle2.current(0)
  frame = Frame(fifthtab, width=953, height=300)
  frame.pack(expand=True, fill=BOTH)
  frame.place(x=247,y=90)
  canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
        
  vertibar=Scrollbar(frame, orient=VERTICAL)
  vertibar.pack(side=RIGHT,fill=Y)
  vertibar.config(command=canvas.yview)
    
  canvas.config(width=953,height=300)
  canvas.config(yscrollcommand=vertibar.set)
  canvas.pack(expand=True,side=LEFT,fill=BOTH)
  canvas.create_rectangle(100, 8, 850, 687 , outline='yellow',fill='white')
  canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))

  #canvas.create_image(120,0, anchor=NW, image=est_logo)  
  canvas.create_text(285, 110, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))
    
  canvas.create_text(202, 160, text=""+est_str2.get(), fill="black", font=('Helvetica 11'))
  canvas.create_text(215, 180, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
  canvas.create_text(200, 200, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))
  canvas.create_text(191, 220, text="Terms", fill="black", font=('Helvetica 11'))
  canvas.create_text(205, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
  canvas.create_text(350, 160, text="EST1/2022", fill="black", font=('Helvetica 11'))
  canvas.create_text(350, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
  canvas.create_text(350, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
  canvas.create_text(340, 220, text="NET 15", fill="black", font=('Helvetica 11'))
    
  canvas.create_text(720, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
  # canvas.create_text(700, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'), width=125)
  # T_address = Text(canvas, height=5, width=20 , font=('Helvetica 10'))
  # T_address.insert(END, estdata[2])
  # T_address_window = canvas.create_window(645, 80, anchor="nw", window=T_address)
  canvas.create_text(700, 180, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
  canvas.create_text(700, 205, text=" "+est_str1.get(), fill="black", font=('Helvetica 14 bold'))
  canvas.create_text(706, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
    
  canvas.create_text(210, 260, text=""+est_str5.get(), fill="black", font=('Helvetica 10 underline'))
  canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
  canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
  canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
  canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
  canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
  canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
  canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
  canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
  canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))
    
  s = ttk.Style()
  s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

  tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_1.Treeview')

  tree.column("# 1", anchor=E, stretch=NO, width=100)
  tree.heading("# 1", text="ID/SKU")
  tree.column("# 2", anchor=E, stretch=NO, width=350)
  tree.heading("# 2", text="Product/Service - Description")
  tree.column("# 3", anchor=E, stretch=NO, width=80)
  tree.heading("# 3", text="Quantity")
  tree.column("# 4", anchor=E, stretch=NO, width=90)
  tree.heading("# 4", text="Unit Price")
  tree.column("# 5", anchor=E, stretch=NO, width=80)
  tree.heading("# 5", text="Price")
    
  window = canvas.create_window(120, 340, anchor="nw", window=tree)

  canvas.create_line(120, 390, 820, 390 )
  canvas.create_line(120, 340, 120, 365 )
  canvas.create_line(120, 365, 120, 390 )
  canvas.create_line(820, 340, 820, 540 )
  canvas.create_line(740, 340, 740, 540 )
  canvas.create_line(570, 340, 570, 540 )
  canvas.create_line(570, 415, 820, 415 )
  canvas.create_line(570, 440, 820, 440 )
  canvas.create_line(570, 465, 820, 465 )
  canvas.create_line(570, 490, 820, 490 )
  canvas.create_line(570, 515, 820, 515 )
  canvas.create_line(650, 340, 650, 390 )
  canvas.create_line(220, 340, 220, 390 )
  canvas.create_line(570, 540, 820, 540 )

  canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
  canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
  canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))
  
  if comcursignpla.get() == "before amount":
    canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  elif comcursignpla.get() == "after amount":
    canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(704, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))

  else:
    pass
  # canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  elif comcursignpla.get() == "after amount":
    canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

  if comcursignpla.get() == "before amount":
    canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
  
  if comcursignpla.get() == "before amount":
    canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass

  # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  if comcursignpla.get() == "before amount":
    canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
  else:
    pass

  # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
  canvas.create_text(650, 479, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass

  # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))
  
  if comcursignpla.get() == "before amount":
    canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

  canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
  canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
  canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
  canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
    
  canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
  canvas.create_line(150, 608, 795, 608)
  # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10')) 
  # T = Text(canvas, height=3, width=105, font=('Helvetica 10'))
  # T.insert(END, estdata[39])
  # T_window = canvas.create_window(105, 612, anchor="nw", window=T)


  canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
  canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10')) 
elif estdata[32] == 'Professional 1 (logo on left side)':
  winstyle2.insert(0, estdata[32])
  frame = Frame(fifthtab, width=953, height=300)
  frame.pack(expand=True, fill=BOTH)
  frame.place(x=247,y=90)
  canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
        
  vertibar=Scrollbar(frame, orient=VERTICAL)
  vertibar.pack(side=RIGHT,fill=Y)
  vertibar.config(command=canvas.yview)
    
  canvas.config(width=953,height=300)
  canvas.config(yscrollcommand=vertibar.set)
  canvas.pack(expand=True,side=LEFT,fill=BOTH)
  canvas.create_rectangle(100, 8, 850, 687 , outline='yellow',fill='white')
  canvas.create_text(500, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
  try:
    est_image = Image.open("images/"+estdata[13])
    est_resize_image = est_image.resize((200,100))
    est_image = ImageTk.PhotoImage(est_resize_image)

    est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
    window_image = canvas.create_window(175, 45, anchor="nw", window=est_btlogo)
    est_btlogo.photo = est_image
  except:
    pass  
  canvas.create_text(202, 160, text=""+est_str2.get(), fill="black", font=('Helvetica 11'))
  canvas.create_text(215, 180, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
  canvas.create_text(200, 200, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))
  canvas.create_text(191, 220, text="Terms", fill="black", font=('Helvetica 11'))
  canvas.create_text(205, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
  canvas.create_text(350, 160, text="EST1/2022", fill="black", font=('Helvetica 11'))
  canvas.create_text(350, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
  canvas.create_text(350, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
  canvas.create_text(340, 220, text="NET 15", fill="black", font=('Helvetica 11'))
    
  canvas.create_text(720, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
  # canvas.create_text(700, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'), width=125)
  T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
  T_address.tag_configure('tag_name',justify='right')
  T_address.insert('1.0', estdata[2])
  T_address.tag_add('tag_name','1.0', 'end')
  T_address_window = canvas.create_window(520, 80, anchor="nw", window=T_address)
  canvas.create_text(695, 180, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
  canvas.create_text(700, 205, text=" "+est_str1.get(), fill="black", font=('Helvetica 14 bold'))
  canvas.create_text(706, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
    
  canvas.create_text(210, 260, text=""+est_str5.get(), fill="black", font=('Helvetica 10 underline'))
  canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
  canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
  canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
  canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
  canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
  canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
  canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
  canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
  canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))
    
  s = ttk.Style()
  s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

  tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_1.Treeview')

  tree.column("# 1", anchor=E, stretch=NO, width=100)
  tree.heading("# 1", text="ID/SKU")
  tree.column("# 2", anchor=E, stretch=NO, width=350)
  tree.heading("# 2", text="Product/Service - Description")
  tree.column("# 3", anchor=E, stretch=NO, width=80)
  tree.heading("# 3", text="Quantity")
  tree.column("# 4", anchor=E, stretch=NO, width=90)
  tree.heading("# 4", text="Unit Price")
  tree.column("# 5", anchor=E, stretch=NO, width=80)
  tree.heading("# 5", text="Price")
    
  window = canvas.create_window(120, 340, anchor="nw", window=tree)

  canvas.create_line(120, 390, 820, 390 )
  canvas.create_line(120, 340, 120, 365 )
  canvas.create_line(120, 365, 120, 390 )
  canvas.create_line(820, 340, 820, 540 )
  canvas.create_line(740, 340, 740, 540 )
  canvas.create_line(570, 340, 570, 540 )
  canvas.create_line(570, 415, 820, 415 )
  canvas.create_line(570, 440, 820, 440 )
  canvas.create_line(570, 465, 820, 465 )
  canvas.create_line(570, 490, 820, 490 )
  canvas.create_line(570, 515, 820, 515 )
  canvas.create_line(650, 340, 650, 390 )
  canvas.create_line(220, 340, 220, 390 )
  canvas.create_line(570, 540, 820, 540 )

  canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
  canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
  canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))
  
  if comcursignpla.get() == "before amount":
    canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  elif comcursignpla.get() == "after amount":
    canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(704, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))

  else:
    pass
  # canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  elif comcursignpla.get() == "after amount":
    canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))

  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

  if comcursignpla.get() == "before amount":
    canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))
  
  if comcursignpla.get() == "before amount":
    canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass

  # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  if comcursignpla.get() == "before amount":
    canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
  else:
    pass

  # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
  canvas.create_text(650, 479, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass

  # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))
  
  if comcursignpla.get() == "before amount":
    canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

  canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
  canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
  canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
  canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))
    
  canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
  canvas.create_line(150, 608, 795, 608)
  # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10')) 
  T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
  T.insert(END, estdata[39])
  T_window = canvas.create_window(155, 612, anchor="nw", window=T)

  canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
  canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
elif estdata[32] == 'Professional 2 (logo on right side)':
  winstyle2.insert(0, estdata[32])
  frame = Frame(fifthtab, width=953, height=300)
  frame.pack(expand=True, fill=BOTH)
  frame.place(x=247,y=90)
    
  canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
    
  vertibar=Scrollbar(frame, orient=VERTICAL)
  vertibar.pack(side=RIGHT,fill=Y)
  vertibar.config(command=canvas.yview)
  canvas.config(width=953,height=300)
    
  canvas.config(yscrollcommand=vertibar.set)
  canvas.pack(expand=True,side=LEFT,fill=BOTH)
  canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
  canvas.create_text(500, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
  try:
    est_image = Image.open("images/"+estdata[13])
    est_resize_image = est_image.resize((200,100))
    est_image = ImageTk.PhotoImage(est_resize_image)

    est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
    window_image = canvas.create_window(500, 45, anchor="nw", window=est_btlogo)
    est_btlogo.photo = est_image
  except:
    pass  
  canvas.create_text(250, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
  # canvas.create_text(225, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
  T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
  T_address.tag_configure('tag_name',justify='right')
  T_address.insert('1.0', estdata[2])
  T_address.tag_add('tag_name','1.0', 'end')
  T_address_window = canvas.create_window(100, 80, anchor="nw", window=T_address)
  canvas.create_text(225, 180, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
  canvas.create_text(225, 205, text=""+est_str1.get(), fill="black", font=('Helvetica 14 bold'))
  canvas.create_text(232, 225, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))
    
  canvas.create_text(502, 160, text=""+est_str2.get(), fill="black", font=('Helvetica 11'))
  canvas.create_text(515, 180, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
  canvas.create_text(500, 200, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))
  canvas.create_text(491, 220, text="Terms", fill="black", font=('Helvetica 11'))
  canvas.create_text(505, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
  canvas.create_text(690, 160, text="EST1/2022", fill="black", font=('Helvetica 11'))
  canvas.create_text(690, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
  canvas.create_text(690, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
  canvas.create_text(680, 220, text="NET 15", fill="black", font=('Helvetica 11'))      
    
  canvas.create_text(210, 260, text=""+est_str5.get(), fill="black", font=('Helvetica 10 underline'))
  canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
  canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
  canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
  canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
  canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
  canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
  canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
  canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
  canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

  s = ttk.Style()
  s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

  tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_1.Treeview')
    
  tree.column("# 1", anchor=E, stretch=NO, width=100)
  tree.heading("# 1", text="ID/SKU")
  tree.column("# 2", anchor=E, stretch=NO, width=350)
  tree.heading("# 2", text="Product/Service - Description")
  tree.column("# 3", anchor=E, stretch=NO, width=80)
  tree.heading("# 3", text="Quantity")
  tree.column("# 4", anchor=E, stretch=NO, width=90)
  tree.heading("# 4", text="Unit Price")
  tree.column("# 5", anchor=E, stretch=NO, width=80)
  tree.heading("# 5", text="Price")
    
  window = canvas.create_window(120, 340, anchor="nw", window=tree)

  canvas.create_line(120, 390, 820, 390 )
  canvas.create_line(120, 340, 120, 365 )
  canvas.create_line(120, 365, 120, 390 )
  canvas.create_line(820, 340, 820, 540 )
  canvas.create_line(740, 340, 740, 540 )
  canvas.create_line(570, 340, 570, 540 )
  canvas.create_line(570, 415, 820, 415 )
  canvas.create_line(570, 440, 820, 440 )
  canvas.create_line(570, 465, 820, 465 )
  canvas.create_line(570, 490, 820, 490 )
  canvas.create_line(570, 515, 820, 515 )
  canvas.create_line(650, 340, 650, 390 )
  canvas.create_line(220, 340, 220, 390 )
  canvas.create_line(570, 540, 820, 540 )

  canvas.create_text(165, 372, text="PROD-0001", fill="black", font=('Helvetica 10'))
  canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
  canvas.create_text(610, 372, text="1", fill="black", font=('Helvetica 10'))

  if comcursignpla.get() == "before amount":
    canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(704, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(704, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass

  # canvas.create_text(704, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  if comcursignpla.get() == "before amount":
    canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass

  # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))

  if comcursignpla.get() == "before amount":
    canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass

  # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

  if comcursignpla.get() == "before amount":
    canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass

  # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))

  if comcursignpla.get() == "before amount":
    canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass

  # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  if comcursignpla.get() == "before amount":
    canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10 bold'))
  else:
    pass

  # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
  canvas.create_text(650, 479, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))

  if comcursignpla.get() == "before amount":
    canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass

  # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))
  
  if comcursignpla.get() == "before amount":
    canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass

  # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

  canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
  canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
  canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
  canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))

  canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
  canvas.create_line(150, 608, 795, 608)
  # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10'))
  T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
  T.insert(END, estdata[39])
  T_window = canvas.create_window(155, 612, anchor="nw", window=T)
  canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
  canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
elif estdata[32] == 'Simplified 1 (logo on left side)':
  winstyle2.insert(0, estdata[32])
  frame = Frame(fifthtab, width=953, height=300)
  frame.pack(expand=True, fill=BOTH)
  frame.place(x=247,y=90)
  canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))

  vertibar=Scrollbar(frame, orient=VERTICAL)
  vertibar.pack(side=RIGHT,fill=Y)
  vertibar.config(command=canvas.yview)
  canvas.config(width=953,height=300)

  canvas.config(yscrollcommand=vertibar.set)
  canvas.pack(expand=True,side=LEFT,fill=BOTH)
  canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
  canvas.create_text(500, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
  try:
    est_image = Image.open("images/"+estdata[13])
    est_resize_image = est_image.resize((200,100))
    est_image = ImageTk.PhotoImage(est_resize_image)

    est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
    window_image = canvas.create_window(175, 45, anchor="nw", window=est_btlogo)
    est_btlogo.photo = est_image
  except:
    pass  
  canvas.create_text(202, 160, text=""+est_str2.get(), fill="black", font=('Helvetica 11'))
  canvas.create_text(215, 180, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
  canvas.create_text(200, 200, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))
  canvas.create_text(191, 220, text="Terms", fill="black", font=('Helvetica 11'))
  canvas.create_text(205, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
  canvas.create_text(350, 160, text="EST1/2022", fill="black", font=('Helvetica 11'))
  canvas.create_text(350, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
  canvas.create_text(350, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
  canvas.create_text(340, 220, text="NET 15", fill="black", font=('Helvetica 11'))      

  canvas.create_text(720, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
  # canvas.create_text(710, 200, text=caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
  T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
  T_address.tag_configure('tag_name',justify='right')
  T_address.insert('1.0', estdata[2])
  T_address.tag_add('tag_name','1.0', 'end')
  T_address_window = canvas.create_window(520, 80, anchor="nw", window=T_address)

  canvas.create_text(708, 170, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
  canvas.create_text(710, 205, text=""+est_str1.get(), fill="black", font=('Helvetica 14 bold'))
    
  canvas.create_text(210, 260, text=""+est_str5.get(), fill="black", font=('Helvetica 10 underline'))
  canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
  canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
  canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
  canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
  canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
  canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
  canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
  canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
  canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

  s = ttk.Style()
  s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

  tree=ttk.Treeview(canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle_1.Treeview')
    
  tree.column("# 1", anchor=E, stretch=NO, width=530)
  tree.heading("# 1", text="Product/Service - Description")
  tree.column("# 2", anchor=E, stretch=NO, width=90)
  tree.heading("# 2", text="Quantity")
  tree.column("# 3", anchor=E, stretch=NO, width=80)
  tree.heading("# 3", text="Price")
    
  window = canvas.create_window(120, 340, anchor="nw", window=tree)

  canvas.create_line(120, 390, 820, 390 )
  canvas.create_line(120, 340, 120, 365 )
  canvas.create_line(120, 365, 120, 390 )
  canvas.create_line(820, 340, 820, 540 )
  canvas.create_line(740, 340, 740, 540 )
  canvas.create_line(570, 390, 570, 540 )
  canvas.create_line(570, 415, 820, 415 )
  canvas.create_line(570, 440, 820, 440 )
  canvas.create_line(570, 465, 820, 465 )
  canvas.create_line(570, 490, 820, 490 )
  canvas.create_line(570, 515, 820, 515 )
  canvas.create_line(650, 340, 650, 390 )
  canvas.create_line(570, 540, 820, 540 )

    
  canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
  canvas.create_text(710, 372, text="1", fill="black", font=('Helvetica 10'))

  if comcursignpla.get() == "before amount":
    canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass

  # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))

  if comcursignpla.get() == "before amount":
    canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass

  # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

  if comcursignpla.get() == "before amount":
    canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass

  # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))

  if comcursignpla.get() == "before amount":
    canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass

  # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  if comcursignpla.get() == "before amount":
    canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass

  # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
  canvas.create_text(650, 479, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))

  if comcursignpla.get() == "before amount":
    canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass

  # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))

  if comcursignpla.get() == "before amount":
    canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass

  # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

  canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
  canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
  canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
  canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))

  canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
  canvas.create_line(150, 608, 795, 608)
  # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10'))
  T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
  T.insert(END, estdata[39])
  T_window = canvas.create_window(155, 612, anchor="nw", window=T)
  canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
  canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
elif estdata[32] == 'Simplified 2 (logo on right side)':
  winstyle2.insert(0, estdata[32])
  frame = Frame(fifthtab, width=953, height=300)
  frame.pack(expand=True, fill=BOTH)
  frame.place(x=247,y=90)

  canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))

  vertibar=Scrollbar(frame, orient=VERTICAL)
  vertibar.pack(side=RIGHT,fill=Y)
  vertibar.config(command=canvas.yview)
  canvas.config(width=953,height=300)

  canvas.config(yscrollcommand=vertibar.set)
  canvas.pack(expand=True,side=LEFT,fill=BOTH)
  canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
  canvas.create_text(500, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
  try:
    est_image = Image.open("images/"+estdata[13])
    est_resize_image = est_image.resize((200,100))
    est_image = ImageTk.PhotoImage(est_resize_image)

    est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
    window_image = canvas.create_window(500, 45, anchor="nw", window=est_btlogo)
    est_btlogo.photo = est_image
  except:
    pass  
  canvas.create_text(250, 60, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
  # canvas.create_text(224, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
  T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
  T_address.tag_configure('tag_name',justify='right')
  T_address.insert('1.0', estdata[2])
  T_address.tag_add('tag_name','1.0', 'end')
  T_address_window = canvas.create_window(100, 80, anchor="nw", window=T_address)
  canvas.create_text(224, 180, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))
  canvas.create_text(225, 205, text=""+est_str1.get(), fill="black", font=('Helvetica 14 bold'))

  canvas.create_text(502, 160, text=""+est_str2.get(), fill="black", font=('Helvetica 11'))
  canvas.create_text(515, 180, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
  canvas.create_text(500, 200, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))
  canvas.create_text(491, 220, text="Terms", fill="black", font=('Helvetica 11'))
  canvas.create_text(505, 240, text="Order ref.#", fill="black", font=('Helvetica 11'))
  canvas.create_text(680, 160, text="EST1/2022", fill="black", font=('Helvetica 11'))
  canvas.create_text(680, 180, text="05-05-2022", fill="black", font=('Helvetica 11'))
  canvas.create_text(680, 200, text="20-05-2022", fill="black", font=('Helvetica 11'))
  canvas.create_text(670, 220, text="NET 15", fill="black", font=('Helvetica 11'))      

  canvas.create_text(210, 260, text=""+est_str5.get(), fill="black", font=('Helvetica 10 underline'))
  canvas.create_text(203, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
  canvas.create_text(246, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
  canvas.create_text(255, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
  canvas.create_text(215, 325, text="United States", fill="black", font=('Helvetica 10'))
  canvas.create_text(550, 260, text="Ship to", fill="black", font=('Helvetica 10 underline'))
  canvas.create_text(556, 280, text="John Doe", fill="black", font=('Helvetica 10 '))
  canvas.create_text(598, 295, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
  canvas.create_text(608, 310, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
  canvas.create_text(568, 325, text="United States", fill="black", font=('Helvetica 10'))

  s = ttk.Style()
  s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

  tree=ttk.Treeview(canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle_1.Treeview')
    
  tree.column("# 1", anchor=E, stretch=NO, width=530)
  tree.heading("# 1", text="Product/Service - Description")
  tree.column("# 2", anchor=E, stretch=NO, width=90)
  tree.heading("# 2", text="Quantity")
  tree.column("# 3", anchor=E, stretch=NO, width=80)
  tree.heading("# 3", text="Price")
    
  window = canvas.create_window(120, 340, anchor="nw", window=tree)

  canvas.create_line(120, 390, 820, 390 )
  canvas.create_line(120, 340, 120, 365 )
  canvas.create_line(120, 365, 120, 390 )
  canvas.create_line(820, 340, 820, 540 )
  canvas.create_line(740, 340, 740, 540 )
  canvas.create_line(570, 390, 570, 540 )
  canvas.create_line(570, 415, 820, 415 )
  canvas.create_line(570, 440, 820, 440 )
  canvas.create_line(570, 465, 820, 465 )
  canvas.create_line(570, 490, 820, 490 )
  canvas.create_line(570, 515, 820, 515 )
  canvas.create_line(650, 340, 650, 390 )
  canvas.create_line(570, 540, 820, 540 )

    
  canvas.create_text(370, 372, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
  canvas.create_text(710, 372, text="1", fill="black", font=('Helvetica 10'))

  if comcursignpla.get() == "before amount":
    canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(784, 372, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(784, 372, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass

  # canvas.create_text(784, 372, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  canvas.create_text(650, 404, text="Subtotal", fill="black", font=('Helvetica 10'))

  if comcursignpla.get() == "before amount":
    canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(784, 404, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(784, 404, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass

  # canvas.create_text(784, 404, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  canvas.create_text(650, 428, text="TAX1", fill="black", font=('Helvetica 10'))

  if comcursignpla.get() == "before amount":
    canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(786, 428, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(786, 428, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass

  # canvas.create_text(786, 428, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  canvas.create_text(650, 454, text="Shipping and handling", fill="black", font=('Helvetica 10'))

  if comcursignpla.get() == "before amount":
    canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(786, 454, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(786, 454, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass

  # canvas.create_text(786, 454, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  if comcursignpla.get() == "before amount":
    canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(784, 479, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(784, 479, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass

  # canvas.create_text(784, 479, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
  canvas.create_text(650, 479, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))

  if comcursignpla.get() == "before amount":
    canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(784, 502, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(784, 502, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass

  # canvas.create_text(784, 502, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  canvas.create_text(650, 502, text="Total Paid", fill="black", font=('Helvetica 10'))

  if comcursignpla.get() == "before amount":
    canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(784, 526, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(784, 526, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass

  # canvas.create_text(784, 526, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  canvas.create_text(650, 526, text="Balance", fill="black", font=('Helvetica 10'))

  canvas.create_text(275, 550, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
  canvas.create_text(182, 560, text="...", fill="black", font=('Helvetica 10'))
  canvas.create_text(182, 570, text="...", fill="black", font=('Helvetica 10'))
  canvas.create_text(182, 580, text="...", fill="black", font=('Helvetica 10'))

  canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
  canvas.create_line(150, 608, 795, 608)
  # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10'))
  T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
  T.insert(END, estdata[39])
  T_window = canvas.create_window(155, 612, anchor="nw", window=T)
  canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
  canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
elif estdata[32] == 'Business Classic':
  winstyle2.insert(0, estdata[32])
  frame = Frame(fifthtab, width=953, height=300)
  frame.pack(expand=True, fill=BOTH)
  frame.place(x=247,y=90)
    
  canvas=Canvas(frame, bg='grey', width=953, height=300, scrollregion=(0,0,700,700))
    
  vertibar=Scrollbar(frame, orient=VERTICAL)
  vertibar.pack(side=RIGHT,fill=Y)
  vertibar.config(command=canvas.yview)
  canvas.config(width=953,height=300)
    
  canvas.config(yscrollcommand=vertibar.set)
  canvas.pack(expand=True,side=LEFT,fill=BOTH)
  canvas.create_rectangle(100, 10, 850, 687 , outline='yellow',fill='white')
  canvas.create_text(500, 50, text="Title text goes here...", fill="black", font=('Helvetica 10'))
  canvas.create_line(150, 70, 800, 70, fill='orange')
  
  try:
    est_image = Image.open("images/"+estdata[13])
    est_resize_image = est_image.resize((200,100))
    est_image = ImageTk.PhotoImage(est_resize_image)

    est_btlogo = Label(canvas,width=200,height=100,image = est_image) 
    window_image = canvas.create_window(140, 120, anchor="nw", window=est_btlogo)
    est_btlogo.photo = est_image
  except:
    pass  

  canvas.create_text(500, 90, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
  # canvas.create_text(480, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
  T_address = Text(canvas, height=5, width=35, font=('Helvetica 10'),borderwidth=0)
  T_address.tag_configure('tag_name',justify='right')
  T_address.insert('1.0', estdata[2])
  T_address.tag_add('tag_name','1.0', 'end')
  T_address_window = canvas.create_window(350, 100, anchor="nw", window=T_address)
      
      
  canvas.create_text(480, 210, text=" "+comsalestax.get(), fill="black", font=('Helvetica 10'))

  canvas.create_text(655, 100, text="John Doe", fill="black", font=('Helvetica 10 '))
  canvas.create_text(696, 120, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
  canvas.create_text(706, 135, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
  canvas.create_text(665, 150, text="United States", fill="black", font=('Helvetica 10'))

  canvas.create_text(659, 180, text=""+est_str1.get(), fill="black", font=('Helvetica 11'))
  canvas.create_text(675, 210, text=""+est_str3.get(), fill="black", font=('Helvetica 11'))
  canvas.create_text(659, 240, text=""+est_str4.get(), fill="black", font=('Helvetica 11'))

  canvas.create_text(776, 180, text="EST1/2022", fill="black", font=('Helvetica 11'))
  canvas.create_text(776, 210, text="05 May 2022", fill="black", font=('Helvetica 11'))
  canvas.create_text(776, 240, text="20-05-2022", fill="black", font=('Helvetica 11'))

  s = ttk.Style()
  s.configure('mystyle_1.Treeview.Heading', background=''+win_menu1.get(),State='DISABLE')

  tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_1.Treeview')
    
  tree.column("# 1", anchor=E, stretch=NO, width=200)
  tree.heading("# 1", text="Product/Service")
  tree.column("# 2", anchor=E, stretch=NO, width=250)
  tree.heading("# 2", text="Description")
  tree.column("# 3", anchor=E, stretch=NO, width=90)
  tree.heading("# 3", text="Unit Price")
  tree.column("# 4", anchor=E, stretch=NO, width=80)
  tree.heading("# 4", text="Quantity")
  tree.column("# 5", anchor=E, stretch=NO, width=80)
  tree.heading("# 5", text="Price")
    
  window = canvas.create_window(120, 255, anchor="nw", window=tree)

  canvas.create_line(120, 295, 820, 295 )
  canvas.create_line(120, 255, 120, 295 )
  canvas.create_line(320, 255, 320, 295 )
  canvas.create_line(570, 255, 570, 295 )
  canvas.create_line(660, 255, 660, 295 )
  canvas.create_line(740, 255, 740, 295 )
  canvas.create_line(820, 255, 820, 445 )
  canvas.create_line(570, 320, 820, 320 )
  canvas.create_line(570, 345, 820, 345 )
  canvas.create_line(570, 370, 820, 370 )
  canvas.create_line(570, 395, 820, 395 )
  canvas.create_line(570, 420, 820, 420 )
  canvas.create_line(570, 445, 820, 445 )
    
  canvas.create_text(160, 285, text="PROD-0001", fill="black", font=('Helvetica 10'))
  canvas.create_text(450, 285, text="Example product - Description text...", fill="black", font=('Helvetica 10'))

  if comcursignpla.get() == "before amount":
    canvas.create_text(624, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(624, 285, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(624, 285, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(624, 285, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  # canvas.create_text(624, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  canvas.create_text(700, 285, text="1", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(784, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(784, 285, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(784, 285, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(784, 285, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  # canvas.create_text(784, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(784, 310, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(784, 310, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(784, 310, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(784, 310, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  # canvas.create_text(784, 310, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(789, 335, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(789, 335, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(789, 335, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(789, 335, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  # canvas.create_text(789, 335, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(789, 360, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(789, 360, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(789, 360, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(789, 360, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  # canvas.create_text(789, 360, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(784, 385, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(784, 385, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(784, 385, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(784, 385, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  # canvas.create_text(784, 385, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(784, 410, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(784, 410, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(784, 410, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(784, 410, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  # canvas.create_text(784, 410, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(784, 435, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(784, 435, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(784, 435, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(784, 435, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  # canvas.create_text(784, 435, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  canvas.create_text(595, 310, text="Subtotal", fill="black", font=('Helvetica 10'))
  canvas.create_text(585, 335, text="TAX1", fill="black", font=('Helvetica 10'))
  canvas.create_text(635, 360, text="Shipping and handling", fill="black", font=('Helvetica 10'))
  canvas.create_text(615, 385, text=""+est_str6.get(), fill="black", font=('Helvetica 10 bold'))
  canvas.create_text(600, 410, text="Total Paid", fill="black", font=('Helvetica 10'))
  canvas.create_text(595, 435, text="Balance", fill="black", font=('Helvetica 10'))

  canvas.create_line(150, 470, 800, 470, fill='orange')
  canvas.create_text(275, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
  canvas.create_text(182, 510, text="...", fill="black", font=('Helvetica 10'))
  canvas.create_text(182, 520, text="...", fill="black", font=('Helvetica 10'))
  canvas.create_text(182, 530, text="...", fill="black", font=('Helvetica 10'))
    
  canvas.create_text(500, 600, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
  canvas.create_line(150, 608, 795, 608, fill='orange')
  # canvas.create_text(280, 640, text= ""+est_str7.get(), fill="black", font=('Helvetica 10'))
  T = Text(canvas, height=3, width=90, font=('Helvetica 10'),borderwidth=0)
  T.insert(END, estdata[39])
  T_window = canvas.create_window(155, 612, anchor="nw", window=T)
  canvas.create_text(280, 670, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
  canvas.create_text(720, 670, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
else:
  pass
winstyle2.place(x=770 ,y=40, width=220)
#winstyle2.current(0)



################### tab07 ###################################
seventhtab1=Frame(tab07, relief=GROOVE, bg="#f8f8f2")
seventhtab1.pack(side="top", fill=BOTH)

sql = "select * from company"
fbcursor.execute(sql)
advdata = fbcursor.fetchone()
#print(estdata)


seventhtab=Frame(seventhtab1, bg="#f5f3f2", height=700)
seventhtab.pack(side="top", fill=BOTH)

adv_messagelbframe=LabelFrame(seventhtab,text="Template advanced settings", height=250, width=1150)
adv_messagelbframe.place(x=2, y=10)

adv_fbill = Label(seventhtab,text="Template",font="arial 10 bold").place(x=20,y=30)

adv_ver = Label(seventhtab,text="Professional 1 (logo on left side)")
adv_ver.place(x=20,y=60)

adv_ver = Label(seventhtab,text="Professional 2 (logo on right side)")
adv_ver.place(x=20,y=90)

adv_ver = Label(seventhtab,text="Simplified 1 (logo on left side)")
adv_ver.place(x=20,y=120)

adv_ver = Label(seventhtab,text="Simplified 2 (logo on right side)")
adv_ver.place(x=20,y=150)

adv_ver = Label(seventhtab,text="Business Classic")
adv_ver.place(x=20,y=180)

adv_fbill = Label(seventhtab,text="Page size",font="arial 10 bold").place(x=255,y=30)

adv_win_menu3 = StringVar()
adv_winstyle3 = ttk.Combobox(seventhtab,textvariable=adv_win_menu3)
adv_winstyle3['values'] = ('Letter','A4')
adv_win_menu3.set('Letter')
#adv_winstyle3.current(0)
adv_winstyle3.place(x=225 ,y=60)
  

adv_win_menu4 = StringVar()
adv_winstyle4 = ttk.Combobox(seventhtab,textvariable=adv_win_menu4)
adv_winstyle4.place(x=225,y=90)
adv_winstyle4['values'] = ("Letter","A4")
adv_winstyle4.set("Letter")
adv_winstyle4.current(0)

adv_win_menu5 = StringVar()
adv_winstyle5 = ttk.Combobox(seventhtab,textvariable=adv_win_menu5)
adv_winstyle5.place(x=225,y=120)
adv_winstyle5['values'] = ("Letter","A4")
adv_winstyle5.set("Letter")
adv_winstyle5.current(0)

adv_win_menu6 = StringVar()
adv_winstyle6 = ttk.Combobox(seventhtab,textvariable=adv_win_menu6)
adv_winstyle6.place(x=225,y=150)
adv_winstyle6['values'] = ("Letter","A4")
adv_winstyle6.set("Letter")
adv_winstyle6.current(0)

adv_win_menu7 = StringVar()
adv_winstyle7 = ttk.Combobox(seventhtab,textvariable=adv_win_menu7)
adv_winstyle7.place(x=225,y=180)
adv_winstyle7['values'] = ("Letter","A4")
adv_winstyle7.set("Letter")
adv_winstyle7.current(0)

adv_fbill = Label(seventhtab,text="Right Margin(mm)",font="arial 10 bold").place(x=450,y=30)

adv_spin00 = Spinbox(seventhtab,from_=5,to=20,width=10)
adv_spin00.place(x=465,y=60)

adv_spin01 = Spinbox(seventhtab,from_=5,to=20,width=10)
adv_spin01.place(x=465,y=90)

adv_spin02 = Spinbox(seventhtab,from_=5,to=20,width=10)
adv_spin02.place(x=465,y=120)

adv_spin03 = Spinbox(seventhtab,from_=5,to=20,width=10)
adv_spin03.place(x=465,y=150)

adv_spin04 = Spinbox(seventhtab,from_=5,to=20,width=10)
adv_spin04.place(x=465,y=180)


adv_fbill = Label(seventhtab,text="'Invoice to'block position shift(mm)",font="arial 10 bold").place(x=650,y=30)

adv_lbl1 = Label(seventhtab, text="Left : ").place(x=651,y=60)
adv_lbl1 = Label(seventhtab, text="Left : ").place(x=651,y=90)
adv_lbl1 = Label(seventhtab, text="Left : ").place(x=651,y=120)
adv_lbl1 = Label(seventhtab, text="Left : ").place(x=651,y=150)

adv_spin10 = Spinbox(seventhtab,from_=-10,to=100,width=10)
adv_spin10.place(x=685,y=60)

adv_spin11 = Spinbox(seventhtab,from_=-10,to=100,width=10)
adv_spin11.place(x=685,y=90)

adv_spin12 = Spinbox(seventhtab,from_=-10,to=100,width=10)
adv_spin12.place(x=685,y=120)

adv_spin13 = Spinbox(seventhtab,from_=-10,to=100,width=10)
adv_spin13.place(x=685,y=150)

adv_lbl1 = Label(seventhtab, text="Top : ").place(x=785,y=60)
adv_lbl1 = Label(seventhtab, text="Top : ").place(x=785,y=90)
adv_lbl1 = Label(seventhtab, text="Top : ").place(x=785,y=120)
adv_lbl1 = Label(seventhtab, text="Top : ").place(x=785,y=150)

adv_spin20 = Spinbox(seventhtab,from_=0,to=100,width=10)
adv_spin20.place(x=820,y=60)

adv_spin21 = Spinbox(seventhtab,from_=0,to=100,width=10)
adv_spin21.place(x=820,y=90)

adv_spin22 = Spinbox(seventhtab,from_=0,to=100,width=10)
adv_spin22.place(x=820,y=120)

adv_spin23 = Spinbox(seventhtab,from_=0,to=100,width=10)
adv_spin23.place(x=820,y=150)

adv_bttermadd = Button(seventhtab,image=photo8,compound = LEFT,text="Refresh preview",width=115)
adv_bttermadd.place(x=1000,y=50)

adv_bttermadd = Button(seventhtab,image=saves,compound = LEFT,text="Save Settings",width=115)
adv_bttermadd.place(x=1000,y=140)

def adv_restore():
  adv_spin10.delete(0,'end')
  adv_spin10.insert(0,"0")
  adv_spin11.delete(0,'end')
  adv_spin11.insert(0,"0")
  adv_spin12.delete(0,'end')
  adv_spin12.insert(0,"0")
  adv_spin13.delete(0,'end')
  adv_spin13.insert(0,"0")
  adv_spin20.delete(0,'end')
  adv_spin20.insert(0,"0")
  adv_spin21.delete(0,'end')
  adv_spin21.insert(0,"0")
  adv_spin22.delete(0,'end')
  adv_spin22.insert(0,"0")
  adv_spin23.delete(0,'end')
  adv_spin23.insert(0,"0")
  adv_spin00.delete(0,'end')
  adv_spin00.insert(0,"10")
  adv_spin01.delete(0,'end')
  adv_spin01.insert(0,"10")
  adv_spin02.delete(0,'end')
  adv_spin02.insert(0,"10")
  adv_spin03.delete(0,'end')
  adv_spin03.insert(0,"10")
  adv_spin04.delete(0,'end')
  adv_spin04.insert(0,"10")
  adv_winstyle3.delete(0,'end')
  adv_winstyle3.insert(0,"Letter")
  adv_winstyle4.delete(0,'end')
  adv_winstyle4.insert(0,"Letter")
  adv_winstyle5.delete(0,'end')
  adv_winstyle5.insert(0,"Letter")
  adv_winstyle6.delete(0,'end')
  adv_winstyle6.insert(0,"Letter")
  adv_winstyle7.delete(0,'end')
  adv_winstyle7.insert(0,"Letter")

adv_bttermadd = Button(seventhtab,text="Restore defaults",width=16, command=adv_restore)
adv_bttermadd.place(x=1000,y=180)

adv_ver = Label(seventhtab,text="By positioning 'Invoice to'block,the customer name/address can be displayed in right place in the windowed envelope. If you networking, you need to setup this on all computer.\nExample:(Left:20 and Top:10 means that shift 'Invoice to'block to right 20mm and shift down 10mm) Original position Left:0 Top:0")
adv_ver.place(x=50,y=210)

adv_ver = Label(seventhtab,text="Selected template preview (example, click on preview for mouse scrolling)")
adv_ver.place(x=230,y=270)

#------------Professional 1 (logo on left side)------------- 
def adv_maindropmenu(event):
    menuvar=adv_win_menu8.get()
    print(menuvar)
    sql = "select * from company"
    fbcursor.execute(sql)
    advdata1 = fbcursor.fetchone()

    if menuvar == 'Professional 1 (logo on left side)':
        frame = Frame(seventhtab, width=1200, height=155)
        frame.pack(expand=True, fill=BOTH)
        frame.place(x=2,y=309)
        canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

        vertibar=Scrollbar(frame, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=canvas.yview)
        canvas.config(width=1200,height=155)

        canvas.config(yscrollcommand=vertibar.set)
        canvas.pack(expand=True,side=LEFT,fill=BOTH)
        canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')

        canvas.create_text(600, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))

        try:
          adv_image = Image.open("images/"+advdata1[13])
          adv_resize_image = adv_image.resize((200,75))
          adv_image = ImageTk.PhotoImage(adv_resize_image)

          adv_btlogo = Label(canvas,width=200,height=75,image = adv_image) 
          adv_window_image = canvas.create_window(150, 30, anchor="nw", window=adv_btlogo)
          adv_btlogo.photo = adv_image
        except:
          pass  

        canvas.create_text(130, 120, text="Invoice#", fill="black", font=('Helvetica 11'))
        canvas.create_text(141, 140, text="Invoice date", fill="black", font=('Helvetica 11'))
        canvas.create_text(130, 160, text="Due date", fill="black", font=('Helvetica 11'))
        canvas.create_text(120, 180, text="Terms", fill="black", font=('Helvetica 11'))
        canvas.create_text(134, 200, text="Order ref.#", fill="black", font=('Helvetica 11'))
        canvas.create_text(347, 120, text="INV1/2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(350, 140, text="03-05-2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(350, 160, text="18-05-2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(340, 180, text="NET 15", fill="black", font=('Helvetica 11'))

        canvas.create_text(1050, 65, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
        # canvas.create_text(1080, 200, text=""+caddent.get('1.0','end-1c'), fill="black", font=('Helvetica 10'))
        T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
        T_address.tag_configure('tag_name',justify='right')
        T_address.insert('1.0', advdata[2])
        T_address.tag_add('tag_name','1.0', 'end')
        T_address_window = canvas.create_window(850, 80, anchor="nw", window=T_address)
        canvas.create_text(1050, 170, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
        # canvas.create_text(1085, 125, text="Address line 3", fill="black", font=('Helvetica 10'))
        # canvas.create_text(1085, 140, text="Address line 4", fill="black", font=('Helvetica 10'))
        # canvas.create_text(1080, 155, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
        # canvas.create_text(1080, 170, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
        canvas.create_text(1050, 190, text="Invoice", fill="black", font=('Helvetica 14 bold'))
        canvas.create_text(1050, 210, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))

        canvas.create_text(140, 215, text="Bill to", fill="black", font=('Helvetica 10 underline'))
        canvas.create_text(149, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas.create_text(191, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas.create_text(200, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas.create_text(160, 275, text="United States", fill="black", font=('Helvetica 10'))
        canvas.create_text(550, 215, text="Ship to", fill="black", font=('Helvetica 10 underline'))
        canvas.create_text(556, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas.create_text(598, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas.create_text(608, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas.create_text(568, 275, text="United States", fill="black", font=('Helvetica 10'))

        s = ttk.Style()
        s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')
            
        tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_2.Treeview')
          
        tree.column("# 1", anchor=E, stretch=NO, width=150)
        tree.heading("# 1", text="ID/SKU")
        tree.column("# 2", anchor=E, stretch=NO, width=400)
        tree.heading("# 2", text="Product/Service - Description")
        tree.column("# 3", anchor=E, stretch=NO, width=150)
        tree.heading("# 3", text="Quantity")
        tree.column("# 4", anchor=E, stretch=NO, width=150)
        tree.heading("# 4", text="Unit Price")
        tree.column("# 5", anchor=E, stretch=NO, width=150)
        tree.heading("# 5", text="Price")
          
        window = canvas.create_window(120, 290, anchor="nw", window=tree)

        canvas.create_line(120, 330, 1120, 330 )
        canvas.create_line(120, 290, 120, 330 )
        canvas.create_line(270, 290, 270, 330 )
        canvas.create_line(670, 290, 670, 330 )
        canvas.create_line(820, 290, 820, 330 )
        canvas.create_line(970, 290, 970, 330 )
        canvas.create_line(1120, 290, 1120, 330 )
        canvas.create_line(670, 330, 670, 480)
        canvas.create_line(970, 330, 970, 480)
        canvas.create_line(1120, 330, 1120, 480)
        canvas.create_line(670, 355, 1120, 355)
        canvas.create_line(670, 380, 1120, 380)
        canvas.create_line(670, 405, 1120, 405)
        canvas.create_line(670, 430, 1120, 430)
        canvas.create_line(670, 455, 1120, 455)
        canvas.create_line(670, 480, 1120, 480)

        canvas.create_text(165, 320, text="PROD-0001", fill="black", font=('Helvetica 10'))
        canvas.create_text(400, 320, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
        canvas.create_text(740, 320, text="1", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(884, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(884, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        #canvas.create_text(884, 320, text="$200.00", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(1080, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(1080, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        #canvas.create_text(1080, 320, text="$200.00", fill="black", font=('Helvetica 10'))

        canvas.create_text(820, 345, text="Subtotal", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(1080, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(1080, 345, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        #canvas.create_text(1080, 345, text="$200.00", fill="black", font=('Helvetica 10'))

        canvas.create_text(820, 370, text="TAX1", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(1085, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(1085, 370, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        #canvas.create_text(1085, 370, text="$18.00", fill="black", font=('Helvetica 10'))

        canvas.create_text(820, 395, text="Shipping and handling", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(1085, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(1085, 395, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        #canvas.create_text(1085, 395, text="$20.00", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(1080, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(1080, 420, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        #canvas.create_text(1080, 420, text="$238.00", fill="black", font=('Helvetica 10 bold'))
        canvas.create_text(820, 420, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(1080, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(1080, 445, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        #canvas.create_text(1080, 445, text="$100.00", fill="black", font=('Helvetica 10'))
        canvas.create_text(820, 445, text="Total Paid", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(1080, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(1080, 465, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        #canvas.create_text(1080, 465, text="$138.00", fill="black", font=('Helvetica 10'))
        canvas.create_text(820, 465, text="Balance", fill="black", font=('Helvetica 10'))


        canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
        canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

        canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
        canvas.create_line(110, 600, 1120, 600)
        canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
        canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
        canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))

#------------Professional 2 (logo on right side)------------- 

    elif menuvar == 'Professional 2 (logo on right side)':
        frame = Frame(seventhtab, width=1200, height=155)
        frame.pack(expand=True, fill=BOTH)
        frame.place(x=2,y=309)
        canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

        vertibar=Scrollbar(frame, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=canvas.yview)
        canvas.config(width=1200,height=155)

        canvas.config(yscrollcommand=vertibar.set)
        canvas.pack(expand=True,side=LEFT,fill=BOTH)
        canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')
        canvas.create_text(600, 45, text="Title text goes here...", fill="black", font=('Helvetica 10'))

        try:
          adv_image = Image.open("images/"+advdata1[13])
          adv_resize_image = adv_image.resize((200,75))
          adv_image = ImageTk.PhotoImage(adv_resize_image)

          adv_btlogo = Label(canvas,width=200,height=75,image = adv_image) 
          adv_window_image = canvas.create_window(850, 25, anchor="nw", window=adv_btlogo)
          adv_btlogo.photo = adv_image
        except:
          pass  

        # canvas.create_text(1000, 70, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

        canvas.create_text(829, 110, text="Invoice#", fill="black", font=('Helvetica 11'))
        canvas.create_text(841, 130, text="Invoice date", fill="black", font=('Helvetica 11'))
        canvas.create_text(830, 150, text="Due date", fill="black", font=('Helvetica 11'))
        canvas.create_text(820, 170, text="Terms", fill="black", font=('Helvetica 11'))
        canvas.create_text(834, 190, text="Order ref.#", fill="black", font=('Helvetica 11'))
        canvas.create_text(1047, 110, text="INV1/2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(1050, 130, text="06-05-2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(1050, 150, text="21-05-2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(1040, 170, text="NET 15", fill="black", font=('Helvetica 11'))

        canvas.create_text(170, 65, text=""+comname.get(), fill="black", font=('Helvetica 12 '))
        # canvas.create_text(130, 200, text=""+caddent.get('1.0','end-1c'), fill="black", font=('Helvetica 10'))
        T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
        T_address.tag_configure('tag_name',justify='right')
        T_address.insert('1.0', advdata[2])
        T_address.tag_add('tag_name','1.0', 'end')
        T_address_window = canvas.create_window(10, 80, anchor="nw", window=T_address)
        #T_address_window = canvas.create_window(95, 80, anchor="nw", window=T_address)
        canvas.create_text(130, 170, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
        # canvas.create_text(130, 125, text="Address line 3", fill="black", font=('Helvetica 10'))
        # canvas.create_text(130, 140, text="Address line 4", fill="black", font=('Helvetica 10'))
        # canvas.create_text(136, 155, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
        # canvas.create_text(136, 170, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
        canvas.create_text(124, 190, text="Invoice", fill="black", font=('Helvetica 14 bold'))

        canvas.create_text(140, 215, text="Bill to", fill="black", font=('Helvetica 10 underline'))
        canvas.create_text(149, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas.create_text(191, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas.create_text(200, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas.create_text(160, 275, text="United States", fill="black", font=('Helvetica 10'))
        canvas.create_text(550, 215, text="Ship to", fill="black", font=('Helvetica 10 underline'))
        canvas.create_text(556, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas.create_text(598, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas.create_text(608, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas.create_text(568, 275, text="United States", fill="black", font=('Helvetica 10'))

        tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_2.Treeview')
    
        tree.column("# 1", anchor=E, stretch=NO, width=150)
        tree.heading("# 1", text="ID/SKU")
        tree.column("# 2", anchor=E, stretch=NO, width=400)
        tree.heading("# 2", text="Product/Service - Description")
        tree.column("# 3", anchor=E, stretch=NO, width=150)
        tree.heading("# 3", text="Quantity")
        tree.column("# 4", anchor=E, stretch=NO, width=150)
        tree.heading("# 4", text="Unit Price")
        tree.column("# 5", anchor=E, stretch=NO, width=150)
        tree.heading("# 5", text="Price")
    
        window = canvas.create_window(120, 290, anchor="nw", window=tree)

        canvas.create_line(120, 330, 1120, 330 )
        canvas.create_line(120, 290, 120, 330 )
        canvas.create_line(270, 290, 270, 330 )
        canvas.create_line(670, 290, 670, 330 )
        canvas.create_line(820, 290, 820, 330 )
        canvas.create_line(970, 290, 970, 330 )
        canvas.create_line(1120, 290, 1120, 330 )
        canvas.create_line(670, 330, 670, 480)
        canvas.create_line(970, 330, 970, 480)
        canvas.create_line(1120, 330, 1120, 480)
        canvas.create_line(670, 355, 1120, 355)
        canvas.create_line(670, 380, 1120, 380)
        canvas.create_line(670, 405, 1120, 405)
        canvas.create_line(670, 430, 1120, 430)
        canvas.create_line(670, 455, 1120, 455)
        canvas.create_line(670, 480, 1120, 480)

        canvas.create_text(165, 320, text="PROD-0001", fill="black", font=('Helvetica 10'))
        canvas.create_text(400, 320, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
        canvas.create_text(740, 320, text="1", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(884, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(884, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        #canvas.create_text(1080, 320, text="$200.00", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(1080, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(1080, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        #canvas.create_text(1084, 320, text="$200.00", fill="black", font=('Helvetica 10'))

        canvas.create_text(820, 345, text="Subtotal", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(1080, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(1080, 345, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        #canvas.create_text(1084, 345, text="$200.00", fill="black", font=('Helvetica 10'))

        canvas.create_text(820, 370, text="TAX1", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(1085, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(1085, 370, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        #canvas.create_text(1089, 370, text="$18.00", fill="black", font=('Helvetica 10'))

        canvas.create_text(820, 395, text="Shipping and handling", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(1085, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(1085, 395, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        #canvas.create_text(1089, 395, text="$20.00", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(1080, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(1080, 420, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        #canvas.create_text(1084, 420, text="$238.00", fill="black", font=('Helvetica 10 bold'))
        canvas.create_text(820, 420, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(1080, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(1080, 445, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        #canvas.create_text(1084, 445, text="$100.00", fill="black", font=('Helvetica 10'))
        canvas.create_text(820, 445, text="Total Paid", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(1080, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(1080, 465, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        #canvas.create_text(1084, 465, text="$138.00", fill="black", font=('Helvetica 10'))
        canvas.create_text(820, 465, text="Balance", fill="black", font=('Helvetica 10'))

        canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
        canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

        canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
        canvas.create_line(110, 600, 1120, 600)
        canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
        canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
        canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))

#------------Simplified 1 (logo on left side)------------- 

    elif menuvar == 'Simplified 1 (logo on left side)':
        frame = Frame(seventhtab, width=1200, height=155)
        frame.pack(expand=True, fill=BOTH)
        frame.place(x=2,y=309)
        canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

        vertibar=Scrollbar(frame, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=canvas.yview)
        canvas.config(width=1200,height=155)

        canvas.config(yscrollcommand=vertibar.set)
        canvas.pack(expand=True,side=LEFT,fill=BOTH)
        canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')
        canvas.create_text(600, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
        try:
          adv_image = Image.open("images/"+advdata1[13])
          adv_resize_image = adv_image.resize((200,75))
          adv_image = ImageTk.PhotoImage(adv_resize_image)

          adv_btlogo = Label(canvas,width=200,height=75,image = adv_image) 
          adv_window_image = canvas.create_window(150, 25, anchor="nw", window=adv_btlogo)
          adv_btlogo.photo = adv_image
        except:
          pass  
        #canvas.create_text(250, 70, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

        canvas.create_text(130, 120, text="Invoice#", fill="black", font=('Helvetica 11'))
        canvas.create_text(141, 140, text="Invoice date", fill="black", font=('Helvetica 11'))
        canvas.create_text(130, 160, text="Due date", fill="black", font=('Helvetica 11'))
        canvas.create_text(120, 180, text="Terms", fill="black", font=('Helvetica 11'))
        canvas.create_text(134, 200, text="Order ref.#", fill="black", font=('Helvetica 11'))
        canvas.create_text(347, 120, text="INV1/2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(350, 140, text="06-05-2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(350, 160, text="21-05-2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(340, 180, text="NET 15", fill="black", font=('Helvetica 11'))

        canvas.create_text(1050, 65, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
        # canvas.create_text(1080, 200, text=""+caddent.get('1.0','end-1c'), fill="black", font=('Helvetica 10'))
        T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
        T_address.tag_configure('tag_name',justify='right')
        T_address.insert('1.0', advdata[2])
        T_address.tag_add('tag_name','1.0', 'end')
        T_address_window = canvas.create_window(850, 80, anchor="nw", window=T_address)
        canvas.create_text(1050, 170, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
        # canvas.create_text(1085, 125, text="Address line 3", fill="black", font=('Helvetica 10'))
        # canvas.create_text(1085, 140, text="Address line 4", fill="black", font=('Helvetica 10'))
        # canvas.create_text(1080, 155, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
        # canvas.create_text(1080, 170, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
        canvas.create_text(1050, 190, text="Invoice", fill="black", font=('Helvetica 14 bold'))

        canvas.create_text(140, 215, text="Bill to", fill="black", font=('Helvetica 10 underline'))
        canvas.create_text(149, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas.create_text(191, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas.create_text(200, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas.create_text(160, 275, text="United States", fill="black", font=('Helvetica 10'))
        canvas.create_text(550, 215, text="Ship to", fill="black", font=('Helvetica 10 underline'))
        canvas.create_text(556, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas.create_text(598, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas.create_text(608, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas.create_text(568, 275, text="United States", fill="black", font=('Helvetica 10'))

        s = ttk.Style()
        s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')

        tree=ttk.Treeview(canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle_2.Treeview')
    
        tree.column("# 1", anchor=E, stretch=NO, width=700)
        tree.heading("# 1", text="Product/Service - Description")
        tree.column("# 2", anchor=E, stretch=NO, width=150)
        tree.heading("# 2", text="Quantity")
        tree.column("# 3", anchor=E, stretch=NO, width=150)
        tree.heading("# 3", text="Price")
          
        window = canvas.create_window(120, 290, anchor="nw", window=tree)

        canvas.create_line(120, 330, 1120, 330 )
        canvas.create_line(120, 290, 120, 330 )
        canvas.create_line(820, 290, 820, 330 )
        canvas.create_line(970, 290, 970, 330 )
        canvas.create_line(1120, 290, 1120, 330 )
        canvas.create_line(670, 330, 670, 480)
        canvas.create_line(970, 330, 970, 480)
        canvas.create_line(1120, 330, 1120, 480)
        canvas.create_line(670, 355, 1120, 355)
        canvas.create_line(670, 380, 1120, 380)
        canvas.create_line(670, 405, 1120, 405)
        canvas.create_line(670, 430, 1120, 430)
        canvas.create_line(670, 455, 1120, 455)
        canvas.create_line(670, 480, 1120, 480)

        canvas.create_text(250, 320, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
        canvas.create_text(900, 320, text="1", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(1080, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(1080, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        #canvas.create_text(1084, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(820, 345, text="Subtotal", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(1080, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(1080, 345, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        #canvas.create_text(1084, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(820, 370, text="TAX1", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(1085, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(1085, 370, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        #canvas.create_text(1089, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(820, 395, text="Shipping and handling", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(1085, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(1085, 395, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        #canvas.create_text(1089, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(1080, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(1080, 420, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        #canvas.create_text(1084, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
        canvas.create_text(820, 420, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(1080, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(1080, 445, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        #canvas.create_text(1084, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        canvas.create_text(820, 445, text="Total Paid", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(1080, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(1080, 465, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        #canvas.create_text(1084, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        canvas.create_text(820, 465, text="Balance", fill="black", font=('Helvetica 10'))

        canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
        canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

        canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
        canvas.create_line(110, 600, 1120, 600)
        canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
        canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
        canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))


#------------Simplified 2 (logo on right side)-------------

    elif menuvar == 'Simplified 2 (logo on right side)':
        frame = Frame(seventhtab, width=1200, height=155)
        frame.pack(expand=True, fill=BOTH)
        frame.place(x=2,y=309)
        canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

        vertibar=Scrollbar(frame, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=canvas.yview)
        canvas.config(width=1200,height=155)

        canvas.config(yscrollcommand=vertibar.set)
        canvas.pack(expand=True,side=LEFT,fill=BOTH)
        canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')
        canvas.create_text(600, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
        try:
          adv_image = Image.open("images/"+advdata1[13])
          adv_resize_image = adv_image.resize((200,75))
          adv_image = ImageTk.PhotoImage(adv_resize_image)

          adv_btlogo = Label(canvas,width=200,height=75,image = adv_image) 
          adv_window_image = canvas.create_window(850, 25, anchor="nw", window=adv_btlogo)
          adv_btlogo.photo = adv_image
        except:
          pass  

        # canvas.create_text(1000, 70, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

        canvas.create_text(829, 120, text="Invoice#", fill="black", font=('Helvetica 11'))
        canvas.create_text(841, 140, text="Invoice date", fill="black", font=('Helvetica 11'))
        canvas.create_text(830, 160, text="Due date", fill="black", font=('Helvetica 11'))
        canvas.create_text(820, 180, text="Terms", fill="black", font=('Helvetica 11'))
        canvas.create_text(834, 200, text="Order ref.#", fill="black", font=('Helvetica 11'))
        canvas.create_text(1047, 120, text="INV1/2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(1050, 140, text="06-05-2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(1050, 160, text="21-05-2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(1040, 180, text="NET 15", fill="black", font=('Helvetica 11'))

        canvas.create_text(170, 65, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
        # canvas.create_text(130, 200, text=""+caddent.get('1.0','end-1c'), fill="black", font=('Helvetica 10'))
        T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
        T_address.tag_configure('tag_name',justify='right')
        T_address.insert('1.0', advdata[2])
        T_address.tag_add('tag_name','1.0', 'end')
        T_address_window = canvas.create_window(10, 80, anchor="nw", window=T_address)
        canvas.create_text(130, 170, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
        # canvas.create_text(130, 125, text="Address line 3", fill="black", font=('Helvetica 10'))
        # canvas.create_text(130, 140, text="Address line 4", fill="black", font=('Helvetica 10'))
        # canvas.create_text(136, 155, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
        # canvas.create_text(136, 170, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
        canvas.create_text(124, 190, text="Invoice", fill="black", font=('Helvetica 14 bold'))

        canvas.create_text(140, 215, text="Bill to", fill="black", font=('Helvetica 10 underline'))
        canvas.create_text(149, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas.create_text(191, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas.create_text(200, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas.create_text(160, 275, text="United States", fill="black", font=('Helvetica 10'))
        canvas.create_text(550, 215, text="Ship to", fill="black", font=('Helvetica 10 underline'))
        canvas.create_text(556, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas.create_text(598, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas.create_text(608, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas.create_text(568, 275, text="United States", fill="black", font=('Helvetica 10'))

        s = ttk.Style()
        s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')

        tree=ttk.Treeview(canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle_2.Treeview')
            
        tree.column("# 1", anchor=E, stretch=NO, width=700)
        tree.heading("# 1", text="Product/Service - Description")
        tree.column("# 2", anchor=E, stretch=NO, width=150)
        tree.heading("# 2", text="Quantity")
        tree.column("# 3", anchor=E, stretch=NO, width=150)
        tree.heading("# 3", text="Price")
      
        window = canvas.create_window(120, 290, anchor="nw", window=tree)

        canvas.create_line(120, 330, 1120, 330 )
        canvas.create_line(120, 290, 120, 330 )
        canvas.create_line(820, 290, 820, 330 )
        canvas.create_line(970, 290, 970, 330 )
        canvas.create_line(1120, 290, 1120, 330 )
        canvas.create_line(670, 330, 670, 480)
        canvas.create_line(970, 330, 970, 480)
        canvas.create_line(1120, 330, 1120, 480)
        canvas.create_line(670, 355, 1120, 355)
        canvas.create_line(670, 380, 1120, 380)
        canvas.create_line(670, 405, 1120, 405)
        canvas.create_line(670, 430, 1120, 430)
        canvas.create_line(670, 455, 1120, 455)
        canvas.create_line(670, 480, 1120, 480)

        canvas.create_text(250, 320, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
        canvas.create_text(900, 320, text="1", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(1080, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(1080, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        #canvas.create_text(1084, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(820, 345, text="Subtotal", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(1080, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(1080, 345, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        #canvas.create_text(1084, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(820, 370, text="TAX1", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(1085, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(1085, 370, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        #canvas.create_text(1089, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

        canvas.create_text(820, 395, text="Shipping and handling", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(1085, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(1085, 395, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        #canvas.create_text(1089, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(1080, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(1080, 420, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        #canvas.create_text(1084, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
        canvas.create_text(820, 420, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(1080, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(1080, 445, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        #canvas.create_text(1084, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        canvas.create_text(820, 445, text="Total Paid", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(1080, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(1080, 465, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        #canvas.create_text(1084, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        canvas.create_text(820, 465, text="Balance", fill="black", font=('Helvetica 10'))

        canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
        canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

        canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
        canvas.create_line(110, 600, 1120, 600)
        canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
        canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
        canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))

#------------Business Classic------------- 

    elif menuvar == 'Business Classic':
        frame = Frame(seventhtab, width=1200, height=155)
        frame.pack(expand=True, fill=BOTH)
        frame.place(x=2,y=309)
        canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

        vertibar=Scrollbar(frame, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=canvas.yview)
        canvas.config(width=1200,height=155)

        canvas.config(yscrollcommand=vertibar.set)
        canvas.pack(expand=True,side=LEFT,fill=BOTH)
        canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')
        canvas.create_text(600, 45, text="Title text goes here...", fill="black", font=('Helvetica 10'))
        canvas.create_line(100, 60, 1120, 60, fill="orange")
        #canvas.create_line(1000, 60, 600, 60, fill="grey")

        try:
          adv_image = Image.open("images/"+advdata1[13])
          adv_resize_image = adv_image.resize((200,100))
          adv_image = ImageTk.PhotoImage(adv_resize_image)

          adv_btlogo = Label(canvas,width=200,height=100,image = adv_image) 
          adv_window_image = canvas.create_window(140, 100, anchor="nw", window=adv_btlogo)
          adv_btlogo.photo = adv_image
        except:
          pass  


        # canvas.create_text(250, 155, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

        canvas.create_text(560, 85, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
        # canvas.create_text(535, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
        T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
        T_address.tag_configure('tag_name',justify='right')
        T_address.insert('1.0', advdata[2])
        T_address.tag_add('tag_name','1.0', 'end')
        T_address_window = canvas.create_window(350, 100, anchor="nw", window=T_address)
        # adv_btlabel = Label(canvas,width=20,height=10,text=""+caddent.get('1.0', 'end-1c')) 
        # adv_window_label = canvas.create_window(530, 110, anchor="nw", window=adv_btlabel)
        canvas.create_text(530, 190, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
        # canvas.create_text(530, 140, text="Address line 3", fill="black", font=('Helvetica 10'))
        # canvas.create_text(530, 155, text="Address line 4", fill="black", font=('Helvetica 10'))
        # canvas.create_text(536, 170, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
        # canvas.create_text(536, 190, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
        canvas.create_text(524, 210, text="Invoice", fill="black", font=('Helvetica 14 bold'))

        canvas.create_text(749, 95, text="John Doe", fill="black", font=('Helvetica 10 '))
        canvas.create_text(791, 110, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
        canvas.create_text(800, 125, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
        canvas.create_text(760, 140, text="United States", fill="black", font=('Helvetica 10'))

        canvas.create_text(745, 160, text="Invoice", fill="black", font=('Helvetica 11'))
        canvas.create_text(760, 180, text="Invoice date", fill="black", font=('Helvetica 11'))
        canvas.create_text(750, 200, text="Due date", fill="black", font=('Helvetica 11'))

        canvas.create_text(947, 160, text="INV1/2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(950, 180, text="06-05-2022", fill="black", font=('Helvetica 11'))
        canvas.create_text(950, 200, text="21-05-2022", fill="black", font=('Helvetica 11'))
        s = ttk.Style()
        s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')

        tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_2.Treeview')
      
        tree.column("# 1", anchor=E, stretch=NO, width=150)
        tree.heading("# 1", text="Product/Service")
        tree.column("# 2", anchor=E, stretch=NO, width=400)
        tree.heading("# 2", text="Description")
        tree.column("# 3", anchor=E, stretch=NO, width=150)
        tree.heading("# 3", text="Unit Price")
        tree.column("# 4", anchor=E, stretch=NO, width=150)
        tree.heading("# 4", text="Quantity")
        tree.column("# 5", anchor=E, stretch=NO, width=150)
        tree.heading("# 5", text="Price")
            
        window = canvas.create_window(120, 230, anchor="nw", window=tree)

        canvas.create_line(120, 270, 1120, 270 )
        canvas.create_line(120, 230, 120, 270 )
        canvas.create_line(270, 230, 270, 270 )
        canvas.create_line(670, 230, 670, 270 )
        canvas.create_line(820, 230, 820, 270 )
        canvas.create_line(970, 230, 970, 270 )
        canvas.create_line(1120, 230, 1120, 270)
        canvas.create_line(1120, 270, 1120, 420)
        canvas.create_line(670, 295, 1120, 295)
        canvas.create_line(670, 320, 1120, 320)
        canvas.create_line(670, 345, 1120, 345)
        canvas.create_line(670, 370, 1120, 370)
        canvas.create_line(670, 395, 1120, 395)
        canvas.create_line(670, 420, 1120, 420)

        canvas.create_text(165, 260, text="PROD-0001", fill="black", font=('Helvetica 10'))
        canvas.create_text(400, 260, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(734, 260, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(734, 260, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(734, 260, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(734, 260, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        #canvas.create_text(734, 260, text="$200.00", fill="black", font=('Helvetica 10'))
        canvas.create_text(890, 260, text="1", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(1080, 260, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(1080, 260, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(1080, 260, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(1080, 260, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        # canvas.create_text(1080, 260, text="$200.00", fill="black", font=('Helvetica 10'))

        canvas.create_text(697, 285, text="Subtotal", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(1080, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(1080, 285, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(1080, 285, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(1080, 285, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        #canvas.create_text(1080, 285, text="$200.00", fill="black", font=('Helvetica 10'))

        canvas.create_text(692, 310, text="TAX1", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(1085, 310, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(1085, 310, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(1085, 310, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(1085, 310, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        #canvas.create_text(1085, 310, text="$18.00", fill="black", font=('Helvetica 10'))

        canvas.create_text(737, 335, text="Shipping and handling", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(1085, 335, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(1085, 335, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(1085, 335, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(1085, 335, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        #canvas.create_text(1085, 335, text="$20.00", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(1080, 360, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(1080, 360, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(1080, 360, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(1080, 360, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        #canvas.create_text(1080, 360, text="$238.00", fill="black", font=('Helvetica 10 bold'))
        canvas.create_text(715, 360, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(1080, 385, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(1080, 385, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(1080, 385, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(1080, 385, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        #canvas.create_text(1080, 385, text="100.00", fill="black", font=('Helvetica 10'))
        canvas.create_text(705, 385, text="Total Paid", fill="black", font=('Helvetica 10'))
        if comcursignpla.get() == "before amount":
          canvas.create_text(1080, 410, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount":
          canvas.create_text(1080, 410, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "before amount with space":
          canvas.create_text(1080, 410, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
        elif comcursignpla.get() == "after amount with space":
          canvas.create_text(1080, 410, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
        else:
          pass
        #canvas.create_text(1080, 410, text="$138.00", fill="black", font=('Helvetica 10'))
        canvas.create_text(700, 410, text="Balance", fill="black", font=('Helvetica 10'))

        canvas.create_line(100, 480, 1120, 480, fill="orange")
        canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
        canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
        canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

        canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
        canvas.create_line(100, 600, 1120, 600, fill="orange")
        canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
        canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
        canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
    else:
        pass

adv_win_menu8 = StringVar()
adv_winstyle8 = ttk.Combobox(seventhtab,textvariable=adv_win_menu8)
adv_winstyle8.bind("<<ComboboxSelected>>", adv_maindropmenu)
adv_winstyle8["values"] = ("Professional 1 (logo on left side)","Professional 2 (logo on right side)","Simplified 1 (logo on left side)","Simplified 2 (logo on right side)","Business Classic")
if not advdata:
  adv_winstyle8.current(0)
  frame = Frame(seventhtab, width=1200, height=155)
  frame.pack(expand=True, fill=BOTH)
  frame.place(x=2,y=309)
  canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

  vertibar=Scrollbar(frame, orient=VERTICAL)
  vertibar.pack(side=RIGHT,fill=Y)
  vertibar.config(command=canvas.yview)
  canvas.config(width=1200,height=155)

  canvas.config(yscrollcommand=vertibar.set)
  canvas.pack(expand=True,side=LEFT,fill=BOTH)
  canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')

  canvas.create_text(600, 45, text="Title text goes here...", fill="black", font=('Helvetica 10'))

  canvas.create_text(250, 70, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

  canvas.create_text(130, 120, text="Invoice#", fill="black", font=('Helvetica 11'))
  canvas.create_text(141, 140, text="Invoice date", fill="black", font=('Helvetica 11'))
  canvas.create_text(130, 160, text="Due date", fill="black", font=('Helvetica 11'))
  canvas.create_text(120, 180, text="Terms", fill="black", font=('Helvetica 11'))
  canvas.create_text(134, 200, text="Order ref.#", fill="black", font=('Helvetica 11'))
  canvas.create_text(347, 120, text="INV1/2022", fill="black", font=('Helvetica 11'))
  canvas.create_text(350, 140, text="03-05-2022", fill="black", font=('Helvetica 11'))
  canvas.create_text(350, 160, text="18-05-2022", fill="black", font=('Helvetica 11'))
  canvas.create_text(340, 180, text="NET 15", fill="black", font=('Helvetica 11'))

  canvas.create_text(1050, 65, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
  # canvas.create_text(1080, 200, text=""+caddent.get('1.0','end-1c'), fill="black", font=('Helvetica 10'))
  # T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
  # T_address.tag_configure('tag_name',justify='right')
  # T_address.insert('1.0', advdata[2])
  # T_address.tag_add('tag_name','1.0', 'end')
  # T_address_window = canvas.create_window(850, 80, anchor="nw", window=T_address)
  canvas.create_text(1050, 170, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
  # canvas.create_text(1085, 125, text="Address line 3", fill="black", font=('Helvetica 10'))
  # canvas.create_text(1085, 140, text="Address line 4", fill="black", font=('Helvetica 10'))
  # canvas.create_text(1080, 155, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
  # canvas.create_text(1080, 170, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
  canvas.create_text(1050, 190, text="Invoice", fill="black", font=('Helvetica 14 bold'))
  canvas.create_text(1050, 210, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))

  canvas.create_text(140, 215, text="Bill to", fill="black", font=('Helvetica 10 underline'))
  canvas.create_text(149, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
  canvas.create_text(191, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
  canvas.create_text(200, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
  canvas.create_text(160, 275, text="United States", fill="black", font=('Helvetica 10'))
  canvas.create_text(550, 215, text="Ship to", fill="black", font=('Helvetica 10 underline'))
  canvas.create_text(556, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
  canvas.create_text(598, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
  canvas.create_text(608, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
  canvas.create_text(568, 275, text="United States", fill="black", font=('Helvetica 10'))

  s = ttk.Style()
  s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')
      
  tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_2.Treeview')
    
  tree.column("# 1", anchor=E, stretch=NO, width=150)
  tree.heading("# 1", text="ID/SKU")
  tree.column("# 2", anchor=E, stretch=NO, width=400)
  tree.heading("# 2", text="Product/Service - Description")
  tree.column("# 3", anchor=E, stretch=NO, width=150)
  tree.heading("# 3", text="Quantity")
  tree.column("# 4", anchor=E, stretch=NO, width=150)
  tree.heading("# 4", text="Unit Price")
  tree.column("# 5", anchor=E, stretch=NO, width=150)
  tree.heading("# 5", text="Price")
    
  window = canvas.create_window(120, 290, anchor="nw", window=tree)

  canvas.create_line(120, 330, 1120, 330 )
  canvas.create_line(120, 290, 120, 330 )
  canvas.create_line(270, 290, 270, 330 )
  canvas.create_line(670, 290, 670, 330 )
  canvas.create_line(820, 290, 820, 330 )
  canvas.create_line(970, 290, 970, 330 )
  canvas.create_line(1120, 290, 1120, 330 )
  canvas.create_line(670, 330, 670, 480)
  canvas.create_line(970, 330, 970, 480)
  canvas.create_line(1120, 330, 1120, 480)
  canvas.create_line(670, 355, 1120, 355)
  canvas.create_line(670, 380, 1120, 380)
  canvas.create_line(670, 405, 1120, 405)
  canvas.create_line(670, 430, 1120, 430)
  canvas.create_line(670, 455, 1120, 455)
  canvas.create_line(670, 480, 1120, 480)

  canvas.create_text(165, 320, text="PROD-0001", fill="black", font=('Helvetica 10'))
  canvas.create_text(400, 320, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
  canvas.create_text(740, 320, text="1", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(884, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(884, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  #canvas.create_text(884, 320, text="$200.00", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(1080, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(1080, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  #canvas.create_text(1080, 320, text="$200.00", fill="black", font=('Helvetica 10'))

  canvas.create_text(820, 345, text="Subtotal", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(1080, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(1080, 345, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  #canvas.create_text(1080, 345, text="$200.00", fill="black", font=('Helvetica 10'))

  canvas.create_text(820, 370, text="TAX1", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(1085, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(1085, 370, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  #canvas.create_text(1085, 370, text="$18.00", fill="black", font=('Helvetica 10'))

  canvas.create_text(820, 395, text="Shipping and handling", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(1085, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(1085, 395, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  #canvas.create_text(1085, 395, text="$20.00", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(1080, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(1080, 420, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  #canvas.create_text(1080, 420, text="$238.00", fill="black", font=('Helvetica 10 bold'))
  canvas.create_text(820, 420, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(1080, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(1080, 445, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  #canvas.create_text(1080, 445, text="$100.00", fill="black", font=('Helvetica 10'))
  canvas.create_text(820, 445, text="Total Paid", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(1080, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(1080, 465, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  #canvas.create_text(1080, 465, text="$138.00", fill="black", font=('Helvetica 10'))
  canvas.create_text(820, 465, text="Balance", fill="black", font=('Helvetica 10'))


  canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
  canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
  canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
  canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

  canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
  canvas.create_line(110, 600, 1120, 600)
  canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
  canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
  canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
elif advdata[32] == 'Professional 1 (logo on left side)':
  adv_winstyle8.insert(0, advdata[40])
  frame = Frame(seventhtab, width=1200, height=155)
  frame.pack(expand=True, fill=BOTH)
  frame.place(x=2,y=309)
  canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

  vertibar=Scrollbar(frame, orient=VERTICAL)
  vertibar.pack(side=RIGHT,fill=Y)
  vertibar.config(command=canvas.yview)
  canvas.config(width=1200,height=155)

  canvas.config(yscrollcommand=vertibar.set)
  canvas.pack(expand=True,side=LEFT,fill=BOTH)
  canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')

  canvas.create_text(600, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))

  try:
    adv_image = Image.open("images/"+advdata[13])
    adv_resize_image = adv_image.resize((200,75))
    adv_image = ImageTk.PhotoImage(adv_resize_image)

    adv_btlogo = Label(canvas,width=200,height=75,image = adv_image) 
    adv_window_image = canvas.create_window(150, 30, anchor="nw", window=adv_btlogo)
    adv_btlogo.photo = adv_image
  except:
    pass  

  canvas.create_text(130, 120, text="Invoice#", fill="black", font=('Helvetica 11'))
  canvas.create_text(141, 140, text="Invoice date", fill="black", font=('Helvetica 11'))
  canvas.create_text(130, 160, text="Due date", fill="black", font=('Helvetica 11'))
  canvas.create_text(120, 180, text="Terms", fill="black", font=('Helvetica 11'))
  canvas.create_text(134, 200, text="Order ref.#", fill="black", font=('Helvetica 11'))
  canvas.create_text(347, 120, text="INV1/2022", fill="black", font=('Helvetica 11'))
  canvas.create_text(350, 140, text="03-05-2022", fill="black", font=('Helvetica 11'))
  canvas.create_text(350, 160, text="18-05-2022", fill="black", font=('Helvetica 11'))
  canvas.create_text(340, 180, text="NET 15", fill="black", font=('Helvetica 11'))

  canvas.create_text(1050, 65, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
  # canvas.create_text(1080, 200, text=""+caddent.get('1.0','end-1c'), fill="black", font=('Helvetica 10'))
  T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
  T_address.tag_configure('tag_name',justify='right')
  T_address.insert('1.0', advdata[2])
  T_address.tag_add('tag_name','1.0', 'end')
  T_address_window = canvas.create_window(850, 80, anchor="nw", window=T_address)
      
  canvas.create_text(1050, 170, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
  # canvas.create_text(1085, 125, text="Address line 3", fill="black", font=('Helvetica 10'))
  # canvas.create_text(1085, 140, text="Address line 4", fill="black", font=('Helvetica 10'))
  # canvas.create_text(1080, 155, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
  # canvas.create_text(1080, 170, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
  canvas.create_text(1050, 190, text="Invoice", fill="black", font=('Helvetica 14 bold'))
  canvas.create_text(1050, 210, text="TAX EXEMPTED", fill="black", font=('Helvetica 10'))

  canvas.create_text(140, 215, text="Bill to", fill="black", font=('Helvetica 10 underline'))
  canvas.create_text(149, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
  canvas.create_text(191, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
  canvas.create_text(200, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
  canvas.create_text(160, 275, text="United States", fill="black", font=('Helvetica 10'))
  canvas.create_text(550, 215, text="Ship to", fill="black", font=('Helvetica 10 underline'))
  canvas.create_text(556, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
  canvas.create_text(598, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
  canvas.create_text(608, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
  canvas.create_text(568, 275, text="United States", fill="black", font=('Helvetica 10'))

  s = ttk.Style()
  s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')
      
  tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_2.Treeview')
    
  tree.column("# 1", anchor=E, stretch=NO, width=150)
  tree.heading("# 1", text="ID/SKU")
  tree.column("# 2", anchor=E, stretch=NO, width=400)
  tree.heading("# 2", text="Product/Service - Description")
  tree.column("# 3", anchor=E, stretch=NO, width=150)
  tree.heading("# 3", text="Quantity")
  tree.column("# 4", anchor=E, stretch=NO, width=150)
  tree.heading("# 4", text="Unit Price")
  tree.column("# 5", anchor=E, stretch=NO, width=150)
  tree.heading("# 5", text="Price")
    
  window = canvas.create_window(120, 290, anchor="nw", window=tree)

  canvas.create_line(120, 330, 1120, 330 )
  canvas.create_line(120, 290, 120, 330 )
  canvas.create_line(270, 290, 270, 330 )
  canvas.create_line(670, 290, 670, 330 )
  canvas.create_line(820, 290, 820, 330 )
  canvas.create_line(970, 290, 970, 330 )
  canvas.create_line(1120, 290, 1120, 330 )
  canvas.create_line(670, 330, 670, 480)
  canvas.create_line(970, 330, 970, 480)
  canvas.create_line(1120, 330, 1120, 480)
  canvas.create_line(670, 355, 1120, 355)
  canvas.create_line(670, 380, 1120, 380)
  canvas.create_line(670, 405, 1120, 405)
  canvas.create_line(670, 430, 1120, 430)
  canvas.create_line(670, 455, 1120, 455)
  canvas.create_line(670, 480, 1120, 480)

  canvas.create_text(165, 320, text="PROD-0001", fill="black", font=('Helvetica 10'))
  canvas.create_text(400, 320, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
  canvas.create_text(740, 320, text="1", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(884, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(884, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  #canvas.create_text(884, 320, text="$200.00", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(1080, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(1080, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  #canvas.create_text(1080, 320, text="$200.00", fill="black", font=('Helvetica 10'))

  canvas.create_text(820, 345, text="Subtotal", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(1080, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(1080, 345, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  #canvas.create_text(1080, 345, text="$200.00", fill="black", font=('Helvetica 10'))

  canvas.create_text(820, 370, text="TAX1", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(1085, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(1085, 370, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  #canvas.create_text(1085, 370, text="$18.00", fill="black", font=('Helvetica 10'))

  canvas.create_text(820, 395, text="Shipping and handling", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(1085, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(1085, 395, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  #canvas.create_text(1085, 395, text="$20.00", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(1080, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(1080, 420, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  #canvas.create_text(1080, 420, text="$238.00", fill="black", font=('Helvetica 10 bold'))
  canvas.create_text(820, 420, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(1080, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(1080, 445, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  #canvas.create_text(1080, 445, text="$100.00", fill="black", font=('Helvetica 10'))
  canvas.create_text(820, 445, text="Total Paid", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(1080, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(1080, 465, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  #canvas.create_text(1080, 465, text="$138.00", fill="black", font=('Helvetica 10'))
  canvas.create_text(820, 465, text="Balance", fill="black", font=('Helvetica 10'))


  canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
  canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
  canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
  canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

  canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
  canvas.create_line(110, 600, 1120, 600)
  canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
  canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
  canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
elif advdata[32] == 'Professional 2 (logo on right side)':
  adv_winstyle8.insert(0, advdata[40])
  frame = Frame(seventhtab, width=1200, height=155)
  frame.pack(expand=True, fill=BOTH)
  frame.place(x=2,y=309)
  canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

  vertibar=Scrollbar(frame, orient=VERTICAL)
  vertibar.pack(side=RIGHT,fill=Y)
  vertibar.config(command=canvas.yview)
  canvas.config(width=1200,height=155)

  canvas.config(yscrollcommand=vertibar.set)
  canvas.pack(expand=True,side=LEFT,fill=BOTH)
  canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')
  canvas.create_text(600, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
  try:
    adv_image = Image.open("images/"+advdata[13])
    adv_resize_image = adv_image.resize((200,75))
    adv_image = ImageTk.PhotoImage(adv_resize_image)

    adv_btlogo = Label(canvas,width=200,height=75,image = adv_image) 
    adv_window_image = canvas.create_window(850, 25, anchor="nw", window=adv_btlogo)
    adv_btlogo.photo = adv_image
  except:
    pass  
  #canvas.create_text(1000, 70, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

  canvas.create_text(829, 110, text="Invoice#", fill="black", font=('Helvetica 11'))
  canvas.create_text(841, 130, text="Invoice date", fill="black", font=('Helvetica 11'))
  canvas.create_text(830, 150, text="Due date", fill="black", font=('Helvetica 11'))
  canvas.create_text(820, 170, text="Terms", fill="black", font=('Helvetica 11'))
  canvas.create_text(834, 190, text="Order ref.#", fill="black", font=('Helvetica 11'))
  canvas.create_text(1047, 110, text="INV1/2022", fill="black", font=('Helvetica 11'))
  canvas.create_text(1050, 130, text="06-05-2022", fill="black", font=('Helvetica 11'))
  canvas.create_text(1050, 150, text="21-05-2022", fill="black", font=('Helvetica 11'))
  canvas.create_text(1040, 170, text="NET 15", fill="black", font=('Helvetica 11'))

  canvas.create_text(170, 65, text=""+comname.get(), fill="black", font=('Helvetica 12 '))
  # canvas.create_text(130, 200, text=""+caddent.get('1.0','end-1c'), fill="black", font=('Helvetica 10'))
  T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
  T_address.tag_configure('tag_name',justify='right')
  T_address.insert('1.0', advdata[2])
  T_address.tag_add('tag_name','1.0', 'end')
  T_address_window = canvas.create_window(10, 80, anchor="nw", window=T_address)
  canvas.create_text(125, 170, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
  # canvas.create_text(130, 125, text="Address line 3", fill="black", font=('Helvetica 10'))
  # canvas.create_text(130, 140, text="Address line 4", fill="black", font=('Helvetica 10'))
  # canvas.create_text(136, 155, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
  # canvas.create_text(136, 170, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
  canvas.create_text(124, 190, text="Invoice", fill="black", font=('Helvetica 14 bold'))

  canvas.create_text(140, 215, text="Bill to", fill="black", font=('Helvetica 10 underline'))
  canvas.create_text(149, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
  canvas.create_text(191, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
  canvas.create_text(200, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
  canvas.create_text(160, 275, text="United States", fill="black", font=('Helvetica 10'))
  canvas.create_text(550, 215, text="Ship to", fill="black", font=('Helvetica 10 underline'))
  canvas.create_text(556, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
  canvas.create_text(598, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
  canvas.create_text(608, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
  canvas.create_text(568, 275, text="United States", fill="black", font=('Helvetica 10'))
  
  s = ttk.Style()
  s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')

  tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_2.Treeview')
    
  tree.column("# 1", anchor=E, stretch=NO, width=150)
  tree.heading("# 1", text="ID/SKU")
  tree.column("# 2", anchor=E, stretch=NO, width=400)
  tree.heading("# 2", text="Product/Service - Description")
  tree.column("# 3", anchor=E, stretch=NO, width=150)
  tree.heading("# 3", text="Quantity")
  tree.column("# 4", anchor=E, stretch=NO, width=150)
  tree.heading("# 4", text="Unit Price")
  tree.column("# 5", anchor=E, stretch=NO, width=150)
  tree.heading("# 5", text="Price")
    
  window = canvas.create_window(120, 290, anchor="nw", window=tree)

  canvas.create_line(120, 330, 1120, 330 )
  canvas.create_line(120, 290, 120, 330 )
  canvas.create_line(270, 290, 270, 330 )
  canvas.create_line(670, 290, 670, 330 )
  canvas.create_line(820, 290, 820, 330 )
  canvas.create_line(970, 290, 970, 330 )
  canvas.create_line(1120, 290, 1120, 330 )
  canvas.create_line(670, 330, 670, 480)
  canvas.create_line(970, 330, 970, 480)
  canvas.create_line(1120, 330, 1120, 480)
  canvas.create_line(670, 355, 1120, 355)
  canvas.create_line(670, 380, 1120, 380)
  canvas.create_line(670, 405, 1120, 405)
  canvas.create_line(670, 430, 1120, 430)
  canvas.create_line(670, 455, 1120, 455)
  canvas.create_line(670, 480, 1120, 480)

  canvas.create_text(165, 320, text="PROD-0001", fill="black", font=('Helvetica 10'))
  canvas.create_text(400, 320, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
  canvas.create_text(740, 320, text="1", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(884, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(884, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(884, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  #canvas.create_text(1080, 320, text="$200.00", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(1080, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(1080, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  #canvas.create_text(1084, 320, text="$200.00", fill="black", font=('Helvetica 10'))

  canvas.create_text(820, 345, text="Subtotal", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(1080, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(1080, 345, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  #canvas.create_text(1084, 345, text="$200.00", fill="black", font=('Helvetica 10'))

  canvas.create_text(820, 370, text="TAX1", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(1085, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(1085, 370, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  #canvas.create_text(1089, 370, text="$18.00", fill="black", font=('Helvetica 10'))

  canvas.create_text(820, 395, text="Shipping and handling", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(1085, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(1085, 395, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  #canvas.create_text(1089, 395, text="$20.00", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(1080, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(1080, 420, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  #canvas.create_text(1084, 420, text="$238.00", fill="black", font=('Helvetica 10 bold'))
  canvas.create_text(820, 420, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(1080, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(1080, 445, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  #canvas.create_text(1084, 445, text="$100.00", fill="black", font=('Helvetica 10'))
  canvas.create_text(820, 445, text="Total Paid", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(1080, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(1080, 465, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  #canvas.create_text(1084, 465, text="$138.00", fill="black", font=('Helvetica 10'))
  canvas.create_text(820, 465, text="Balance", fill="black", font=('Helvetica 10'))

  canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
  canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
  canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
  canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

  canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
  canvas.create_line(110, 600, 1120, 600)
  canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
  canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
  canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))


elif advdata[32] == 'Simplified 1 (logo on left side)':
  adv_winstyle8.insert(0, advdata[40])
  frame = Frame(seventhtab, width=1200, height=155)
  frame.pack(expand=True, fill=BOTH)
  frame.place(x=2,y=309)
  canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

  vertibar=Scrollbar(frame, orient=VERTICAL)
  vertibar.pack(side=RIGHT,fill=Y)
  vertibar.config(command=canvas.yview)
  canvas.config(width=1200,height=155)

  canvas.config(yscrollcommand=vertibar.set)
  canvas.pack(expand=True,side=LEFT,fill=BOTH)
  canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')
  canvas.create_text(600, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
  try:
    adv_image = Image.open("images/"+advdata[13])
    adv_resize_image = adv_image.resize((200,75))
    adv_image = ImageTk.PhotoImage(adv_resize_image)

    adv_btlogo = Label(canvas,width=200,height=75,image = adv_image) 
    adv_window_image = canvas.create_window(150, 25, anchor="nw", window=adv_btlogo)
    adv_btlogo.photo = adv_image
  except:
    pass  
  #canvas.create_text(250, 70, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

  canvas.create_text(130, 120, text="Invoice#", fill="black", font=('Helvetica 11'))
  canvas.create_text(141, 140, text="Invoice date", fill="black", font=('Helvetica 11'))
  canvas.create_text(130, 160, text="Due date", fill="black", font=('Helvetica 11'))
  canvas.create_text(120, 180, text="Terms", fill="black", font=('Helvetica 11'))
  canvas.create_text(134, 200, text="Order ref.#", fill="black", font=('Helvetica 11'))
  canvas.create_text(347, 120, text="INV1/2022", fill="black", font=('Helvetica 11'))
  canvas.create_text(350, 140, text="06-05-2022", fill="black", font=('Helvetica 11'))
  canvas.create_text(350, 160, text="21-05-2022", fill="black", font=('Helvetica 11'))
  canvas.create_text(340, 180, text="NET 15", fill="black", font=('Helvetica 11'))

  canvas.create_text(1050, 65, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
  # canvas.create_text(1080, 200, text=""+caddent.get('1.0','end-1c'), fill="black", font=('Helvetica 10'))
  T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
  T_address.tag_configure('tag_name',justify='right')
  T_address.insert('1.0', advdata[2])
  T_address.tag_add('tag_name','1.0', 'end')
  T_address_window = canvas.create_window(850, 80, anchor="nw", window=T_address)
  canvas.create_text(1050, 170, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
  # canvas.create_text(1085, 125, text="Address line 3", fill="black", font=('Helvetica 10'))
  # canvas.create_text(1085, 140, text="Address line 4", fill="black", font=('Helvetica 10'))
  # canvas.create_text(1080, 155, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
  # canvas.create_text(1080, 170, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
  canvas.create_text(1050, 190, text="Invoice", fill="black", font=('Helvetica 14 bold'))

  canvas.create_text(140, 215, text="Bill to", fill="black", font=('Helvetica 10 underline'))
  canvas.create_text(149, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
  canvas.create_text(191, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
  canvas.create_text(200, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
  canvas.create_text(160, 275, text="United States", fill="black", font=('Helvetica 10'))
  canvas.create_text(550, 215, text="Ship to", fill="black", font=('Helvetica 10 underline'))
  canvas.create_text(556, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
  canvas.create_text(598, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
  canvas.create_text(608, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
  canvas.create_text(568, 275, text="United States", fill="black", font=('Helvetica 10'))

  s = ttk.Style()
  s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')

  tree=ttk.Treeview(canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle_2.Treeview')
    
  tree.column("# 1", anchor=E, stretch=NO, width=700)
  tree.heading("# 1", text="Product/Service - Description")
  tree.column("# 2", anchor=E, stretch=NO, width=150)
  tree.heading("# 2", text="Quantity")
  tree.column("# 3", anchor=E, stretch=NO, width=150)
  tree.heading("# 3", text="Price")
    
  window = canvas.create_window(120, 290, anchor="nw", window=tree)

  canvas.create_line(120, 330, 1120, 330 )
  canvas.create_line(120, 290, 120, 330 )
  canvas.create_line(820, 290, 820, 330 )
  canvas.create_line(970, 290, 970, 330 )
  canvas.create_line(1120, 290, 1120, 330 )
  canvas.create_line(670, 330, 670, 480)
  canvas.create_line(970, 330, 970, 480)
  canvas.create_line(1120, 330, 1120, 480)
  canvas.create_line(670, 355, 1120, 355)
  canvas.create_line(670, 380, 1120, 380)
  canvas.create_line(670, 405, 1120, 405)
  canvas.create_line(670, 430, 1120, 430)
  canvas.create_line(670, 455, 1120, 455)
  canvas.create_line(670, 480, 1120, 480)

  canvas.create_text(250, 320, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
  canvas.create_text(900, 320, text="1", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(1080, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(1080, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  #canvas.create_text(1084, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  canvas.create_text(820, 345, text="Subtotal", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(1080, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(1080, 345, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  #canvas.create_text(1084, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  canvas.create_text(820, 370, text="TAX1", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(1085, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(1085, 370, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  #canvas.create_text(1089, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  canvas.create_text(820, 395, text="Shipping and handling", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(1085, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(1085, 395, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  #canvas.create_text(1089, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(1080, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(1080, 420, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  #canvas.create_text(1084, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
  canvas.create_text(820, 420, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(1080, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(1080, 445, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  #canvas.create_text(1084, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  canvas.create_text(820, 445, text="Total Paid", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(1080, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(1080, 465, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  #canvas.create_text(1084, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  canvas.create_text(820, 465, text="Balance", fill="black", font=('Helvetica 10'))

  canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
  canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
  canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
  canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

  canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
  canvas.create_line(110, 600, 1120, 600)
  canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
  canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
  canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
elif advdata[32] == 'Simplified 2 (logo on right side)':
  adv_winstyle8.insert(0, advdata[40])
  frame = Frame(seventhtab, width=1200, height=155)
  frame.pack(expand=True, fill=BOTH)
  frame.place(x=2,y=309)
  canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

  vertibar=Scrollbar(frame, orient=VERTICAL)
  vertibar.pack(side=RIGHT,fill=Y)
  vertibar.config(command=canvas.yview)
  canvas.config(width=1200,height=155)

  canvas.config(yscrollcommand=vertibar.set)
  canvas.pack(expand=True,side=LEFT,fill=BOTH)
  canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')
  canvas.create_text(600, 25, text="Title text goes here...", fill="black", font=('Helvetica 10'))
  try:
    adv_image = Image.open("images/"+advdata[13])
    adv_resize_image = adv_image.resize((200,75))
    adv_image = ImageTk.PhotoImage(adv_resize_image)

    adv_btlogo = Label(canvas,width=200,height=75,image = adv_image) 
    adv_window_image = canvas.create_window(850, 25, anchor="nw", window=adv_btlogo)
    adv_btlogo.photo = adv_image
  except:
    pass  

  # canvas.create_text(1000, 70, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

  canvas.create_text(829, 120, text="Invoice#", fill="black", font=('Helvetica 11'))
  canvas.create_text(841, 140, text="Invoice date", fill="black", font=('Helvetica 11'))
  canvas.create_text(830, 160, text="Due date", fill="black", font=('Helvetica 11'))
  canvas.create_text(820, 180, text="Terms", fill="black", font=('Helvetica 11'))
  canvas.create_text(834, 200, text="Order ref.#", fill="black", font=('Helvetica 11'))
  canvas.create_text(1047, 120, text="INV1/2022", fill="black", font=('Helvetica 11'))
  canvas.create_text(1050, 140, text="06-05-2022", fill="black", font=('Helvetica 11'))
  canvas.create_text(1050, 160, text="21-05-2022", fill="black", font=('Helvetica 11'))
  canvas.create_text(1040, 180, text="NET 15", fill="black", font=('Helvetica 11'))

  canvas.create_text(170, 55, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
  # canvas.create_text(135, 200, text=""+caddent.get('1.0','end-1c'), fill="black", font=('Helvetica 10'))
  T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
  T_address.tag_configure('tag_name',justify='right')
  T_address.insert('1.0', advdata[2])
  T_address.tag_add('tag_name','1.0', 'end')
  T_address_window = canvas.create_window(10, 80, anchor="nw", window=T_address)
  canvas.create_text(130, 170, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
  # canvas.create_text(130, 125, text="Address line 3", fill="black", font=('Helvetica 10'))
  # canvas.create_text(130, 140, text="Address line 4", fill="black", font=('Helvetica 10'))
  # canvas.create_text(136, 155, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
  # canvas.create_text(136, 170, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
  canvas.create_text(124, 190, text="Invoice", fill="black", font=('Helvetica 14 bold'))

  canvas.create_text(140, 215, text="Bill to", fill="black", font=('Helvetica 10 underline'))
  canvas.create_text(149, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
  canvas.create_text(191, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
  canvas.create_text(200, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
  canvas.create_text(160, 275, text="United States", fill="black", font=('Helvetica 10'))
  canvas.create_text(550, 215, text="Ship to", fill="black", font=('Helvetica 10 underline'))
  canvas.create_text(556, 230, text="John Doe", fill="black", font=('Helvetica 10 '))
  canvas.create_text(598, 245, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
  canvas.create_text(608, 260, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
  canvas.create_text(568, 275, text="United States", fill="black", font=('Helvetica 10'))

  s = ttk.Style()
  s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')

  tree=ttk.Treeview(canvas, column=("c1", "c2","c3"), show='headings',height= 0, style='mystyle_2.Treeview')
      
  tree.column("# 1", anchor=E, stretch=NO, width=700)
  tree.heading("# 1", text="Product/Service - Description")
  tree.column("# 2", anchor=E, stretch=NO, width=150)
  tree.heading("# 2", text="Quantity")
  tree.column("# 3", anchor=E, stretch=NO, width=150)
  tree.heading("# 3", text="Price")
      
  window = canvas.create_window(120, 290, anchor="nw", window=tree)

  canvas.create_line(120, 330, 1120, 330 )
  canvas.create_line(120, 290, 120, 330 )
  canvas.create_line(820, 290, 820, 330 )
  canvas.create_line(970, 290, 970, 330 )
  canvas.create_line(1120, 290, 1120, 330 )
  canvas.create_line(670, 330, 670, 480)
  canvas.create_line(970, 330, 970, 480)
  canvas.create_line(1120, 330, 1120, 480)
  canvas.create_line(670, 355, 1120, 355)
  canvas.create_line(670, 380, 1120, 380)
  canvas.create_line(670, 405, 1120, 405)
  canvas.create_line(670, 430, 1120, 430)
  canvas.create_line(670, 455, 1120, 455)
  canvas.create_line(670, 480, 1120, 480)

  canvas.create_text(250, 320, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
  canvas.create_text(900, 320, text="1", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(1080, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(1080, 320, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(1080, 320, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  #canvas.create_text(1084, 320, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  canvas.create_text(820, 345, text="Subtotal", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(1080, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(1080, 345, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(1080, 345, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  #canvas.create_text(1084, 345, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  canvas.create_text(820, 370, text="TAX1", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(1085, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(1085, 370, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(1085, 370, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  #canvas.create_text(1089, 370, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))

  canvas.create_text(820, 395, text="Shipping and handling", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(1085, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(1085, 395, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(1085, 395, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  #canvas.create_text(1089, 395, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(1080, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(1080, 420, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(1080, 420, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  #canvas.create_text(1084, 420, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10 bold'))
  canvas.create_text(820, 420, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(1080, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(1080, 445, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(1080, 445, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  #canvas.create_text(1084, 445, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  canvas.create_text(820, 445, text="Total Paid", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(1080, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(1080, 465, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(1080, 465, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  #canvas.create_text(1084, 465, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  canvas.create_text(820, 465, text="Balance", fill="black", font=('Helvetica 10'))

  canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
  canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
  canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
  canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

  canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
  canvas.create_line(110, 600, 1120, 600)
  canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
  canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
  canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
elif advdata[32] == 'Business Classic':
  adv_winstyle8.insert(0, advdata[40])
  frame = Frame(seventhtab, width=1200, height=155)
  frame.pack(expand=True, fill=BOTH)
  frame.place(x=2,y=309)
  canvas=Canvas(frame, bg='grey', width=1200, height=155, scrollregion=(0,0,700,700))

  vertibar=Scrollbar(frame, orient=VERTICAL)
  vertibar.pack(side=RIGHT,fill=Y)
  vertibar.config(command=canvas.yview)
  canvas.config(width=1200,height=155)

  canvas.config(yscrollcommand=vertibar.set)
  canvas.pack(expand=True,side=LEFT,fill=BOTH)
  canvas.create_rectangle(10, 10, 1190, 690 , outline='yellow',fill='white')
  canvas.create_text(600, 45, text="Title text goes here...", fill="black", font=('Helvetica 10'))
  canvas.create_line(100, 60, 1120, 60, fill="orange")
  #canvas.create_line(1000, 60, 600, 60, fill="grey")

  try:
    adv_image = Image.open("images/"+advdata[13])
    adv_resize_image = adv_image.resize((200,100))
    adv_image = ImageTk.PhotoImage(adv_resize_image)

    adv_btlogo = Label(canvas,width=200,height=100,image = adv_image) 
    adv_window_image = canvas.create_window(140, 100, anchor="nw", window=adv_btlogo)
    adv_btlogo.photo = adv_image
  except:
    pass  


  # canvas.create_text(250, 155, text="Your Company Logo", fill="black", font=('Helvetica 18 bold'))

  canvas.create_text(560, 85, text=" "+comname.get(), fill="black", font=('Helvetica 12 '))
  # canvas.create_text(535, 200, text=""+caddent.get('1.0', 'end-1c'), fill="black", font=('Helvetica 10'))
  T_address = Text(canvas, height=5, width=40, font=('Helvetica 10'),borderwidth=0)
  T_address.tag_configure('tag_name',justify='right')
  T_address.insert('1.0', advdata[2])
  T_address.tag_add('tag_name','1.0', 'end')
  T_address_window = canvas.create_window(350, 100, anchor="nw", window=T_address)
  # adv_btlabel = Label(canvas,width=20,height=10,text=""+caddent.get('1.0', 'end-1c')) 
  # adv_window_label = canvas.create_window(530, 110, anchor="nw", window=adv_btlabel)
  canvas.create_text(530, 190, text=""+comsalestax.get(), fill="black", font=('Helvetica 10'))
  # canvas.create_text(530, 140, text="Address line 3", fill="black", font=('Helvetica 10'))
  # canvas.create_text(530, 155, text="Address line 4", fill="black", font=('Helvetica 10'))
  # canvas.create_text(536, 170, text="Phone: 555-5555", fill="black", font=('Helvetica 10'))
  # canvas.create_text(536, 190, text="Sales tax reg No.", fill="black", font=('Helvetica 10'))
  canvas.create_text(524, 210, text="Invoice", fill="black", font=('Helvetica 14 bold'))

  canvas.create_text(749, 95, text="John Doe", fill="black", font=('Helvetica 10 '))
  canvas.create_text(791, 110, text="381 South Bedford Road", fill="black", font=('Helvetica 10'))
  canvas.create_text(800, 125, text="Bedford Corners, NY 10549", fill="black", font=('Helvetica 10'))
  canvas.create_text(760, 140, text="United States", fill="black", font=('Helvetica 10'))

  canvas.create_text(745, 160, text="Invoice", fill="black", font=('Helvetica 11'))
  canvas.create_text(760, 180, text="Invoice date", fill="black", font=('Helvetica 11'))
  canvas.create_text(750, 200, text="Due date", fill="black", font=('Helvetica 11'))

  canvas.create_text(947, 160, text="INV1/2022", fill="black", font=('Helvetica 11'))
  canvas.create_text(950, 180, text="06-05-2022", fill="black", font=('Helvetica 11'))
  canvas.create_text(950, 200, text="21-05-2022", fill="black", font=('Helvetica 11'))
  s = ttk.Style()
  s.configure('mystyle_2.Treeview.Heading', background='orange',State='DISABLE')

  tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5"), show='headings',height= 0, style='mystyle_2.Treeview')
      
  tree.column("# 1", anchor=E, stretch=NO, width=150)
  tree.heading("# 1", text="Product/Service")
  tree.column("# 2", anchor=E, stretch=NO, width=400)
  tree.heading("# 2", text="Description")
  tree.column("# 3", anchor=E, stretch=NO, width=150)
  tree.heading("# 3", text="Unit Price")
  tree.column("# 4", anchor=E, stretch=NO, width=150)
  tree.heading("# 4", text="Quantity")
  tree.column("# 5", anchor=E, stretch=NO, width=150)
  tree.heading("# 5", text="Price")
      
  window = canvas.create_window(120, 230, anchor="nw", window=tree)

  canvas.create_line(120, 270, 1120, 270 )
  canvas.create_line(120, 230, 120, 270 )
  canvas.create_line(270, 230, 270, 270 )
  canvas.create_line(670, 230, 670, 270 )
  canvas.create_line(820, 230, 820, 270 )
  canvas.create_line(970, 230, 970, 270 )
  canvas.create_line(1120, 230, 1120, 270)
  canvas.create_line(1120, 270, 1120, 420)
  canvas.create_line(670, 295, 1120, 295)
  canvas.create_line(670, 320, 1120, 320)
  canvas.create_line(670, 345, 1120, 345)
  canvas.create_line(670, 370, 1120, 370)
  canvas.create_line(670, 395, 1120, 395)
  canvas.create_line(670, 420, 1120, 420)

  canvas.create_text(165, 260, text="PROD-0001", fill="black", font=('Helvetica 10'))
  canvas.create_text(400, 260, text="Example product - Description text...", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(734, 260, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(734, 260, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(734, 260, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(734, 260, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  #canvas.create_text(734, 260, text="$200.00", fill="black", font=('Helvetica 10'))
  canvas.create_text(890, 260, text="1", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(1080, 260, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(1080, 260, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(1080, 260, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(1080, 260, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  # canvas.create_text(1080, 260, text="$200.00", fill="black", font=('Helvetica 10'))

  canvas.create_text(697, 285, text="Subtotal", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(1080, 285, text=""+comcursign.get()+"200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(1080, 285, text="200"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(1080, 285, text=""+comcursign.get()+" 200"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(1080, 285, text="200"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  #canvas.create_text(1080, 285, text="$200.00", fill="black", font=('Helvetica 10'))

  canvas.create_text(692, 310, text="TAX1", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(1085, 310, text=""+comcursign.get()+"18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(1085, 310, text="18"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(1085, 310, text=""+comcursign.get()+" 18"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(1085, 310, text="18"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  #canvas.create_text(1085, 310, text="$18.00", fill="black", font=('Helvetica 10'))

  canvas.create_text(737, 335, text="Shipping and handling", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(1085, 335, text=""+comcursign.get()+"20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(1085, 335, text="20"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(1085, 335, text=""+comcursign.get()+" 20"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(1085, 335, text="20"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  #canvas.create_text(1085, 335, text="$20.00", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(1080, 360, text=""+comcursign.get()+"238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(1080, 360, text="238"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(1080, 360, text=""+comcursign.get()+" 238"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(1080, 360, text="238"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  #canvas.create_text(1080, 360, text="$238.00", fill="black", font=('Helvetica 10 bold'))
  canvas.create_text(715, 360, text="Invoice total", fill="black", font=('Helvetica 10 bold'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(1080, 385, text=""+comcursign.get()+"100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(1080, 385, text="100"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(1080, 385, text=""+comcursign.get()+" 100"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(1080, 385, text="100"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  #canvas.create_text(1080, 385, text="100.00", fill="black", font=('Helvetica 10'))
  canvas.create_text(705, 385, text="Total Paid", fill="black", font=('Helvetica 10'))
  if comcursignpla.get() == "before amount":
    canvas.create_text(1080, 410, text=""+comcursign.get()+"138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount":
    canvas.create_text(1080, 410, text="138"+""+comdecsep.get()+"00"+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "before amount with space":
    canvas.create_text(1080, 410, text=""+comcursign.get()+" 138"+""+comdecsep.get()+"00", fill="black", font=('Helvetica 10'))
  elif comcursignpla.get() == "after amount with space":
    canvas.create_text(1080, 410, text="138"+""+comdecsep.get()+"00 "+""+comcursign.get(), fill="black", font=('Helvetica 10'))
  else:
    pass
  #canvas.create_text(1080, 410, text="$138.00", fill="black", font=('Helvetica 10'))
  canvas.create_text(700, 410, text="Balance", fill="black", font=('Helvetica 10'))

  canvas.create_line(100, 480, 1120, 480, fill="orange")
  canvas.create_text(200, 500, text="Multiline comment text goes here..", fill="black", font=('Helvetica 10'))
  canvas.create_text(106, 510, text="...", fill="black", font=('Helvetica 10'))
  canvas.create_text(106, 520, text="...", fill="black", font=('Helvetica 10'))
  canvas.create_text(106, 530, text="...", fill="black", font=('Helvetica 10'))

  canvas.create_text(600, 580, text="Terms and Conditions", fill="black", font=('Helvetica 10'))
  canvas.create_line(100, 600, 1120, 600, fill="orange")
  canvas.create_text(620, 620, text="Invoices are payable on receipt unless other terms, negotiated and noted on the invoice. By accepting delivery of goods, Buyer agrees to pay the invoiced cost for those goods,\nand agrees to be bound to thses contract terms. No acceptance may vary these terms unless specifically agreed in writing by Seller ", fill="black", font=('Helvetica 10'))
  canvas.create_text(196, 650, text="Page footer text goes here...", fill="black", font=('Helvetica 10'))
  canvas.create_text(1090, 650, text="Page 1 of 1", fill="black", font=('Helvetica 10'))
else:
  pass
adv_winstyle8.place(x=2 ,y=270, width=220)
#adv_winstyle8.current(0)


root.mainloop()


