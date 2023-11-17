# compiler.py

from languageAPI import riskuap_builder, InvalidArgvLength
import argparse
import tkinter as tk
from tkinter import filedialog
from tkinter.messagebox import showinfo
from ttkthemes import ThemedTk
from tkinter import ttk
import os
import platform


def clear_terminal():
    system = platform.system()
    
    if system == "Windows":
        os.system("cls")
    elif system == "Linux" or system == "Darwin":  # Якщо ви використовуєте macOS, включіть його в цей блок
        os.system("clear")



def compile_files(files):
    try:
        builder_: riskuap_builder = riskuap_builder(files, [], False)
        print(builder_.start_language_builder())
    except SyntaxError as e:
        print(f"Warning: SyntaxError in the file {files}. Compilation will continue. Error details: {e}")
    except AttributeError as e:
        print(f"Error: {e}. Compilation failed. Please check if the provided file is valid.")

def select_file(entry):
    file_path = filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(0, file_path)

    # Виклик функції для очищення терміналу після вибору файлу
    clear_terminal()


# ...

def open_file_editor(selected_file):
    def save_content():
        try:
            with open(selected_file, 'w') as file:
                content = file_content_text.get("1.0", tk.END)
                file.write(content)
            showinfo("Save", "File saved successfully.")

            # Виклик функції для очищення терміналу після збереження
            clear_terminal()

        except Exception as e:
            showinfo("Error", f"Error saving file: {e}")

    def save_on_ctrl_s(event):
        if (event.state & 0x4) != 0:  # Check if Ctrl key is pressed (Ctrl+S)
            # Display information about saving
            print("Saving file...")

            # Save the content
            save_content()

    def highlight_words(event=None):
        words_to_highlight = ["import", "as", "env", "function",
                                "end", "cmd", "conditional"]  # Add your list of words here
        for word in words_to_highlight:
            file_content_text.tag_configure(word, foreground="red")  # Set the tag color (foreground) to red

            start_index = "1.0"
            while True:
                start_index = file_content_text.search(word, start_index, stopindex="end", nocase=True)
                if not start_index:
                    break
                end_index = f"{start_index}+{len(word)}c"
                file_content_text.tag_add(word, start_index, end_index)
                start_index = end_index

    file_edit_window = tk.Toplevel()
    file_edit_window.title("File Editor")
    file_edit_window.geometry("500x500")
    file_edit_window.resizable(False, False)

    # Menu bar
    menu_bar = tk.Menu(file_edit_window)
    file_edit_window.config(menu=menu_bar)

    # File menu
    file_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="File", menu=file_menu)

    # Save option in the File menu
    file_menu.add_command(label="Save", command=save_content)

    # Highlight words option in the File menu
    file_menu.add_command(label="Highlight Words", command=highlight_words)

    # Text widget to display the content of the selected file
    file_content_text = tk.Text(file_edit_window, wrap=tk.WORD, height=20, width=60)
    file_content_text.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Use a system-independent default font
    file_content_text.configure(font=("TkDefaultFont", 14))

    # Scrollbar for vertical scrolling
    scrollbar = tk.Scrollbar(file_edit_window, command=file_content_text.yview)
    scrollbar.grid(row=0, column=1, sticky="nse")

    file_content_text.config(yscrollcommand=scrollbar.set)

    # Set the content of the text widget
    try:
        with open(selected_file, 'r') as file:
            content = file.read()
            file_content_text.insert(tk.END, content)
    except FileNotFoundError:
        file_content_text.insert(tk.END, f"File not found: {selected_file}")
    except Exception as e:
        file_content_text.insert(tk.END, f"Error reading file: {e}")

    # Configure row and column weights to make the Text widget and scrollbar expand
    file_edit_window.grid_rowconfigure(0, weight=1)
    file_edit_window.grid_columnconfigure(0, weight=1)

    # Bind Ctrl+S to save_content
    file_edit_window.bind('<Control-s>', save_on_ctrl_s)

    # Bind KeyRelease event to highlight_words
    file_content_text.bind('<KeyRelease>', highlight_words)

# ...






def gui():
    def update_button_states():
        file_selected = bool(file_entry.get())
        edit_button["state"] = tk.NORMAL if file_selected else tk.DISABLED
        compile_button["state"] = tk.NORMAL if file_selected else tk.DISABLED

    def compile_and_display_message():
        compile_files(file_entry.get())
        showinfo("Compilation", "Compilation completed.")

    root = ThemedTk(theme="breeze")  # Set the theme to "breeze"
    root.title("RAPL Compiler GUI")
    root.geometry("308x300")
    root.resizable(False, False)

    # Entry widget to display the selected file path
    file_entry = ttk.Entry(root, width=40)
    file_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

    # Button to open the file dialog
    select_button = ttk.Button(root, text="Select File", command=lambda: [select_file(file_entry), update_button_states()])
    select_button.grid(row=1, column=0, pady=10, columnspan=2)

    # Button to open the file editor window
    edit_button = ttk.Button(root, text="Edit", command=lambda: open_file_editor(file_entry.get()), state=tk.DISABLED)
    edit_button.grid(row=2, column=0, pady=10, columnspan=2)

    # Button to compile the file
    compile_button = ttk.Button(root, text="Compile", command=compile_and_display_message, state=tk.DISABLED)
    compile_button.grid(row=3, column=0, columnspan=2, pady=10)

    root.mainloop()


# ...

def main():
    parser = argparse.ArgumentParser(description='RAPL Compiler script.')
    
    parser.add_argument('-mode', choices=['normal', 'gui'], help='Mode for script execution: normal or gui')
    parser.add_argument('-file', dest='file_path', nargs='?', help='Path to the file to compile')

    args = parser.parse_args()

    if args.mode == 'gui':
        gui()
    elif args.mode == 'normal':
        compile_files(args.file_path)
    else:
        print("Error: Unknown mode.")

if __name__ == "__main__":
    main()

# ...

