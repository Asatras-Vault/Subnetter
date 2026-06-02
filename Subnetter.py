from tkinter import *

#Root Window
root = Tk()
root.title("Subnetter")
root.geometry("600x300")


#Functions
def calculate():

    oct1 = ip1.get()
    oct2 = ip2.get()
    oct3 = ip3.get()
    oct4 = ip4.get()
    cidr = bits.get()

    oct1 = int(oct1)
    oct2 = int(oct2)
    oct3 = int(oct3)
    oct4 = int(oct4)
    cidr = int(cidr)

    #Network ID, code doesn't check if ip is a host or not
    if oct1 > 255 or oct1 < 0 or oct2 > 255 or oct2 < 0 or oct3 > 255 or oct3 < 0 or oct4 > 255 or oct4 < 0 or cidr >= 32 or cidr <= 0:
        pass
    else:
        net_id = Label(root, text=(oct1, ".", oct2, ".", oct3, ".", oct4), width=20)
        net_id.grid(row= 2, column=1)

        #Subnet Mask
        if cidr == 32:
            sub1 = 255
            sub2 = 255
            sub3 = 255
            sub4 = 255
            subnets = Label(root, text=(sub1, ".", sub2, ".", sub3, ".", sub4), width=20)
            subnets.grid(row=3, column=1)
        elif cidr >= 24 and cidr < 32:
            sub1 = 255
            sub2 = 255
            sub3 = 255
            sub4 = 1
            for b in range(32 - cidr):
                sub4 *= 2
            sub4 = 256 - sub4
            subnets = Label(root, text=(sub1, ".", sub2, ".", sub3, ".", sub4), width=20)
            subnets.grid(row=3, column=1)
        elif cidr >= 16 and cidr < 24:
            sub1 = 255
            sub2 = 255
            sub3 = 1
            sub4 = 0
            for b in range(24 - cidr):
                sub3 *= 2
            sub3 = 256 - sub3
            subnets = Label(root, text=(sub1, ".", sub2, ".", sub3, ".", sub4), width=20)
            subnets.grid(row=3, column=1)
        elif cidr >= 8 and cidr < 16:
            sub1 = 255
            sub2 = 1
            sub3 = 0
            sub4 = 0
            for b in range(16 - cidr):
                sub2 *= 2
            sub2 = 256 - sub2
            subnets = Label(root, text=(sub1, ".", sub2, ".", sub3, ".", sub4), width=20)
            subnets.grid(row=3, column=1)
        elif cidr <= 8:
            sub1 = 1
            sub2 = 0
            sub3 = 0
            sub4 = 0
            for b in range(8 - cidr):
                sub1 *= 2
            sub1 = 256 - sub1
            subnets = Label(root, text=(sub1, ".", sub2, ".", sub3, ".", sub4), width=20)
            subnets.grid(row=3, column=1)

        #First Host
        if cidr != 32:
            first = Label(root, text=(oct1, ".", oct2, ".", oct3, ".", oct4+1), width=20)
            first.grid(row= 4, column=1)
        else:
            first = Label(root, text=(oct1, ".", oct2, ".", oct3, ".", oct4), width=20)
            first.grid(row= 4, column=1)

        #last host
        ips = 1
        if cidr == 32:
            last = Label(root, text=(oct1, ".", oct2, ".", oct3, ".", oct4), width=20)
            last.grid(row=5, column=1)

        elif cidr >= 24 and cidr < 32:
            for b in range(32 - cidr):
                ips *= 2
            oct4 += ips -2
            if oct4 > 255:
                oct3 += 1
                oct4 = oct4 - 255
            last = Label(root, text=(oct1, ".", oct2, ".", oct3, ".", oct4), width=20)
            last.grid(row=5, column=1)

        elif cidr >= 16 and cidr < 24:
            for b in range(24 - cidr):
                ips *= 2
            oct4 = 254
            oct3 += ips -1
            if oct3 > 255:
                oct2 += 1
                oct3 = oct3 - 255
            last = Label(root, text=(oct1, ".", oct2, ".", oct3, ".", oct4), width=20)
            last.grid(row=5, column=1)

        elif cidr >= 8 and cidr < 16:
            for b in range(16 - cidr):
                ips *= 2
            oct4 = 254
            oct3 = 255
            oct2 += ips -1
            if oct2 > 255:
                oct1 += 1
                oct2 = oct2 - 255
            last = Label(root, text=(oct1, ".", oct2, ".", oct3, ".", oct4), width=20)
            last.grid(row=5, column=1)

        elif cidr <= 8:
            for b in range(8 - cidr):
                ips *= 2
            oct4 = 254
            oct3 = 255
            oct2 = 255
            oct1 += ips - 1
            if oct1 > 255:
                pass
            else:
                last = Label(root, text=(oct1, ".", oct2, ".", oct3, ".", oct4), width=20)
                last.grid(row=5, column=1)

            #Total Host
        bit = 32 - cidr
        hosts = 1
        for i in range(bit):
            hosts *= 2
        hosts -= 2

        total_hosts = Label(root, text=hosts, width=20)
        total_hosts.grid(row=6, column= 1)

        #Broadcast
        broad = Label(root, text=(oct1, ".", oct2, ".", oct3, ".", oct4+1), width=20)
        broad.grid(row=7, column=1)



#Creating
subtitle = Label(root, text="Use Subnetter to calculate subnets!")
ipdescription = Label(root, text="IP Address/CIDR")
ipdot1 = Label(root, text=".")
ipdot2 = Label(root, text=".")
ipdot3 = Label(root, text=".")
ipslash = Label(root, text="/")
network = Label(root, text="Network ID: ", pady=5)
subnetmask = Label(root, text="Subnet Mask: ", pady=5)
first = Label(root, text="First Host: ", pady=5)
last = Label(root, text="Last Host: ", pady=5)
n_hosts = Label(root, text="Total Hosts: ", pady=5)
broadcast = Label(root, text="Broadcast IP: ", pady=5)
whitespace = Label(root, width=20)
space = Label(root, width=1)
developer = Label(root, font=("TkDefaultFont", 7), fg="grey", text="Developed with Python\n by Riccardo Milani")
#Buttons
calculatebutton = Button(root, text="Go!", padx=5, command=calculate)
#Inputs
ip1 = Entry(root, width=5)
ip2 = Entry(root, width=5)
ip3 = Entry(root, width=5)
ip4 = Entry(root, width=5)
bits = Entry(root, width=5)

#Showing
subtitle.grid(row=0, column=0)
#
ipdescription.grid(row=1, column=0, pady=20)
whitespace.grid(row=1, column=1)
ip1.grid(row=1, column=2)
ipdot1.grid(row=1, column=3)
ip2.grid(row=1, column=4)
ipdot2.grid(row=1, column=5)
ip3.grid(row=1, column=6)
ipdot3.grid(row=1, column=7)
ip4.grid(row=1, column=8)
ipslash.grid(row=1, column=9)
bits.grid(row=1, column=10)
space.grid(row=1, column=11)
calculatebutton.grid(row=1, column=12)
#
network.grid(row=2)
#
subnetmask.grid(row=3)
#
first.grid(row=4)
#
last.grid(row=5)
#
n_hosts.grid(row=6)
#
broadcast.grid(row=7)

developer.grid(row=8)


root.mainloop()
