from operator import pos
from taipy.gui import Gui, notify
class Opportunity:
    opp_num = 1
    def __init__(self,company, position, status):
        self.company = company
        self.position = position
        self.status = status
        self.idNum = Opportunity.opp_num
        Opportunity.opp_num += 1

    def changeStatus(self, newStat):
        self.status = newStat 
    def __repr__(self) -> str:
        return f'Company: {self.company}, Position: {self.position}, Status:{self.status}'

class InternshipTracker:
    def __init__(self):
        self.opportunities = {}

    def addAplication(self, company, position, status):
        newOpp = Opportunity(company, position, status)
        self.opportunities[newOpp.idNum] = newOpp 

    def getApplication(self, target_company):
        matching_opportunities = []

        for id_number, opportunity in self.opportunities.items():
            if opportunity.company == target_company:
                matching_opportunities.append(opportunity)
        return matching_opportunities        
#main
tracker = InternshipTracker()
tracker.addAplication("Amazon", "SWE", "applied")
tracker.addAplication("Amazon", "SWE2", "interviewd")
tracker.addAplication("Google", "SWE2", "interviewd")
print(tracker.opportunities)
print(tracker.getApplication("Amazon"))

        
