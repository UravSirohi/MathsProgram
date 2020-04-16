import tkinter as tk


def test_function(entry):
    print('This entry is:', entry)


root = tk.Tk()

canvas = tk.Canvas(root, height=500, width=600, bg='Black')
canvas.pack()

frame = tk.Frame(root, bg='dodgerblue', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=40,
                   command=lambda: test_function(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='dodgerblue', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

root.mainloop()

