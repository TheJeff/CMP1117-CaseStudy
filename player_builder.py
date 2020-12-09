class Player:

    #init
    def __init__(
        self,
        name,
        games,
        FG,
        three_pointers,
        two_pointers,
        FTP,
        TRB,
        AST,
        PPG
    ):
        self.__name = name
        self.__games = games
        self.__FG_per_game = FG
        self.__3P = three_pointers
        self.__2P = two_pointers
        self.__FTP = FTP
        self.__TRB = TRB
        self.__AST = AST
        self.__PPG = PPG



    # Setters
    def setGames(self, games):
        self.__games = games
 
    def setFieldGoals(self, FG):
        self.__FG_per_game = FG
    
    def set3P(self, three_pointers):
        self.__3P = three_pointers
    
    def set2P(self, two_pointers):
        self.__2P = two_pointers
    
    def setFTP(self, FTP):
        self.__FTP = FTP
  
    def setTRB(self, TRB):
        self.__TRB = TRB 
    
    def setAST(self, AST):
        self.__AST = AST 
    
    def setPPG(self, PPG):
        self.__PPG = PPG


    # Getters
    def getGames(self):
        return self.__games
    
    def getFieldGoals(self):
        return self.__FG_per_game
    
    def get3P(self):
        return self.__3P

    def get2P(self):
        return self.__2P
    
    def getFTP(self):
        return self.__FTP
    
    def getTRB(self):
        return self.__TRB
    
    def getAST(self):
        return self.__AST
    
    def getPPG(self):
        return self.__PPG

    # Returns a dictionary of all stats for the player
    def getStats(self):
        stats = {
            "Name" : self.__name,
            "G" : self.__games,
            "FG" : self.__FG_per_game,
            "3P" : self.__3P,
            "22" : self.__2P,
            "FT" : self.__FTP,
            "TRB" : self.__TRB,
            "AST" : self.__AST,
            "PTS" : self.__PPG
        }
        return stats
       

    # Returns the stat by the glossary name
    # input: name, name of the stat in the glossary
    def getStatByName(self, name):
        player_stats = self.getStats()
        try: 
            stat = player_stats[name]
            return stat
        except KeyError:
            print("That stat was not found. try using the Glossary")


    # Returns a list of all the stat names for the player
    def getStatNames(self):
        # This is memory inefficient
        player_stats = self.getStats()
        stat_names = []

        for key, value in player_stats.items():
            stat_names.append(key)
        
        return stat_names


    # Returns a list of all the stats without the name
    def getPlayerStats(self):
        # Memory inefficient
        player_stats = self.getStats()
        stats = []

        for key, value in player_stats.items():
            stats.append(value)
        
        return stats


    # returns an average of all
    def averageOfStats(self):
        # It's not the most useful but it's here
        # Memory inefficient
        stats = self.getStats()
        total = sum(stats)
        amount = len(stats)
        return total / amount


    # Prints out all player stats 
    # Input: switch, 0 to print with title bar
    def printStats(self, switch):
        player_stats = self.getStats()
        title_bar = []
        stat_bar = []

        for name, stat in player_stats.items():
            title_bar.append(name)
            stat_bar.append(stat)
        
        if switch == 0:
            for heading in title_bar:
                print(heading, end='\t')
            print("\n")
        
        for stat in stat_bar:
            print(stat, end='\t')
        print("\n")
    

    # String method of the object
    # Input: switch, 0 to add the title bar
    def toString(self, switch):
        player_stats = self.getStats()
        title_bar = []
        stat_bar = []
        return_string = ""

        for name, stat in player_stats.items():
            title_bar.append(name)
            stat_bar.append(stat)
        
        if switch == 0:
            for heading in title_bar:
                return_string = return_string + heading + "\t"
            return_string = return_string + "\n"
        
        for stat in stat_bar:
            return_string = return_string + stat + "\t"
        return return_string


    
    



    