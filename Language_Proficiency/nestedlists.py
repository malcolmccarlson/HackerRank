

def main():
    students = []
    I = int(input())
    for i in range(I):
        name = input()
        grade = float(input())
        students.append([name, grade])
        students.sort(key = lambda student: (student[1], student[0]))
    second_lowest = []
    for student in students: 
        if student[1] == students[0][1]:
            pass
        elif student[1] > students[0][1]:
            second_lowest.append(student[1])
            break
    second_lowest_list = []
    for student in students:
        if student[1] == second_lowest[0]:
            second_lowest_list.append(student)
        else:
            pass

    for student in second_lowest_list:
        print(student[0])


if __name__ == '__main__':
    main()        

