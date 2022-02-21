
class Student:

    def __init__(self, name, gender, data_sheet, image_url):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url
    
    def get_avg_grade(self):
        grades = self.data_sheet.get_grades_as_list()
        return sum(grades) / len(grades)

    def show_progression(self):
        max_value = len(self.data_sheet.courses) * 150
        ects_sum = self.data_sheet.get_ects_sum()
        return ects_sum / max_value * 100
            
    

