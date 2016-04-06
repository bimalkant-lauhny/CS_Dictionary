import Tkinter
import query_retrieval

class App:

    def __init__(self,master):

        self.frame = Tkinter.Frame(master,width=768, height=76, bg="",colormap="new", relief="raised")
        self.frame.pack()

        self.frame2 = Tkinter.Frame(master, width=768, height=500,bg="",colormap="new", bd=10)
        self.frame2.pack()

        self.search_var = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self.frame,highlightbackground="blue",highlightcolor="red",textvariable=self.search_var)
        self.entry.grid(row=0,column=0,ipadx=5,ipady=5,padx=20,pady=20)

        self.btn = Tkinter.Button(self.frame, text="Search",fg="Green", command=self.frame.quit)
        self.btn.grid(row=0,column=1,ipadx=3,ipady=3,padx=20,pady=20)

        self.check_var = Tkinter.IntVar()
        self.check_btn = Tkinter.Checkbutton(self.frame, text="Enable Advanced Search", variable = self.check_var,font=("Ubuntu","12",""),command=self.cb)
        self.check_btn.grid(row=0,column=2,padx=20,pady=20)

        inp_text=""
        for i in range(1000):
            inp_text+= (str(i)+"\n")

        self.scrollbar = Tkinter.Scrollbar(self.frame2)
        self.scrollbar.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)

        self.res_area  = Tkinter.Text(self.frame2,yscrollcommand=self.scrollbar.set,bg="yellow",bd=2)
        for i in range(1000):
            self.res_area.insert(Tkinter.END, str(i)+"\n")
        self.res_area.pack(side=Tkinter.LEFT,fill=Tkinter.BOTH)
        #self.res_area.grid(row=0,column=0,columnspan=3)
        '''
        self.res_area  = Tkinter.Listbox(self.frame2,yscrollcommand=self.scrollbar.set,bg="yellow",bd=2)
        for i in range(1000):
            self.res_area.insert(Tkinter.END, str(i))
        self.res_area.pack(side=Tkinter.LEFT,fill=Tkinter.BOTH)
        #self.res_area.grid(row=0,column=0,columnspan=3)
        '''
        self.scrollbar.config(command=self.res_area.yview)

    def cb(self):
        print self.check_var.get(), self.search_var.get()



root = Tkinter.Tk()
root.title("Computer Science Dictionary v1.0")
app = App(root)
root.mainloop()

