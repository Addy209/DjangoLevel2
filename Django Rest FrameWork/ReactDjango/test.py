import wikipedia

def ask_me(question):
    answer=wikipedia.summary(question)
    return answer

if __name__ == "__main__":
    question=str(input("Enter Your Question:"))
    print(ask_me(question))