class Student:
    """The class for student, and it not only could record the information of student, but subject and scores."""
    def __init__(self, department, grade, id_num, name, economic,
                 accounting, statistics, management, intro_com, programming):
        """Initialize the class and define the attributions of it."""
        self.department = department
        self.grade = grade
        self.id = id_num
        self.name = name
        self.__economic = economic
        self.__accounting = accounting
        self.__statistics = statistics
        self.__management = management
        self.__intro_com = intro_com
        self.__programming = programming
        self.score_table = [self.__economic,
                            self.__accounting,
                            self.__statistics,
                            self.__management,
                            self.__intro_com,
                            self.__programming]

    def getinfo(self):
        """Return student's personal information"""
        return self.department, self.grade, self.id, self.name

    def sored_score(self):
        """sorted the score"""
        origin_score = {'economic': self.__economic,
              'accounting': self.__accounting,
              'statistics': self.__statistics,
              'management': self.__management,
              'intro_com': self.__intro_com,
              'programming': self.__programming}

        order_list = sorted(self.score_table)

        return order_list

    def average(self):
        """Return average score"""
        return round(sum(self.score_table) / len(self.score_table), 2)

    def highest(self):
        """Return highest subject and score"""
        return max(self.score_table)

    def lowest(self):
        """Return lowest subject and score"""
        return min(self.score_table)


def main():

    st1 = Student('BA', '3', 'S04410376', 'Andrew', 65, 15, 33, 28, 89, 92)
    print(st1.sored_score())


main()
