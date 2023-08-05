class Job:
    def __init__(self, profession: str, place: str = None, salary: str = None, link: str = None, modality: str = None):
        self.profession = profession
        self.place = place
        if (salary != None):
            salary = self.checkSalary(salary)
        self.salary = salary
        self.modality = modality
        self.link = link

    def checkSalary(self, salary):
        fixed = salary[2:(salary.find("."))].replace(",", "").replace("'", "")
        return fixed
