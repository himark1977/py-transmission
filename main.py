import car
import rpi
from Tkinter import *
import tkMessageBox

root = Tk(className = "OpenCar")
root.geometry("800x600")

# TK wigets


# MENU BAR
def about():
    tkMessageBox.showinfo("About", "Credits: \n Ilie-Adrian Avramescu \n Python-OBD")
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About...", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
# END
# START

def obd_speed():
    speed_var.set(car.response_speed)
def obd_rpm():
    rpm_var.set(car.response_rpm.value)
def obd_fuel():
    fuel_var.set(car.response_fuel.value)
def do_nothing():
    print("da")
#Speed button
speed = Button()
speed["text"] = "Read Speed"
speed["command"] = obd_speed
speed.grid(row=1,column=0)
#Speed Text
speed_var = StringVar()
speed_var.set("Speed: ")
speedtext = Label(root,textvariable=speed_var)
speedtext.grid(row=1,column=2)

#RPM button
rpm = Button()
rpm["text"] = "Read RPM"
rpm["command"] = obd_rpm
rpm.grid(row=3,column=0)
#RPM Text
rpm_var = StringVar()
rpm_var.set("RPM: ")
rpmtext = Label(root,textvariable=rpm_var)
rpmtext.grid(row=3,column=2)
#Ports Text
connectionstatus = Label(root,text=car.connectstats).grid(row=0,column=0)
ports = Label(root,text=car.ports).grid(row=0,column=2)
# Fuel Level Text
fuel_var = StringVar()
fuel_var.set("Fuel Level: ")
fueltext = Label(root,textvariable=fuel_var).grid(row=5,column=2)
# END
root.mainloop()
root.destroy()