from flask import Flask, render_template, request

from ai import predict

app = Flask(__name__)

app.config['SECRET_KEY'] = 'this_is_secret_af_boii'
app.config['DEBUG']=True

@app.route('/',methods=['GET','POST'])
def home():
    message = None
    if request.method == 'POST':
        area = request.form['area']
        try:
            price = str(int(predict(area)))
            return render_template('home.html',price=price)
        except ValueError:
            message = 'Invalid input'
    return render_template('home.html', message=message)
        

if __name__ == '__main__':
    app.run(debug=True)