class Player:

    #init
    def __init__(self, name):
        self.__name = name

    # Setters

    def setAge(self, age):
        self.__age = age
    
    def setGames(self, games):
        self.__games = games

    def setStarted(self, started):
        self.__started = started

    def setMinutesPlayed(self, minutes):
        self.__minutes_played = minutes 

    def setEFG(self, EFG):
        self.__effective_field_goals = EFG

    # Field Goal Setters 
    def setFieldGoals(self, FG):
        self.__FG_per_game = FG
    
    def setFGA(self, FGA):
        self.__FG_attempts = FGA
    
    def setFGP(self, FGP):
        self.__FG_percent = FGP 

    # 3-Point Setters
    def set3P(self, three_pointers):
        self.__3P = three_pointers
    
    def set3PA(self, TPA):
        self.__3PA = TPA
    
    def set3PP(self, TPP):
        self.__3PP = TPP
    
    # 2-Point Setters
    def set2P(self, two_pointers):
        self.__2P = two_pointers
    
    def setTPA(self, TPA):
        self.__2PA = TPA
    
    def setTPP(self, TPP):
        self.__2PP = TPP

    # Free Throws
    def setFreeThrows(self, FT):
        self.__FT = FT
    
    def setFTA(self, FTA):
        self.__FTA = FTA
    
    def setFTP(self, FTP):
        self.__FTP = FTP

    # Rebounds per game
    def setORB(self, ORB):
        self.__ORB = ORB
    
    def setDRB(self, DRB):
        self.__DRB = DRB
    
    def setTRB(self, TRB):
        self.__TRB = TRB 
    
    # Other stats
    def setAST(self, AST):
        self.__AST = AST 
    
    def setSTL(self, STL):
        self.__STL = STL
    
    def setBLK(self, BLK):
        self.__BLK = BLK
    
    def setTOV(self, TOV):
        self.__TOV = TOV
    
    def setPF(self, PF):
        self.__PF = PF
    
    def setPPG(self, PPG):
        self.__PPG = PPG


    # Getters
    def getGames(self):
        return self.__games
    
    def getStarted(self):
        return self.__started
    
    def getMinPlayed(self):
        return self.__minutes_played
    
    def getFieldGoals(self):
        return self.__FG_per_game
    
    def getFGA(self):
        return self.__FG_attempts
    
    def getFGP(self):
        return self.__FG_percent
    
    def get3P(self):
        return self.__3P
    
    def get3PA(self):
        return self.__3PA
    
    def get3PP(self):
        return self.__3PP
    
    def get2P(self):
        return self.__2P
    
    def get2PA(self):
        return self.__2PA
    
    def get2PP(self):
        return self.__2PP
    
    def getFT(self):
        return self.__FT
    
    def getFTA(self):
        return self.__FTA
    
    def getFTP(self):
        return self.__FTP
    
    def getORB(self):
        return self.__ORB
    
    def getTRB(self):
        return self.__TRB
    
    def getAST(self):
        return self.__AST
    
    def getSTL(self):
        return self.__STL
    
    def getBLK(self):
        return self.__BLK
    
    def getTOV(self):
        return self.__TOV
    
    def getPF(self):
        return self.__PF
    
    def getPPG(self):
        return self.__PPG

    
    



    