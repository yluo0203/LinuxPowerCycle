import sys, getopt
from get_func import *
import subprocess
import python_safe_reboot
import time
import tkinter
import tkinter.messagebox


# def get_count(file_name):
#     # read files
#     # Using readlines()
#     file1 = open(file_name, 'r')
#     Lines = file1.readlines()
#
#     count = 0
#     # Strips the newline character
#     for line in Lines:
#         if "Rebooting" in line:
#             count += 1
#             # print("Line{}: {}".format(count, line.strip()))
#     return count

# print(get_filepath("testfile.txt"))

# python_safe_reboot.main()


print("Hello")

def buttonClick():
	tkinter.messagebox.showinfo("Power Cycling", "rebooting")
	time.sleep(3)
	# tkinter.messagebox.showinfo("Power Cycling", "rebooting")
	print("World~")


root=tkinter.Tk()
root.title("GUI")
root.geometry('100x100')
root.resizable(False, False)
tkinter.Button(root, text = 'Hello Button', command=buttonClick).pack()
root.mainloop()
# subprocess.getstatusoutput("python3 /root/Desktop/Rev3/python_safe_reboot.py")
