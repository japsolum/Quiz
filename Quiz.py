#Quiz program will display a paragraph with a set of blanks which the user will have to correctly fill in before moving on
#to the next level

import sys

#String and correct answers for toddler level quiz
tdlrString = "If you're atleast 4 years old this test should be too easy for you, but a warmup cant hurt. If you mix blue and yellow you will get (--1--). A cow says (--2--). One plus two equals (--3--)."
tdlrAnswers = ["green", "moo", "three"]
# String and correct answers for easy level quiz
easyString = "The (--1--) is made up of multiple computers working together to get you the info you need. The computer you're using has a (--2--). It will send command (--3--) to a (--4--) that then sends back the webpage you are requesting."
easyAnswers = ["internet", "browser", "protocols", "server"]
# String and correct answers for medium level quiz
medString = "In programming there are many different (--1--) you can use to accomplish different things. Like (--2--) which is the structure of a webpage. Or there is (--3--) which is what this quiz is using, but can also be used for a wide array of computer programs. There are also languages aimed for more specific tasks like (--4--) which is only used to program ios apps. No matter what language you decide to use they all follow their own (--5--) which is a set of rules the programmer must follow to avoid errors"
medAnswers = ["languages", "html", "python", "swift", "syntax"]
# String and correct answers for hard level quiz
hardString = "Syntax can be tricky. Sometimes the (--1--) you will get will be big and easy to spot, other times they may require you to do some searching. For example 'if a == 2' may seem correct at a first glance but you would actually get a (--2--) error because there is no (--3--). Or 'index = Index + 1' being incorrect due to the second (--4--) not needing to be (--5--). Debugging can be difficult. But using the steps we've learned already, it should get easier with time."
hardAnswers = ["bugs", "syntax", ":", "i", "capital"]

    #  isCorrect uses "answer" which will be provided by user and "correctAnswer" which is the true answer,
    #  and checks to see if they match.
def isCorrect(answer, correctAnswer):
    return answer.lower() == correctAnswer

    # newString replaces the correct blank for whichever question we're on, in oldString with the correct answer ("word")
    # after it is correctly inputted
def newString(answer, num, oldString):
    return oldString.replace("(--" + str(num) +"--)", answer.lower())

keepGoing = True
print "At any time, type 'quit' to end quiz."
# Starting a while loop that will keep program running until user says they dont want to play anymore after either winning, or
# losing a level.
while keepGoing == True:
    value = 0
    while value == 0:
        whichLevel = raw_input("Which difficulty would you like to play? Toddler | Easy | Medium | Hard ")
        print " "
        whichLevel = whichLevel.lower()
        if whichLevel == "toddler":
            value += 1
            thisString = tdlrString
            thisAnswers = tdlrAnswers
        if whichLevel == "easy":
            value += 1
            thisString = easyString
            thisAnswers = easyAnswers
        if whichLevel == "medium":
            value += 1
            thisString = medString
            thisAnswers = medAnswers
        if whichLevel == "hard":
            value += 1
            thisString = hardString
            thisAnswers = hardAnswers
        if whichLevel == "quit":
            sys.exit()

    index = 1
    tries = 5
    print " "
    print thisString
    print " "
    #Loop that will run through once for every blank in the current quiz, will be the bulk of the
    #code and will call all other methods to run the quiz.''
    while index <= len(thisAnswers):
        answer = raw_input("Please enter answer for (--" + str(index) + "--) ")
        print " "
        if answer == "quit":
            sys.exit()
        elif isCorrect(answer, thisAnswers[index-1]):
            if index == len(thisAnswers):
                thisString = newString(answer, index, thisString)
                print "Correct! You've finished the quiz!"
                print " "
                print thisString
                print " "
                index +=1
                tries = 5
            else:
                thisString = newString(answer, index, thisString)
                print "Correct! Now time to move on to next blank!"
                print " "
                print thisString
                print " "
                index +=1
                tries = 5
        else:
            if tries > 1:
                tries -= 1
                print "That answer is incorrect. Try again you have " + str(tries) + " left."
                print " "
            else:
                break

    #Determines if user wants to keep playing or end the program
    nextLevel = raw_input("Would you like to move on to try another level? Yes or No ")
    nextLevel = nextLevel.lower()
    if nextLevel == "yes":
        keepGoing = True
    else:
        keepGoing = False
