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

        self.btn = Tkinter.Button(self.frame, text="Search", command=self.fetch_res)
        self.btn.grid(row=0,column=1,ipadx=3,ipady=3,padx=20,pady=20)

        self.check_var = Tkinter.IntVar()
        self.check_btn = Tkinter.Checkbutton(self.frame, text="Enable Advanced Search", variable = self.check_var,font=("Ubuntu","12",""))
        self.check_btn.grid(row=0,column=2,padx=20,pady=20)

        self.scrollbar = Tkinter.Scrollbar(self.frame2)
        self.scrollbar.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)

        self.res_area  = Tkinter.Text(self.frame2,padx=5,pady=5,spacing2=5,yscrollcommand=self.scrollbar.set,bd=2,wrap=Tkinter.WORD)
        self.res_area.config(state=Tkinter.DISABLED)
        self.res_area.pack(side=Tkinter.LEFT,fill=Tkinter.BOTH)
        #self.res_area.grid(row=0,column=0,columnspan=3)

    def fetch_res(self):
        self.results = query_retrieval.main(self.check_var.get(),self.search_var.get())
        self.res_area.config(state=Tkinter.NORMAL)
        self.res_area.delete(1.0, Tkinter.END)
        self.res_area.insert(Tkinter.END,"\n\n")
        if len(self.results)==0:
            self.res_area.insert(Tkinter.END,"No results found!!!")
        for i in self.results:
            self.res_area.insert(Tkinter.END, str(i[1])+"\n\n")
        self.res_area.config(state=Tkinter.DISABLED)
        '''
        self.res_area  = Tkinter.Listbox(self.frame2,yscrollcommand=self.scrollbar.set,bg="yellow",bd=2)
        for i in range(1000):
            self.res_area.insert(Tkinter.END, str(i))
        self.res_area.pack(side=Tkinter.LEFT,fill=Tkinter.BOTH)
        #self.res_area.grid(row=0,column=0,columnspan=3)
        '''
        self.scrollbar.config(command=self.res_area.yview)

root = Tkinter.Tk()
root.title("Computer Science Dictionary v1.0")
app = App(root)
root.mainloop()

