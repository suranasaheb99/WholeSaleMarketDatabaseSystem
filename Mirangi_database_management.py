from tkinter import *
import tkinter.messagebox
import MirangiDatabase_Backend

#import MirangiDatabase
#frontEND
class Mirangi:
    
    def __init__(self, root):
        self.root = root
        self.root.title("MIRANGI_PRINTS_DATABASE")
        self.root.geometry("1350x7500+0+0")
        self.root.config(bg="cadet blue")

        worker_id = StringVar()
        first_name = StringVar()
        last_name = StringVar()
        birth_date = StringVar()
        address = StringVar()
        mobile_number = IntVar()

#=====================================================Functions===============================================================
        def iExit():
            iExit = tkinter.messagebox.askyesno("MIRANGI_PRINTS_DATABASE","Bubyee buddy!see u later.")
            if iExit > 0:
                root.destroy()
                return

        def clearData():
            self.txtworker_id.delete(0,END)
            self.txtfirst_name.delete(0,END)
            self.txtlast_name.delete(0,END)
            self.txtbirth_date.delete(0,END)
            self.txtaddress.delete(0,END)
            self.txtmobile_number.delete(0,END)
        
        def addData():
            if(len(worker_id.get())!=0):
                MirangiDatabase_Backend.addwdata(worker_id.get(), first_name.get(), last_name.get(), birth_date.get(), address.get(), mobile_number.get())
                workerlist.delete(0,END)
                workerlist.insert(END,(worker_id.get(), first_name.get(), last_name.get(), birth_date.get(), address.get(), mobile_number.get()))

        def DisplayData():
            workerlist.delete(0,END)
            for row in MirangiDatabase_Backend.viewData():
                workerlist.insert(END,row,str(""))

        def WorkerRec(event):
            global wk
            searchWorker = workerlist.curselection()[0]
            wk = workerlist.get(searchWorker)

            self.txtworker_id.delete(0,END)
            self.txtworker_id.insert(END,wk[0])
            self.txtfirst_name.delete(0,END)
            self.txtfirst_name.insert(END,wk[1])
            self.txtlast_name.delete(0,END)
            self.txtlast_name.insert(END,wk[2])
            self.txtbirth_date.delete(0,END)
            self.txtbirth_date.insert(END,wk[3])
            self.txtaddress.delete(0,END)
            self.txtaddress.insert(END,wk[4])
            self.txtmobile_number.delete(0,END)
            self.txtmobile_number.insert(END,wk[5])

        def DeleteData():
            if(len(worker_id.get())!=0):
                MirangiDatabase_Backend.deleteRec(wk[0])
                clearData()
                DisplayData()

        def searchDatabase():
            workerlist.delete(0,END)
            for row in MirangiDatabase_Backend.searchData(worker_id.get(), first_name.get(), last_name.get(), birth_date.get(), address.get(), mobile_number.get()):
                workerlist.insert(END,row,str(""))

        def update():
            if(len(worker_id.get())!=0):
                MirangiDatabase_Backend.deleteRec(wk[0])
            if(len(worker_id.get())!=0):
                 MirangiDatabase_Backend.addwdata(worker_id.get(), first_name.get(), last_name.get(), birth_date.get(), \
                                                  address.get(), mobile_number.get())
            workerlist.delete(0,END)
            workerlist.insert(END,(worker_id.get(), first_name.get(), last_name.get(), birth_date.get(), \
                                  address.get(), mobile_number.get()))
        
#=====================================================FREMES===========================================================

        MainFrame = Frame(self.root, bg="cadet blue")
        MainFrame.grid()

        TitFrame = Frame(MainFrame, bd=2, padx=54,pady=8, bg="Ghost White", relief=RIDGE)
        TitFrame.pack(side=TOP)

        self.lblTit = Label(TitFrame, font=('arial', 42,'bold'), text="MIRANGI PRINTS DATABASE MANAGEMENT SYSTEM", bg="Ghost White")
        self.lblTit.grid()
        
        ButtonFrame = Frame(MainFrame, bd=2, width=1350, height=70, padx=18,pady=10, bg="Ghost White", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20,pady=20, bg="cadet blue", relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLeft = LabelFrame(DataFrame, bd=1, width=1000, height=600, padx=20, bg="Ghost White", font=('arial', 20,'bold'), text="WORKERS AUTHENTICATIONS\n", relief=RIDGE)
        DataFrameLeft.pack(side=LEFT)

        DataFrameRight = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31,pady=3, bg="Ghost White", relief=RIDGE, font=('arial', 20,'bold'), text="WORKERS DETAILS\n")
        DataFrameRight.pack(side=RIGHT)
#=====================================================LABELS AND ENTRIES=============================================

        self.lblworker_id = Label(DataFrameLeft, font=('arial', 20,'bold'), text="WorkerID:", padx=2,pady=2, bg="Ghost White")
        self.lblworker_id.grid(row=0, column=0, sticky=W)
        self.txtworker_id = Entry(DataFrameLeft, font=('arial', 20,'bold'), textvariable=worker_id, width=39, bg="Ghost White")
        self.txtworker_id.grid(row=0, column=1)

        self.lblfirst_name = Label(DataFrameLeft, font=('arial', 20,'bold'), text="FirstName:", padx=2,pady=2, bg="Ghost White")
        self.lblfirst_name.grid(row=1, column=0, sticky=W)
        self.txtfirst_name = Entry(DataFrameLeft, font=('arial', 20,'bold'), textvariable=first_name, width=39, bg="Ghost White")
        self.txtfirst_name.grid(row=1, column=1)

        self.lbllast_name = Label(DataFrameLeft, font=('arial', 20,'bold'), text="LastName:", padx=2,pady=2, bg="Ghost White")
        self.lbllast_name.grid(row=2, column=0, sticky=W)
        self.txtlast_name = Entry(DataFrameLeft, font=('arial', 20,'bold'), textvariable=last_name, width=39, bg="Ghost White")
        self.txtlast_name.grid(row=2, column=1)

        self.lblbirth_date = Label(DataFrameLeft, font=('arial', 20,'bold'), text="Birth_Date:", padx=2,pady=2, bg="Ghost White")
        self.lblbirth_date.grid(row=3, column=0, sticky=W)
        self.txtbirth_date = Entry(DataFrameLeft, font=('arial', 20,'bold'), textvariable=birth_date, width=39, bg="Ghost White")
        self.txtbirth_date.grid(row=3, column=1)

        self.lbladdress = Label(DataFrameLeft, font=('arial', 20,'bold'), text="Address:", padx=2,pady=2, bg="Ghost White")
        self.lbladdress.grid(row=4, column=0, sticky=W)
        self.txtaddress = Entry(DataFrameLeft, font=('arial', 20,'bold'), textvariable=address, width=39, bg="Ghost White")
        self.txtaddress.grid(row=4, column=1)

        self.lblmobile_number = Label(DataFrameLeft, font=('arial', 20,'bold'), text="PhoneNumber:", padx=2,pady=2, bg="Ghost White")
        self.lblmobile_number.grid(row=5, column=0, sticky=W)
        self.txtmobile_number = Entry(DataFrameLeft, font=('arial', 20,'bold'), textvariable=mobile_number, width=39, bg="Ghost White")
        self.txtmobile_number.grid(row=5, column=1)

#=====================================================LISTS AND SCROLLBAR WIDGET=============================================

        scrollbar = Scrollbar(DataFrameRight)
        scrollbar.grid(row=0, column=1, sticky='ns')

        workerlist = Listbox(DataFrameRight, width=41, height=16, font=('arial', 12,'bold'), yscrollcommand=Scrollbar.set)
        workerlist.bind('<<ListboxSelect>>', WorkerRec)
        workerlist.grid(row=0, column=0, padx=8)
        scrollbar.config(command = workerlist.yview)
#=====================================================BUTTON WIDGET=============================================        
        self.btnAddData = Button(ButtonFrame, text="Add New", font=('arial', 20,'bold'), height=1,width=10, bd=4, command=addData)
        self.btnAddData.grid(row=0, column=0)

        self.btnDisplayData = Button(ButtonFrame, text="Display", font=('arial', 20,'bold'), height=1,width=10, bd=4, command=DisplayData)
        self.btnDisplayData.grid(row=0, column=1)

        self.btnClearData = Button(ButtonFrame, text="Clear", font=('arial', 20,'bold'), height=1,width=10, bd=4, command=clearData)
        self.btnClearData.grid(row=0, column=2)

        self.btnDeleteData = Button(ButtonFrame, text="Delete", font=('arial', 20,'bold'), height=1,width=10, bd=4, command=DeleteData)
        self.btnDeleteData.grid(row=0, column=3)

        self.btnSearchData = Button(ButtonFrame, text="Search", font=('arial', 20,'bold'), height=1,width=10, bd=4, command=searchDatabase)
        self.btnSearchData.grid(row=0, column=4)

        self.btnUpdateData = Button(ButtonFrame, text="Update", font=('arial', 20,'bold'), height=1,width=10, bd=4, command=update)
        self.btnUpdateData.grid(row=0, column=5)

        self.btnExit = Button(ButtonFrame, text="Exit", font=('arial', 20,'bold'), height=1,width=10, bd=4, command=iExit)
        self.btnExit.grid(row=0, column=6)

            
if __name__ == '__main__':
    MirangiDatabase_Backend.workerDATA()
    root = Tk()
    application = Mirangi(root)
    root.mainloop()
