from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror, askokcancel
import sounddevice
from scipy.io.wavfile import write
import threading
from datetime import datetime
import time
import os

def close_window():
    if askokcancel(title='Close Voice Recorder', message='Are you sure you want to close the Voice Recorder?'):
        window.destroy()

def record_voice():
    try:
        freq = 44100
        duration = int(duration_entry.get())
            
        recording  = sounddevice.rec(duration*freq, samplerate=freq, channels=2)

        counter = 0
        while counter < duration:
            window.update()
            time.sleep(1)
            counter += 1
            progress_label.config(text=str(counter))
        sounddevice.wait()
        write('recording.wav', freq, recording)
        for file in os.listdir():
            if file == 'recording.wav':
                base, ext = os.path.splitext(file)
                current_time = datetime.now()
                new_name = 'recording-' + str(current_time.hour) + '.' + str(current_time.minute) + '.' + str(current_time.second) + ext
                os.rename(file, new_name) 
        showinfo('Recording complete', 'Your recording is complete')
    except:
        showerror(title='Error', message='An error occurred' \
                   '\nThe following could ' \
                    'be the causes:\n->Bad duration value\n->An empty entry field\n' \
                    'Do not leave the entry empty and make sure to enter a valid duration value')
def recording_thread():
    t1 = threading.Thread(target=record_voice)
    t1.start()


window = Tk()
window.protocol('WM_DELETE_WINDOW', close_window)
window.title('Voice Recorder')
window.geometry('500x450+440+180')
window.resizable(height=FALSE, width=FALSE)

label_style = ttk.Style()
label_style.configure('TLabel', foreground='#000000', font=('OCR A Extended', 15))
entry_style = ttk.Style()
entry_style.configure('TEntry', font=('Dotum', 15))
button_style = ttk.Style()
button_style.configure('TButton', foreground='#000000', font='DotumChe')
canvas = Canvas(window, width=500, height=400)
canvas.pack()
logo = PhotoImage(file='recorder.png')
logo = logo.subsample(2, 2)
canvas.create_image(240, 135, image=logo)
duration_label = ttk.Label(window, text='Enter Recording Duration in Seconds:', style='TLabel')
duration_entry = ttk.Entry(window, width=76, style='TEntry')
canvas.create_window(235, 290, window=duration_label)
canvas.create_window(250, 315, window=duration_entry)

progress_label = ttk.Label(window, text='')
record_button = ttk.Button(window, text='Record', style='TButton', command=recording_thread)
canvas.create_window(240, 365, window=progress_label)
canvas.create_window(240, 410, window=record_button)
window.mainloop()