from prompt_toolkit.shortcuts import input_dialog
import os
import os
import urllib
import json
from urllib.request import urlopen
from home import HomePage, root

from pagemaker import PageMaker
# from ProfilePage import ProfilePage

class LoginPage(PageMaker):
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
                url = root + "/user/login/"

                data = json.dumps(post_data).encode('utf-8')
                req = urllib.request.Request(url, data)
                resp2 = urlopen(req)
                print(resp2.getcode())

                if resp2.getcode() == 200: 
                    os.system('cls' if os.name == 'nt' else 'clear')
                    home_page = HomePage()
                    # home_page.username = self.username
                    # print(home_page.username)
                    break

                elif resp2.getcode() == 403:
                    print('log in wasnot successfull')


            elif command == "4":
                from  welcome import WelcomePage
                os.system('cls' if os.name == 'nt' else 'clear')
                welcome_Page = WelcomePage()
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('login again')
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
        self.drawLine(self.pageLength)
    
def user_sender():
    log = LoginPage()
    username = log.username
    print(username) 
