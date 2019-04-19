import math


def Average(lst): 
    answer = sum(lst) / len(lst)
    return float(answer)


def main():
    n = int(input())
    student_grades = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_grades[name] = scores
    query_name = input()
    grades = []
    for key, value in student_grades.items():
        if key == query_name:
            grades.append(value)
    flatgrades = [i for sublist in grades for i in sublist]
    answer = Average(flatgrades)
    print("%.2f" % answer)

if __name__ == '__main__':
    main()

