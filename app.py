from flask import Flask, render_template, request

# from model import gen

app = Flask(__name__)


@app.route('/')
def main():  # put application's code here
  # if request.method=='POST':
  # else:
  answer = ''
  return render_template('main.html', answer=answer)

@app.route('/get_question', methods=['POST'])
def get_question():
#   question = request.form['question']
  answer = '답변' #gen(question)
  return render_template('main.html', answer=answer)


if __name__ == '__main__':
  app.run()