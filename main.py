from final_word import Word
import json
import execution
import pyttsx3 as pt

if __name__ == '__main__':
    engine = pt.init()
    engine.setProperty(
        'voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')

    execution.execute_app('please open word', engine)
