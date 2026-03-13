from tkinter import *
items = ['Korean', 'English', 'Math', 'Science', 'History']

def delete():
    global items
    selection = listbox.curselection()
    if(len(selection) == 0):
        return
    
    value = listbox.get(selection[0])
    ind = items.index(value)
    del items[ind]
    listbox.delete(selection[0])
    print(items)

root = Tk()

listbox = Listbox(root)
listbox.pack()

#리스트 박스에 데이터 추가

for i in range(len(items)):
    listbox.insert(END, items[i])

buttondel = Button(root, width=10, text="Delete", overrelief="solid", command=delete)
buttondel.pack()

root.mainloop()

    
    