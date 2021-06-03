import tkinter
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title("Login to to-do list")
root.configure(bg="light grey")
username = input("Enter your username. > ")
password = input("Enter the password. > ")
if username != "Mum":
    root.configure(bg="red")
    tkinter.messagebox.showwarning(title="Incorrect username", message="Incorrect username")

if username == "Mum":
    if password != "Mum":
        root.configure(bg="red")
        tkinter.messagebox.showwarning(title="Incorrect password", message="Incorrect password")

    if password == "Mum":
        root.configure(bg="green")
        tkinter.messagebox.showinfo(title="Success!", message="""Success!
        
        Username and password are correct!
        
        You may now press 'OK'.""")
        root.title("Mum's To-Do List")
        root.configure(bg="light grey")
        def add_task():
            task = entry_task.get()
            if task != "":
                listbox_tasks.insert(tkinter.END, task)
                entry_task.delete(0, tkinter.END)
            else:
                tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")

        def delete_task():
            try:
                task_index = listbox_tasks.curselection()[0]
                listbox_tasks.delete(task_index)
            except:
                tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")

        def load_tasks():
            try:
                tasks = pickle.load(open("tasks3.dat", "rb"))
                listbox_tasks.delete(0, tkinter.END)
                for task in tasks:
                    listbox_tasks.insert(tkinter.END, task)
            except:
                tkinter.messagebox.showwarning(title="Warning!", message="Cannot find tasks3.dat.")

        def donothing():
            pass

        def save_tasks():
            tasks = listbox_tasks.get(0, listbox_tasks.size())
            pickle.dump(tasks, open("tasks3.dat", "wb"))

        # Create GUI
        frame_tasks = tkinter.Frame(root)
        frame_tasks.pack()

        listbox_tasks = tkinter.Listbox(frame_tasks, height=10, width=50)
        listbox_tasks.pack(side=tkinter.LEFT)

        scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
        scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
        scrollbar_tasks.config(command=listbox_tasks.yview)

        entry_task = tkinter.Entry(root, width=50)
        entry_task.pack()

        button_add_task = tkinter.Button(root, text="Add task", width=48, command=add_task)
        button_add_task.pack()

        button_delete_task = tkinter.Button(root, text="Delete task", width=48, command=delete_task)
        button_delete_task.pack()

        button_load_tasks = tkinter.Button(root, text="Load tasks", width=48, command=load_tasks)
        button_load_tasks.pack()

        button_save_tasks = tkinter.Button(root, text="Save tasks", width=48, command=save_tasks)
        button_save_tasks.pack()
        
        root.mainloop()