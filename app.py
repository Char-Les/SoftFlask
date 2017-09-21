#Charles Weng
#Period 7 Soft Dev
#HW4 Let Me Flask You Something

from flask import Flask

my_app = Flask(__name__)

@my_app.route('/')
def hello():
	return "I'm not actually here, but <a href= '/here'>here</a>."
@my_app.route('/here')
def here():
	return "I've moved <a href= '/overthere'>overthere</a>, sorry"
@my_app.route('/overthere')
def overthere():
	return "<b>Oh no you found me!<b>"

if __name__ == '__main__':
    my_app.debug == True
    my_app.run()
