# Importing Required Library
from tkinter import *
from tkinter import filedialog
from pygame import mixer
from tkinter.ttk import Progressbar
import datetime
from mutagen.mp3 import MP3

# Global Variables
global statusLabel, progressBarLabel, progressBar, volumeLabel, seekBarLabel, startTimeLabel, endTimeLabel
global seekBar, songLength, currentTime


# Play Functions - Plays Music
def play():
    track = audio.get()
    mixer.music.load(track)
    mixer.music.play()
    statusLabel.configure(text="Playing...")
    progressBarLabel.grid()
    seekBarLabel.grid()
    mixer.music.set_volume(0.3)
    progressBar["value"] = 30
    volumeLabel["text"] = "30%"
    root.muteButton.grid()
    song = MP3(track)
    songLength = int(song.info.length)
    seekBar["maximum"] = songLength
    endTimeLabel.configure(text="{}".format(datetime.timedelta(seconds=songLength)))

    def timeLapsed():
        global currentTime
        currentTime = mixer.music.get_pos() // 1000
        seekBar["value"] = currentTime
        startTimeLabel.configure(text="{}".format(datetime.timedelta(seconds=currentTime)))
        seekBar.after(2, timeLapsed)

    timeLapsed()


# Pause Function - Pauses Music
def pause():
    mixer.music.pause()
    root.pauseButton.grid_remove()
    root.resumeButton.grid()
    statusLabel.configure(text="Paused...")


# Resume Function - Resumes Music that was paused by Pause Function
def resume():
    root.resumeButton.grid_remove()
    root.pauseButton.grid()
    mixer.music.unpause()
    statusLabel.configure(text="Playing...")


# Stop Function - Stops the music
def stop():
    mixer.music.stop()
    statusLabel.configure(text="Stopped...")
    seekBarLabel.grid_remove()


# Volume Up Function - Increases Volume
def volumeUp():
    volume = mixer.music.get_volume()
    mixer.music.set_volume(volume + 0.01)
    volumeLabel.configure(text="{}%".format(int(mixer.music.get_volume() * 100)))
    progressBar["value"] = mixer.music.get_volume() * 100


# Volume Down Function - Decreases Volume
def volumeDown():
    volume = mixer.music.get_volume()
    mixer.music.set_volume(volume - 0.01)
    volumeLabel.configure(text="{}%".format(int(mixer.music.get_volume() * 100)))
    progressBar["value"] = mixer.music.get_volume() * 100


# Mute Function - Mutes the sound
def mute():
    root.muteButton.grid_remove()
    root.unmuteButton.grid()
    global currentVolume
    currentVolume = mixer.music.get_volume()
    mixer.music.set_volume(0)


# Unmute Function - unmutes the sound
def unmute():
    root.unmuteButton.grid_remove()
    root.muteButton.grid()
    mixer.music.set_volume(currentVolume)


# Search Function - Used to open the file dialog to select the song
def searchSong():
    try:
        song = filedialog.askopenfilename(initialdir="D:/Songs", title="Select Music File",
                                          filetype=(("MP3", "*.mp3"), ("WAV", "*.wav")))
    except:
        song = filedialog.askopenfilename(title="Select Music File",
                                          filetype=(("MP3", "*.mp3"), ("WAV", "*.wav")))

    audio.set(song)


# Create Widgets Function - Used to create the various buttons, labels and progress bars
def createWidgets():
    # Labels
    trackLabel = Label(root, text="Select Audio Track:", bg="deepskyblue", font=('Calibri', 16, 'italic bold'))
    trackLabel.grid(row=0, column=0, padx=30, pady=30)

    global statusLabel
    statusLabel = Label(root, text="", bg="deepskyblue", font=('Calibri', 16, 'italic bold'))
    statusLabel.grid(row=2, column=1)

    # Entry Box
    trackName = Entry(root, width=35, font=('Calibri', 16, 'italic bold'), textvariable=audio)
    trackName.grid(row=0, column=1, padx=30, pady=30)

    # Buttons
    # 1. Search Button
    searchButton = Button(root, font=('Calibri', 12, 'bold'), width=15, background="mediumpurple2",
                          text="Search🔎", bd=5, activebackground="purple", command=searchSong)
    searchButton.grid(row=0, column=2, padx=30, pady=30)

    # 2. Play Button
    playButton = Button(root, font=('Calibri', 12, 'bold'), width=15, background="green2",
                        text="Play▶️", bd=5, activebackground="darkgreen", command=play)
    playButton.grid(row=1, column=0, padx=30, pady=30)

    # Pause Button
    root.pauseButton = Button(root, font=('Calibri', 12, 'bold'), width=15, background="lightyellow",
                              text="Pause⏯️", bd=5, activebackground="khaki2", command=pause)
    root.pauseButton.grid(row=1, column=1, padx=30, pady=30)

    # Resume Button
    root.resumeButton = Button(root, font=('Calibri', 12, 'bold'), width=15, background="lightyellow",
                               text="Resume▶️", bd=5, activebackground="khaki2", command=resume)
    root.resumeButton.grid(row=1, column=1, padx=30, pady=30)
    root.resumeButton.grid_remove()

    # Stop Button
    stopButton = Button(root, font=('Calibri', 12, 'bold'), width=15, background="firebrick1",
                        text="Stop⏹️", bd=5, activebackground="red4", command=stop)
    stopButton.grid(row=2, column=0, padx=30, pady=30)

    # Volume Up Button
    volumeUpButton = Button(root, font=('Calibri', 12, 'bold'), width=15, background="lightgoldenrod1",
                            text="Volume up➕", bd=5, activebackground="gold2", command=volumeUp)
    volumeUpButton.grid(row=1, column=2, padx=30, pady=30)

    # Volume Down Button
    volumeDownButton = Button(root, font=('Calibri', 12, 'bold'), width=15, background="lightgoldenrod1",
                              text="Volume Down➖", bd=5, activebackground="gold2", command=volumeDown)
    volumeDownButton.grid(row=2, column=2, padx=30, pady=30)

    # Mute Button
    root.muteButton = Button(root, text="Mute🔇", font=('Calibri', 12, 'bold'), width=10, bg="lavenderblush2",
                             activebackground="pink", bd=5, command=mute)
    root.muteButton.grid(row=3, column=3, padx=2, pady=20)
    root.muteButton.grid_remove()

    # Unmute Button
    root.unmuteButton = Button(root, text="Unmute🔊", font=('Calibri', 12, 'bold'), width=10, bg="lavenderblush2",
                               activebackground="pink", bd=5, command=unmute)
    root.unmuteButton.grid(row=3, column=3, padx=2, pady=20)
    root.unmuteButton.grid_remove()

    # Progress Bar for volume
    global progressBarLabel
    progressBarLabel = Label(root, text="", bg="darkgreen")
    progressBarLabel.grid(row=0, column=3, rowspan=3, padx=20, pady=20)
    progressBarLabel.grid_remove()

    global progressBar
    progressBar = Progressbar(progressBarLabel, orient=VERTICAL, mode="determinate", value=0, length=190)
    progressBar.grid(row=0, column=0, ipadx=5)

    global volumeLabel
    volumeLabel = Label(progressBarLabel, text="0%", bg="lightgrey", width=3)
    volumeLabel.grid(row=0, column=0)

    # Seek Bar to see the time lapsed for the song
    global seekBarLabel
    seekBarLabel = Label(root, text="", bg="lightgrey")
    seekBarLabel.grid(row=3, column=0, columnspan=3, padx=20, pady=20)
    seekBarLabel.grid_remove()

    global startTimeLabel
    startTimeLabel = Label(seekBarLabel, text="0:00:00", bg="lightgrey", width=10)
    startTimeLabel.grid(row=0, column=0)

    global endTimeLabel
    endTimeLabel = Label(seekBarLabel, text="0:00:00", bg="lightgrey", width=10)
    endTimeLabel.grid(row=0, column=2)

    global seekBar
    seekBar = Progressbar(seekBarLabel, orient=HORIZONTAL, mode="determinate", value=0)
    seekBar.grid(row=0, column=1, ipadx=250, ipady=3)


root = Tk()   # Used to create the window using Tkinter module
root.geometry('1000x500+200+50')   # sets the size of window
root.title("My Music Player")    # sets the title of the window
root.iconbitmap('Icon.ico')    # sets the icon of the window
root.resizable(False, False)    # sets the condition that the window created cannot be resized in any direction
root.configure(bg="deepskyblue")   # sets the background colour of he window to deepskyblue
audio = StringVar()
currentVolume = 0
createWidgets()
mixer.init()     # mixer is initialized to be used
root.mainloop()   # makes the window visible
