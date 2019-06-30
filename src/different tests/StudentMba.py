from student import Student



class StudentMba(Student):
    def on_honor_roll(self):
        if self.gpa >= 2.5:
            return True
        else:
            return False
