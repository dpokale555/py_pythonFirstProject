# Given the names and grades for each student in a class of
#
# students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
#
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

if __name__ == '__main__':
    students={}
    for N in range(int(input())):
        name = input()
        score = float(input())
        students[name]= score
        print(students)

    def get_score(student):
        return student[1]

    sorted_students = sorted(students.items(), key=get_score, reverse=True)

    unique_scores = sorted(set(score for name, score in sorted_students), reverse=True)
    second_highest_score = unique_scores[1]

    second_highest_students = [name for name, score in sorted_students if score == second_highest_score]

    second_highest_students.sort()

    print("Names of the students with the second highest score:")
    for student in second_highest_students:
        print(student)