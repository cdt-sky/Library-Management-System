from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import mysql.connector
from tkinter import messagebox
import datetime
import tkinter

class LibraryManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")

        #-------Variables ----------
        self.membertype=StringVar()
        self.prnno= StringVar()
        self.id= StringVar()
        self.firstname = StringVar()
        self.lastname= StringVar()
        self.address1=StringVar()
        self.address2= StringVar()
        self.pincode = StringVar()
        self.mobileno = StringVar()
        self.bookid = StringVar()
        self.booktitle = StringVar()
        self.author = StringVar()
        self.dateborrowed = StringVar()
        self.datedue = StringVar()
        self.daysonbook = StringVar()
        self.lateratefine = StringVar()
        self.dateoverdue = StringVar()
        self.finalprice = StringVar()

        #-----Main Label Title------

        lblmaintitle= Label(self.root, text="LIBRARY MANAGEMENT SYSTEM", bg="powder blue", fg='green', bd=20, relief=RIDGE, font=('Times New Roman', 50, 'bold'), padx=2, pady=6)
        lblmaintitle.pack(side=TOP, fill=X)

        #-------Frame-----------

        frame= Frame(self.root, bd=12, relief=RIDGE, padx=20, bg='powder blue')
        frame.place(x=0, y=130, width=1530, height=400)

        #---------Data Frame Left ----------

        dataframeleft= LabelFrame(frame, text='Library Membership Information', bg='powder blue', fg='black', bd=12, relief=RIDGE, font=('Times New Roman', 12, 'bold'))
        dataframeleft.place(x=0, y=5, width=900, height=350)

        lblMember = Label(dataframeleft, bg='powder blue', text='Member Type', font=('Times New Roman', 12, 'bold'), padx=2, pady=6)
        lblMember.grid(row=0, column=0, sticky=W)

        #---------Combobox-------------
        comboMember = ttk.Combobox(dataframeleft,state='readonly',textvariable=self.membertype, font=('Times New Roman', 12, 'bold'),width=27)
        comboMember['values'] = ('Admin Staff', 'Student', 'Lecturer')
        comboMember.current(0)
        comboMember.grid(row=0, column=1)

        #--------- PRN----------
        lblprn = Label(dataframeleft, bg='powder blue', text='PRN No.', font=('Times New Roman', 12, 'bold'), padx=2, pady=6)
        lblprn.grid(row=1, column=0, sticky=W)
        txtprn= Entry(dataframeleft,font=('Times New Roman', 13, 'bold'),textvariable=self.prnno, width=29 )
        txtprn.grid(row=1, column=1)

        #--------- Title ------------
        lbltitle = Label(dataframeleft, bg='powder blue', text='Id No.', font=('Times New Roman', 12, 'bold'), padx=2, pady=6)
        lbltitle.grid(row=2, column=0, sticky=W)
        txttitle= Entry(dataframeleft,font=('Times New Roman', 13, 'bold'),textvariable=self.id , width=29 )
        txttitle.grid(row=2, column=1)

        #---------- First Name ----------
        lblfname = Label(dataframeleft, bg='powder blue', text='First Name', font=('Times New Roman', 12, 'bold'), padx=2, pady=6)
        lblfname.grid(row=3, column=0, sticky=W)
        txtfname= Entry(dataframeleft,font=('Times New Roman', 13, 'bold'),textvariable=self.firstname, width=29 )
        txtfname.grid(row=3, column=1)

        # Last Name -----
        lbllname = Label(dataframeleft, bg='powder blue', text='Last Name', font=('Times New Roman', 12, 'bold'), padx=2, pady=6)
        lbllname.grid(row=4, column=0, sticky=W)
        txtlname= Entry(dataframeleft,font=('Times New Roman', 13, 'bold'),textvariable=self.lastname, width=29 )
        txtlname.grid(row=4, column=1)

        # Address 1 -----
        lblladdress1 = Label(dataframeleft, bg='powder blue', text='Address 1', font=('Times New Roman', 12, 'bold'), padx=2, pady=6)
        lblladdress1.grid(row=5, column=0, sticky=W)
        txtaddress1= Entry(dataframeleft,font=('Times New Roman', 13, 'bold'),textvariable=self.address1, width=29 )
        txtaddress1.grid(row=5, column=1)

        # Address 2 -------
        lbladdress2 = Label(dataframeleft, bg='powder blue', text='Address 2', font=('Times New Roman', 12, 'bold'), padx=2, pady=6)
        lbladdress2.grid(row=6, column=0, sticky=W)
        txtaddress2= Entry(dataframeleft,font=('Times New Roman', 13, 'bold'),textvariable=self.address2, width=29 )
        txtaddress2.grid(row=6, column=1)

        # Post Code -------
        lblpostcode = Label(dataframeleft, bg='powder blue', text='Pincode', font=('Times New Roman', 12, 'bold'), padx=2, pady=6)
        lblpostcode.grid(row=7, column=0, sticky=W)
        txtpin = Entry(dataframeleft,font=('Times New Roman', 13, 'bold'),textvariable=self.pincode, width=29 )
        txtpin.grid(row=7, column=1)

        # Mobile Number ------
        lblmobile = Label(dataframeleft, bg='powder blue', text='Mobile No.', font=('Times New Roman', 12, 'bold'), padx=2, pady=6)
        lblmobile.grid(row=8, column=0, sticky=W)
        txtmobile= Entry(dataframeleft,font=('Times New Roman', 13, 'bold'),textvariable=self.mobileno, width=29 )
        txtmobile.grid(row=8, column=1)

        # Book Id -------
        lblbid = Label(dataframeleft, bg='powder blue', text='Book Id', font=('Times New Roman', 12, 'bold'), padx=2, pady=6)
        lblbid.grid(row=0, column=2, sticky=W)
        txtbid= Entry(dataframeleft,font=('Times New Roman', 13, 'bold'),textvariable=self.bookid, width=29 )
        txtbid.grid(row=0, column=3)

        # Book Name -----
        lblbname = Label(dataframeleft, bg='powder blue', text='Book Title', font=('Times New Roman', 12, 'bold'), padx=2, pady=6)
        lblbname.grid(row=1, column=2, sticky=W)
        txtbname= Entry(dataframeleft,font=('Times New Roman', 13, 'bold'),textvariable=self.booktitle, width=29 )
        txtbname.grid(row=1, column=3)

        # Book Author ------
        lblauthor = Label(dataframeleft, bg='powder blue', text='Author Name', font=('Times New Roman', 12, 'bold'), padx=2, pady=6)
        lblauthor.grid(row=2, column=2, sticky=W)
        txtauthor= Entry(dataframeleft,font=('Times New Roman', 13, 'bold'),textvariable=self.author, width=29)
        txtauthor.grid(row=2, column=3)
        
        # Date Borrowed -------
        lbldateborrowed = Label(dataframeleft, bg='powder blue', text='Borrowed Date', font=('Times New Roman', 12, 'bold'), padx=2, pady=6)
        lbldateborrowed.grid(row=3, column=2, sticky=W)
        txtdateborrowed= Entry(dataframeleft,font=('Times New Roman', 13, 'bold'),textvariable=self.dateborrowed, width=29 )
        txtdateborrowed.grid(row=3, column=3)

        # Date Due -----------
        lblduedate = Label(dataframeleft, bg='powder blue', text='Due Date:', font=('Times New Roman', 12, 'bold'), padx=2, pady=6)
        lblduedate.grid(row=4, column=2, sticky=W)
        txtdue = Entry(dataframeleft,font=('Times New Roman', 13, 'bold'),textvariable=self.datedue, width=29 )
        txtdue.grid(row=4, column=3)

        # Days on book --------
        lbldayonbook = Label(dataframeleft, bg='powder blue', text='Day on Book:', font=('Times New Roman', 12, 'bold'), padx=2, pady=6)
        lbldayonbook.grid(row=5, column=2, sticky=W)
        txtdayonbook= Entry(dataframeleft,font=('Times New Roman', 13, 'bold'),textvariable=self.daysonbook, width=29 )
        txtdayonbook.grid(row=5, column=3)


        # Late Return fine -------
        lblfine = Label(dataframeleft, bg='powder blue', text='Fine: ', font=('Times New Roman', 12, 'bold'), padx=2, pady=6)
        lblfine.grid(row=6, column=2, sticky=W)
        txtfine= Entry(dataframeleft,font=('Times New Roman', 13, 'bold'),textvariable=self.lateratefine, width=29 )
        txtfine.grid(row=6, column=3)

        # Date Overdue --------
        lbloverdue = Label(dataframeleft, bg='powder blue', text='OverDue Date:', font=('Times New Roman', 12, 'bold'), padx=2, pady=6)
        lbloverdue.grid(row=7, column=2, sticky=W)
        txtoverdue= Entry(dataframeleft,font=('Times New Roman', 13, 'bold'),textvariable=self.dateoverdue, width=29 )
        txtoverdue.grid(row=7, column=3)

        # Actual Price --------
        lblprice = Label(dataframeleft, bg='powder blue', text='Actual Price:', font=('Times New Roman', 12, 'bold'), padx=2, pady=6)
        lblprice.grid(row=8, column=2, sticky=W)
        txtprice= Entry(dataframeleft,font=('Times New Roman', 13, 'bold'),textvariable=self.finalprice, width=29 )
        txtprice.grid(row=8, column=3)


        #----------Data Frame Right------------
        dataframeright= LabelFrame(frame, text='Book Details', bg='powder blue', fg='black', bd=12, relief=RIDGE, font=('Times New Roman', 12, 'bold'))
        dataframeright.place(x=910, y=5, width=540, height=350)

        self.txtBox= Text(dataframeright,font=('Times New Roman', 12, 'bold'), width=35, height=16, padx=2, pady=6)
        self.txtBox.grid(row=0, column=2)

        # List Scroll Bar ------

        listscrollbar = Scrollbar(dataframeright)
        listscrollbar.grid(row=0, column=1, sticky='ns')

        # List of Books----

        listbooks= ["The Midnight Chronicles", "Echoes of Eternity", "Whispers in the Wind", "The Last Ember","Python Master", "Algorithms - Made Easy", "System Programming", "Best Actor", "Garam Chulha", "Beneath the Crimson Sky", "Shadows of the Forgotten", "The Glass Sanctuary", "Realm of the Lost", "Tides of Time", "The Phoenix Reborn", "Silent Storm", "Cursed by Fate", "The Hidden Oracle", "Legacy of the Fallen", "The Silver Veil"]
        
        
        def selectbook(event=""):
            value = str(listbox.get(listbox.curselection()))
            x = value
            if x == "The Midnight Chronicles":
                self.bookid.set('BKID5454')
                self.booktitle.set("Python Master")
                self.author.set("Paul Berry")

                d1 = datetime.datetime.today().strftime('%Y-%m-%d')
                d2 = datetime.timedelta(days=15)
                d3 = (datetime.datetime.today() + d2).strftime('%Y-%m-%d')

                self.dateborrowed.set(d1)
                self.datedue.set(d3)
                self.daysonbook.set(15)
                self.lateratefine.set("Rs. 20")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs. 788")

            elif x == "Echoes of Eternity":
                self.bookid.set('BKID5754')
                self.booktitle.set("The Last Ember")
                self.author.set("Richard Daniel")

                d1 = datetime.datetime.today().strftime('%Y-%m-%d')
                d2 = datetime.timedelta(days=15)
                d3 = (datetime.datetime.today() + d2).strftime('%Y-%m-%d')

                self.dateborrowed.set(d1)
                self.datedue.set(d3)
                self.daysonbook.set(15)
                self.lateratefine.set("Rs. 30")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs. 628")

            elif x == "Whispers in the Wind":
                self.bookid.set('BKID5460')
                self.booktitle.set("Algorithms - Made Easy")
                self.author.set("Steve Berry")

                d1 = datetime.datetime.today().strftime('%Y-%m-%d')
                d2 = datetime.timedelta(days=15)
                d3 = (datetime.datetime.today() + d2).strftime('%Y-%m-%d')

                self.dateborrowed.set(d1)
                self.datedue.set(d3)
                self.daysonbook.set(15)
                self.lateratefine.set("Rs. 40")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs. 245")

            elif x == "The Last Ember":
                self.bookid.set('BKID6354')
                self.booktitle.set("System Programming")
                self.author.set("Richard Headly")

                d1 = datetime.datetime.today().strftime('%Y-%m-%d')
                d2 = datetime.timedelta(days=15)
                d3 = (datetime.datetime.today() + d2).strftime('%Y-%m-%d')

                self.dateborrowed.set(d1)
                self.datedue.set(d3)
                self.daysonbook.set(15)
                self.lateratefine.set("Rs. 70")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs. 148")

            elif x == "Python Master":
                self.bookid.set('BKID3339')
                self.booktitle.set("Best Actor")
                self.author.set("Munshi PremChand")

                d1 = datetime.datetime.today().strftime('%Y-%m-%d')
                d2 = datetime.timedelta(days=15)
                d3 = (datetime.datetime.today() + d2).strftime('%Y-%m-%d')

                self.dateborrowed.set(d1)
                self.datedue.set(d3)
                self.daysonbook.set(15)
                self.lateratefine.set("Rs. 10")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs. 80")

            elif x == "Algorithms - Made Easy":
                self.bookid.set('BKID7389')
                self.booktitle.set("Garam Chulha")
                self.author.set("Ram Prasad")

                d1 = datetime.datetime.today().strftime('%Y-%m-%d')
                d2 = datetime.timedelta(days=15)
                d3 = (datetime.datetime.today() + d2).strftime('%Y-%m-%d')

                self.dateborrowed.set(d1)
                self.datedue.set(d3)
                self.daysonbook.set(15)
                self.lateratefine.set("Rs. 24")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs. 308")


        listbox = Listbox(dataframeright,font=('Times New Roman', 12, 'bold'), width=25, height=16)
        listbox.bind("<<ListboxSelect>>", selectbook)
        listbox.grid(row=0, column=0, padx=4)
        listscrollbar.config(command=listbox.yview)

        # Entering Book In Book List -----

        for item in listbooks:
            listbox.insert(END, item)

        #-----------Button Frame --------------
        framebutton= Frame(self.root, bd=12, relief=RIDGE, padx=20, bg='powder blue')
        framebutton.place(x=0, y=530, width=1530, height=70)

        btnAddData = Button(framebutton, text='Add Data',command=self.addData, font=('Times New Roman', 12, 'bold'), width=25, bg='blue', fg='white')
        btnAddData.grid(row=0, column=0)

        btnShowData = Button(framebutton, text='Show Data',command=self.showData, font=('Times New Roman', 12, 'bold'), width=25, bg='blue', fg='white')
        btnShowData.grid(row=0, column=1)

        btnUpdate = Button(framebutton, text='Update',command=self.update, font=('Times New Roman', 12, 'bold'), width=25, bg='blue', fg='white')
        btnUpdate.grid(row=0, column=2)

        btndelete = Button(framebutton, text='Delete', command=self.delete, font=('Times New Roman', 12, 'bold'), width=25, bg='blue', fg='white')
        btndelete.grid(row=0, column=3)

        btnReset = Button(framebutton, text='Reset',command=self.reset, font=('Times New Roman', 12, 'bold'), width=25, bg='blue', fg='white')
        btnReset.grid(row=0, column=4)

        btnExit = Button(framebutton, text='Exit', command=self.iexit, font=('Times New Roman', 12, 'bold'), width=25, bg='blue', fg='white')
        btnExit.grid(row=0, column=5)
        

        #------------Information Frame------------
        framedetails= Frame(self.root, bd=12, relief=RIDGE, padx=20, bg='powder blue')
        framedetails.place(x=0, y=590, width=1530, height=210)

        #------------ Table Frame -------------
        tableframe= Frame(framedetails, bd=6, relief=RIDGE, bg='powder blue') 
        tableframe.place(x=0, y=2, width=1460, height=190)

        xscrollbar=Scrollbar(tableframe, orient=HORIZONTAL)
        yscrollbar=Scrollbar(tableframe, orient=VERTICAL)

        self.librarytable=ttk.Treeview(tableframe, column=("membertype", "prnno", "title", "firstname", "lastname", "address1", "address2", "pincode", "mobileno", "bookid", "booktitle", "author", "borroweddate", "duedate", "dayonbook", "fine", "overdue", "price"),xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set)
        
        xscrollbar.pack(side=BOTTOM, fill=X)
        yscrollbar.pack(side=RIGHT, fill=Y)

        xscrollbar.config(command=self.librarytable.xview)
        yscrollbar.config(command=self.librarytable.yview)

        self.librarytable.heading("membertype", text="Member Type")
        self.librarytable.heading("prnno", text="PRN No.")
        self.librarytable.heading("title", text="Title")
        self.librarytable.heading("firstname", text="First Name")
        self.librarytable.heading("lastname", text="Last Name")
        self.librarytable.heading("address1", text="Address 1")
        self.librarytable.heading("address2", text="Address 2")
        self.librarytable.heading("pincode", text="Pincode")
        self.librarytable.heading("mobileno", text="Mobile No.")
        self.librarytable.heading("bookid", text="Book Id")
        self.librarytable.heading("booktitle", text="Book Title")
        self.librarytable.heading("author", text="Author Name")
        self.librarytable.heading("borroweddate", text="Borrowed Date")
        self.librarytable.heading("duedate", text="Due Date")
        self.librarytable.heading("dayonbook", text="Day on Book")
        self.librarytable.heading("fine", text="Late Fine")
        self.librarytable.heading("overdue", text="OverDue Date")
        self.librarytable.heading("price", text="Actual Price")


        self.librarytable['show'] = 'headings'
        self.librarytable.pack(fill=BOTH, expand=1)

        #---- setting width to adjust the width of column entry-------

        self.librarytable.column("membertype", width=100)
        self.librarytable.column("prnno", width=100)
        self.librarytable.column("title", width=100)
        self.librarytable.column("firstname", width=100)
        self.librarytable.column("lastname", width=100)
        self.librarytable.column("address1", width=100)
        self.librarytable.column("address2", width=100)
        self.librarytable.column("pincode", width=100)
        self.librarytable.column("mobileno", width=100)
        self.librarytable.column("bookid", width=100)
        self.librarytable.column("booktitle", width=100)
        self.librarytable.column("author", width=100)
        self.librarytable.column("borroweddate", width=100)
        self.librarytable.column("duedate", width=100)
        self.librarytable.column("dayonbook", width=100)
        self.librarytable.column("fine", width=100)
        self.librarytable.column("overdue", width=100)
        self.librarytable.column("price", width=100)

        self.fetchData()
        self.librarytable.bind("<ButtonRelease-1>", self.getcursor)

    #---- Add data function ---------

    def addData(self):
        conn = mysql.connector.connect(host='localhost', username= 'root', password='SumitKumar2004@', database='Mydata')
        m_cursor= conn.cursor()
        m_cursor.execute('insert into library values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                                                                self.membertype.get(),
                                                                                                                self.prnno.get(),
                                                                                                                self.id.get(),
                                                                                                                self.firstname.get(),
                                                                                                                self.lastname.get(),
                                                                                                                self.address1.get(),
                                                                                                                self.address2.get(),
                                                                                                                self.pincode.get(),
                                                                                                                self.mobileno.get(),
                                                                                                                self.bookid.get(),
                                                                                                                self.booktitle.get(),
                                                                                                                self.author.get(),
                                                                                                                self.dateborrowed.get(),
                                                                                                                self.datedue.get(),
                                                                                                                self.daysonbook.get(),
                                                                                                                self.lateratefine.get(),
                                                                                                                self.dateoverdue.get(),
                                                                                                                self.finalprice.get()
                                                                                                            ))
        conn.commit()
        self.fetchData()
        conn.close()
        messagebox.showinfo('Success', 'Member has been added successfully.')

    def update(self):
        if self.prnno.get() == "" or self.firstname.get() == "":
            messagebox.showerror("Error", "Please select a record to update")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="SumitKumar2004@", database="Mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("UPDATE library SET membertype=%s, id=%s, firstname=%s, lastname=%s, address1=%s, address2=%s, pincode=%s, mobileno=%s, bookid=%s, booktitle=%s, author=%s, borroweddate=%s, duedate=%s, dayonbook=%s, fine=%s, overdue=%s, price=%s WHERE prnno=%s", (
                self.membertype.get(),
                self.id.get(),
                self.firstname.get(),
                self.lastname.get(),
                self.address1.get(),
                self.address2.get(),
                self.pincode.get(),
                self.mobileno.get(),
                self.bookid.get(),
                self.booktitle.get(),
                self.author.get(),
                self.dateborrowed.get(),
                self.datedue.get(),
                self.daysonbook.get(),
                self.lateratefine.get(),
                self.dateoverdue.get(),
                self.finalprice.get(),
                self.prnno.get()
            ))
            conn.commit()
            self.fetchData()
            conn.close()
            messagebox.showinfo("Success", "Record has been updated")

    def fetchData(self):
        conn = mysql.connector.connect(host='localhost', username= 'root', password='SumitKumar2004@', database='Mydata')
        m_cursor= conn.cursor()
        m_cursor.execute("select * from library")
        rows= m_cursor.fetchall()
        if(len(rows)!= 0):
            self.librarytable.delete(*self.librarytable.get_children())
            for i in rows:
                self.librarytable.insert("", END, values= i)
            conn.commit()
        conn.close()

    def getcursor(self, event=""):
        cursor_row=self.librarytable.focus()
        content=self.librarytable.item(cursor_row)
        row=content['values']

        self.membertype.set(row[0]),
        self.prnno.set(row[1]),
        self.id.set(row[2]),
        self.firstname.set(row[3]),
        self.lastname.set(row[4]),
        self.address1.set(row[5]),
        self.address2.set(row[6]),
        self.pincode.set(row[7]),
        self.mobileno.set(row[8]),
        self.bookid.set(row[9]),
        self.booktitle.set(row[10]),
        self.author.set(row[11]),
        self.dateborrowed.set(row[12]),
        self.datedue.set(row[13]),
        self.daysonbook.set(row[14]),
        self.lateratefine.set(row[15]),
        self.dateoverdue.set(row[16]),
        self.finalprice.set(row[17])

    def showData(self):
        self.txtBox.insert(END," Member Type\t\t" + self.membertype.get() + '\n')
        self.txtBox.insert(END," PRN No.:\t\t"+ self.prnno.get()+ '\n')
        self.txtBox.insert(END," Title:\t\t"+ self.id.get()+ '\n')
        self.txtBox.insert(END, "First Name: \t\t" + self.firstname.get() + '\n')
        self.txtBox.insert(END," Last Name:\t\t"+ self.lastname.get()+ '\n')
        self.txtBox.insert(END," Address 1:\t\t"+ self.address1.get()+ '\n')
        self.txtBox.insert(END," Address 2:\t\t"+ self.address2.get()+ '\n')
        self.txtBox.insert(END," Pincode:\t\t"+ self.pincode.get()+ '\n')
        self.txtBox.insert(END," Mobile No.:\t\t"+ self.mobileno.get()+ '\n')
        self.txtBox.insert(END," Book Id:\t\t"+ self.bookid.get()+ '\n')
        self.txtBox.insert(END," Book Title:\t\t"+ self.booktitle.get()+ '\n')
        self.txtBox.insert(END," Author Name:\t\t"+ self.author.get()+ '\n')
        self.txtBox.insert(END," Borrowed Date:\t\t"+ self.dateborrowed.get()+ '\n')
        self.txtBox.insert(END," Due Date:\t\t"+ self.datedue.get()+ '\n')
        self.txtBox.insert(END," Day On Book:\t\t"+ self.daysonbook.get()+ '\n')
        self.txtBox.insert(END," Late Fine:\t\t"+ self.lateratefine.get()+ '\n')
        self.txtBox.insert(END,"OverDue Date:\t\t"+ self.dateoverdue.get()+ '\n')
        self.txtBox.insert(END," Actual Price:\t\t"+ self.finalprice.get()+ '\n')

    def reset(self):
        self.membertype.set("")
        self.prnno.set("")
        self.id.set("")
        self.firstname.set("")
        self.lastname.set("")
        self.address1.set("")
        self.address2.set("")
        self.pincode.set("")
        self.mobileno.set("")
        self.bookid.set("")
        self.booktitle.set("")
        self.author.set("")
        self.dateborrowed.set("")
        self.datedue.set("")
        self.daysonbook.set("")
        self.lateratefine.set("")
        self.dateoverdue.set("")
        self.finalprice.set("")

    def iexit(self):
        iexit = tkinter.messagebox.askyesno("Library Management System", "Do you want to exit?")
        if iexit>0:
            self.root.destroy()
            return

    def delete(self):
        if self.prnno.get() == "" or self.id.get()== "":
            messagebox.showerror("Error!", "First Select the Member")
        else:
            conn = mysql.connector.connect(host='localhost', username= 'root', password='SumitKumar2004@', database='Mydata')
            m_cursor= conn.cursor()
            query='delete from library where prnno=%s'
            value=(self.prnno.get(),)
            m_cursor.execute(query, value)

            conn.commit()
            self.fetchData()
            self.reset()
            conn.close()
            messagebox.showinfo("Success!!", "Member has been Deleted.")


if __name__ == '__main__':
    root = Tk()
    obj= LibraryManagement(root)
    root.mainloop()