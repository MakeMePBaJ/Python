# importing time module
from tkinter import *
from datetime import datetime

# timer clock
def timer_01():

      now = datetime.now()
      clock_time = now.strftime("%H:%M:%S.%f") [:-4]
      visual_01.config(text = clock_time)
      window_01.after(1, timer_01) # every 1000 ms / 1 sec, gets refreshed

def timer_02():

      now = datetime.now()
      clock_time = now.strftime("%d.%m.%Y")
      visual_02.config(text = clock_time)
      window_02.after(1, timer_02) # every 1000 ms / 1 sec, gets refreshed

# main window config
window_01 = Tk()
window_01.title("Main Python Clock - PRECISE TIME")

# Change the background color using configure
window_01.configure(bg = "black")

# window 01
visual_01 = Label(window_01, 
      font = ("coolvetica", 100),
      bg = "black",
      fg = "white"
      )
visual_01.pack(expand=True)

# starts main clock
timer_01()

# second window config
window_02 = Toplevel(window_01)
window_02.title("Second Python Clock - CURRENT DATE")

# Change the background color using configure
window_02.configure(bg = "black")

# window 01
visual_02 = Label(window_02, 
      font = ("coolvetica", 70),
      bg = "black",
      fg = "white"
      )
visual_02.pack(expand=True)

# starts second clock
timer_02()

# runs the window
window_01.mainloop()

