import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Create the main window
root = tk.Tk()
root.geometry("300x400")
root.title("Simple Calculator")

# Entry widget
entry = tk.Entry(root, font="Arial 20")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Frame for buttons
frame = tk.Frame(root)
frame.pack()

# Buttons layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

# Create and place buttons in grid
for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(expand=True, fill='both')
    for btn_text in row:
        btn = tk.Button(row_frame, text=btn_text, font="Arial 18", relief='ridge', border=1)
        btn.pack(side='left', expand=True, fill='both', padx=1, pady=1)
        btn.bind("<Button-1>", click)

# Run the application
root.mainloop()
