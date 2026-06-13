print("Welcome to the Quiz")
quiz = []
def add_list():
    while True:
        print("enter list of your questions")
        num = int(input("enter your range of questions"))
        for i in range(1, num+1):
            qst = input("enter your first question")
            opt = input("enter your options").split(",")
            ans = input("enter your answer ")
            list_1 = {"question":qst,"option":opt, "ans":ans}
            quiz.append(list_1)
            print(quiz)
def list_quiz():
    while True:
        
    




    