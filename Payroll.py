from Employee import Employee

class Payroll():
    def __init__(self):
        self.emp = []

    def __repr__(self):
        return str(self.emp)
    
    def addEmp(self, e):
        self.emp.append(e)
    
    def total(self):
        total_Pay = 0
        for i in self.emp:
            total_Pay += i.getPay()
        return total_Pay


    