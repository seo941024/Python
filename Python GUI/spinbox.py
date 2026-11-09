from tkinter import *

root = Tk()
root.title("Siso")
root.geometry("300x200+100+100")
root.resizable(True, True)

label = Label(root, text="숫자를 입력하거나 선택하시오", height=3)
label.pack()

def value_check(value):
    label.config(text="숫자를 입력하거나 선택하시오")
    
    if value == "":
        return True

    valid = False
    if value.isdigit():
        if 0 <= int(value) <= 100:
            valid = True

    return valid

def value_error(value):
    label.config(text=str(value) + "는 잘못된 값입니다.\n다시 입력하세요.")

validate_command = (root.register(value_check), '%P')
invalid_command = (root.register(value_error), '%P')

spinbox = Spinbox(
    root,
    width=10,
    from_=0,
    to=100,
    validate='all',
    validatecommand=validate_command,
    invalidcommand=invalid_command
)
spinbox.pack()

root.mainloop()