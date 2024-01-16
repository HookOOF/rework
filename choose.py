import tkinter as tk
import json
def chs(labels):
    global var,var1,root1
    root1 = tk.Toplevel()  
    root1.title("Radio Buttons Example")

    var = tk.StringVar()
    var1 = labels
    option1 = tk.Radiobutton(root1, text="Confirm", variable=var, value="Confirm")
    option2 = tk.Radiobutton(root1, text="Decline", variable=var, value="Decline")

    show_button = tk.Button(root1, text="Show Selection", command=show_selection)

    global selected_option
    selected_option = tk.StringVar()
    selection_label = tk.Label(root1, textvariable=selected_option)

    option1.grid(row=0, column=0, padx=10, pady=5)
    option2.grid(row=1, column=0, padx=10, pady=5)
    show_button.grid(row=3, column=0, pady=10)
    selection_label.grid(row=4, column=0, pady=5)

def show_selection():
    selected_option.set(f"Selected option: {var.get()}")
    if var.get() == 'Confirm':
        parameters = {
        "labels": var1
    }
        with open("parameters.json", "w") as json_file:
            json.dump(parameters, json_file)
        root1.destroy()
        return True
    else:
        return False
