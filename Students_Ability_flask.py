from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('SA_index.html')

@app.route('/prediction',methods=['POST','GET'])
def calc():
    import pandas as pd
    import pickle
    kmeans_new=pickle.load(open("model.pkl","rb"))
    clusters_new=pd.read_excel("clusters_new.xlsx")
    input_para=[float(request.form['Graduation Marks']),float(request.form['Entrance Marks'])]
    input_para[0]=(input_para[0]-77.3172)/9.2327
    input_para[1]=(input_para[1]-127.9162)/27.4483

    print(kmeans_new.predict([input_para]))
    if (kmeans_new.predict([input_para])==0):
        result="Not Selected this time. Better luck next time."
    elif (kmeans_new.predict([input_para])==1):
        result="Congratulations! Selected for the course."
    elif(kmeans_new.predict([input_para])==2):
        result="Congratulations! Selected for the next second exam."
    else:
        result="Congratulations! Selected for the interview."

    return render_template('SA_result.html',result=result)
    

app.run(debug=True)
