import datetime
import time
import tkinter
from threading import *
from tkinter import *
from tkinter import messagebox



root = Tk()

root.geometry("450x260")




def Threading():
    t1 = Thread(target=alarm)
    t1.start()


def alarm():
    while True:
        setalarm = f"{hour.get()}:{minute.get()}:{second.get()}"

        time.sleep(1)

        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        print(currenttime, setalarm)

        if currenttime == setalarm:
            print("Time To Wake Up")
            MsgBox = messagebox.askquestion('Alarm-Clock', 'Time To Wake Up', icon="warning")
            if MsgBox != 'Yes':
                root.destroy()
                sys.exit()



Label(root, text="ALARM CLOCK", font="Castellar 20 bold", fg="black").pack(pady=15)
Label(root, text="Set Time", font="Arial 15 bold", fg="Blue").pack(pady=10)
Label(root, text="H       M        S", font="Arial 15 bold",fg="black").pack(pady=1)

frame = Frame(root)
frame.pack()

hour = StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07','08', '09', '10', '11', '12', '13', '14', '15', '16',
         '17', '18', '19', '20', '21', '22', '23', '24')
hour.set(hours[0])
hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minute = StringVar(root)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16',
           '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46',
           '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60')
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

second = StringVar(root)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16'
        ,'17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47','48',
           '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60')
second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)


Button(root, text="Set Alarm", font="Aileron 15", command=Threading).pack(pady=20)


root.mainloop()




