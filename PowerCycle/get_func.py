import subprocess
import time
import python_safe_reboot
import tkinter
import tkinter.messagebox


def get_filepath(file_name):
    s = subprocess.getstatusoutput("pwd")[1] + "/" + file_name
    print(s)
    return s

def get_count(file_name):
    # read files
    # Using readlines()
    file1 = open(file_name, 'r')
    Lines = file1.readlines()

    count = 0
    # Strips the newline character
    for line in Lines:
        if "Rebooting" in line:
            count += 1
            # print("Line{}: {}".format(count, line.strip()))
    return count

def add_log(count, action_list, file_name):
    subprocess.getstatusoutput("echo " + str(count + 1) + " >> " + file_name)
    for action in action_list:
        action = str(action)
        subprocess.getstatusoutput(action + " >> " + file_name)[1]
        wait("logging: " + action, 1)
    print(str(count + 1) + ": " + str(action_list)[1:-1])
    return

def go_reboot(file_name):
    action = "reboot"
    # action = "whoami"
    subprocess.getstatusoutput("echo Rebooting >> " + file_name)
    subprocess.getstatusoutput("echo  >> " + file_name)
    wait("reboot", 10)

    subprocess.getstatusoutput("echo reboot >> " + file_name)[1]
    #subprocess.getstatusoutput("sh /root/Desktop/Rev3/reboot.sh")
    # subprocess.getstatusoutput(action)
    # subprocess.getstatusoutput("python3 /root/Desktop/Rev3/python_safe_reboot.py")
    # subprocess.getstatusoutput("python3 /root/Desktop/Rev3/python_safe_reboot.py")
    python_safe_reboot.main()
    subprocess.getstatusoutput("echo  >> " + file_name)

def wait(action_string, sec):
    for i in range(sec):
        print(action_string + ", wait for " + str(sec - i) + " second.")
        time.sleep(1)
    # print(action_string)

def msgBox(num):
    message = "Cycling " + str(num) + " times."
    tkinter.messagebox.showinfo("Power Cycling", "Tset Completed!")

def go_finish(file_name, count):
    print(" ===== Test Completed! =====")
    subprocess.getstatusoutput("echo ===== Test Completed! ===== >> " + file_name)
    subprocess.getstatusoutput("echo ")
    subprocess.getstatusoutput("echo |==================================================================================| >> " + file_name)
    subprocess.getstatusoutput("echo |                                                                                  | >> " + file_name)
    subprocess.getstatusoutput("echo |       Test Completed!                                                            | >> ")
    subprocess.getstatusoutput("echo |       Total: " + str(count) + " cycles.                                                          | >> " + file_name)
    subprocess.getstatusoutput("echo |       Log File: " + file_name + "                    | >> " + file_name)
    subprocess.getstatusoutput("echo |                                                                                  | >>" + file_name)
    subprocess.getstatusoutput("echo |                                                                                  | >>" + file_name)
    subprocess.getstatusoutput("echo |==================================================================================|>> " + file_name)
    return
