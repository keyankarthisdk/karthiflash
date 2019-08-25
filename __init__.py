from flask import Flask, render_template, request
import sqlite3
import random

app = Flask(__name__,template_folder='template')
#app = Flask(__name__, static_url_path='/static')

@app.route('/',methods = ['GET']) #for home
def first():
   return render_template('index.html')

@app.route('/home',methods = ['GET']) #for home
def home():
   return render_template('home1.html')

@app.route('/signup') #for signup
def signup():
   return render_template('signup.html')

@app.route('/login')#methods=['GET','POST']) #for login
def login():
   return render_template('login.html')


@app.route('/transport',methods = ['GET']) #for home
def transport():
   return render_template('transport.html')

@app.route('/tour')#methods=['GET','POST']) #for login
def tour():
   return render_template('tour.html')
@app.route('/emer')#methods=['GET','POST']) #for login
def emer():
   return render_template('emergency.html')
@app.route('/safe',methods=['GET','POST']) 
def safe():
   return render_template('harass.html')


@app.route('/hospital',methods=['GET','POST']) 
def hospital():
   return render_template('hospital.html')


@app.route('/create',methods = ['POST', 'GET'])
def create():
    state=-1
    #conn = sqlite3.connect('main.sqlite')
    conn = sqlite3.connect('manipal')
    cur = conn.cursor()
    if request.method == 'POST':
      result = request.form
      print(result)
      gg=result.to_dict(flat=True)
      cur.execute('''INSERT into signup (name,email,password,username,address,ContactNumber,pincode) VALUES ( ?,?,?,?,?,?,?)''', (result['name'],result['email'],result['password'],result['username'],result['address'],result['contact_number'],result['location'] ))
      conn.commit()    
      return render_template('home.html', seto=2)
      #return redirect(url_for('login'))
    # return "hi"
    return render_template('home1.html', seto=0)


@app.route('/result',methods = ['POST', 'GET'])
def result():
    # print("insude res")
    state='hi'
    result = request.form
    conn = sqlite3.connect('manipal')
    cur = conn.cursor()
    if request.method == 'POST':
      result = request.form
      print(result)
      gg=result.to_dict(flat=True)
      cur.execute('SELECT * FROM signup WHERE username = ? and password = ?', (result['name'],result['password'],))
      if(result['name']=='root' and result['password'] == 'admin'):
        return render_template("admin.html")
      elif len(cur.fetchall()):
        return render_template('home1.html',seto=1)
    return render_template("login.html",result = 1)



@app.route('/govt',methods=['POST','GET'])
def govt():
    state=-1
    conn = sqlite3.connect('manipal')
    #conn = sqlite3.connect('rog')
    cur = conn.cursor()
    print(request.method)
    if request.method == 'POST':
      result = request.form
      print(result)
      gg=result.to_dict(flat=True)
      cur.execute('''INSERT into govt (fname,lname,gender,dob,email,dori,iloc,cdetails,outc,img) VALUES ( ?,?,?,?,?,?,?,?,?,?)''', (result['name1'],result['name2'],result['Gender'],result['date'],result['Email'],result['incident_date'],result['location'],result['complaint details'],result['desired outcome'],result['file'] ))
      conn.commit()    
      return render_template('home.html',seto=2)


    return render_template('reg1.html')

@app.route('/road',methods=['GET','POST']) #for login
def road():
    state=-1
    conn = sqlite3.connect('manipal')
    #conn = sqlite3.connect('rog')
    cur = conn.cursor()
    print(request.method)
    if request.method == 'POST':
      result = request.form
      print(result)
      gg=result.to_dict(flat=True)
      cur.execute('''INSERT into road (date,location,image,fb) VALUES ( ?,?,?,?)''', (result['dateupdate'],result['location'],result['file'],result['Feedback'] ))
      conn.commit()     
      return render_template('home.html')
    return render_template('road.html')








@app.route('/pu',methods=['GET','POST']) #for login
def pu():
    state=-1
    #conn = sqlite3.connect('main.sqlite')
    conn = sqlite3.connect('rog')
    cur = conn.cursor()
    if request.method == 'POST':
      result = request.form
      print(result)
      gg=result.to_dict(flat=True)
      cur.execute('''INSERT into PublicUpdate (Date,subject,upin,apin,CAUSE,ACAUSE,disease,fd) VALUES ( ?,?,?,?,?,?,?,?)''', (result['dateupdate'],result['Subject'],result['upin'],result['apin'],result['describe'],result['acause'],result['disease'],result['desicion'] ))
      conn.commit()    
      return render_template('publicupdate.html',seto=2)
    return render_template('publicupdate.html', seto=0)





@app.route('/admin') #for signup
def admin():
   return render_template('admin.html')



@app.route('/dcl')#methods=['GET','POST']) #for login
def dcl():
   return render_template('daash.html')

@app.route('/dp')#methods=['GET','POST']) #for login
def dp():
   return render_template('dashpublic.html')

@app.route('/dwl')#methods=['GET','POST']) #for login
def dwl():
   return render_template('dashwtl.html')

@app.route('/dpwl')#methods=['GET','POST']) #for login
def dpwl():
   return render_template('dashprivatewtl.html')

@app.route('/dpcl')#methods=['GET','POST']) #for login
def dpcl():
   return render_template('dashprivateclinic.html')

@app.route('/dcl_update',methods=['GET','POST']) #for login
def dcl_update():
   result = request.form
   print(result)
   return render_template('clinicupdate.html')

@app.route('/au')#methods=['GET','POST']) #for login
def any_update():
   return render_template('userupdate.html')

@app.route('/dcl1')#methods=['GET','POST']) #for login
def dcl1():
   print(request.form)

@app.route('/pclu')#methods=['GET','POST']) #for login
def pclu():
   return render_template('privateclinicupdate.html')

@app.route('/wlu')#methods=['GET','POST']) #for login
def wlu():
   return render_template('wtlupdate.html')

@app.route('/pwtu')#methods=['GET','POST']) #for login
def pwtu():
   return render_template('privatewtlupdate.html')


if __name__ == '__main__':
   app.run(debug = True)


