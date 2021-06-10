from tkinter import *


import tkinter.messagebox
root=Tk()
canvas=Canvas(root,width=500,height=600)
root.title("Complete Dictionary of SEO")


textin = StringVar()

def A():
    Label(root, text="ALGORITHMS", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)
    Label(root, text="ALT ATTRIBUTE", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=120)
    Label(root, text="ANCHOR  TEST", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=160)

def B():
    Label(root, text="BACKLINK", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)
    Label(root, text="BLACK HAT SEO", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=120)
    Label(root, text="BOT", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=160)
    Label(root, text="BROKEN", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800, y=200)

def C():
    Label(root, text="CACHE", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)
    Label(root, text="CLICK BAIT", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=120)
    Label(root, text="CLICK THROUGH RATE", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=160)
    Label(root, text="CONTENT", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800, y=200)
    Label(root, text="CRAWLER", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800, y=240)
    Label(root, text="CRAWLING", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800, y=280)
    Label(root, text="CLOAKING", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800, y=320)

def D():
    Label(root, text="DOORWAY PAGE", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)
    Label(root, text="DUPLICATE CONTENT", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=120)

def E():
    Label(root, text="EXTERNAL LINK", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)

def F():
    Label(root, text="FEATURED SNIPPET", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)
    Label(root, text="FINDABILITY", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=120)

def G():
    Label(root, text="GOOGLE ANALYTICS", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)
    Label(root, text="GOOGLEBOT", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=120)
    Label(root, text="GRAY HAT", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=160)
    Label(root, text="GOOGLE SEARCH CONSOLE", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800, y=200)
    Label(root, text="GOOGLE TRENDS", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800, y=240)

def H():
    Label(root, text="HEADING", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)
    Label(root, text="HIDDEN TEXT", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=120)
    Label(root, text="HOMEPAGE", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=160)
    Label(root, text="HTML", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800, y=200)
    Label(root, text="HTTP", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800, y=240)

def I():
    Label(root, text="INDEX", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)
    Label(root, text="INDEXABILITY", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=120)
    Label(root, text="INDEXED PAGE", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=160)
    Label(root, text="IPADDRESS", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800, y=200)

def J():
    Label(root, text="JAVASCRIPT", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)

def K():
    Label(root, text="KEYWORD", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)
    Label(root, text="KEYWORD DENSITY", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=120)
    Label(root, text="KEYWORD RESEARCH", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=160)
    Label(root, text="KEYWORD STUFFING", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800, y=200)

def L():
    Label(root, text="LANDING PAGE", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)
    Label(root, text="LINK", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=120)
    Label(root, text="LINK BAIT", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=160)
    Label(root, text="LINK BUILDING", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800, y=200)
    Label(root, text="LINK FARM", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800, y=240)
    Label(root, text="LINK PROFILE", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800, y=280)

def M():
    Label(root, text="META KEYWORDS", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)
    Label(root, text="META DESCRIPTION", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=120)
    Label(root, text="META TAGS", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=160)

def N():
    Label(root, text="NICHE", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)
    Label(root, text="NO INDEX TAG", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=120)
    Label(root, text="NO SNIPPET TAG", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=160)
    Label(root, text="NEGATIVE SEO", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800, y=200)

def O():
    Label(root, text="OFF PAGE SEO", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)
    Label(root, text="ON PAGE SEO", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=120)
    Label(root, text="ORGANIC SEARCH", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=160)
    Label(root, text="ORPHAN PAGE", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800, y=200)

def P():
    Label(root, text="PAGE RANK", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)
    Label(root, text="PERSONALISATION", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=120)
    Label(root, text="PHP", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=160)
    Label(root, text="PIRACY", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800, y=200)

def Q():
    Label(root, text="QUERY", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)

def R():
    Label(root, text="RANK", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)
    Label(root, text="REDIRECT", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=120)
    Label(root, text="RESPONSIVE WEBSITE", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=160)

def S():
    Label(root, text="SEARCH ENGINE", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)
    Label(root, text="SEARCH ENGINE OPTIMISATION", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=120)
    Label(root, text="SITE MAP", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=160)
    Label(root, text="SUBDOMAIN", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800, y=200)
    Label(root, text="SEARCH HISTORY", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800, y=240)

def T():
    Label(root, text="TITLE", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)
    Label(root, text="TOP LEVEL DOMAIN", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=120)
    Label(root, text="TRAFFIC", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=160)

def U():
    Label(root, text="UNIVERSAL SEARCH", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)
    Label(root, text="URL", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=120)
    Label(root, text="USER AGENT", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=160)
    Label(root, text="USER EXPERIENCE", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800, y=200)

def V():
    Label(root, text="VERTICAL SEARCH", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)
    Label(root, text="VISIBILITY", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=120)

def W():
    Label(root, text="WEBPAGE", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)
    Label(root, text="WEBSITE", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=120)
    Label(root, text="WHITE HAT", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=160)
    Label(root, text="WORD COUNT", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800, y=200)

def X():
    Label(root, text="X-X-X-X", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)

def Y():
    Label(root, text="Y-Y-Y-Y", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)

def Z():
    Label(root, text="Z-Z-Z-Z", width=20, font="comicansans 12 bold", height=2, bg="pink", ).place(x=800, y=80)


def clk():
    entered = ent.get()
    output.delete(0.0,END)
    try:
        textin = exlist[entered]
    except:
        textin = 'Sorry this Keyword is not available!\n'
    output.insert(0.0,textin)

def ex():
    tkinter.messagebox.showinfo("Program",'Exit')
    exit()

def exitt():
    tkinter.messagebox.showinfo("program",'Exit')
    exit()

def me():
    text='\n XYZ \n OKEY DEXTER \n NICE'
    saveFile = open('text.txt', 'w')
    saveFile.write(text)
    print('This are the entries::', text)

def hel():
    help(tkinter)


def cont():
    tkinter.messagebox.showinfo('__Version 1.0__')


def clr():
    textin.set("")
    output.delete(0.0, END)


menu = Menu(root)
root.config(menu=menu)

subm = Menu(menu)
menu.add_cascade(label="File",menu=subm)
subm.add_command(label="Memo",command=me)
subm.add_command(label="Save")
subm.add_command(label="Save As")
subm.add_command(label="Print")
subm.add_command(label="Exit",command=ex)

subm1 = Menu(menu)
menu.add_cascade(label="Tools",menu=subm1)
subm1.add_command(label="Tkinter Help",command=hel)

subm2 = Menu(menu)
menu.add_cascade(label="About",menu=subm2)
subm2.add_command(label="Contributors",command=cont)

TITLE=Label(root,text='WELCOME TO COMPLETE SEO DICTIONARY',font=('none 15 bold'),bg ='silver')
TITLE.place(x=85,y=3,)

lab=Label(root,text='Keyword :',font=('none 15 bold'),bg ='silver')
lab.place(x=100,y=100,)

ent=Entry(root,width=22,font=('none 12 bold'),textvar=textin,bg='white')
ent.place(x=210 ,y=100,)

but1=Button(root,padx=2,pady=2,text='Search',command=clk,bg='powder blue',font=('none 15 bold'))
but1.place(x=225,y=150)

but2=Button(root,padx=2,pady=2,text='Clear',font=('none 15 bold'),bg='powder blue',command=clr)
but2.place(x=285,y=400)

output=Text(root,width=21,height=8,font=('Time 15 bold'),fg="black")
output.place(x=200,y=200)

labb=Label(root,text='Result   :',font=('non 15 bold'),bg='silver')
labb.place(x=100,y=200)

but3=Button(root,padx=2,pady=2,text='Exit',command=exitt,bg='powder blue',font=('none 15 bold'))
but3.place(x=175,y=400)

but4=Button(root,padx=2,pady=2,text='A',command=A,width=3,height=0,bg='green',font=('none 15 bold'))
but4.place(x=30,y=90)
but5=Button(root,padx=2,pady=2,text='B',command=B,width=3,height=0,bg='green',font=('none 15 bold'))
but5.place(x=30,y=135)
but6=Button(root,padx=2,pady=2,text='C',command=C,width=3,height=0,bg='green',font=('none 15 bold'))
but6.place(x=30,y=180)
but7=Button(root,padx=2,pady=2,text='D',command=D,width=3,height=0,bg='green',font=('none 15 bold'))
but7.place(x=30,y=225)
but8=Button(root,padx=2,pady=2,text='E',command=E,width=3,height=0,bg='green',font=('none 15 bold'))
but8.place(x=30,y=270)
but9=Button(root,padx=2,pady=2,text='F',command=F,width=3,height=0,bg='green',font=('none 15 bold'))
but9.place(x=30,y=315)
but10=Button(root,padx=2,pady=2,text='G',command=G,width=3,height=0,bg='green',font=('none 15 bold'))
but10.place(x=30,y=360)
but11=Button(root,padx=2,pady=2,text='H',command=H,width=3,height=0,bg='green',font=('none 15 bold'))
but11.place(x=30,y=405)
but12=Button(root,padx=2,pady=2,text='I ',command=I,width=3,height=0,bg='green',font=('none 15 bold'))
but12.place(x=30,y=450)
but13=Button(root,padx=2,pady=2,text='J',command=J,width=3,height=0,bg='green',font=('none 15 bold'))
but13.place(x=30,y=495)
but14=Button(root,padx=2,pady=2,text='K',command=K,width=3,height=0,bg='green',font=('none 15 bold'))
but14.place(x=30,y=540)
but15=Button(root,padx=2,pady=2,text='L',command=L,width=3,height=0,bg='green',font=('none 15 bold'))
but15.place(x=30,y=585)
but16=Button(root,padx=2,pady=2,text='M',command=M,width=3,height=0,bg='green',font=('none 15 bold'))
but16.place(x=30,y=630)


but17=Button(root,padx=2,pady=2,text='N',command=N,width=3,height=0,bg='green',font=('none 15 bold'))
but17.place(x=600,y=90)
but18=Button(root,padx=2,pady=2,text='O',command=O,width=3,height=0,bg='green',font=('none 15 bold'))
but18.place(x=600,y=135)
but19=Button(root,padx=2,pady=2,text='P',command=P,width=3,height=0,bg='green',font=('none 15 bold'))
but19.place(x=600,y=180)
but20=Button(root,padx=2,pady=2,text='Q',command=Q,width=3,height=0,bg='green',font=('none 15 bold'))
but20.place(x=600,y=225)
but21=Button(root,padx=2,pady=2,text='R',command=R,width=3,height=0,bg='green',font=('none 15 bold'))
but21.place(x=600,y=270)
but22=Button(root,padx=2,pady=2,text='S',command=S,width=3,height=0,bg='green',font=('none 15 bold'))
but22.place(x=600,y=315)
but23=Button(root,padx=2,pady=2,text='T',command=T,width=3,height=0,bg='green',font=('none 15 bold'))
but23.place(x=600,y=360)
but24=Button(root,padx=2,pady=2,text='U',command=U,width=3,height=0,bg='green',font=('none 15 bold'))
but24.place(x=600,y=405)
but25=Button(root,padx=2,pady=2,text='V',command=V,width=3,height=0,bg='green',font=('none 15 bold'))
but25.place(x=600,y=450)
but26=Button(root,padx=2,pady=2,text='W',command=W,width=3,height=0,bg='green',font=('none 15 bold'))
but26.place(x=600,y=495)
but27=Button(root,padx=2,pady=2,text='X',command=X,width=3,height=0,bg='green',font=('none 15 bold'))
but27.place(x=600,y=540)
but27=Button(root,padx=2,pady=2,text='Y',command=Y,width=3,height=0,bg='green',font=('none 15 bold'))
but27.place(x=600,y=585)
but28=Button(root,padx=2,pady=2,text='Z',command=Z,width=3,height=0,bg='green',font=('none 15 bold'))
but28.place(x=600,y=630)




canvas.pack()
root.mainloop()