# Chris Danyluk & Jeremy Gargana
# Class to hold game data

class data:

    def __init__(self, curPoints, time_limit, move_num, light, secret, curLoc, curLocBool):
        self.score = curPoints
        self.time_limit = time_limit
        self.move_num = move_num
        self.light = light
        self.secret = secret
        self.curLoc = curLoc
        self.curLB = curLocBool

    def getScore(self):
        return self.score
    
    def getTime_Limit(self):
        return self.time_limit
        
    def getMove_Num(self):
        return self.move_num

    def getLight(self):
        return self.light
    
    def getSecret(self):
        return self.secret

    def getLocation(self):
        return self.curLoc

    def getLocBool(self):
        return self.curLB

    def goto(self):
        self.score += 5

    def incMove_Num(self, i):
        self.move_num += i

    def obtLight(self):
        self.light = True

    def obtSecret(self):
        self.secret = True

    def setLocBool(self, i):
        self.curLB[i] = True
