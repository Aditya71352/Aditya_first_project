#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask,render_template,request
box=Flask(__name__)
@box.route('/')
def xyz():
    return render_template('d:project.html')
@box.route('/adi',methods=['POST'])

def ac():
    if(request.method=="POST"):
        u=request.form['n']
        i=request.form['p']
        uu=request.form['curry']
        ii=request.form['quantity']
        print(u,i,uu,ii)
        return render_template('d:project.html')
box.run()


# In[ ]:


from flask import Flask,render_template,request
world=Flask(__name__)
@world.route('/')
def nitin():
    return render_template('d:deployment.html')
@world.route('/deployment',methods=['POST'])
def abc():
    if(request.method=="POST"):
        n=request.form['num1']
        m=request.form['num2']
        total=int(n)+int(m)
        
        return render_template('d:deployment.html',aditya=total)

world.run()


# In[ ]:




