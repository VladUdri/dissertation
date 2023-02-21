from tkinter import *
import customtkinter
from save_json import SaveJson


class AppInt():
    def __init__(self) -> None:
        self.gl = 0
        self.root = customtkinter.CTk()
        self.frame = customtkinter.CTkFrame(self.root, corner_radius=10)
        self.checkboxes = []
        self.textboxes = []
        self.text_voice_command = ''
        self.apps_for_command = ''
        self.new_button = customtkinter.CTkButton(
            self.frame, text="Add command", command=self.button_fnc)
        self.save_button = customtkinter.CTkButton(
            self.frame, text="Save", command=self.save_fnc)
        self.text_voice_command = customtkinter.CTkEntry(self.frame, width=650, height=40,
                                                         border_width=1, placeholder_text="Add voice command",
                                                         text_color="silver")
        self.apps_for_command = customtkinter.CTkEntry(self.frame, width=650, height=40,
                                                       border_width=1,
                                                       placeholder_text="Apps for which should work (optional)",
                                                       text_color="silver")
        self.error_label = customtkinter.CTkLabel(master=self.frame,
                                    textvariable='text_var',
                                    width=120,
                                    height=25,
                                    # fg_color=("white"),
                                    corner_radius=8)

        self.data = {'voice_command': '',
                     'apps_command': '', 'actions': [], 'keys': []}

    def get_val(self):
        if self.gl == 0:
            return 0
        else:
            return self.gl + 1

    def refresh(self):
        self.run()

    def add_checkbox(self):
        combobox = customtkinter.CTkComboBox(self.frame,
                                             values=[
                                                 "Press", "Keep pressed"], height=40, state="readonly", border_color='red')
        self.checkboxes.append(combobox)
        combobox_var = customtkinter.StringVar(value="Press")
        self.data['actions'].append(combobox_var)

    def add_textbox(self):
        textbox = customtkinter.CTkEntry(self.frame, width=200, height=40,
                                         border_width=1, placeholder_text="Enter a key", text_color="silver")
        self.textboxes.append(textbox)
        self.data['keys'].append('')

    def save_fnc(self):
        for i in range(0, self.gl):
            # print(self.checkboxes[i].get())
            if self.data['actions'][i] != None and self.data['keys'][i] != '':
                self.data['actions'][i] = self.checkboxes[i].get()
                self.data['keys'][i] = self.textboxes[i].get()
            self.data['voice_command'] = self.text_voice_command.get()
            self.data['apps_command'] = self.apps_for_command.get()

        SaveJson(self.data).execute()
        # print(self.data)

    def button_fnc(self):
        if self.gl > 0:
            self.data['voice_command'] = self.text_voice_command.get()
            self.data['apps_command'] = self.apps_for_command.get()
        self.gl += 1
        self.add_checkbox()
        self.add_textbox()
        for i in range(0, self.gl):
            self.data['actions'][i] = self.checkboxes[i].get()
            self.data['keys'][i] = self.textboxes[i].get()

        self.refresh()

    def run(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        # set initial value

        self.root.title('Add commands')
        self.root.geometry("800x500")

        self.frame.grid(pady=10, sticky="we")
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=1)
        self.frame.pack()

        self.root.grid_columnconfigure(0, weight=1)

        if self.gl > 0:
            self.text_voice_command.grid(
                row=0, column=0, padx=10, pady=10, columnspan=3)

            self.apps_for_command.grid(
                row=1, column=0, padx=10, pady=10, columnspan=3)

        for i in range(0, self.gl):
            self.checkboxes[i].grid(row=i + 2, column=0, padx=10,
                                    pady=10)
            self.textboxes[i].grid(
                row=i + 2, column=1, padx=10, pady=10)

        self.new_button.grid(row=self.get_val(), column=2, padx=10,
                             pady=10)
        if self.gl > 0:
            self.save_button.grid(row=self.gl + 2, column=1, padx=100,
                                  pady=10)

        # if self.error ==
#         text_var = tkinter.StringVar(value="CTkLabel")

        
        self.error_label.grid(row=self.gl + 3, column=1, padx=10,
                             pady=10)

        self.root.mainloop()
