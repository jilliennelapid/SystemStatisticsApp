# I've attempted the extra credit.
# Please give program the 5 seconds to update,
# Hopefully it works :) Thank you!
from tkinter import *
from tkinter import ttk
import requests

# method refresh allows the percent values to update.
# A Button is implemented further down that allows the values to be refreshed at anytime.
# After running for the first time, the GUI will refresh after 5 seconds by using the after() method.
def refresh():
    # Makes function calls to the dedicated functions for updating the values.
    updateCPU()
    updateDisk()
    updateMem()

    # Allows the values to refresh after 5000ms (5secs)
    _root.after(5000, refresh)


# The following 3 methods make use of requests.get() pointing to http://localhost:8000/____
# in order to retrieve the data sent via routing. The text from these specific urls is acquired
# then using a set() method, the variables holding the text data for the Labels below are updated:

# method updateCPU that updates the value of percent usage of the CPU.
def updateCPU():
    cpu_req = requests.get('http://localhost:8000/cpu')
    c = cpu_req.text

    _cpu_msg.set(c)

# method updateDisk that updates the value of percent usage of the Disk
def updateDisk():
    disk_req = requests.get('http://localhost:8000/disk')
    d = disk_req.text

    _disk_msg.set(d)

# method updateMem that updates the value of percent usage of Memory
def updateMem():
    mem_req = requests.get('http://localhost:8000/mem')
    m = mem_req.text

    _mem_msg.set(m)


# Meant to run from the terminal
if __name__ == "__main__":
    # Creates the main window by creating an instance of tkinter's Tk.
    # Names the window and makes the window un-resizable.
    _root = Tk()
    _root.title("System Monitor")
    _root.resizable(False, False)

    # Creates the main Frame that will contain all the elements of the window.
    _mainframe = ttk.Frame(_root, padding='50 20 50 20')
    _mainframe.grid(row=0, column=0, sticky="")

    # smaller frame, _display_frame that holds the cpu, disk, and memory info
    _display_frame = ttk.LabelFrame(_mainframe, padding='3 3 3 3')
    _display_frame.grid(row=0, column=0, sticky="")


    # CPU Labels
    # Displays the basic text "CPU Usage %" and the percent usage.
    _cpu = ttk.Label(_display_frame, text="CPU Usage %: ")
    _cpu.grid(row=0, column=0)

    _cpu_msg = StringVar()
    _cpuP = ttk.Label(_display_frame, textvariable=_cpu_msg)
    cR = Entry(_display_frame, textvariable=_cpu_msg)
    _cpuP.grid(row=0, column=1)

    # Disk Labels
    # Displays the basic text "Disk Usage %" and the percent usage.
    _disk = ttk.Label(_display_frame, text="Disk Usage %: ")
    _disk.grid(row=1, column=0)

    _disk_msg = StringVar()
    _diskP = ttk.Label(_display_frame, textvariable=_disk_msg)
    dR = Entry(_display_frame, textvariable=_disk_msg)
    _diskP.grid(row=1, column=1)

    # Memory Labels
    # Displays the basic text "Memory Usage %" and the percent usage.
    _mem = ttk.Label(_display_frame, text="Memory Usage %: ")
    _mem.grid(row=2, column=0)

    _mem_msg = StringVar()
    _memP = ttk.Label(_display_frame, textvariable=_mem_msg)
    mR = Entry(_display_frame, textvariable=_mem_msg)
    _memP.grid(row=2, column=1)


    # Refresh button
    # Can be pressed to update the values whenever desired.
    _refresh_btn = ttk.Button(_mainframe, text='Refresh', command=refresh)
    _refresh_btn.grid(row=4, column=0, sticky="", pady=2)

    # Makes the initial refresh call to acquire the first values
    # as well as begin the automatic refreshing of the values.
    refresh()

    _root.mainloop()
