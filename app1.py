from flask import Flask

FAI=Flask(__name__)

@FAI.route('/sample')
def sample():
    return '<h1><marquee>U BELIVE THE GOD DONT BELIVE THE DEVOOTE</marquee></h1>'

FAI.run(debug=True)
