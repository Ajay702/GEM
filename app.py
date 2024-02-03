from flask import Flask, render_template, request
import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


userdata = {'api_key': 'AIzaSyBAU40ZzbdBd50jtFQ_iolr9HT4rBY7yJs'}
GOOGLE_API_KEY = userdata.get('api_key')
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)






app = Flask(__name__)

main = ""
submit_clicked = False

@app.route('/', methods=['GET', 'POST'])
def home():
    global main, submit_clicked

    if request.method == 'POST':
        user_input = request.form['myTextarea']
   
        submit_clicked = True

      
        response = model.generate_content(user_input)
        main = response.text  

    return render_template('home.html', main=main, submit_clicked=submit_clicked)

if __name__ == '__main__':
    app.run(debug=True)
