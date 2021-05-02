#UNMUTE MUSIC
def unmute_music():
    global current
    root.unmute_button.grid_remove()
    root.mute_button.grid()
    mixer.music.set_volume(current)
    audio_status.configure(text="playing.............")
#MUTE MUSIC
def mute_music():
    global current
    root.mute_button.grid_remove()
    root.unmute_button.grid()
    current=mixer.music.get_volume()
    mixer.music.set_volume(0)
    audio_status.configure(text="muted.............")
#VOLUME UP
def vol_up_music():
    vol=mixer.music.get_volume()
    if(vol>=vol*100):
        mixer.music.set_volume(vol+0.1)
    else:
        mixer.music.set_volume(vol+0.01)
    vol_label.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    progressbar_volume['value']=mixer.music.get_volume()*100
#VOLUME LOW
def vol_low_music():
    vol=mixer.music.get_volume()
    if(vol<=vol*100):
        mixer.music.set_volume(vol-0.1)
    else:
        mixer.music.set_volume(vol-0.05)
    vol_label.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    progressbar_volume['value']=mixer.music.get_volume()*100
#STOP MUSIC
def stop_music():
    mixer.music.stop()
    audio_status.configure(text="stoped!.............")
    pb_music_start.configure(text="0:00:0")
#RESUME FUNCTION
def resume_music():
    root.resume_button.grid_remove()
    root.pause_button.grid()
    mixer.music.unpause()
    audio_status.configure(text="playing.............")
#PAUSE FUNCTION
def pause_music():
    mixer.music.pause()
    root.pause_button.grid_remove()
    root.resume_button.grid()
    audio_status.configure(text="paused.............")
#FUNCTION THAT PLAYS MUSIC
def plmusic():
    ad=audiot.get()
    mixer.music.load(ad)
    mixer.music.play()
    progress_bar.grid()
    pb_music_label.grid()
    mixer.music.set_volume(0.4)
    progressbar_volume['value']=40
    vol_label['text']='40%'
    audio_status.configure(text="playing.............")
    #for music progress bar
    song = MP3(ad)
    totallength = int(song.info.length)
    pb_music['maximum'] = totallength
    pb_music_end.configure(text='{}'.format(str(datetime.timedelta(seconds=totallength))))
    def prostatus():
        currsonglen = mixer.music.get_pos()//1000
        pb_music['value'] = currsonglen
        pb_music_start.configure(text='{}'.format(str(datetime.timedelta(seconds=currsonglen))))
        pb_music.after(1,prostatus)
    prostatus()
#OPENING MUSIC FILE
def url():
    try:
        dd=filedialog.askopenfilename(initialdir='Music',title="select audio file",filetype=(('MP3','*.mp3'),('WAV','*.wav')))
    except:
        dd=filedialog.askopenfilename(title="select audio file",filetype=(('MP3','*.mp3'),('WAV','*.wav')))
    audiot.set(dd)
def kk():
    bg_icon=ImageTk.PhotoImage(file="H:\\kk.jpg")
    logolbl=Label(root,image=bg_icon).pack()
    main_Frame=Frame(root,bg="crimson")
    main_Frame.place(x=200,y=200)
    #**********************CREATING SLIDER*************************************
    ss="DESIGNED BY AANCHAL MITTAL"
    intro_label=Label(main_Frame,text=ss,font=("alergian",15,"italic bold"),bg="crimson",fg="white")
    intro_label.grid(row=5,column=0,padx=10,pady=10,columnspan=3)
    def intro():
        global count
        global text
        if (count>=len(ss)):
            #TO START AGAIN
            count=-1
            text=''
            intro_label.configure(text=text)
        else:
            text=text+ss[count]
            intro_label.configure(text=text)
        count+=1
        #CALLING AFTER EVERY 2 SECONDS
        intro_label.after(200,intro)
    intro()
    #**************************************************************************
    #GLOBAL VARIABLES
    global audiot
    global audio_status
    global vol_label,totallength
    global progressbar_volume,progress_bar,pb_music_label,pb_music,pb_music_end,pb_music_start
    #*****************************SETTING UP WIDGETS*******************************************************
    #MAIN LABEL
    main_label=Label(main_Frame,text="SELECT THE AUDIO TRACK!",font=("alergian",15),bg="crimson",fg="black")
    main_label.grid(row=0,column=0,padx=10,pady=10)
    #STATUS IN PROCESS
    audio_status=Label(main_Frame,text="",font=("alergian",15),bg="crimson",fg="black")
    audio_status.grid(row=3,column=1,padx=10,pady=10)
    #ENTRY BOX
    main_entry=Entry(main_Frame,font=("alergian",15),bg="white",fg="black",textvariable=audiot)
    main_entry.grid(row=0,column=1,padx=10,pady=10)
    #BUTTONS
    #SEARCH BUTTON
    search_button=Button(main_Frame,text="SEARCH!",font=("alergian",15),bg="black",fg="white",bd=5,command=url)
    search_button.grid(row=0,column=2,padx=10,pady=10)
    #PLAY BUTTON
    play_button=Button(main_Frame,text="PLAY!",font=("alergian",15),bg="black",fg="white",bd=5,command=plmusic)
    play_button.grid(row=1,column=0,padx=10,pady=10)
    #PAUSE BUTTON
    root.pause_button=Button(main_Frame,text="PAUSE!",font=("alergian",15),bg="black",fg="white",bd=5,command=pause_music)
    root.pause_button.grid(row=1,column=1,padx=10,pady=10)
    #RESUME BUTTON
    root.resume_button=Button(main_Frame,text="RESUME!",font=("alergian",15),bg="black",fg="white",bd=5,command=resume_music)
    root.resume_button.grid(row=1,column=1,padx=10,pady=10)
    root.resume_button.grid_remove()
    #MUTE BUTTON
    root.mute_button=Button(main_Frame,text="MUTE!",font=("alergian",15),bg="black",fg="white",bd=5,command=mute_music)
    root.mute_button.grid(row=2,column=0,padx=10,pady=10)
    #UNMUTE BUTTON
    root.unmute_button=Button(main_Frame,text="UNMUTE!",font=("alergian",15),bg="black",fg="white",bd=5,command=unmute_music)
    root.unmute_button.grid(row=2,column=0,padx=10,pady=10)
    root.unmute_button.grid_remove()
    #STOP BUTTON
    stop_button=Button(main_Frame,text="STOP!",font=("alergian",15),bg="black",fg="white",bd=5,command=stop_music)
    stop_button.grid(row=1,column=2,padx=10,pady=10)
    #VOLUME UP
    vol_up_button=Button(main_Frame,text="VOLUME UP!",font=("alergian",15),bg="black",fg="white",bd=5,command=vol_up_music)
    vol_up_button.grid(row=2,column=1,padx=10,pady=10)
    #VOLUME LOW
    vol_low_button=Button(main_Frame,text="VOLUME LOW!",font=("alergian",15),bg="black",fg="white",bd=5,command=vol_low_music)
    vol_low_button.grid(row=2,column=2,padx=10,pady=10)
    #***************************************PROGRESS BAR*******************************************************************************
    progress_bar=Label(main_Frame,text='',bg='purple')
    progress_bar.grid(row=0,column=3,rowspan=3,padx=20,pady=20)
    progress_bar.grid_remove()
    #for volume
    progressbar_volume=Progressbar(progress_bar,orient='vertical',mode='determinate',value=10,length=190)
    progressbar_volume.grid(row=0,column=0,ipadx=5)
    vol_label=Label(progress_bar,text='0%',bg='grey',width=3)
    vol_label.grid(row=0,column=0)
    #for music
    pb_music_label=Label(main_Frame,text='',bg='purple')
    pb_music_label.grid(row=4,column=0,columnspan=3,padx=20,pady=20)
    pb_music_label.grid_remove()
    #start time
    pb_music_start=Label(pb_music_label,text="0:00:0",width=6)
    pb_music_start.grid(row=0,column=0)
    #inner layout
    pb_music=Progressbar(pb_music_label,orient="horizontal",mode="determinate",value=0)
    pb_music.grid(row=0,column=1,ipadx=370,ipady=3)
    #end time
    pb_music_end=Label(pb_music_label,text="0:00:0")
    pb_music_end.grid(row=0,column=2)
count=0
text=''
#*****************************************IMPORTING FILES OR MODULES*********************************
from tkinter import *
from PIL import ImageTk
from tkinter import filedialog
#FOR PLAYING MUSIC
from pygame import mixer
from tkinter.ttk import Progressbar
import datetime
import time
from mutagen.mp3 import MP3
#*****************************************CREATING WINDOW********************************************
root=Tk()
root.geometry("1300x1100")
root.resizable(0,0)
root.title("MUSIC PLAYER")
bg_icon=ImageTk.PhotoImage(file="H:\\kk.jpg")
logolbl=Label(root,image=bg_icon).pack()
#AUDIO VARIABLE

audiot=StringVar()
current=0
totallength=0
kk()
mixer.init()
#INFINITE LOOP

root.mainloop()
