from prettytable import PrettyTable

markRangers = [0, 20, 40, 60, 80, 100, 120]
initial_state_of_pass_credits = False
initial_state_of_defer_credits = False
initial_state_of_fail_credits = False
number_of_pass_credits = number_of_defer_credits = number_of_fail_credits = 0
array_pass_credits = array_defer_credits = array_fail_credits = 0
total = 0
total_progress_students = total_trailer_students = total_retriever_students = total_exclude_students = 0
total_students = 0


def getPassCredits(number_of_pass_credits):
    try:
        number_of_pass_credits = int(number_of_pass_credits)
        if number_of_pass_credits in markRangers:
            global initial_state_of_pass_credits
            initial_state_of_pass_credits = True
        else:
            print("Input is out of range.")
            print()
    except ValueError:
        print("Input is not a number.")
        print()


def getDeferCredits(number_of_defer_credits):
    try:
        number_of_defer_credits = int(number_of_defer_credits)
        if number_of_defer_credits in markRangers:
            global initial_state_of_defer_credits
            initial_state_of_defer_credits = True
        else:
            print("Input is out of range.")
            print()
    except ValueError:
        print("Input is not a number.")
        print()


def getFailCredits(number_of_fail_credits):
    try:
        number_of_fail_credits = int(number_of_fail_credits)
        if number_of_fail_credits in markRangers:
            global initial_state_of_fail_credits
            initial_state_of_fail_credits = True
        else:
            print("Input is out of range.")
            print()
    except ValueError:
        print("Input is not a number.")
        print()


def getPassDeferFail():

    while not initial_state_of_pass_credits:
        global number_of_pass_credits
        number_of_pass_credits = input("Enter the Pass Credits: ")
        getPassCredits(number_of_pass_credits)

    while not initial_state_of_defer_credits:
        global number_of_defer_credits
        number_of_defer_credits = input("Enter the Defer Credits: ")
        getDeferCredits(number_of_defer_credits)

    while not initial_state_of_fail_credits:
        global number_of_fail_credits
        number_of_fail_credits = input("Enter the Fail Credits: ")
        getFailCredits(number_of_fail_credits)


def checkTotal():
    while True:
        global array_pass_credits, array_defer_credits, array_fail_credits
        global initial_state_of_pass_credits, initial_state_of_defer_credits, initial_state_of_fail_credits, total
        getPassDeferFail()

        initial_state_of_pass_credits = initial_state_of_defer_credits = initial_state_of_fail_credits = False

        total = int(number_of_pass_credits) + int(number_of_defer_credits) + int(number_of_fail_credits)

        if total == 120:
            for i in range(len(markRangers)):
                if int(number_of_pass_credits) == markRangers[i]:
                    array_pass_credits = markRangers[i]
                if int(number_of_defer_credits) == markRangers[i]:
                    array_defer_credits = markRangers[i]
                if int(number_of_fail_credits) == markRangers[i]:
                    array_fail_credits = markRangers[i]
            break
        else:
            print("Total credits are Incorrect")
            print()


def getProgressionOutcome():
    global total_progress_students, total_trailer_students, total_exclude_students, total_retriever_students
    if int(array_pass_credits) == 120:
        print("Progress")
        total_progress_students += 1
    elif int(array_pass_credits) == 100:
        print("Progress – module trailer")
        total_trailer_students += 1
    elif int(array_fail_credits) >= 80:
        print("Exclude")
        total_exclude_students += 1
    else:
        print("Do not progress – module retriever")
        total_retriever_students += 1


def showHistogram():
    while True:

        global total_progress_students, total_trailer_students, total_retriever_students, total_exclude_students
        checkTotal()
        print()
        print("Progression Outcome: ", end="")
        getProgressionOutcome()

        quit = input("If you want to Quit the programme enter q: ")
        print()
        if quit.lower() == "q":
            break

    print(f"Progress {total_progress_students}: " + "*" * total_progress_students)
    print(f"Trailing {total_trailer_students}: " + "*" * total_trailer_students)
    print(f"Retriever {total_retriever_students}: " + "*" * total_retriever_students)
    print(f"Excluded {total_exclude_students}: " + "*" * total_exclude_students)

    global total_students
    total_students = total_progress_students + total_trailer_students + total_retriever_students + total_exclude_students
    print()
    print(f"{total_students} outcomes in total.")
    print()

    max_students_array = [total_progress_students, total_trailer_students, total_retriever_students, total_exclude_students]
    max_students = max_students_array[0]

    max_index = len(max_students_array)
    for i in range(1, max_index):
        if max_students_array[i] > max_students:
            max_students = max_students_array[i]

    # print(max_students)
    row_1 = []
    for j in range(max_students):

        if total_progress_students > 0:
            row_1.append("*")
            total_progress_students -= 1
        else:
            row_1.append(" ")

        if total_trailer_students > 0:
            row_1.append("*")
            total_trailer_students -= 1
        else:
            row_1.append(" ")

        if total_retriever_students > 0:
            row_1.append("*")
            total_retriever_students -= 1
        else:
            row_1.append(" ")

        if total_exclude_students > 0:
            row_1.append("*")
            total_exclude_students -= 1
        else:
            row_1.append(" ")

    # print(row_1)

    my_table = PrettyTable()
    my_table.field_names = ["Progress", "Trailing", "Retriever", "Excluded"]

    a = 0
    b = 0
    while b < max_students:
        my_table.add_row([row_1[a], row_1[a + 1], row_1[a + 2], row_1[a + 3]])
        a += 4
        b += 1


    print(my_table)


print()
print("                                 *** Progression Outcome Calculator ***")
print()
showHistogram()
