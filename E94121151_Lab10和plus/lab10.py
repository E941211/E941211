from flask import *
import random as r

app=Flask(__name__)

@app.route('/',methods = ["GET"])
def index():
    return render_template('lab10.html')

@app.route('/student_data',methods = ['POST'])
def student_data():
    a1 = request.form["name"]
    a2 = request.form["student_id"]
    print(f'name : {a1}')
    print(f'student_id : {a2}')
    return 'ok'

@app.route('/rsp',methods = ['GET'])
def rsp():

    result = request.args.get('choice',default="none")
    computer = r.sample("rsp",1)

    if result !="r" and result !="s" and result !="p" :
        return "Wrong input ! try again"
    elif (result == "r"and computer[0] =="s") or (result == "s"and computer[0] =="p") or (result == "p" and computer[0]=="r"):
        print(f"computer : {computer[0]} user : {result}")
        return 'You win!'
    elif result == computer[0] :
        print(f'computer : {computer[0]} user : {result}')
        return "It's Tie!"
    else :
        print(f'computer : {computer[0]} user : {result}')
        return "You lose!"
app.run(host="192.168.137.73", port=3000, debug=True)