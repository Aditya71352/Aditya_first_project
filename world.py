#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask,render_template,request
world=Flask(__name__)
@world.route('/')
def nitin():
    return render_template('world.html')
@world.route('/deployment',methods=['POST'])
def abc():
    if(request.method=="POST"):
        n=request.form['num1']
        m=request.form['num2']
        total=int(n)+int(m)
        
        return render_template('world.html',aditya=total)
if(__name__)=='__main__':
    world.run()


# In[4]:





# In[ ]:




