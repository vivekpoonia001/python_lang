print("Welcome to the Quiz")
quiz = []
def add_list():
        print("enter list of your questions")
        num = int(input("enter your range of questions"))
        for i in range(1, num+1):
            qst = input("enter your  question")
            opt = input("enter your options").split(",")
            ans = input("enter your answer ")
            list_1 = {"qst":qst,"opt":opt, "ans":ans}
            quiz.append(list_1)
            print(quiz)
def list_quiz():
        for index , list_1 in enumerate(quiz, start = 1):
            print(f"{index} .{list_1['qst']} {list_1['opt']}{list_1['ans']}")


def update_list():
    for i , q in enumerate(quiz, start = 1):
          print(f"{i}.{q['qst']}")
    index = int(input("enter the index question for update"))
    if 1<= index<=len(quiz):
          quiz[index-1]['qst'] = input("enter new question")
          quiz[index-1]['opt'] = input("enter new options").split(",")
          quiz[index-1]['ans'] = input("enter your new answer")
          print("updated sucesfully")
          print(quiz)
    else:
          print("invalid index")

def delete_list():
      if not quiz:
            print("there is now such index")
      else:
         for index ,q in enumerate(quiz, start =1):
               print(f"{index}. {q['qst']}")
         index = int(input("enter your question to delete"))
         if 1<=index<=len(quiz):
               deleted_question = quiz[index-1]['qst']
               del quiz[index-1]
               print("deleteion succsesfull")
               print("deleted file is",deleted_question)

def play_list():

    if not quiz:
        print("No questions available")
        return

    score = 0

    for index, q in enumerate(quiz, start=1):

        print(f"\n{index}. {q['qst']}")

        for opt_index, option in enumerate(q['opt'], start=1):
            print(f"{opt_index}. {option}")

        answer = input("Enter your answer: ")

        if answer.lower() == q['ans'].lower():
            print("Correct")
            score += 1
        else:
            print("Wrong answer")
            print("Correct answer is:", q['ans'])

    print("\nQuiz completed successfully")
    print(f"Your score: {score}/{len(quiz)}")

def end_quiz():
      print("quiz ended")
      print("thankyou")
def main():
      while True :
            print("\n quiz managemnet system") 
            print("1.add_quiz")
            print("2.list_quiz")
            print("3.update_quiz")
            print("4.delete_quiz")
            print("5.play_quiz")
            print("6.exit")
            choice = int(input("enter your choice "))
            if choice== 1:
                  add_list()
            elif choice == 2:
                  list_quiz()
            elif choice == 3:
                  update_list()
            elif choice == 4:
                  delete_list()
            elif choice == 5:
                  play_list()
            elif choice == 6:
                  end_quiz()
                  break
            else:
                  print("invalid choice")
                  

main()


        
               
        



    




    