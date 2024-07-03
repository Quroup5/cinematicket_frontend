from prompt_toolkit.shortcuts import input_dialog
import os
import urllib
import json
from urllib.request import urlopen
from pagemaker import PageMaker
from adminhome import AdminHomePage

# from ProfilePage import ProfilePage

root = "http://172.17.0.2:8000"

class AdminLogin(PageMaker):
    def __init__(self):
        super().__init__()
        # Initializing page length
        self.pageLength = 100

        # Initializing variables
        self.username = ""
        self.password = ""

        # Drawing Ui 
        self.drawUi()

        # Handle commands
        while(1):
            command = input("Enter the number representing your command:\n")
            if command == "1":
                self.username = input_dialog(title = "Username", text = "Enter your username:",
                                             style = self.dialogStyles).run() 
                os.system('cls' if os.name == 'nt' else 'clear')
                self.drawUi()
            elif command == "2":
                self.password = input_dialog(title = "Password", 
                                             text = "Enter your Password:", 
                                             password = True,
                                             style = self.dialogStyles).run()
                os.system('cls' if os.name == 'nt' else 'clear')
                self.drawUi()
            elif command == "3":
                    post_data = {'name': self.username,
                        'password': self.password
                        }
                    url = root + "/admin/login/"

                    data = json.dumps(post_data).encode('utf-8')
                    req = urllib.request.Request(url, data)

                    try:
                        resp2 = urlopen(req)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        Admin_home_page = AdminHomePage()
                        break
                        # print(resp2.getcode())
                    except Exception as e:
                        print('log in wasnot successfull.Please try again')
            elif command == "4":
                from  welcome import WelcomePage
                os.system('cls' if os.name == 'nt' else 'clear')
                welcome_Page = WelcomePage()
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                self.drawUi()


    def drawUi(self):
        self.drawLine(self.pageLength)
        self.drawLogo()
        self.drawLine(self.pageLength)
        self.pageLength = max([self.pageLength, 
                                len(self.username) + 27, 
                                len(self.password) + 27])
        self.drawLine(self.pageLength)
        self.drawEndedLine(self.pageLength)
        self.drawEndedLine(self.pageLength)
        # drawing username
        if self.username != "":
            self.drawLineWithParametersStartAt(self.pageLength, 2, '1 - Username', ':', 
                                                     self.username)
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '1 - Username') 

        # drawing password
        if self.password != "":
            self.drawLineWithParametersStartAt(self.pageLength, 2, '2 - Password', ':', 
                                                     len(self.password) * "*")
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '2 - Password') 

        self.drawEndedLine(self.pageLength)
        self.drawLineWithParametersStartAt(self.pageLength, 2, '3 - Confirm')
        self.drawEndedLine(self.pageLength)
        self.drawLineWithParametersStartAt(self.pageLength, 2, '4 - Back to Welcome Page')
        self.drawEndedLine(self.pageLength)
        self.drawEndedLine(self.pageLength)
        self.drawLine(self.pageLength)

