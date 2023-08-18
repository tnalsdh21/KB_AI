from flask import Flask, render_template, request

from model import gen

app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
def main():  # put application's code here
  # if request.method=='POST':
  # else:
  return render_template('main.html')

@app.route('/get_question',methods=['POST'])
def get_question():
  question = request.form['question']
  answer = gen(question)
  return render_template('main.html', answer=answer)


if __name__ == '__main__':
  app.run()
