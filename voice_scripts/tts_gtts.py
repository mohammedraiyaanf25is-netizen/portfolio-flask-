from gtts import gTTS
import textwrap
import os

def generate_gtts(text, filename="instructions_gtts.mp3", lang="en", slow=False):
    tts = gTTS(text=text, lang=lang, slow=slow)
    tts.save(filename)
    print("Saved:", filename)

if __name__ == "__main__":
    instr = """
    Welcome. This voice will guide you to build your Flask portfolio.
    First create a folder, then make a virtual environment, install Flask, create app dot py and templates.
    Next run python app dot py and open the site on your browser.
    Finally push to GitHub and deploy to Render or PythonAnywhere.
    """
    # optional: wrap and save
    generate_gtts(textwrap.fill(instr, 80), filename=os.path.join("..","instructions_gtts.mp3"))