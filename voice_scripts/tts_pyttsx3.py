import pyttsx3
import textwrap
import os

def generate_voice(text, filename="instructions_offline.mp3", rate=160, voice_index=None):
    engine = pyttsx3.init()
    # optional: set voice
    voices = engine.getProperty('voices')
    if voice_index is not None and 0 <= voice_index < len(voices):
        engine.setProperty('voice', voices[voice_index].id)
    engine.setProperty('rate', rate)
    # pyttsx3 saves only to WAV by some backends; we will save by writing to file using save_to_file
    engine.save_to_file(text, filename)
    engine.runAndWait()
    print("Saved:", filename)

if __name__ == "__main__":
    # A short instructional text — you can expand or read from a file
    instructions = """
    Step one: open the terminal and create a new folder named my underscore portfolio underscore py.
    Step two: create and activate a python virtual environment.
    Step three: install flask and required packages.
    Step four: create app dot py and templates folder with html pages.
    Step five: run the app with python app dot py and open localhost five thousand.
    Step six: push the project to GitHub and deploy to Render or PythonAnywhere.
    """
    # wrap text to keep it neat
    generate_voice(textwrap.fill(instructions, 80), filename=os.path.join("..","instructions_offline.mp3"))