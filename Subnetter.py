from tkinter import *
from tkinter import messagebox

#Root Window
root = Tk()
root.title("Subnetter")
root.minsize(800, 600)
root.maxsize(800, 600)

#Functions
def calculate():

    oct1 = ip1.get()
    oct2 = ip2.get()
    oct3 = ip3.get()
    oct4 = ip4.get()
    cidr = bits.get()
    try:
        oct1 = int(oct1)
        oct2 = int(oct2)
        oct3 = int(oct3)
        oct4 = int(oct4)
        cidr = int(cidr)


        #Network ID, code doesn't check if ip is a host or not
        if oct1 > 255 or oct1 < 0 or oct2 > 255 or oct2 < 0 or oct3 > 255 or oct3 < 0 or oct4 > 255 or oct4 < 0 or cidr > 32 or cidr <= 0:
            error()
        else:
            net_id = Label(root, text=(oct1, ".", oct2, ".", oct3, ".", oct4), font=("TkDefaultFont", 12))
            net_id.place(relx=0.5, rely=0.5, anchor=E)

            #Subnet Mask
            if cidr == 32:
                sub1 = 255
                sub2 = 255
                sub3 = 255
                sub4 = 255
            elif cidr >= 24 and cidr < 32:
                sub1 = 255
                sub2 = 255
                sub3 = 255
                sub4 = 1
                for b in range(32 - cidr):
                    sub4 *= 2
                sub4 = 256 - sub4
            elif cidr >= 16 and cidr < 24:
                sub1 = 255
                sub2 = 255
                sub3 = 1
                sub4 = 0
                for b in range(24 - cidr):
                    sub3 *= 2
                sub3 = 256 - sub3
            elif cidr >= 8 and cidr < 16:
                sub1 = 255
                sub2 = 1
                sub3 = 0
                sub4 = 0
                for b in range(16 - cidr):
                    sub2 *= 2
                sub2 = 256 - sub2
            elif cidr <= 8:
                sub1 = 1
                sub2 = 0
                sub3 = 0
                sub4 = 0
                for b in range(8 - cidr):
                    sub1 *= 2
                sub1 = 256 - sub1
            subnets = Label(root, text=(sub1, ".", sub2, ".", sub3, ".", sub4), font=("TkDefaultFont", 12))
            subnets.place(relx=0.5, rely=0.6, anchor=E)

            #First Host
            if cidr != 32:
                first_host = oct4+1
            else:
                first_host = oct4
            first = Label(root, text=(oct1, ".", oct2, ".", oct3, ".", first_host), font=("TkDefaultFont", 12))
            first.place(relx=0.5, rely=0.7, anchor=E)

            #last host
            ips = 1
            if cidr == 32:
                pass
            elif cidr >= 24 and cidr < 32:
                for b in range(32 - cidr):
                    ips *= 2
                oct4 += ips -2
                if oct4 > 255:
                    error()

            elif cidr >= 16 and cidr < 24:
                for b in range(24 - cidr):
                    ips *= 2
                oct4 = 254
                oct3 += ips -1
                if oct3 > 255:
                    error()

            elif cidr >= 8 and cidr < 16:
                for b in range(16 - cidr):
                    ips *= 2
                oct4 = 254
                oct3 = 255
                oct2 += ips -1
                if oct2 > 255:
                    error()

            elif cidr <= 8:
                for b in range(8 - cidr):
                    ips *= 2
                oct4 = 254
                oct3 = 255
                oct2 = 255
                oct1 += ips - 1
                if oct1 > 255:
                    error()
            last = Label(root, text=(oct1, ".", oct2, ".", oct3, ".", oct4), font=("TkDefaultFont", 12))
            last.place(relx=0.5, rely=0.8, anchor=E)

                #Total Host
            bit = 32 - cidr
            hosts = 1
            for i in range(bit):
                hosts *= 2
            hosts -= 2

            total_hosts = Label(root, text=hosts, font=("TkDefaultFont", 12))
            total_hosts.place(relx=0.8, rely=0.5, anchor=E)

            #Broadcast
            if cidr == 32:
                broad = oct4
            else:
                broad = oct4+1
            broad = Label(root, text=(oct1, ".", oct2, ".", oct3, ".", broad), font=("TkDefaultFont", 12))
            broad.place(relx=0.5, rely=0.9, anchor=E)

    except ValueError, TypeError:
        error()

def error():
    warning = messagebox.showerror("ERROR", "NOT A VALID IP ADDRESS/CIDR")

#Creating
title = Label(root, text="SUBNETTER", font=("TkDefaultFont", 25, "bold"))
subtitle = Label(root, text="A Simple Tool For Calculating Subnets!", font=("TkDefaultFont", 15))
ipdescription = Label(root, text="IP Address/CIDR", font=("TkDefaultFont", 12))
ipdot1 = Label(root, text=".", font=("TkDefaultFont", 20))
ipdot2 = Label(root, text=".", font=("TkDefaultFont", 20))
ipdot3 = Label(root, text=".", font=("TkDefaultFont", 20))
ipslash = Label(root, text="/", font=("TkDefaultFont", 20))
network = Label(root, text="Network ID: ", font=("TkDefaultFont", 12))
subnetmask = Label(root, text="Subnet Mask: ", font=("TkDefaultFont", 12))
first = Label(root, text="First Host: ", font=("TkDefaultFont", 12))
last = Label(root, text="Last Host: ", font=("TkDefaultFont", 12))
n_hosts = Label(root, text="Total Hosts: ", font=("TkDefaultFont", 12))
broadcast = Label(root, text="Broadcast IP: ", font=("TkDefaultFont", 12))
developer = Label(root, font=("TkDefaultFont", 7), fg="grey", text="Developed with Python\n by Riccardo Milani")
#Buttons
calculatebutton = Button(root, text="Calculate!", font=("TkDefaultFont", 12), width=45, padx=5, command=calculate)
#Inputs
ip1 = Entry(root, width=5,font=("TkDefaultFont", 12))
ip2 = Entry(root, width=5, font=("TkDefaultFont", 12))
ip3 = Entry(root, width=5, font=("TkDefaultFont", 12))
ip4 = Entry(root, width=5, font=("TkDefaultFont", 12))
bits = Entry(root, width=5, font=("TkDefaultFont", 12))

#Showing
title.place(relx=0.5, rely=0.01,anchor=N)
#
subtitle.place(relx=0.5, rely=0.15, anchor=N)
#
ipdescription.place(relx=0.1, rely=0.3, anchor=W)
ip1.place(relx=0.5, rely=0.3, anchor=E)
ipdot1.place(relx=0.52, rely=0.3, anchor=E)
ip2.place(relx=0.58, rely=0.3, anchor=E)
ipdot2.place(relx=0.6, rely=0.3, anchor=E)
ip3.place(relx=0.66, rely=0.3, anchor=E)
ipdot3.place(relx=0.68, rely=0.3, anchor=E)
ip4.place(relx=0.74, rely=0.3, anchor=E)
ipslash.place(relx=0.76, rely=0.3, anchor=E)
bits.place(relx=0.82, rely=0.3, anchor=E)
calculatebutton.place(relx=0.5, rely=0.4, anchor=CENTER)
#
network.place(relx=0.1, rely=0.5, anchor=W)
#
subnetmask.place(relx=0.1, rely=0.6, anchor=W)
#
first.place(relx=0.1, rely=0.7, anchor=W)
#
last.place(relx=0.1, rely=0.8, anchor=W)
#
n_hosts.place(relx=0.6, rely=0.5, anchor=W)
#
broadcast.place(relx=0.1, rely=0.9, anchor=W)

#developer.grid(row=9)


root.mainloop()
