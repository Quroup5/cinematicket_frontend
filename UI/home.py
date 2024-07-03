

from pagemaker import PageMaker



class HomePage(PageMaker):
    def __init__(self):
        super().__init__()
        # Initializing page length
        self.pageLength = 100

    # Initializing ui
        self.drawUi()
    

    def drawUi(self):
        self.drawLine(self.pageLength)
        self.drawLogo()
        self.drawLine(self.pageLength)
        for i in range(3):
            self.drawEndedLine(self.pageLength)
        self.drawEndedLine(self.pageLength)   
        self.drawLineWithParameters(self.pageLength, "1 - BuyingTicket")
        self.drawEndedLine(self.pageLength)
        self.drawLineWithParameters(self.pageLength, "2 - Profile")
        for i in range(3):
            self.drawEndedLine(self.pageLength)
        self.drawLine(self.pageLength)
        self.drawLine(self.pageLength)
