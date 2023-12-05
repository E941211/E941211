from flask import *
app = Flask(__name__)
dict1 = {}

@app.route('/',methods = ['GET'])
def index():
    return render_template('lab10_plus.html')
    
@app.route('/set',methods = ['POST'])
def set():
    store_name = request.form['store_name']
    score = request.form['score']
    data = request.form.to_dict()
    dict1[store_name]=score
    print(f"user input data : {data}")
    print(f"Data on server : {dict1}")
    data_string = json.dumps(dict1,ensure_ascii = False)
    return render_template('lab10_plus.html',**locals())

@app.route('/reset/<rsp1>',methods = ['GET'])
def reset(rsp1):
  if rsp1 == "y":
    dict1.clear()
    print(f"Data on server : {dict1}")
    return render_template('reset.html')
    
  else:
    return render_template('lab10_plus.html')
app.run(host="192.168.137.73", port=3000, debug=True)