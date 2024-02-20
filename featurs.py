from flask import Flask,render_template

FAI=Flask(__name__)

@FAI.route('/send_mail')
def send_mail():
    return render_template('send_mail.html')

@FAI.route('/property')
def property():
    return render_template('property.html',name='bashaa')


if __name__=='__main__':
    FAI.run(debug=True)