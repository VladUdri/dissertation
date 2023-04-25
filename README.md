# System manual
## Run the code
1. Go to the Github repository of the project: https://github.com/VladUdr
i/dissertation
2. You can either choose to download the source code from the Github repository,
or you can use the source code provided with this dissertation.
3. Go to the root directory of this project
4. The next step is to install the required libraries. The required libraries are:
- AppOpener: ```pip install AppOpener```
- Customtkinter: ```pip install customtkinter```
- nltk: ```pip install nltk```
- psutil: ```pip install psutil```
- PyAutoGUI: ```pip install PyAutoGUI```
- PyGetWindow: ```pip install PyGetWindow```
- pytesseract: ```pip install pytesseract```
- pyttsx3: ```pip install pyttsx4```
- screen brightness control: ```pip install screen-brightness-control```
- sounddevice: ```pip install sounddevice```
- vosk: pip install vosk
- word2number: pip install word2number
5. Locate the requirements.txt
6. Install all the requirements using the identified requirements.txt files via the
following command: ```pip install -r requirements.txt```
7. You will need to change the path of the Vosk model (variable self.model path
in init voice.py) with the actual path of the model from your computer. The
result should look something like this: self.model\_path="D:\\pythonProj
ect1\\assets\\vosk-model-en-us-daanzu-20200905-lgraph"
8. Next, run the code using the following command ```python main.py```. If the system
prompts you to install more libraries install the library via a pip command.

### Use another Vosk model
If you want to use another Vosk model than the one provided, you need to go https://alphacephei.com/vosk/models and download the model you need.
Based on my testing, the one included in the source code performed the best for me.
After you download the model, you need to add the model to the project’s directory and copy it’s path. Just like before, paste it into the variable self.model path in init voice.py.

# User Manual
## How to use the application
After running the application, to start the system say ”initialize application” and the application will start. Next, you can say the commands you want to be executed commands. They need to be in a normal order, otherwise the application might behave unexpectedly. An example of this is:
1. ”open Microsoft Word”
2. ”create new blank”
3. ”change font”
4. ”start dictating”
5. ”stop dictating”
6. ”save document”
7. ”close Microsoft Word”

The complete list of default available actions is presented in the tables from below. The first table contains the recommended spoken command, and the apps where they are available. If you try to perform an action on an app on which it is not intended to be used, the system will not perform it. 
The second table contains the commands available when dictating. 
| **Action**          | **Application where action is available** |
|----------------------|-------------------------------------------|
| open                 | notepad, outlook, word                    |
| close                | notepad, google, outlook, word            |
| new document         | word                                      |
| new blank            | word                                      |
| save document        | word                                      |
| change font          | word                                      |
| change size          | word                                      |
| create new notepad   | notepad                                   |
| save note notepad    | notepad                                   |
| start dictating      | word, outlook, notepad                    |
| increase brightness  | computer                                  |
| decrease brightness  | computer                                  |
| change brightness    | computer                                  |
| increase volume      | computer                                  |
| decrease volume      | computer                                  |
| change volume        | computer                                  |
| create event         | outlook                                   |
| add title            | outlook                                   |
| add start time       | outlook                                   |
| add finish time      | outlook                                   |
| make all day         | outlook                                   |
| save event           | outlook                                   |
| write body           | outlook                                   |
| compose email        | outlook                                   |
| subject              | outlook                                   |
| destination email    | outlook                                   |
| cc email             | outlook                                   |
| send email           | outlook                                   |
| email body           | outlook                                   |
| search google        | google                                    |
| search wikipedia     | google                                    |
| new command          | Start the application interface           |

| **Dictation actions**                                                                                            |
|--------------------------------------------------------------------------------------------------|
|bold|
| italic/ italics                                                                                  |
| underlined/ underline                                                                            |
| increase font size                                                                               |
| decrease font size                                                                               |
| position center/ align center/ align centre/ alignment center/ alignment centre/ position centre |
| position left/ align left/ alignment left                                                        |
| position right/ align right/ alignment right                                                     |
| position justify/ align justify/ alignment justify                                               |
| full stop/ period symbol/ dot symbol                                                             |
| commma symbol/ pause mark                                                                        |
| question mark                                                                                    |
| exclamation mark                                                                                 |
| at symbol                                                                                        |
| backspace/ delete word/ back space/ delete                                                       |
| erase line/ delete line                                                                          |
| open font editor                                                                                 |
| change font size/ set font size                                                                  |
| change font                                                                                      |
| new line                                                                                         |
| new title                                                                                        |
| stop dictating                                                                                   |

## How to use the GUI
If you want to incorporate new custom actions or commands into the program,
simply say ”new command.” This will open up the GUI and display
all available options. From there, you can either select ”Help” to access instructions
on how to use the system or add new commands. Clicking the green
button will create a new row with keyboard shortcuts, and selecting
”Keep Press” means that the key will be held down while the next key is pressed
(e.g. in ”ctrl+c,” the ctrl key is held down while the ”c” key is pressed). To delete
everything, click the red button, and to save your action, click the dark blue ”save”
button.
