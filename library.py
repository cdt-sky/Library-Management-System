from tkinter import*
from tkinter import ttk
import pymysql
from tkinter import messagebox
import datetime
import sys
import tkinter

class LibraryManagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1350x700+0+0")

# ------------------------------------------ Variables ------------------------------------------
        self.member_var = StringVar()
        self.prn_var = StringVar()
        self.id_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address1_var = StringVar()
        self.address2_var = StringVar()
        self.postcode_var = StringVar()
        self.mobile_var = StringVar()
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.author_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.datedue_var = StringVar()
        self.daysonbook = StringVar()
        self.latereturnfine_var = StringVar()
        self.dateoverdue = StringVar()
        self.finalprice = StringVar()


        lbltitle = Label(self.root, text="LIBRARY MANAGEMENT SYSTEM", bg = "powder blue", fg = "green", bd= 20, relief= RIDGE, font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1350, height=390)

        # ----------------------------------------- Data FrameLeft ------------------------------------------


        DataFrameLeft= LabelFrame(frame, text="Library Membership Information", bg="powder blue", fg="black",bd=12, relief=RIDGE, font=("arial", 12,"bold"))
        DataFrameLeft.place(x=0, y=5, width=800, height=350)

        lblMember = Label(DataFrameLeft, bg = "powder blue", text="Member Type", font=("arial", 12,"bold"), padx=2, pady=6)
        lblMember.grid(row=0, column=0, sticky=W)

        comMember = ttk.Combobox(DataFrameLeft, font=("arial", 12,"bold"),textvariable = self.member_var, width=27, state="readonly")
        comMember["value"] = ("Admin Staff", "Student", "Lecturer")
        comMember.grid(row=0, column=1)

        lblPRN_No = Label(DataFrameLeft, bg = "powder blue" ,text="PRN No: ", font=("arial", 12,"bold"), padx=2, pady=4)
        lblPRN_No.grid(row=1, column=0, sticky=W)
        txtPRN_No = Entry(DataFrameLeft, font=("arial",13,"bold"),textvariable = self.prn_var, width = 29)
        txtPRN_No.grid(row=1, column=1)

        lblTitle = Label(DataFrameLeft, bg = "powder blue" ,text="ID No:", padx=2, pady=4, font=("arial", 12,"bold"))
        lblTitle.grid(row=2, column=0, sticky=W)
        txtTitle = Entry(DataFrameLeft, font=("arial",13,"bold"), textvariable = self.id_var, width = 29)
        txtTitle.grid(row=2, column=1)

        lblFirstName = Label(DataFrameLeft, bg = "powder blue" ,text="FirstName", padx=2, pady=6, font=("arial", 12,"bold"))
        lblFirstName.grid(row=3, column=0, sticky=W)
        txtFirstName = Entry(DataFrameLeft, font=("arial",13,"bold"),textvariable = self.firstname_var, width = 29)
        txtFirstName.grid(row=3, column=1)

        lblLastName = Label(DataFrameLeft, bg = "powder blue" ,text="LastName", padx=2, pady=6, font=("arial", 12,"bold"))
        lblLastName.grid(row=4, column=0, sticky=W)
        txtLastName = Entry(DataFrameLeft, font=("arial",13,"bold"),textvariable = self.lastname_var, width = 29)
        txtLastName.grid(row=4, column=1)

        lblAddress1 = Label(DataFrameLeft, bg = "powder blue" ,text="Address1", padx=2, pady=6, font=("arial", 12,"bold"))
        lblAddress1.grid(row=5, column=0, sticky=W)
        txtAddress1 = Entry(DataFrameLeft, font=("arial",13,"bold"),textvariable = self.address1_var, width = 29)
        txtAddress1.grid(row=5, column=1)

        lblAddress2 = Label(DataFrameLeft, bg = "powder blue" ,text="Address2", padx=2, pady=6, font=("arial", 12,"bold"))
        lblAddress2.grid(row=6, column=0, sticky=W)
        txtAddress2 = Entry(DataFrameLeft, font=("arial",13,"bold"),textvariable = self.address2_var, width = 29)
        txtAddress2.grid(row=6, column=1)

        lblPostCode = Label(DataFrameLeft, bg = "powder blue" ,text="Post Code", padx=2, pady=6, font=("arial", 12,"bold"))
        lblPostCode.grid(row=7, column=0, sticky=W)
        txtPostCode = Entry(DataFrameLeft, font=("arial",13,"bold"), textvariable = self.postcode_var, width = 29)
        txtPostCode.grid(row=7, column=1)

        lblMobile = Label(DataFrameLeft, bg = "powder blue" ,text="Mobile", padx=2, pady=6, font=("arial", 12,"bold"))
        lblMobile.grid(row=8, column=0, sticky=W)
        txtMobile = Entry(DataFrameLeft, font=("arial",13,"bold"),textvariable = self.mobile_var, width = 29)
        txtMobile.grid(row=8, column=1)

        lblBookID = Label(DataFrameLeft, bg = "powder blue" ,text="Book Id: ", padx=2, pady=6, font=("arial", 12,"bold"))
        lblBookID.grid(row=0, column=2, sticky=W)
        txtBookID = Entry(DataFrameLeft, font=("arial",12,"bold"), textvariable = self.bookid_var, width = 27)
        txtBookID.grid(row=0, column=3)

        lblBookTitle = Label(DataFrameLeft, bg = "powder blue" ,text="Book Title: ", padx=2, pady=6, font=("arial", 12,"bold"))
        lblBookTitle.grid(row=1, column=2, sticky=W)
        txtBookTitle = Entry(DataFrameLeft, font=("arial",12,"bold"), textvariable = self.booktitle_var, width = 27)
        txtBookTitle.grid(row=1, column=3)

        lblAuthor = Label(DataFrameLeft, bg = "powder blue" ,text="Author Name: ", padx=2, pady=6, font=("arial", 12,"bold"))
        lblAuthor.grid(row=2, column=2, sticky=W)
        txtAuthor = Entry(DataFrameLeft, font=("arial",12,"bold"),textvariable = self.author_var, width = 27)
        txtAuthor.grid(row=2, column=3)

        lblDateBorrowed = Label(DataFrameLeft, bg = "powder blue" ,text="Date Borrowed: ", padx=2, pady=6, font=("arial", 12,"bold"))
        lblDateBorrowed.grid(row=3, column=2, sticky=W)
        txtDateBorrowed = Entry(DataFrameLeft, font=("arial",12,"bold"),textvariable = self.dateborrowed_var, width = 27)
        txtDateBorrowed.grid(row=3, column=3)
        
        lblDateDue = Label(DataFrameLeft, bg = "powder blue" ,text="Date Due: ", padx=2, pady=6, font=("arial", 12,"bold"))
        lblDateDue.grid(row=4, column=2, sticky=W)
        txtDateDue = Entry(DataFrameLeft, font=("arial",12,"bold"),textvariable = self.datedue_var, width = 27)
        txtDateDue.grid(row=4, column=3)

        lblDaysOnBook = Label(DataFrameLeft, bg = "powder blue" ,text="Days On Book: ", padx=2, pady=6, font=("arial", 12,"bold"))
        lblDaysOnBook.grid(row=5, column=2, sticky=W)
        txtDaysOnBook = Entry(DataFrameLeft, font=("arial",12,"bold"), textvariable = self.daysonbook, width = 27)
        txtDaysOnBook.grid(row=5, column=3)

        lblLateReturnFine = Label(DataFrameLeft, bg = "powder blue" ,text="Late Return Fine: ", padx=2, pady=6, font=("arial", 12,"bold"))
        lblLateReturnFine.grid(row=6, column=2, sticky=W)
        txtLateReturnFine = Entry(DataFrameLeft, font=("arial",12,"bold"),textvariable = self.latereturnfine_var, width = 27)
        txtLateReturnFine.grid(row=6, column=3)

        lblDateOverDue = Label(DataFrameLeft, bg = "powder blue" ,text="Date Over Due: ", padx=2, pady=6, font=("arial", 12,"bold"))
        lblDateOverDue.grid(row=7, column=2, sticky=W)
        txtDateOverDue = Entry(DataFrameLeft, font=("arial",12,"bold"),textvariable = self.dateoverdue, width = 27)
        txtDateOverDue.grid(row=7, column=3)

        lblActualPrice = Label(DataFrameLeft, bg = "powder blue" ,text="Actual Price: ", padx=2, pady=6, font=("arial", 12,"bold"))
        lblActualPrice.grid(row=8, column=2, sticky=W)
        txtActualPrice = Entry(DataFrameLeft, font=("arial",12,"bold"), textvariable = self.finalprice, width = 27)
        txtActualPrice.grid(row=8, column=3)

        # ----------------------------------------- Data FrameRight -----------------------------------------

        DataFrameRight= LabelFrame(frame, text="Book Details", bg="powder blue", fg="black",bd=12, relief=RIDGE, font=("arial", 12,"bold"))
        DataFrameRight.place(x=810, y=5, width=480, height=350)

        self.txtBox = Text(DataFrameRight, font=("arial", 12, "bold"), width=32, height=15, padx=2, pady=6)
        self.txtBox.grid(row=0, column=2)

        listScrollbar = Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0, column=1, sticky='ns')


        listBooks = ['Head First Book','Learn Python The Hard Way','Python Programming',"Secret Rahshy",'Python CookBook','Into Machine Learning','Fluent Python', 'Machine tecno',
                   'My Python', 'Joss Ellif guru', 'Elite Jungle python', 'Jungli Python', 'Mumbai Python', 'Pune Python', 'Machine python', 'Advance Python', 'Inton Python', 
                   'RedChilli Python', 'Ishq Python']
        

        def SelectBook(event=""):
            selection = listBox.curselection()
            if not selection:
                return
            value = str(listBox.get(selection[0]))

            x = value
            if (x == "Head First Book"):
                self.bookid_var.set("B001")
                self.booktitle_var.set("Head First Book")
                self.author_var.set("Kathy Sierra")
                
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs. 780")

            elif (x == "Learn Python The Hard Way"):
                self.bookid_var.set("B002")
                self.booktitle_var.set("Learn Python The Hard Way")
                self.author_var.set("Zed A. Shaw")
                
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs. 600")

            elif (x == "Python Programming"):
                self.bookid_var.set("B003")
                self.booktitle_var.set("Python Programming")
                self.author_var.set("John Zelle")
                
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs. 500")

            elif (x == "Secret Rahshy"):
                self.bookid_var.set("B004")
                self.booktitle_var.set("Secret Rahshy")
                self.author_var.set("Rahul Dravid")
                
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs. 450")

            elif (x == "Python CookBook"):
                self.bookid_var.set("B005")
                self.booktitle_var.set("Python CookBook")
                self.author_var.set("David Beazley")
                
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs. 700")

            elif (x == "Into Machine Learning"):
                self.bookid_var.set("B006")
                self.booktitle_var.set("Into Machine Learning")
                self.author_var.set("Andrew Ng")
                
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs. 900")

            elif (x == "Fluent Python"):
                self.bookid_var.set("B007")
                self.booktitle_var.set("Fluent Python")
                self.author_var.set("Luciano Ramalho")
                
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs. 800")

            elif (x == "Machine tecno"):
                self.bookid_var.set("B008")
                self.booktitle_var.set("Machine tecno")
                self.author_var.set("Ian Goodfellow")
                
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs. 950")

            elif (x == "My Python"):
                self.bookid_var.set("B009")
                self.booktitle_var.set("My Python")
                self.author_var.set("Sandy Kumar")
                
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs. 600")

            elif (x == "Joss Ellif guru"):
                self.bookid_var.set("B010")
                self.booktitle_var.set("Joss Ellif guru")
                self.author_var.set("Joss Ellif")
                
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs. 700")

            elif (x == "Elite Jungle python"):
                self.bookid_var.set("B011")
                self.booktitle_var.set("Elite Jungle python")
                self.author_var.set("Elite Jungle")
                
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs. 750")

            elif (x == "Jungli Python"):
                self.bookid_var.set("B012")
                self.booktitle_var.set("Jungli Python")
                self.author_var.set("Ramesh Patel")
                
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs. 800")

            elif (x == "Mumbai Python"):
                self.bookid_var.set("B013")
                self.booktitle_var.set("Mumbai Python")
                self.author_var.set("Manish Kumar")
                
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs. 650")

            elif (x == "Pune Python"):
                self.bookid_var.set("B014")
                self.booktitle_var.set("Pune Python")
                self.author_var.set("Puneet Singh")
                
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs. 700")

            elif (x == "Machine python"):
                self.bookid_var.set("B015")
                self.booktitle_var.set("Machine python")
                self.author_var.set("Mahesh Patel")
                
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs. 900")

            elif (x == "Advance Python"):
                self.bookid_var.set("B016")
                self.booktitle_var.set("Advance Python")
                self.author_var.set("Amit Bhandari")
                
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs. 950")

            elif (x == "Inton Python"):
                self.bookid_var.set("B017")
                self.booktitle_var.set("Inton Python")
                self.author_var.set("Inglish Jack")
                
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs. 800")

            elif (x == "RedChilli Python"):
                self.bookid_var.set("B018")
                self.booktitle_var.set("RedChilli Python")
                self.author_var.set("Ravi Shastri")
                
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs. 850")

            elif (x == "Ishq Python"):
                self.bookid_var.set("B019")
                self.booktitle_var.set("Ishq Python")
                self.author_var.set("Robert Lee")
                
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.latereturnfine_var.set("Rs. 50")
                self.dateoverdue.set("NO")
                self.finalprice.set("Rs. 600")


        listBox = Listbox(DataFrameRight, font=("arial", 12, "bold"), width=14, height=15)
        listBox.bind("<<ListboxSelect>>", SelectBook)
        listBox.grid(row=0, column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END, item)




        # ----------------------------------------- Buttons Frame -----------------------------------------
        Framebutton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        Framebutton.place(x=0, y=518, width=1350, height=70)

        btnAddData = Button(Framebutton, text="Add Data", command=self.add_data, font=("arial", 12, "bold"), width=20, bg="blue", fg="white")
        btnAddData.grid(row=0, column=0, padx = 5,pady = 5)

        btnShowData = Button(Framebutton, command = self.showData, text="Show Data", font=("arial", 12, "bold"), width=20, bg="blue", fg="white")
        btnShowData.grid(row=0, column=1, padx = 5,pady = 5)

        btnUpdateData = Button(Framebutton, command = self.update, text="Update", font=("arial", 12, "bold"), width=20, bg="blue", fg="white")
        btnUpdateData.grid(row=0, column=2, padx = 5,pady = 5)

        btnDeleteData = Button(Framebutton, command = self.delete, text="Delete", font=("arial", 12, "bold"), width=20, bg="blue", fg="white")
        btnDeleteData.grid(row=0, column=3, padx = 5,pady = 5)

        btnResetData = Button(Framebutton, command = self.reset, text="Reset", font=("arial", 12, "bold"), width=20, bg="blue", fg="white")
        btnResetData.grid(row=0, column=4, padx = 5,pady = 5)

        btnExit = Button(Framebutton,command = self.iExit, text="Exit", font=("arial", 12, "bold"), width=19, bg="blue", fg="white")
        btnExit.grid(row=0, column=5, padx = 5,pady = 5)


        # ----------------------------------------- Information Frame -----------------------------------------
        FrameDetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        FrameDetails.place(x=0, y=588, width=1350, height= 110)

        Table_frame = Frame(FrameDetails, bd=6, relief=RIDGE, bg="powder blue")
        Table_frame.place(x=0, y=2, width=1300, height = 90)

        xscroll = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(Table_frame, orient=VERTICAL)

        self.library_table = ttk.Treeview(Table_frame, columns=("membertype", "prn_no", "id_no", "first_name", "last_name",
                                                                 "address1", "address2", "post_code", "mobile", "bookid", 
                                                                 "booktitle", "author", "dateborrowed", "datedue", "days",
                                                                 "latereturnfine", "dateoverdue", "finalprice"), xscrollcommand=xscroll.set, 
                                                                 yscrollcommand=yscroll.set)
        
        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)


        self.library_table.heading("membertype", text="Member Type")
        self.library_table.heading("prn_no", text="PRN No.")
        self.library_table.heading("id_no", text="Id No.")
        self.library_table.heading("first_name", text="First Name")
        self.library_table.heading("last_name", text="Last Name")
        self.library_table.heading("address1", text="Address1")
        self.library_table.heading("address2", text="Address2")
        self.library_table.heading("post_code", text="Post Code")
        self.library_table.heading("mobile", text="Mobile No.")
        self.library_table.heading("bookid", text="Book Id")
        self.library_table.heading("booktitle", text="Book Title")
        self.library_table.heading("author", text="Author")
        self.library_table.heading("dateborrowed", text="Date Borrowed")
        self.library_table.heading("datedue", text="Date Due")
        self.library_table.heading("days", text="Days on Book")
        self.library_table.heading("latereturnfine", text="Late Return Fine")
        self.library_table.heading("dateoverdue", text="Date Over Due")
        self.library_table.heading("finalprice", text="Final Price")

        self.library_table["show"] = "headings"
        self.library_table.pack(fill=BOTH, expand=1)

        self.library_table.column("membertype", width=100)
        self.library_table.column("prn_no", width=100)
        self.library_table.column("id_no", width=100)
        self.library_table.column("first_name", width=100)
        self.library_table.column("last_name", width=100)
        self.library_table.column("address1", width=100)
        self.library_table.column("address2", width=100)
        self.library_table.column("post_code", width=100)
        self.library_table.column("mobile", width=100)
        self.library_table.column("bookid", width=100)
        self.library_table.column("booktitle", width=100)
        self.library_table.column("author", width=100)
        self.library_table.column("dateborrowed", width=100)
        self.library_table.column("datedue", width=100)
        self.library_table.column("days", width=100)
        self.library_table.column("latereturnfine", width=100)
        self.library_table.column("dateoverdue", width=100)
        self.library_table.column("finalprice", width=100)

        self.fetch_data() 
        self.library_table.bind("<ButtonRelease-1>", self.get_cursor) 


    def add_data(self):
            conn = pymysql.connect(host="localhost",user="root",password="SumitKumar2004@",database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute(""" insert into library values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)""",(
            str(self.member_var.get()),
            str(self.prn_var.get()),
            str(self.id_var.get()),
            str(self.firstname_var.get()),
            str(self.lastname_var.get()),
            str(self.address1_var.get()),
            str(self.address2_var.get()),
            str(self.postcode_var.get()),
            str(self.mobile_var.get()),
            str(self.bookid_var.get()),
            str(self.booktitle_var.get()),
            str(self.author_var.get()),
            str(self.dateborrowed_var.get()),
            str(self.datedue_var.get()),
            str(self.daysonbook.get()),
            str(self.latereturnfine_var.get()),
            str(self.dateoverdue.get()),
            str(self.finalprice.get())
            ))

            conn.commit()
            self.fetch_data()  
            conn.close()

            messagebox.showinfo("Success", "Data has been inserted successfully")

    def update(self):
        conn = pymysql.connect(host="localhost",user="root",password="SumitKumar2004@",database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute(""" UPDATE library SET Member = %s,FirstName = %s,LastName = %s,Address1 = %s,Address2 = %s,PostId = %s,Mobile = %s,BookId = %s,BookTitle = %s,Author = %s,
                             DateBorrowed = %s,DateDue = %s,DaysOnBook = %s,LateReturnFine = %s,DateOverDue = %s,FinalPrice = %s WHERE PRN_No = %s """, (
                                                                                                                                                            str(self.member_var.get()),
                                                                                                                                                            str(self.firstname_var.get()),
                                                                                                                                                            str(self.lastname_var.get()),
                                                                                                                                                            str(self.address1_var.get()),
                                                                                                                                                            str(self.address2_var.get()),
                                                                                                                                                            str(self.postcode_var.get()),
                                                                                                                                                            str(self.mobile_var.get()),
                                                                                                                                                            str(self.bookid_var.get()),
                                                                                                                                                            str(self.booktitle_var.get()),
                                                                                                                                                            str(self.author_var.get()),
                                                                                                                                                            str(self.dateborrowed_var.get()),
                                                                                                                                                            str(self.datedue_var.get()),
                                                                                                                                                            str(self.daysonbook.get()),
                                                                                                                                                            str(self.latereturnfine_var.get()),
                                                                                                                                                            str(self.dateoverdue.get()),
                                                                                                                                                            str(self.finalprice.get()),
                                                                                                                                                            str(self.prn_var.get()) 
                                                                                                                                                            ))


        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("Success", "Data has been updated successfully")
    

    def fetch_data(self):
        conn = pymysql.connect(host="localhost",user="root",password="SumitKumar2004@",database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from library")
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.library_table.delete(*self.library_table.get_children())
            for row in rows:
                self.library_table.insert("", "end", values=row)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row = self.library_table.focus()
        content = self.library_table.item(cursor_row)
        row = content['values']

        self.member_var.set(row[0])
        self.prn_var.set(row[1])
        self.id_var.set(row[2])
        self.firstname_var.set(row[3])
        self.lastname_var.set(row[4])
        self.address1_var.set(row[5])
        self.address2_var.set(row[6])
        self.postcode_var.set(row[7])
        self.mobile_var.set(row[8])
        self.bookid_var.set(row[9])
        self.booktitle_var.set(row[10])  
        self.author_var.set(row[11])
        self.dateborrowed_var.set(row[12])
        self.datedue_var.set(row[13])
        self.daysonbook.set(row[14])
        self.latereturnfine_var.set(row[15])
        self.dateoverdue.set(row[16])
        self.finalprice.set(row[17])

    def showData(self):
        self.txtBox.insert(END, "Member Type\t\t"+ self.member_var.get() + "\n")
        self.txtBox.insert(END, "PRN No:\t\t"+ self.prn_var.get() + "\n")
        self.txtBox.insert(END, "ID No:\t\t"+ self.id_var.get() + "\n")
        self.txtBox.insert(END, "First Name:\t\t"+ self.firstname_var.get() + "\n")
        self.txtBox.insert(END, "Last Name:\t\t"+ self.lastname_var.get() + "\n")
        self.txtBox.insert(END, "Address1:\t\t"+ self.address1_var.get() + "\n")
        self.txtBox.insert(END, "Address2:\t\t"+ self.address2_var.get() + "\n")
        self.txtBox.insert(END, "Post Code:\t\t"+ self.postcode_var.get() + "\n")
        self.txtBox.insert(END, "Mobile No:\t\t"+ self.mobile_var.get() + "\n")
        self.txtBox.insert(END, "Book Id:\t\t"+ self.bookid_var.get() + "\n")
        self.txtBox.insert(END, "Book Title:\t\t"+ self.booktitle_var.get() + "\n")
        self.txtBox.insert(END, "Author:\t\t"+ self.author_var.get() + "\n")
        self.txtBox.insert(END, "Date Borrowed:\t\t"+ self.dateborrowed_var.get() + "\n")
        self.txtBox.insert(END, "Date Due:\t\t"+ self.datedue_var.get() + "\n")
        self.txtBox.insert(END, "Days on Book:\t\t"+ self.daysonbook.get() + "\n")
        self.txtBox.insert(END, "Late Return Fine:\t\t"+ self.latereturnfine_var.get() + "\n")
        self.txtBox.insert(END, "Date Over Due:\t\t"+ self.dateoverdue.get() + "\n")
        self.txtBox.insert(END, "Final Price:\t\t"+ self.finalprice.get() + "\n")

    def reset(self):
        self.member_var.set("")
        self.txtPRN_No.config(state="normal")
        self.prn_var.set("")
        self.id_var.set("")
        self.firstname_var.set("")
        self.lastname_var.set("")
        self.address1_var.set("")
        self.address2_var.set("")
        self.postcode_var.set("")
        self.mobile_var.set("")
        self.bookid_var.set("")
        self.booktitle_var.set("")
        self.author_var.set("")
        self.dateborrowed_var.set("")
        self.datedue_var.set("")
        self.daysonbook.set("")
        self.latereturnfine_var.set("")
        self.dateoverdue.set("")
        self.finalprice.set("")
        self.txtBox.delete("1.0", END)

    def iExit(self):
        iExit = tkinter.messagebox.askyesno("Library Management System", "Do you want to exit")
        if iExit > 0:
            self.root.destroy()
            return
        
    def delete(self):
        if self.prn_var.get() == "" or self.id_var.get() == "":
            messagebox.showerror("Error", "Please select a record to delete")
        else:
            conn = pymysql.connect(host="localhost",user="root",password="SumitKumar2004@",database="mydata")
            my_cursor = conn.cursor()
            query = "delete from library where PRN_No = %s"
            value = (self.prn_var.get(),)
            my_cursor.execute(query, value)

            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success", "Data has been deleted successfully")

if __name__ == "__main__":
        print("Starting Library Management System...")
        root = Tk()
        obj = LibraryManagementSystem(root)
        root.mainloop()
    
