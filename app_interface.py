from tkinter import *
import customtkinter
from save_json import SaveJson
import json


class AppInterface():
    def __init__(self) -> None:
        # Initializes the object with instance variables
        self.gl = 0
        self.root = customtkinter.CTk()
        self.frame = customtkinter.CTkFrame(self.root, corner_radius=10)
        self.checkboxes = []
        self.textboxes = []
        self.new_button = customtkinter.CTkButton(
            self.frame, text='Add new', fg_color='#008000', hover_color='#006400', command=self.add_new_func, height=45, font=('Helvetica', 18), text_color='#fff')
        self.start_button = customtkinter.CTkButton(self.frame, fg_color='red', hover_color='#D10000',
                                                    text_color='#fff', text='Reset', command=self.reset, height=45, font=('Helvetica', 18))
        self.help_button = customtkinter.CTkButton(
            self.frame, text='Help', command=self.see_help, height=45, font=('Helvetica', 18), text_color='#fff')
        self.save_button = customtkinter.CTkButton(
            self.frame, text="Save", fg_color='#00008B', hover_color='#00003f', command=self.save_fnc, height=45, font=('Helvetica', 18), text_color='#fff')
        self.text_voice_command = customtkinter.CTkEntry(self.frame, width=650, height=45,
                                                         border_width=1, placeholder_text="Add speech command",
                                                         text_color="black", font=('Helvetica', 18))
        self.error = ''
        self.error_text = StringVar()
        self.error_label = customtkinter.CTkLabel(master=self.frame,
                                                  textvariable=self.error_text,
                                                  width=120,
                                                  height=25,
                                                  corner_radius=8)
        self.data = {'voice_command': '', 'actions': [], 'keys': []}
        self.s = "In order to start the application say \"initialise application\".\nTo stop the application say \"close application\".\n\nTo add new custom commands, say \"new command\", then the application user interface will start.\nThe red button will reset the interface and empty all the boxes.\n The green button will add a new fild for a command. \nThe light blue button will save the custom action."
        with open('jsons/all_commands.json') as f:
            comm = json.load(f)
        with open('jsons/custom_commands.json') as g:
            custom_comm = json.load(g)
        with open('jsons/write_commands.json') as h:
            write_comm = json.load(h)

        self.s += '\n\nYour custom actions\n\n'
        if len(custom_comm.keys()) > 1:
            for i in custom_comm.keys():
                self.s += (str(i) + '\n')
        self.s += '\n\n\nDefault actions and the appplications where they are available\n\n'
        for i in comm:
            if len(comm[i]['apps']) > 0:
                self.s += (str(' '.join(comm[i]['patterns'][0])) +
                           ' -> ' + str(', '.join(comm[i]['apps'])) + '\n')
            else:
                self.s += (str(' '.join(comm[i]['patterns'][0])) +
                           ' -> ' + 'Start the application interface\n')
        self.s += '\n\n\nDefault dictation actions\n\n'
        for i in write_comm:
            self.s += (str('/ '.join(write_comm[i]['pattern'])) + '\n')

    def get_val(self):
        # Returns the value of the instance variable 'gl'
        if self.gl == 0:
            return 2
        else:
            return self.gl + 1

    def refresh(self):
        # Calls the 'run()' method
        self.run()

    def add_checkbox(self):
        # Creates a combobox with two values, 'Press' and 'Keep pressed'
        combobox = customtkinter.CTkComboBox(self.frame,
                                             values=["Press", "Keep pressed"], height=45,
                                             state="readonly", font=('Helvetica', 15))
        # Appends the combobox to the checkboxes list
        self.checkboxes.append(combobox)
        # Creates a StringVar object with value 'Press' and appends to the actions list in data dictionary
        combobox_var = customtkinter.StringVar(value="Press")
        self.data['actions'].append(combobox_var)

    def add_textbox(self):
        # Creates an entry textbox with width 200 and height 45
        textbox = customtkinter.CTkEntry(self.frame, width=200, height=45,
                                         border_width=1, placeholder_text="Enter a key",
                                         text_color="black", font=('Helvetica', 18))
        # Appends the textbox to the textboxes list
        self.textboxes.append(textbox)
        # Appends an empty string to the keys list in data dictionary
        self.data['keys'].append('')

    def see_help(self):
        # Creates a new window
        newWindow = customtkinter.CTkToplevel(self.root)
        customtkinter.set_appearance_mode("light")
        newWindow.title('Help')
        newWindow.geometry("800x500")
        newWindow.attributes('-topmost', True)

        # Adds a label to display title
        title = customtkinter.CTkLabel(master=newWindow,
                                    text="Help - Instructions on how to use the application",
                                    text_color="#000",
                                    width=250,
                                    justify="left",
                                    anchor="w",
                                    font=('Helvetica', 18, 'bold'))
        title.place(x=10, y=0)

        # Adds a CTkText widget to display instructions
        instructions_text = customtkinter.CTkTextbox(master=newWindow,
                                                wrap="word",
                                                font=('Helvetica', 12),
                                                height=450,
                                                width=780)
        instructions_text.insert("1.0", self.s)
        instructions_text.place(x=10, y=30)

        # Adds a CTkScrollbar widget for the CTkText widget
        scrollbar = customtkinter.CTkScrollbar(master=newWindow,
                                            orientation='vertical',height=400,
                                            command=instructions_text.yview)
        scrollbar.place(x=780, y=30)
        instructions_text.configure(yscrollcommand=scrollbar.set)


    def save_fnc(self):
        # Clear previous errors
        self.error = ''
        self.error_label.grid_remove()

        # Update data dictionary with current values
        for i in range(0, self.gl):
            self.data['actions'][i] = self.checkboxes[i].get()
            self.data['keys'][i] = self.textboxes[i].get()
        self.data['voice_command'] = self.text_voice_command.get()

        # Check for incomplete fields
        if len(self.data['actions']) == 0 or len(self.data['keys']) == 0 or self.data['actions'][0] == '' or self.data['keys'][0] == '' or self.data['voice_command'] == '':
            self.error = 'You must complete the field'

        # If there is an error, refresh the page and return
        if self.error != '':
            self.refresh()
            return

        # Save data to JSON file
        res = SaveJson(self.data).execute()

        # Show success or error message
        if res == True:
            self.error = 'Successfully added!'
        else:
            self.error = 'An error occured'
        self.refresh()

    def add_new_func(self):
        # Check if maximum number of functions has been reached
        if self.gl < 7:
            # Update data dictionary with current values
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

    def reset(self):
        # Reset all values and clear inputs
        self.gl = 0
        self.data = {'voice_command': '', 'actions': [], 'keys': []}
        for check in self.checkboxes:
            check.destroy()
        self.checkboxes.clear()
        for tb in self.textboxes:
            tb.destroy()
        self.textboxes.clear()
        self.text_voice_command.delete(0, END)
        self.error = ''
        self.refresh()

    def run(self):
        # Set appearance mode of tkinter window
        customtkinter.set_appearance_mode("light")

        # Set title and size of tkinter window
        self.root.title('Add action')
        self.root.geometry("900x750")
        self.frame.grid(pady=10, sticky="nsew")
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=1)
        self.frame.pack()

        self.root.grid_columnconfigure(0, weight=1)

        # Show voice command input and buttons for adding and saving functions
        if self.gl >= 0:
            self.text_voice_command.grid(
                row=1, column=0, padx=10, pady=10, columnspan=3)

            self.new_button.grid(row=self.get_val(), column=2, padx=10,
                                 pady=10)

            self.save_button.grid(row=self.gl + 2, column=1, padx=100,
                                  pady=10)

        # Show checkboxes and textboxes for each function
        for i in range(0, self.gl):
            self.checkboxes[i].grid(row=i + 2, column=0, padx=10,
                                    pady=10)
            self.textboxes[i].grid(
                row=i + 2, column=1, padx=10, pady=10)

        # Define the position of the start button
        self.start_button.grid(row=0, column=0, padx=10, pady=10)

        # Define the position of the help button
        self.help_button.grid(row=0, column=2, padx=10, pady=10)

        # If there is an error, display the error message
        if self.error != '':
            self.error_text.set(self.error)
            self.error_label.grid(row=self.gl + 3, column=1, padx=10, pady=10)
        # If there is no error, remove the error message
        else:
            self.error_text.set(self.error)
            self.error_label.grid_remove()

        # Start the event loop
        self.root.mainloop()
