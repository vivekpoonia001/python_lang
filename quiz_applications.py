print("Welcome to the Quiz")
quiz = []
def add_list():
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
        for index , list_1 in enumerate(quiz, start = 1):
            print(f"{index} {list_1['question']} {list_1['option']}{list_1['answer']}")


def update_list():
    for i , q in enumerate(quiz, start = 1):
          print(f"{i}.{q['quiz']}")
    index = print(input("enter the index question for update"))
    if 1<= index<=len(quiz):
          quiz[index-1]('qst') = input("enter new question")
          quiz[index-1]('opt') = input("enter new options").split(",")
          quiz[index-1]('ans') = input("enter your new answer")
          print("updated sucesfully")
          print(quiz)
    else:
          print("invalid index")

def delete_list():
      if not quiz:
            print("there is now such index")
      else:
         for index ,q in enumerate(quiz, start =1):
               print(f"{index}. {q['quiz']}")
         index = print(input("enter your question to delete"))
         if 1<=index<=len(quiz):
               deleted_question = quiz[index-1]['question']
               del quiz[index-1]
               

        
               
        



    




    