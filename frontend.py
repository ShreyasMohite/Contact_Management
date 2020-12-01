from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
import tkinter.messagebox
from tkinter.ttk import Notebook,Progressbar,Combobox
from backend import *




class Contact:
    def __init__(self,root):
        self.root=root
        self.root.title("Contact Management")
        self.root.geometry("450x600")
        self.root.iconbitmap("logo235.ico")
        self.root.resizable(0,0)

        names=StringVar()
        contacts=StringVar()
        ids=StringVar()
        sid=StringVar()




        def on_enter1(e):
            button_see_contacts['background']="black"
            button_see_contacts['foreground']="cyan"  
        def on_leave1(e):
            button_see_contacts['background']="SystemButtonFace"
            button_see_contacts['foreground']="SystemButtonText"

            

        def on_enter2(e):
            button_clear_tree['background']="black"
            button_clear_tree['foreground']="cyan"  
        def on_leave2(e):
            button_clear_tree['background']="SystemButtonFace"
            button_clear_tree['foreground']="SystemButtonText"


        def on_enter3(e):
            but_add['background']="black"
            but_add['foreground']="cyan"  
        def on_leave3(e):
            but_add['background']="SystemButtonFace"
            but_add['foreground']="SystemButtonText"

            

        def on_enter4(e):
            but_edit['background']="black"
            but_edit['foreground']="cyan"  
        def on_leave4(e):
            but_edit['background']="SystemButtonFace"
            but_edit['foreground']="SystemButtonText"


        def on_enter5(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"  
        def on_leave5(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"

        def on_enter6(e):
            but_delete['background']="black"
            but_delete['foreground']="cyan"  
        def on_leave6(e):
            but_delete['background']="SystemButtonFace"
            but_delete['foreground']="SystemButtonText"

        def on_enter7(e):
            but_clear_del['background']="black"
            but_clear_del['foreground']="cyan"  
        def on_leave7(e):
            but_clear_del['background']="SystemButtonFace"
            but_clear_del['foreground']="SystemButtonText"


        def clear_name_contact():
            names.set("")
            contacts.set("")
            sid.set("")

        
        def clear_id():
            ids.set("")

        
        def trees():
            contact_trees.delete(*contact_trees.get_children())



        def add_number():
            if(len(names.get())!=0):
                if(len(contacts.get())!=0):

                    add_contacts(names.get(),contacts.get())
                    view_number()
                    clear_name_contact()

                else:
                    tkinter.messagebox.showerror("Error","Please Enter mobile number")
            else:
                tkinter.messagebox.showerror("Error","Please Enter name")


            
        
        def view_number():
            contact_trees.delete(*contact_trees.get_children())
            for row in view_contacts():
                contact_trees.insert('',END,values=row)

        

        def delete_number(): 
            if(len(ids.get())!=0):      
                delete_contact(ids.get())
                view_number()
            else:
                tkinter.messagebox.showerror("Error","Please Enter number to delete contact")

        
        def update_number():
            if(len(names.get())!=0):
                delete_contact(sid.get())
            if(len(names.get())!=0):
                add_contacts(names.get(),contacts.get())
                clear_name_contact()
                view_number()

            





            




#==================Frame===========================#
        
        mainframe=Frame(self.root,width=450,height=600,relief="ridge",bd=3)
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=444,height=220,relief="ridge",bd=3)
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=444,height=373,relief="ridge",bd=3)
        secondframe.place(x=0,y=220)


#=====================firstframe====================#
        tabControl = Notebook(firstframe,width=435,height=189) 
  
        see_contacts = Frame(tabControl,background="grey57") 
        add_edit_contacts = Frame(tabControl,background="grey87") 
        delete_contacts = Frame(tabControl,background="grey77") 
        
        tabControl.add(see_contacts, text ='See Contacts') 
        tabControl.add(add_edit_contacts, text ='Add/Edit Contacts')
        tabControl.add(delete_contacts, text ='Delete Contacts') 
        tabControl.place(x=0,y=0)

#========================see contacts======================#
        
        button_see_contacts=Button(see_contacts,text="See Contacts",width=14,font=('times new roman',15),cursor="hand2",command=view_number)
        button_see_contacts.place(x=130,y=30)
        button_see_contacts.bind("<Enter>",on_enter1)
        button_see_contacts.bind("<Leave>",on_leave1)

        button_clear_tree=Button(see_contacts,text="Clear",width=14,font=('times new roman',15),cursor="hand2",command=trees)
        button_clear_tree.place(x=130,y=120)
        button_clear_tree.bind("<Enter>",on_enter2)
        button_clear_tree.bind("<Leave>",on_leave2)


#========================Add/Edit Contact=================#
        
        lab_name=Label(add_edit_contacts,text="Enter Name",font=('times new roman',14),bg="grey87")
        lab_name.place(x=160,y=5)

        ent_name=Entry(add_edit_contacts,width=35,font=('times new roman',13),relief="ridge",bd=4,textvariable=names)
        ent_name.place(x=55,y=30)

        ent_sid=Entry(add_edit_contacts,width=3,font=('times new roman',13),relief="ridge",bd=4,textvariable=sid)
        ent_sid.place(x=1,y=0)

        lab_contact_number=Label(add_edit_contacts,text="Enter Contact Number",font=('times new roman',14),bg="grey87")
        lab_contact_number.place(x=130,y=75)

        ent_contact_number=Entry(add_edit_contacts,width=35,font=('times new roman',13),relief="ridge",bd=4,textvariable=contacts)
        ent_contact_number.place(x=55,y=100)

        but_add=Button(add_edit_contacts,text="Add Contacts",width=12,font=('times new roman',12),cursor="hand2",command=add_number)
        but_add.place(x=20,y=150)
        but_add.bind("<Enter>",on_enter3)
        but_add.bind("<Leave>",on_leave3)

        but_edit=Button(add_edit_contacts,text="Edit Contacts",width=12,font=('times new roman',12),cursor="hand2",command=update_number)
        but_edit.place(x=159,y=150)
        but_edit.bind("<Enter>",on_enter4)
        but_edit.bind("<Leave>",on_leave4)

        but_clear=Button(add_edit_contacts,text="Clear",width=12,font=('times new roman',12),cursor="hand2",command=clear_name_contact)
        but_clear.place(x=300,y=150)
        but_clear.bind("<Enter>",on_enter5)
        but_clear.bind("<Leave>",on_leave5)

#====================Delete Contact==================================#
        lab_id=Label(delete_contacts,text="ID",font=('times new roman',14),bg="grey77")
        lab_id.place(x=200,y=5)

        ent_id=Entry(delete_contacts,width=35,font=('times new roman',13),relief="ridge",bd=4,textvariable=ids)
        ent_id.place(x=55,y=40)

        but_delete=Button(delete_contacts,text="Delete Contacts",width=12,font=('times new roman',14),cursor="hand2",command=delete_number)
        but_delete.place(x=35,y=100)
        but_delete.bind("<Enter>",on_enter6)
        but_delete.bind("<Leave>",on_leave6)

        but_clear_del=Button(delete_contacts,text="Clear",width=14,font=('times new roman',14),cursor="hand2",command=clear_id)
        but_clear_del.place(x=250,y=100)
        but_clear_del.bind("<Enter>",on_enter7)
        but_clear_del.bind("<Leave>",on_leave7)
        



#===================secondframe======================================#

        def  game(event):
            crow=contact_trees.focus()
            contents=contact_trees.item(crow)
            row=contents['values']
            sid.set(row[0])
            names.set(row[1])
            contacts.set(row[2])

        scol=Scrollbar(secondframe,orient="vertical")
        scol.place(relx=1, rely=0, relheight=1, anchor='ne')

        contact_trees=ttk.Treeview(secondframe,columns=("ID","Name","Contact Number"),height=17,yscrollcommand=scol.set)
        contact_trees.heading("ID",text="ID")
        contact_trees.heading("Name",text="Name")
        contact_trees.heading("Contact Number",text="Contact Number")
        contact_trees['show']="headings"
        contact_trees.column("ID",width=50,minwidth=10)
        contact_trees.column("Name",width=170,minwidth=40)
        contact_trees.column("Contact Number",width=196,minwidth=40)
        contact_trees.place(x=0,y=0)

        contact_trees.bind('<ButtonRelease-1>',game)






if __name__ == "__main__":
    root=Tk()
    Contact(root)
    root.mainloop()
