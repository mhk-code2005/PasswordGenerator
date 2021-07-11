#IMPORTED MODULES
from tkinter import *
import tkinter
import string
import random
master=Tk()
master.title('PASSWORD GENERATOR')

global pin



#PASSWORD CLASS
class password(object):
    def __init__(self,website=None,username=None,password=None,length=None):
        self.website=website
        self.username=username
        self.password=password
    def set_pass(self,other):
        self.password=other
    def set_user(self,other):
        self.username=other
    def set_web(self,other):
        self.website=other
    def get_pass(self):
        return self.password
    def __str__(self):
        return str(self.website)+': '+'username '+str(self.username)+' and password '+str(self.password)
# GENERATING A PASSWORD AND SAVING IT INTO A FILE
def password_setter(website,username):
    c=password()
    c.set_web(website)
    c.set_user(username)
    upper_alphabet=string.ascii_uppercase
    lower_alphabet=string.ascii_lowercase
    punctuations=['!','#','%','^','&','*','+','-','/','@','<','>','.',' ']
    numbers=[1,2,3,4,5,6,7,8,9,0]
    password_elements=[]
    alphabet_lower_copy=lower_alphabet[:]
    for letter in range(3):
        a=random.choice(alphabet_lower_copy)
        password_elements.append(a)    
        alphabet_lower_copy.replace(a,'')
    alphabet_upper_copy=upper_alphabet[:]
    for letter in range(2):
        a=random.choice(alphabet_upper_copy)
        password_elements.append(a)
        alphabet_upper_copy.replace(a,'')
    puncuation_copy=punctuations[:]
    for letter in range(2):
        a=random.choice(puncuation_copy)
        password_elements.append(a)
        puncuation_copy.remove(a)
    numbers_copy=numbers[:]
    for letter in range(3):
        a=random.choice(numbers_copy)
        password_elements.append(a)
        numbers_copy.remove(a)
    random.shuffle(password_elements)
    Password=''
    for s in password_elements:
        Password+=str(s)
    Password=str(Password)
    c.set_pass(Password)
    return c.__str__()
filename="passwords.txt"
def file_updater(filename,Password):
    text_file = open(filename,'a')
    text_file.write('\n')
    text_file.write(Password)
    text_file.close()
#SEARCH PART
Search_entry=Entry(master)
def searcher():
    new2=Tk()
    new2.title('Security')
    new2.configure(bg='green')
    filename="passwords.txt"
    lives_left=3
    Label(new2,text='ENTER COMPUTER PIN',bg='green',fg='yellow').grid(row=0,columnspan=3)
    pintry=Entry(new2,show='*',bg='green',fg='yellow')
    def a():
        rows=6
        pin=1111

        pin2=int(pintry.get())
        new2.destroy()
        if pin==pin2: 
                file1 = open(filename, 'r') 
                Lines = file1.readlines() 
                file1.close()
                search_word=Search_entry.get()
                for line in Lines:
                    if search_word in line:
                        main_line=line
                        s=Label(master, text=line).grid(row=rows,columnspan=4)
                        rows+=1
                def clear():
                    for widget in master.winfo_children():
                        if type(widget)==Label:
                            if widget.cget('text')!='WEBSITE:': 
                                if widget.cget('text')!='USERNAME:':
                                    widget.destroy()
                Button(master,text='CLEAR',command=clear).grid(row=5,columnspan=3)
        else:       
            searcher()
                

                
    Button(new2,text='SUBMIT',command=a,bg='green',fg='yellow').grid(row=1,column=1)       

    
    pintry.grid(row=1,column=2)

            
Search=Button(master,command=searcher,text='search')
#GETTING WEBSITE AND USER NAME
Label(master,text='WEBSITE:').grid(row=2,column=1)
website=Entry(master)
Label(master,text='USERNAME:').grid(row=3,column=1)
username=Entry(master)
#GENERATING A PASSWORD
def command_generate():
    newWindow=Tk()
    newWindow.title('CONFIRMATION')
    name_website=website.get()
    name_username=username.get()
    Password=password_setter(name_website,name_username)
    Label(newWindow,text=(Password.split())[-1]+' password \n will be generated for \n website '+name_website+ '\n and for username '+name_username).grid(row=1,columnspan=4)
    def command_yes():
        file_updater(filename,Password)
        newWindow.destroy()
    def command_no():
        newWindow.destroy()
    Button(newWindow,text='yes',command=command_yes).grid(row=2,column=1)    
    Button(newWindow,text='no',command=command_no).grid(row=2,column=2)    
    
Button(master,text="GENERATE PASSWORD",command=command_generate).grid(row=4,columnspan=3)    
#GRID PARTS
website.grid(row=2,column=2)
username.grid(row=3,column=2)
Search.grid(row=1,column=1)
Search_entry.grid(row=1,column=2)
mainloop()

















