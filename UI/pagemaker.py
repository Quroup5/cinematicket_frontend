from prompt_toolkit.styles import Style


class PageMaker:
    def __init__(self):
        self.dialogStyles = Style.from_dict(
            {
                "dialog": "bg:#999999",
                "dialog frame.label": "bg:#c3c3c3 #575757",
                "dialog.body": "bg:#c3c3c3 #575757",
                "dialog shadow": "bg:#232323",
            }
        )

    @staticmethod
    def drawLine(lineLength):
        print("*" * lineLength + "\n", end = '')

    @staticmethod
    def drawEndedLine(lineLength):
        print("**" + " " * (lineLength - 4) + "**\n", end = '')

    @staticmethod
    def drawSpaces(spaceCount):
        print(" " * spaceCount, end = '')

    def drawLineWithParameters(self, lineLength, *args):
        totalEmptySpaces = lineLength - 4
        for arg in args:
            totalEmptySpaces -= len(arg)
        eachSpace = totalEmptySpaces // (len(args) + 1)
        remainingSpaces = totalEmptySpaces - eachSpace * (len(args) + 1)
        print("**", end = '')
        for arg in args:
            if remainingSpaces > 0:
                self.drawSpaces(eachSpace + 1)
                remainingSpaces -= 1
            else:
                self.drawSpaces(eachSpace)
            print(arg, end = '')
        self.drawSpaces(eachSpace)
        print("**\n", end = '')

    def drawLineWithParametersStartAt(self, lineLength, start, *args):
        remainingSpace = lineLength - 4 - start
        print("**", end = '')
        self.drawSpaces(start)
        for arg in args:
            print(arg, end = '')
            print(" ", end = '')
            remainingSpace -= len(arg) + 1
        self.drawSpaces(remainingSpace)
        print("**\n", end = '')

    def drawMovieGrid(self, lineLength, movies, page):
        spaceCounts = [0, 0, 0, 0]
        pageMovies = movies[(page - 1) * 8: min(page * 8, len(movies))]
        for movie in pageMovies:
            spaceCounts[0] = max(spaceCounts[0], len(movie['name']))
            spaceCounts[1] = max(spaceCounts[1], len(movie['date']))
            spaceCounts[2] = max(spaceCounts[2], len(movie['capacityLeft']))
            spaceCounts[3] = max(spaceCounts[3], len(movie['price']))
        for i in spaceCounts:
            lineLength -= i
        lineLength -= 16
        for i in range(len(pageMovies)):
            movie = pageMovies[i]
            print('**', end = '  ')
            print(str(i + 1) + ' - ', end = '')
            print(movie['name'], end = '')
            print(' ' * (spaceCounts[0] - len(movie['name'])), end = ', ')
            print(movie['date'], end = '')
            print(' ' * (spaceCounts[1] - len(movie['date'])), end = ', ')
            print(movie['capacityLeft'], end = '')
            print(' ' * (spaceCounts[2] - len(movie['capacityLeft'])), end = ', ')
            print(movie['price'], end = '')
            print(' ' * (spaceCounts[3] - len(movie['price'])), end = '')
            self.drawSpaces(max(lineLength, 0))
            print('**', end = '\n')

    def drawLogo(self):
                        print(""" 
                              
                     _                                 _    _        _          _   
                    (_)                               | |  (_)      | |        | |  
                ___  _  _ __    ___  _ __ ___    __ _ | |_  _   ___ | | __ ___ | |_ 
                / __|| || '_ \  / _ \| '_ ` _ \  / _` || __|| | / __|| |/ // _ \| __|
                | (__ | || | | ||  __/| | | | | || (_| || |_ | || (__ |   <|  __/| |_ 
                \___||_||_| |_| \___||_| |_| |_| \__,_| \__||_| \___||_|\_\\___| \__|   
                              
                              
                              """)
