# Python Youtube Download: https://www.youtube.com/watch?v=BPhvbIuq7uM
# How to install Pytube: https://www.youtube.com/watch?v=mUs97qXjw1M

# Importing libraries
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from pytube import YouTube #pip install pytube3

# Global Path
Folder_Name = ""

# File location
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name, fg="green")
    else:
        locationError.config(text="Please Choose Folder!!", fg = "red")

# Download video
def DownloadVideo():
    choice = ytbchoices.get()
    url = ytbEntry.get()
    
    if len(url) < 1:
        messagebox.showerror("Error", "URL cannot be Empty!")
        yt = YouTube(url)
        
        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()
            
        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True, file_extension="mp4").last()
            
        elif(choice == choices[2]): 
            select = yt.streams.filter(only_audio=True).first()
        
        else:
           messagebox.showerror("Error", "Past link again!")
            
     # Download function
        select.download(Folder_Name)
        messagebox.showsuccess("Success", "Download completed!")
        
# Creating a GUI Interface using Tkinter
root = Tk()
root.geometry("350x400") #set window
root.columnconfigure(0,weight=1) # set all content in center
root.title("YTB video Downloader by Mentorama")
root.resizable(0,0)

# Ytb link label
ytbLabel = Label(root, text="Enter the URL of the video:", font = ("jost", 15))
ytbLabel.grid()

# Create a field to enter link
ytbEntryVar = StringVar()
ytbEntry = Entry(root, width = 50, textvariable = ytbEntryVar)
ytbEntry.grid()

# Error msg
YtbError = Label(root, text="Error Msg", fg="red", font=("jost", 10))
YtbError.grid()

# Asking save file label
saveLabel = Label(root, text="Save the Video File", font=("jost", 15, "bold"))
saveLabel.grid()

# Button of save file
saveEntry = Button(root, width=10, bg="red", fg="white",text="Choose Path", command=openLocation)
saveEntry.grid()

# Error msg location
locationError = Label(root, text="Error Msg of Path", fg="red", font=("jost",10))
locationError.grid()

# Download Quality
ytbQuality = Label(root, text="Select Quality", font=("jost",15))
ytbQuality.grid()

# Combobox
choices = ["1080p","720p","144p","Only Audio"]
ytbchoices = ttk.Combobox(root, values = choices)
ytbchoices.grid()

# Download Button
downloadbtn = Button(root, text="Download", width=10, bg="red", fg="white", command=DownloadVideo)
downloadbtn.grid()

# Developer label
developerLabel = Label(root, text="Mentorama - Python do Zero", font = ("jost", 15))
developerLabel.grid()
root.mainloop()

