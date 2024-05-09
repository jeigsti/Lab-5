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

    def sort(self):
        for ind in range(self.emp):
            min_index = ind
 
        for j in range(ind + 1, self.emp):
            # select the minimum element in every iteration
            if self.emp[j].getPay() < self.emp[min_index].getPay():
                min_index = j
         # swapping the elements to sort the array
        (self.emp[ind], self.emp[min_index]) = (self.emp[min_index], self.emp[ind])    
    def employeePay(self, lastName: str):
        for i in self.emp:
            if i.getLastName() == lastName:
                return i.getPay()
