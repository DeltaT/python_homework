class Student:
    """Functions: record student's information, and also their scores for each course.
    Of course, the score would be sorted."""

    def __init__(self, department, grade, id_num, name, economics,
                 accounting, statistics, management, intro_comp, programming):
        """Initialize the attributes of this class"""
        self.department = department
        self.grade = grade
        self.id_num = id_num
        self.name = name
        self.__score_table = {'Economics': economics,
                              'Accounting': accounting,
                              'Statistics': statistics,
                              'Management': management,
                              'Intro_comp': intro_comp,
                              'Programming': programming}

    def get_info(self):
        """You can use this method to get the personal information of the student."""
        title = ['Department:', 'Grade:', 'ID:', 'Name:']
        info = [self.department, self.grade, self.id_num, self.name]

        print('Student Information'.center(25, '='))  # create title line
        for i in range(0, 4):
            print('{:<12s}{:>13s}'.format(title[i], info[i]))  # format the output

    def highest(self):
        """You can use this method to get the highest course name and score."""
        for item in self.__score_table.items():
            if item[1] == max(self.__score_table.values()):
                return item

    def lowest(self):
        """You can use this method to get the lowest course name and score."""
        for item in self.__score_table.items():
            if item[1] == min(self.__score_table.values()):
                return item

    def average(self):
        """You can use this method to get average."""
        return round(sum(self.__score_table.values()) / len(self.__score_table), 2)

    def sorting(self):
        """Sort the courses by its score"""
        non_sort = []  # create an empty list object
        for item in self.__score_table.items():
            non_sort.append(item)  # use for loop to append elements which in dictionary object

        # sorting the origin order with built-in function and lambda, and assign to new list
        sort_res = sorted(non_sort, key=lambda score: score[1], reverse=True)
        return sort_res

    def all(self):
        """Format all you need"""
        self.get_info()

        print('Sorted course'.center(25, '_'))
        st = self.sorting()
        for i in range(0, 6):
            print('{:<12s}{:>13d}'.format(st[i][0], st[i][1]))

        print(''.center(25, '_'))
        avg = self.average()
        print('{:<12s}{:>13.2f}'.format('Average', avg))
        print(''.center(25, '='))

        print('Highest course'.center(25, ':'))
        high = self.highest()
        print('{:<12s}{:>13d}'.format(high[0], high[1]))

        print('Lowest course'.center(25, ':'))
        low = self.lowest()
        print('{:<12s}{:>13d}'.format(low[0], low[1]))

        print('End Of Report'.center(25, '='), '\n\n')


def main():
    st1 = Student('BA', '3RD', 'S04410376', 'Andrew', 66, 15, 33, 28, 89, 92)  # student1's records
    st2 = Student('MIS', '3RD', 'S04290151', 'Bela', 78, 25, 63, 58, 73, 46)  # student2's records
    st3 = Student('MIS', '4TH', 'S03290126', 'Cathy', 34, 66, 71, 98, 44, 25)  # student3's records

    st1.all()
    st2.all()
    st3.all()


main()
