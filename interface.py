from tkinter import *
import customtkinter


class AppInt():
    def __init__(self) -> None:
        self.gl = 0
        self.root = customtkinter.CTk()
        self.frame = customtkinter.CTkFrame(self.root, corner_radius=10)
        self.checkboxes = []
        self.checkbox_vars = []
        self.textboxes = []
        self.textbox_vars = []
        self.new_button = customtkinter.CTkButton(
            self.frame, text="Add command", command=self.button_fnc)

    def get_val(self):
        if self.gl == 0:
            return 0
        else:
            return self.gl-1

    def refresh(self):
        self.run()

    def add_checkbox(self):
        combobox = customtkinter.CTkComboBox(self.frame,
                                             values=[
                                                 "Press", "Keep pressed"], height=40, state="readonly")
        self.checkboxes.append(combobox)
        combobox_var = customtkinter.StringVar(value="Press")
        self.checkbox_vars.append(combobox_var)

    def add_textbox(self):
        textbox = customtkinter.CTkEntry(self.frame, width=200, height=40,
                                         border_width=1, placeholder_text="Enter a key", text_color="silver")
        self.textboxes.append(textbox)
        self.textbox_vars.append('')

    def button_fnc(self):
        self.gl += 1
        self.add_checkbox()
        self.add_textbox()
        for i in range(0, self.gl):
            # print(self.checkboxes[i].get())
            self.checkbox_vars[i] = self.checkboxes[i].get()
            self.textbox_vars[i] = self.textboxes[i].get()
        print(self.textbox_vars)
        self.refresh()

    def run(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        # set initial value

        self.root.title('Add commands')
        self.root.geometry("800x500")

        self.frame.grid(row=0, column=0, padx=10,
                        pady=10, sticky=customtkinter.W)

        for i in range(0, self.gl):

            self.checkboxes[i].grid(row=i, column=0, padx=10,
                                    pady=10, sticky=customtkinter.W)
            self.textboxes[i].grid(
                row=i, column=1, padx=(0, 10), pady=10, sticky="ew")

        self.new_button.grid(row=self.get_val(), column=2, padx=50,
                             pady=10)

        self.root.mainloop()
