



#task_1

# myFinalMarks = {'CSF': 75, 'FunPro': 80, 'WT': 85}
#
# def calculateAverage(finalMarks):
# 	total = 0
# 	average = 0
#
# 	for key in finalMarks:
# 		total = total+finalMarks[key]
# 	average = total/len(finalMarks)
# 	return average
#
# print(calculateAverage(myFinalMarks))

def calculate_average(marks):
    total = 0
    for key in marks:
        total = total + marks[key]
    average = total / len(marks)
    return average


def display_average(mark):
    print(mark)


def main():
    marks = {'CSF': 75, 'FunPro': 80, 'WT': 85}
    display_average(calculate_average(marks))


if __name__ == '__main__':
    main()