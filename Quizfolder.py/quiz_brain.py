# Creating a class that consists of procedural methods that our quiz will follow
class QuizBrain:
    # initializing the attributes to the rest of the methods within the class
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    # method that determines the while loop. Once the boolean is false, our class will exit.
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    '''
    this method finds the index of the question_list, 
    adds 1 to it for the next question outputted to user. 
    Also it introduces the check_answer method so that 
    the next method can compare to this method.
    '''
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_ans, current_question.answer)

    '''
    Taking the user_ans, this method compares the attributes presented in the
    end of the previous method (self.check_answer) and compares them. 
    If true, 1 is added to the score. 
    Either way, the correct answer is printed as well as 
    the user's current score and the question number
    '''
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You are right!")
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.")


