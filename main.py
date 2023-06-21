import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import filedialog
from tkinter import ttk


class NoteApp:
    def __init__(self, master):
        self.master = master
        self.master.title("QuickNote")
        self.text = tk.Text(self.master)
        self.text.pack(fill=tk.BOTH, expand=True)
        self.filename = None

        # Call functions to create widgets and menu
        self.create_widgets()
        self.create_menu()

        # Set the protocol to call on_exit function when the window is closed
        self.master.protocol("WM_DELETE_WINDOW", self.on_exit)

        # Set focus to the text widget
        self.text.focus_set()
        self.text.edit_modified(False)

    # Function to create widgets
    def create_widgets(self):
        pass

    # Function to create menu
    def create_menu(self):
        # Create the menu bar
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)

        # Set the default style for ttk widgets
        style = ttk.Style()
        style.theme_use("default")

        # Configure the main menu bar
        style.configure("TMenuBar", background="#404040", foreground="#fff", font=("Segoe UI", 11))

        # Configure the options menus
        style.configure("TMenu", background="#404040", foreground="#fff", font=("Segoe UI", 11))
        style.map("TMenu", background=[("active", "#555")])

        # Create the file menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New Note", command=self.new_note, accelerator="Ctrl+N")
        file_menu.add_command(label="Open Note", command=self.open_note, accelerator="Ctrl+O")
        file_menu.add_command(label="Save Note", command=self.save_note, accelerator="Ctrl+S")
        file_menu.add_command(label="Delete Note", command=self.delete_note, accelerator="Ctrl+D")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.on_exit, accelerator="Ctrl+Q")
        menubar.add_cascade(label="File", menu=file_menu)

        # Create the edit menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Cut", command=lambda: self.text.event_generate("<<Cut>>"), accelerator="Ctrl+X")
        edit_menu.add_command(label="Copy", command=lambda: self.text.event_generate("<<Copy>>"), accelerator="Ctrl+C")
        edit_menu.add_command(label="Paste", command=lambda: self.text.event_generate("<<Paste>>"),
                              accelerator="Ctrl+V")
        menubar.add_cascade(label="Edit", menu=edit_menu)

    # Function to prompt user to save before performing an action
    def save_before_action(self):
        if self.text.edit_modified():
            result = messagebox.askyesno("Save Changes", "Do you want to save changes to this note?")
            if result:
                self.save_note()

    # Function to create a new note
    def new_note(self):
        self.save_before_action()
        self.filename = None
        self.text.delete(1.0, tk.END)

    # Function to open an existing note
    def open_note(self):
        self.save_before_action()
        self.filename = filedialog.askopenfilename(defaultextension=".txt")
        if self.filename:
            with open(self.filename, 'r') as f:
                self.text.delete(1.0, tk.END)
                self.text.insert(1.0, f.read())
                self.master.title(f"Note App - {self.filename}")

    # Function to save the current note
    def save_note(self):
        if self.filename is None:
            self.filename = filedialog.asksaveasfilename(defaultextension=".txt")
        if self.filename:
            with open(self.filename, 'w') as f:
                f.write(self.text.get(1.0, tk.END))
                messagebox.showinfo("Note Saved", "Note saved successfully.")
                self.master.title(f"Note App - {self.filename}")

    # Function to delete the current note after asking for confirmation
    def delete_note(self):
        result = messagebox.askyesno("Delete Note", "Are you sure you want to delete this note?")
        if result:
            self.new_note()

    # Function to check if the current note has unsaved changes before closing the application
    def on_exit(self):
        if self.text.edit_modified():
            save_prompt = messagebox.askyesnocancel("Save Changes", "Do you want to save changes to this note?")
            if save_prompt is not None:
                if save_prompt:
                    self.save_note()
                self.master.destroy()
        else:
            self.master.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    root.iconphoto(False, tk.PhotoImage(file="pencil.png"))
    app = NoteApp(root)
    root.mainloop()