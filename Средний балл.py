grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
grades_Aaron = grades[0]
grades_Bilbo = grades[1]
grades_Johnny = grades[2]
grades_Khendrik = grades[3]
grades_Steve = grades[4]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
list.sort(students)
grades_Aaron = sum(grades_Aaron)/len(grades_Aaron)
grades_Bilbo = sum(grades_Bilbo)/len(grades_Bilbo)
grades_Johnny = sum(grades_Johnny)/len(grades_Johnny)
grades_Khendrik = sum(grades_Khendrik)/len(grades_Khendrik)
grades_Steve = sum(grades_Steve)/len(grades_Steve)
Grades = [grades_Aaron,grades_Bilbo,grades_Johnny,grades_Khendrik,grades_Steve]
dictionary = dict(zip(students,Grades))
print(dictionary)