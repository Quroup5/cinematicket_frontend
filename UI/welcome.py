import os

from loginpage import LoginPage
from pagemaker import PageMaker
from registerpage import RegisterPage
from adminlogin import AdminLogin

class WelcomePage(PageMaker):
    def __init__(self):
        # Initializing page length
        self.pageLength = 100


        # Initializing ui
        self.drawUi()

        # Handle Commands
        while 1:
            command = input(
                """Enter the number representing your comand:\n(ex. 1 - register -->> your input: 1)\n"""
            )
            if command == "1":
                os.system("cls" if os.name == "nt" else "clear")
                registerPage = RegisterPage()
                break
            elif command == "2":
                os.system("cls" if os.name == "nt" else "clear")
                loginPage = LoginPage()
                break
            elif command == "3":
                os.system("cls" if os.name == "nt" else "clear")
                adminLogin = AdminLogin()
                break
            else:
                os.system("cls" if os.name == "nt" else "clear")
                self.drawUi()

    def drawUi(self):
        self.drawLine(self.pageLength)
        self.drawLogo()
        self.drawLine(self.pageLength)
        for i in range(3):
            self.drawEndedLine(self.pageLength)
        self.drawLineWithParameters(self.pageLength, "1 - register")
        self.drawEndedLine(self.pageLength)
        self.drawLineWithParameters(self.pageLength, "2 - login")
        self.drawEndedLine(self.pageLength)
        self.drawLineWithParameters(self.pageLength, "3 - Adminlogin")
        for i in range(3):
            self.drawEndedLine(self.pageLength)
        self.drawLine(self.pageLength)
        self.drawLine(self.pageLength)
