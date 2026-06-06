from tkinter import *
from tkinter import messagebox

#Root Window
root = Tk()
root.title("Subnetter")
root.minsize(800,600)

#Functions
def calculate():
    net_id.configure(state='normal')
    subnets.configure(state='normal')
    firstip.configure(state='normal')
    lastip.configure(state='normal')
    total_hosts.configure(state='normal')
    broadc.configure(state='normal')

    net_id.delete(0, END)
    subnets.delete(0, END)
    firstip.delete(0, END)
    lastip.delete(0, END)
    total_hosts.delete(0,END)
    broadc.delete(0, END)

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
            net_id.insert(0, (oct1, ".", oct2, ".", oct3, ".", oct4))

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
            subnets.insert(0, (sub1, ".", sub2, ".", sub3, ".", sub4))

            #First Host
            if cidr != 32:
                first_host = oct4+1
            else:
                first_host = oct4
            firstip.insert(0, (oct1, ".", oct2, ".", oct3, ".", first_host))

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
            lastip.insert(0, (oct1, ".", oct2, ".", oct3, ".", oct4))

                #Total Host
            bit = 32 - cidr
            if cidr == 32:
                hosts = 0
                pass
            else:
                hosts = 1
                for i in range(bit):
                    hosts *= 2
                hosts -= 2

            total_hosts.insert(0, hosts)

            #Broadcast
            if cidr == 32:
                broad = oct4
            else:
                broad = oct4+1
            broadc.insert(0, (oct1, ".", oct2, ".", oct3, ".", broad))

    except (ValueError, TypeError):
        error()
    net_id.configure(state='disabled', disabledforeground="black")
    subnets.configure(state='disabled', disabledforeground="black")
    firstip.configure(state='disabled', disabledforeground="black")
    lastip.configure(state='disabled', disabledforeground="black")
    total_hosts.configure(state='disabled', disabledforeground="black")
    broadc.configure(state='disabled', disabledforeground="black")

def error():
    clear_all()
    warning = messagebox.showerror("ERROR", "NOT A VALID IP ADDRESS/CIDR")

def clear_all():
    net_id.configure(state='normal')
    subnets.configure(state='normal')
    firstip.configure(state='normal')
    lastip.configure(state='normal')
    total_hosts.configure(state='normal')
    broadc.configure(state='normal')
    ip1.delete(0, END)
    ip2.delete(0, END)
    ip3.delete(0, END)
    ip4.delete(0, END)
    bits.delete(0, END)
    net_id.delete(0, END)
    subnets.delete(0, END)
    firstip.delete(0, END)
    lastip.delete(0, END)
    total_hosts.delete(0,END)
    broadc.delete(0, END)
    net_id.configure(state='disabled', disabledforeground="black")
    subnets.configure(state='disabled', disabledforeground="black")
    firstip.configure(state='disabled', disabledforeground="black")
    lastip.configure(state='disabled', disabledforeground="black")
    total_hosts.configure(state='disabled', disabledforeground="black")
    broadc.configure(state='disabled', disabledforeground="black")

#Creating
title_frame = Frame(root, width=600)
title = Label(title_frame, text="SUBNETTER", font=("TkDefaultFont", 35, "bold"), pady=30)
subtitle = Label(title_frame, text="A Simple Tool For Calculating Subnets!", font=("TkDefaultFont", 20))
#
input_frame = Frame(root, width=600)
ipdescription = Label(input_frame, text="IP Address/CIDR", font=("TkDefaultFont", 12), pady= 50, padx= 25)
ipdot1 = Label(input_frame, text=".", font=("TkDefaultFont", 20))
ipdot2 = Label(input_frame, text=".", font=("TkDefaultFont", 20))
ipdot3 = Label(input_frame, text=".", font=("TkDefaultFont", 20))
ipslash = Label(input_frame, text="/", font=("TkDefaultFont", 20))
#
result_frame = Frame(root, width=600, pady=45)
result_id = Frame(result_frame)
network = Label(result_id, text="Network ID: ", font=("TkDefaultFont", 12))
subnetmask = Label(result_id, text="Subnet Mask: ", font=("TkDefaultFont", 12))
first = Label(result_id, text="First Host: ", font=("TkDefaultFont", 12))
last = Label(result_id, text="Last Host: ", font=("TkDefaultFont", 12))
n_hosts = Label(result_id, text="Total Hosts: ", font=("TkDefaultFont", 12))
broadcast = Label(result_id, text="Broadcast IP: ", font=("TkDefaultFont", 12))

net_id = Entry(result_id, font=("TkDefaultFont", 12))
net_id.configure(state='disabled')
subnets = Entry(result_id, font=("TkDefaultFont", 12))
subnets.configure(state="disabled")
firstip = Entry(result_id, font=("TkDefaultFont", 12))
firstip.configure(state="disabled")
lastip = Entry(result_id, font=("TkDefaultFont", 12))
lastip.configure(state="disabled")
total_hosts = Entry(result_id, font=("TkDefaultFont", 12))
total_hosts.configure(state="disabled")
broadc = Entry(result_id, font=("TkDefaultFont", 12))
broadc.configure(state="disabled")
#
developer = Label(root, font=("TkDefaultFont", 10), fg="grey", text="Developed with Python\n by Riccardo Milani\n Source Code: https://github.com/Asatras-Vault/Subnetter")
#Buttons
buttons_frame = Frame(root,width=600)
calculatebutton = Button(buttons_frame, text="Calculate!", font=("TkDefaultFont", 12), width=40, command=calculate)
clearbutton = Button(buttons_frame, text="Clear", font=("TkDefaultFont", 12), width=10, command=clear_all)
#Inputs
ip1 = Entry(input_frame, width=5,font=("TkDefaultFont", 12))
ip2 = Entry(input_frame, width=5, font=("TkDefaultFont", 12))
ip3 = Entry(input_frame, width=5, font=("TkDefaultFont", 12))
ip4 = Entry(input_frame, width=5, font=("TkDefaultFont", 12))
bits = Entry(input_frame, width=5, font=("TkDefaultFont", 12))

#Showing
title_frame.pack()
title.pack()
subtitle.pack()
#
input_frame.pack()
ipdescription.pack(side="left")
#
ip1.pack(side="left")
ipdot1.pack(side="left")
ip2.pack(side="left")
ipdot2.pack(side="left")
ip3.pack(side="left")
ipdot3.pack(side="left")
ip4.pack(side="left")
ipslash.pack(side="left")
bits.pack(side="left")
#
buttons_frame.pack()
calculatebutton.pack(side="left")
clearbutton.pack(side="right")
#
result_frame.pack()
result_id.grid(row=0, column=0)
network.grid(row=0, column=0)
subnetmask.grid(row=1, column=0)
first.grid(row=2, column=0)
last.grid(row=3, column=0)
n_hosts.grid(row=4, column=0)
broadcast.grid(row=5, column=0)

net_id.grid(row=0, column=1)
subnets.grid(row=1, column=1)
firstip.grid(row=2, column=1)
lastip.grid(row=3, column=1)
total_hosts.grid(row=4, column=1)
broadc.grid(row=5, column=1)
#
developer.pack()

root.mainloop()
