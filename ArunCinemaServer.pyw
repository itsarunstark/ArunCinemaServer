from flask import Flask,render_template
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile
import os
import socket
import subprocess
def KillServer():
    subprocess.call("taskkill /f /im python.exe",shell=True)
    subprocess.call("taskkill /f /im pythonw.exe",shell=True)
    b2['text'] = "Again Start Cinema Server"


def checker():
    if not os.path.exists(os.getcwd()+"/templates"):
        os.makedirs(os.getcwd()+"/templates")
        content1 = r"""<!DOCTYPE html>
                        <html lang="en">
                        <head>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <title>ArunCinemaServer</title>
                        </head>
                        <body>
                        <center>
                        <h1><b>Welcome To Arun's Cinema Server.</b></h1>
                        <button><a href="/video">Watch Your File</a></button>
                        </center>
                        </body>
                        </html>"""
        content2 = r"""<!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="UTF-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1.0">
                            <title>Arun Cinema Server</title>
                        </head>
                        <body>
                            <h1 size="20px">You Can Go Here!</h1>
                            <!-- <video src="My Video.mp4" alt="This Browser DOn't have this service">Here Is Video</video> -->
                            <video src={{Mysrc}} autoplay="true" controls="true"></video>
                        </body>
                        </html>"""

        open(os.getcwd()+"/templates/"+"index.html","w").write(content1)
        open(os.getcwd()+"/templates/"+"index2.html","w").write(content2)
    if not os.path.exists(os.getcwd()+"/static"):
        os.makedirs(os.getcwd()+"/static")
    
def WatchVid():
    global extension
    name = askopenfile(filetype=[("mp4 files", "*.mp4")],mode="rb")
    if name!=None:
            
            b1['text'] = "Copying Please Wait..."
            root.update()
            extension = name.name.split(".")[-1]
            print(extension)
            
            open(f"{os.getcwd()}/static/MyVid.{extension}","wb").write(name.read())
            b1['text'] = "Video Copied!"

def ServerStart():
    global namess
    namess = socket.gethostbyname(socket.gethostname())
    funntush = False
    lisdir = os.listdir(os.getcwd()+"/static/")
    for i in lisdir:
        if "mp4" in i:
            funntush = True
            break
        else:
            funntush = False
    if funntush:
        if b2['text'] == "Stop Cinema Server":
            KillServer()
        else:

            subprocess.Popen(f'python runner.pyw "{namess}" {s1.get()}',shell=True)
            li['text'] = f"Your Server is Started Please\nVisit http://{namess}:{s1.get()}"
            b2['text'] = "Stop Cinema Server"
    else:
        messagebox.showerror("Oops..","Please Select One Video First")
            

        


def Reader():
    mytop = Toplevel(root)
    mytop.geometry("680x360")
    mytop.wm_maxsize("680","360")
    mytop.wm_minsize("720","400")
    mytop.title("Important Note From Arun")
    Label(mytop,text="Important!",font="times 20 bold",fg="red").pack()
    texts = """
    Hello from Arun! This is an important note! before using the software you 
    have to confirm that you are connected to a LAN connection.(Cause this Server
    is depend upon LAN) you don't have to turn on the data connection! it's not important 
    but you have to connect with a LAN connection. for example open your  mobile hotspot 
    connect your PC to your mobile you can turn off data(it don't need data) but don't 
    turn off the Hotspot. then  just open the software select video to watch and make 
    sure that if someone want  to watch the movie then he have to also connect with 
    your phone through hotspot  but don't need any data. Hope you understand!...
    Please Don't close console or black window because the server will run on that.
    Thanks For Reading
    """
    Label(mytop,text=texts,font="times 15").pack()

namess = socket.gethostbyname(socket.gethostname())


root = Tk()
root.geometry("720x720")
mymen = Menu(root)
mysecmen = Menu(mymen,tearoff=0)
mysecmen.add_command(label="read about it",command=Reader)
mymen.add_cascade(label="Important Note",menu=mysecmen)
root.title("ArunCinemaServer")
Label(root,text="Welcome To Arun Cinema Server",font=("times new roman",30)).pack()
b1 = Button(root,text="Select Video (mp4 file) To Watch",font="times 20",command=WatchVid)
b1.pack(pady=30)
Label(root,text="Please Select The Port",font=("times new roman",20)).pack()

s1 = Spinbox(root,to_=9999,from_=4000,font="times 20")
s1.pack()
li = Label(root,text="",font=("times new roman",20))
li.pack(pady=30)
root.configure(menu=mymen)
# Label(root,text="If you want to kill server Please Close the app\n\n",font=("times new roman",15)).pack(pady=30)
b2 = Button(root,text="Start Cinema Server",font="times 20 bold",command=ServerStart)
b2.pack()
checker()

root.mainloop()