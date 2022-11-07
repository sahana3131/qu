import tkinter as tk
from turtle import bgcolor
import fc_1_0
import fc_1_1
import fc_2_0
import fc_2_1

def func(args, args1):
    #print(args)
    if args=="H":
        #hadamard gate
        if args1=="0":
            fc_1_0.main()
        elif args1=="1":
            fc_1_1.main()



    elif args == "X":
        #X gate
        if args1=="0":
            fc_2_0.main()
        elif args1=="1":
            fc_2_1.main()    

root = tk.Tk()
root.title("Fossclub")
root.geometry("750x250")
label = tk.Label(root, text="hello world", font=('Georgia 18 bold')).pack(padx=20, pady = 20, anchor="n", side = tk.TOP)

label1 = tk.Label(root, text="Choose a gate", font=('Georgia 10 bold')).pack(padx=10, pady = 10, anchor="w", side = tk.LEFT)
text = tk.StringVar()

text.set("Choose a gate")

option = tk.OptionMenu(root, text, "H", "X").pack(pady = 20, anchor = "w")

label2 = tk.Label(root, text="Choose an input", font=('Georgia 10 bold')).pack(padx=10, pady = 10, anchor="e", side = tk.RIGHT)
text2 = tk.StringVar()
text2.set("Choose an input")

option2 = tk.OptionMenu(root, text2, "0", "1").pack(pady = 20, anchor = "e")
get_option = ""
B = tk.Button(root, text="Submit", command=lambda: func(""+text.get(), ""+text2.get())).pack()


root.mainloop()