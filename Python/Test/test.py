import tkinter as tk
from tkinter import messagebox

def create_app():
    # 1. Main Window Setup
    root = tk.Tk()
    root.title("Old-School Tkinter Showcase")
    root.geometry("750x550")
    root.minsize(600, 450)
    
    # In old Tkinter, we often manually set background colors to make things look cohesive
    bg_color = "#d9d9d9"  # Classic light grey
    root.configure(bg=bg_color)

    # --- ACTION FUNCTIONS ---
    def handle_submit():
        name = name_entry.get()
        role = role_var.get()
        subscribed = sub_var.get()
        
        if not name:
            messagebox.showwarning("Input Error", "Please enter a name!")
            return
            
        status = "Subscribed" if subscribed else "Not Subscribed"
        info_text = f"User: {name}\nRole: {role}\nStatus: {status}"
        
        status_label.config(text=f"Last Action: Added {name}")
        messagebox.showinfo("Data Submitted", info_text)
        
        # Insert formatted text into the old Listbox data grid
        formatted_row = f"{name.ljust(25)} | {role.ljust(20)} | {status}"
        data_listbox.insert(tk.END, formatted_row)
        
        # Clear input
        name_entry.delete(0, tk.END)

    def trigger_progress():
        # Old Tkinter doesn't have a Progressbar widget! 
        # We have to fake it by dynamically altering the text of a label.
        current_text = progress_label.cfill_text
        if len(current_text) < 15:
            progress_label.cfill_text += "■■"
            progress_label.config(text=progress_label.cfill_text)
            root.after(200, trigger_progress)
        else:
            progress_label.cfill_text = ""
            progress_label.config(text="[Empty]")
            messagebox.showinfo("Task Complete", "Background processing finished!")

    # 2. Layout Framework (Old Tkinter doesn't have a Tab/Notebook widget!)
    # We simulate tabs by using two main frames and showing/hiding them with buttons.
    def show_tab1():
        tab2_frame.pack_forget()
        tab1_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        btn_tab1.config(relief=tk.SUNKEN, bg="#bbbbbb")
        btn_tab2.config(relief=tk.RAISED, bg=bg_color)

    def show_tab2():
        tab1_frame.pack_forget()
        tab2_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        btn_tab1.config(relief=tk.RAISED, bg=bg_color)
        btn_tab2.config(relief=tk.SUNKEN, bg="#bbbbbb")

    # Tab Navigation Bar
    nav_frame = tk.Frame(root, bg=bg_color)
    nav_frame.pack(fill=tk.X, padx=10, pady=(10, 0))

    btn_tab1 = tk.Button(nav_frame, text="Control Panel & Form", command=show_tab1, bd=2)
    btn_tab1.pack(side=tk.LEFT, padx=2)
    
    btn_tab2 = tk.Button(nav_frame, text="Data Viewer Table", command=show_tab2, bd=2)
    btn_tab2.pack(side=tk.LEFT, padx=2)

    # Base Containers for the "Tabs"
    tab1_frame = tk.Frame(root, bg=bg_color)
    tab2_frame = tk.Frame(root, bg=bg_color)

    # ==================== TAB 1: CONTROLS & FORM ====================
    # Left Column: Form Group (Using standard Frame with a border to fake a LabelFrame)
    form_frame = tk.Frame(tab1_frame, bd=2, relief=tk.GROOVE, bg=bg_color)
    form_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10), pady=10)
    
    tk.Label(form_frame, text="--- User Information Form ---", bg=bg_color, font=("Arial", 10, "bold")).pack(anchor=tk.W, padx=5, pady=5)

    tk.Label(form_frame, text="Full Name:", bg=bg_color).pack(anchor=tk.W, padx=5, pady=(5, 2))
    name_entry = tk.Entry(form_frame, width=30, bd=2, relief=tk.SUNKEN)
    name_entry.pack(fill=tk.X, padx=5, pady=(0, 10))

    tk.Label(form_frame, text="Account Role:", bg=bg_color).pack(anchor=tk.W, padx=5, pady=(5, 2))
    role_var = tk.StringVar(value="Standard User")
    # Old Tkinter doesn't have a Dropdown/Combobox! We use an OptionMenu instead.
    role_menu = tk.OptionMenu(form_frame, role_var, "Standard User", "Moderator", "Administrator")
    role_menu.config(bg=bg_color, bd=2, relief=tk.RAISED)
    role_menu.pack(fill=tk.X, padx=5, pady=(0, 10))

    sub_var = tk.BooleanVar(value=True)
    sub_check = tk.Checkbutton(form_frame, text="Subscribe to automated updates", variable=sub_var, bg=bg_color, activebackground=bg_color)
    sub_check.pack(anchor=tk.W, padx=5, pady=10)

    # Old-school heavy bordered button
    submit_btn = tk.Button(form_frame, text="Submit Data", command=handle_submit, bg=bg_color, bd=3, relief=tk.RAISED)
    submit_btn.pack(fill=tk.X, padx=5, pady=(10, 5))

    # Right Column: System Controls
    util_frame = tk.Frame(tab1_frame, bd=2, relief=tk.GROOVE, bg=bg_color)
    util_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, pady=10)
    
    tk.Label(util_frame, text="--- System Controls ---", bg=bg_color, font=("Arial", 10, "bold")).pack(anchor=tk.W, padx=5, pady=5)

    tk.Label(util_frame, text="Task Automation Progress:", bg=bg_color).pack(anchor=tk.W, padx=5, pady=(5, 2))
    
    # Custom faked progress text bar
    progress_label = tk.Label(util_frame, text="[Empty]", bg="white", fg="blue", bd=2, relief=tk.SUNKEN, width=25, anchor=tk.W)
    progress_label.cfill_text = ""
    progress_label.pack(fill=tk.X, padx=5, pady=(0, 5))

    run_btn = tk.Button(util_frame, text="Simulate Task", command=trigger_progress, bg=bg_color, bd=2, relief=tk.RAISED)
    run_btn.pack(anchor=tk.W, padx=5, pady=(0, 20))

    tk.Label(util_frame, text="System Log / Custom Notes:", bg=bg_color).pack(anchor=tk.W, padx=5, pady=(5, 2))
    log_text = tk.Text(util_frame, height=6, width=30, bd=2, relief=tk.SUNKEN, wrap=tk.WORD)
    log_text.insert(tk.END, "System active...\nUsing classic engine.\n")
    log_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    # ==================== TAB 2: DATA TABLE ====================
    tk.Label(tab2_frame, text="Submitted Information Database (Classic List)", font=("Arial", 12, "bold"), bg=bg_color).pack(anchor=tk.W, pady=(0, 10))

    # Old Tkinter has no multi-column Grid (Treeview). We build a header label and use a standard Listbox.
    header_text = f"{'Name'.ljust(25)} | {'Role'.ljust(20)} | Subscription Status"
    header_label = tk.Label(tab2_frame, text=header_text, font=("Courier", 10, "bold"), bg="#aaaaaa", anchor=tk.W, justify=tk.LEFT)
    header_label.pack(fill=tk.X)

    # Monospaced font ensures columns stay roughly aligned in a plain text listbox
    data_listbox = tk.Listbox(tab2_frame, font=("Courier", 10), bd=2, relief=tk.SUNKEN)
    data_listbox.pack(fill=tk.BOTH, expand=True)

    # Inject Mock Baseline Data
    data_listbox.insert(tk.END, f"{'Alice Smith'.ljust(25)} | {'Administrator'.ljust(20)} | Subscribed")
    data_listbox.insert(tk.END, f"{'Bob Jones'.ljust(25)} | {'Standard User'.ljust(20)} | Not Subscribed")

    # ==================== GLOBAL FOOTER STATUS BAR ====================
    status_label = tk.Label(root, text="System Status: Ready", relief=tk.SUNKEN, bd=1, anchor=tk.W, bg=bg_color)
    status_label.pack(side=tk.BOTTOM, fill=tk.X)

    # Initialize by displaying the first tab
    show_tab1()
    root.mainloop()

if __name__ == "__main__":
    create_app()