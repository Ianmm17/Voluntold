import tkinter as tk
from tkinter import Label, Toplevel

def add_person():
    global pop
    pop = Toplevel(root)
    pop.title('Add Person')
    pop.geometry('250x150')
    pop.configure(background='#3A3B3c')

    entry = tk.Entry(pop, width=25)
    entry.grid(row=0, column=0, padx=10)

    enter = tk.Button(pop, text='Enter', command=lambda: choice("Enter", entry.get()))
    cancel = tk.Button(pop, text='Cancel', command=lambda: choice("Cancel", ""))
    entry.pack(pady=5)
    enter.pack(pady=5)
    cancel.pack()

def remove_person():
    for name in homies_list:
        if people_list.get(tk.ANCHOR) == name:
            homies_list.remove(name)
    people_list.delete(tk.ANCHOR)
    

def choice(choice, entry):
    pop.destroy()
    if choice == 'Enter':
        homies_list.append(entry)
        people_list.insert('end', entry)
    elif choice == 'Cancel':
        return

# Testing only purpose
def test(homies_list):
    blank_str = ""
    for person in homies_list:
        blank_str += f"{person}, "
    my_label.configure(text=blank_str)



    

homies_list = ['Eric Nuno', 'Carl', 'Philip', 'Ben', 'Matt', 'Piere', 'Logan', 'Jacbo', 'Jason', 'Richard', 'Ian Miller']

root = tk.Tk()
root.geometry("800x800")
root.configure(background='#242526')

people_list = tk.Listbox(root, height=25)
add_person_button = tk.Button(root, text='+', command=add_person)
remove_person_button = tk.Button(root, text='-', command=remove_person)

# this is for testing purposes only, shows on gui that my homies_list is being updated as i add/remove peps
test_b = tk.Button(root, text='test', command=lambda: test(homies_list))
global my_label
my_label = Label(root, text='')


for person in homies_list:
    people_list.insert('end', person)

people_list.pack(pady=25)
add_person_button.pack()
remove_person_button.pack()
test_b.pack()
my_label.pack()


root.mainloop()