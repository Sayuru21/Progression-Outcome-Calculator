markRangers = [0, 20, 40, 60, 80, 100, 120]

initial_state_of_pass_credits = False
initial_state_of_defer_credits = False
initial_state_of_fail_credits = False
number_of_pass_credits = number_of_defer_credits = number_of_fail_credits = 0
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
        global initial_state_of_pass_credits, initial_state_of_defer_credits, initial_state_of_fail_credits, total
        getPassDeferFail()
        initial_state_of_pass_credits = initial_state_of_defer_credits = initial_state_of_fail_credits = False

        total = int(number_of_pass_credits) + int(number_of_defer_credits) + int(number_of_fail_credits)
        if total == 120:
            break
        else:
            print("Total credits are Incorrect")
            print()


def getProgressionOutcome():
    global total_progress_students, total_trailer_students, total_exclude_students, total_retriever_students
    if int(number_of_pass_credits) == 120:
        print("Progress")
        total_progress_students += 1
    elif int(number_of_pass_credits) == 100:
        print("Progress – module trailer")
        total_trailer_students += 1
    elif int(number_of_fail_credits) >= 80:
        print("Exclude")
        total_exclude_students += 1
    else:
        print("Do not progress – module retriever")
        total_retriever_students += 1


def showHistogram():
    while True:

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
print("                                 *** Progression Outcome Calculator ***")
print()
showHistogram()


