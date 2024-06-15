

from pagemaker import PageMaker

root = "http://127.0.0.1:8000"



class AdminHomePage(PageMaker):
    def __init__(self):
        super().__init__()
        # Initializing page length
        self.pageLen = 100


    # Initializing ui
        self.drawUi()
    

    def drawUi(self):
        self.drawLine(self.pageLen)
        self.drawLogo()
        self.drawLine(self.pageLen)
        self.drawLine(self.pageLen)
        self.drawLine(self.pageLen)
        for i in range(3):
            self.drawEndedLine(self.pageLen)
        self.drawLineWithParameters(self.pageLen, "1 - AddCinema")
        self.drawEndedLine(self.pageLen)
        self.drawLineWithParameters(self.pageLen, "2 - Profile")
        for i in range(3):
            self.drawEndedLine(self.pageLen)
        self.drawLine(self.pageLen)
        self.drawLine(self.pageLen)
