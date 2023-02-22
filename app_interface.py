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
        self.new_button = customtkinter.CTkButton(
            self.frame, text='Add command', command=self.button_fnc)
        self.start_button = customtkinter.CTkButton(
            self.frame, text='Start', command=self.button_fnc)
        self.help_button = customtkinter.CTkButton(
            self.frame, text='Help', command=self.see_help)
        self.save_button = customtkinter.CTkButton(
            self.frame, text="Save", command=self.save_fnc)
        self.text_voice_command = customtkinter.CTkEntry(self.frame, width=650, height=40,
                                                         border_width=1, placeholder_text="Add voice command",
                                                         text_color="silver")
        self.error = ''
        self.error_text = StringVar()
        self.error_label = customtkinter.CTkLabel(master=self.frame,
                                                  textvariable=self.error_text,
                                                  width=120,
                                                  height=25,
                                                  corner_radius=8)

        self.data = {'voice_command': '', 'actions': [], 'keys': []}

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
                                                 "Press", "Keep pressed"], height=40, state="readonly")
        self.checkboxes.append(combobox)
        combobox_var = customtkinter.StringVar(value="Press")
        self.data['actions'].append(combobox_var)

    def add_textbox(self):
        textbox = customtkinter.CTkEntry(self.frame, width=200, height=40,
                                         border_width=1, placeholder_text="Enter a key", text_color="silver")
        self.textboxes.append(textbox)
        self.data['keys'].append('')

    def see_help(self):
        # Toplevel object which will
        # be treated as a new window
        newWindow = customtkinter.CTkToplevel(self.root)

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        # set initial value

        newWindow.title('Add commands')
        newWindow.geometry("500x500")
        newWindow.attributes('-topmost', True)

        title = customtkinter.CTkLabel(master=newWindow,
                                       text="Instructions on how to use the application",
                                       text_color="#fff",
                                       #    bg_color="green",
                                       width=250,
                                       justify="left",
                                       anchor="w",
                                       font=('Helvetica', 18, 'bold')
                                       )
        instrucitons = customtkinter.CTkLabel(master=newWindow,
                                              text="Instructions on how to use the application",
                                              text_color="#fff",
                                              #    bg_color="green",
                                              width=250,
                                              justify="left",
                                              anchor="w",
                                              font=('Helvetica', 12)
                                              )
        # move the text to the left side of frame
        title.place(x=10, y=0)
        instrucitons.place(x=10, y=30)

    def save_fnc(self):
        self.error = ''
        self.error_label.grid_remove()

        for i in range(0, self.gl):
            self.data['actions'][i] = self.checkboxes[i].get()
            self.data['keys'][i] = self.textboxes[i].get()
        self.data['voice_command'] = self.text_voice_command.get()

        if len(self.data['actions']) == 0 or len(self.data['keys']) == 0 or self.data['actions'][0] == '' or self.data['keys'][0] == '' or self.data['voice_command'] == '':
            self.error = 'You must complete the field'
        if self.error != '':
            self.refresh()
            return
        print(self.data)
        res = SaveJson(self.data).execute()
        print(res)
        if res == True:
            self.error = 'Successfully added!'
        else:
            self.error = 'An error occured'
        self.refresh()

    def button_fnc(self):
        if self.gl > 0:
            self.data['voice_command'] = self.text_voice_command.get()
        self.gl += 1
        self.add_checkbox()
        self.add_textbox()
        for i in range(0, self.gl):
            self.data['actions'][i] = self.checkboxes[i].get()
            self.data['keys'][i] = self.textboxes[i].get()
        self.error = ''
        self.refresh()

#########################################################################################################
    def run(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        # set initial value

        self.root.title('Add commands')
        self.root.geometry("800x800")
        self.frame.grid(pady=10, sticky="nsew")
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=1)
        self.frame.pack()

        self.root.grid_columnconfigure(0, weight=1)

        if self.gl > 0:
            self.text_voice_command.grid(
                row=0, column=0, padx=10, pady=10, columnspan=3)

            self.new_button.grid(row=self.get_val(), column=2, padx=10,
                                 pady=10)

            self.save_button.grid(row=self.gl + 2, column=1, padx=100,
                                  pady=10)

        for i in range(0, self.gl):
            self.checkboxes[i].grid(row=i + 2, column=0, padx=10,
                                    pady=10)
            self.textboxes[i].grid(
                row=i + 2, column=1, padx=10, pady=10)

        if self.gl == 0:
            self.start_button.grid(row=self.get_val(), column=1, padx=10,
                                   pady=10)
            self.help_button.grid(row=self.get_val(), column=2, padx=10,
                                  pady=10)

            # if self.error ==
            #         text_var = tkinter.StringVar(value="CTkLabel")
        if self.error != '':
            self.error_text.set(self.error)
            self.error_label.grid(row=self.gl + 3, column=1, padx=10,
                                  pady=10)
        else:
            self.error_text.set(self.error)
            self.error_label.grid_remove()
        self.root.mainloop()
