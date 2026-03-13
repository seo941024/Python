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

listbox = Listbox(root, height=0, selectmode= "extended")
listbox.pack()

#리스트 박스에 데이터 추가

for i in range(len(items)):
    listbox.insert(END, items[i])

def add(event):
    global items
    items.append(entry.get())
    listbox.insert(END, entry.get())
    entry.delete(0, 'end')

#삭제버튼 생성
buttondel = Button(root, width=10, text="Delete", overrelief="solid", command=delete)
buttondel.pack()

#entry 생성
entry = Entry(root, width=30)
entry.bind("<Return>", add)
entry.pack()

root.mainloop()
