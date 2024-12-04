class Flashcards:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning

    def __str__(self):
        return self.word+ '('+self.meaning+')'
    
flash=[]
print("Hi. This is a flashcard.")

while True:
    word=input("Enter a word: ")
    meaning=input("Enter its meaning: ")
    flash.append(Flashcards(word,meaning))
    option=input("Enter 0 if you want to add another flashcard; otherwise, enter the enter key: ")
    if(option):
        break
    print("|n your flashcard")
    for i in flash:
        print(">",i)

