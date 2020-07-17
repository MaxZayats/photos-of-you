from flask import Flask, render_template, redirect, request
import datetime
import base64
from modules import modify_template


app = Flask(__name__)

user_template = 'template.html'
base_template = 'base.html'
main_temlate = 'main.html'
try:
    modify_template.modify(user_template, base_template, main_temlate)
except:
    print(
        'Ошибка в названии шаблонов.\n'
        'Проверьте название шаблонов!')
    exit()


@app.route('/', methods=['GET'])
def start():
    return render_template(main_temlate)


@app.route('/image', methods=['POST'])
def main():
    imgdata = base64.b64decode(request.form.to_dict().get('img'))
    filename = f'{datetime.datetime.now().strftime("%d-%m-%Y %H-%M-%S")}.jpg'
    with open(r"photos/" + filename, 'wb') as f:
        f.write(imgdata)
    return redirect('/')


if __name__ == "__main__":
    app.run(port=5000, debug=False)
