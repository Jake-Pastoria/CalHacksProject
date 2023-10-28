from operator import pos
from taipy.gui import Gui, notify
class Opportunity:
    def __init__(self,company, position, status):
        self.company = company
        self.position = position
        self.status = status

    def changeStatus(self, newStat):
        self.status = newStat 
    def __repr__(self) -> str:
        return f'postition: {self.position}, status: {self.status}'

class InternshipTracker:
    def __init__(self):
        self.opportunities = {}

    def addAplication(self, company, position, status):
        newOpp = Opportunity(company, position, status)
        self.opportunities[company] = newOpp 

#main
tracker = InternshipTracker()
tracker.addAplication("Amazon", "SWE", "applied")
print(tracker.opportunities)

        
