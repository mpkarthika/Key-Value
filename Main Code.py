import threading 
from threading import*
import t
dict={} 
def create(key,value,tout=0):
    if key in dict:
        print("error: this key already exists") 
    else:
        if(key.isalpha()):
            if len(dict)<(1024*1020*1024) and value<=(16*1024*1024):  
                if tout==0:
                    x=[value,tout]
                else:
                    x=[value,t.t()+tout]
                if len(key)<=32:
                    dict[key]=x
            else:
                print("error: Memory limit exceeded!! ")
        else:
            print("error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")
            
def read(key):
    if key not in dict:
        print("error: given key does not exist in database. Please enter a valid key") 
    else:
        y=dict[key]
        if y[1]!=0:
            if t.t()<y[1]:  
                string=str(key)+":"+str(y[0]) 
                return string
            else:
                print("error: time-to-live of",key,"has expired") #error message5
        else:
            string=str(key)+":"+str(y[0])
            return string

def delete(key):
    if key not in dict:
        print("error: given key does not exist in database. Please enter a valid key") 
    else:
        y=dict[key]
        if y[1]!=0:
            if t.t()<y[1]: 
                del dict[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired") 
        else:
            del dict[key]
            print("key is successfully deleted")

def modify(key,value):
    y=dict[key]
    if y[1]!=0:
        if t.t()<y[1]:
            if key not in dict:
                print("error: given key does not exist in database. Please enter a valid key") 
            else:
                x=[]
                x.append(value)
                x.append(y[1])
                dict[key]=l
        else:
            print("error: time-to-live of",key,"has expired") 
    else:
        if key not in d:
            print("error: given key does not exist in database. Please enter a valid key") 
        else:
            x=[]
            x.append(value)
            x.append(y[1])
            dict[key]=l
 
