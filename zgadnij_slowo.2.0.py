import sys
import random
lista = ['tata', 'mama','brat', ' miasto', 'stolica', 'rodzina', 'milosc']
word = random.choice(lista) 
nomber_of_tries = int(input("Ile chcesz mieć prób?"))
used_letters = []

user_word = []

def find_indexes(word, letter):
    indexes = []
    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)
    return indexes
    
def show_state_of_word():
    print()
    print(user_word)
    print("Pozostało prób", nomber_of_tries)
    print("Użyte litery: ", used_letters)

for _ in word:
    user_word.append("_")

while True:
   letter = input("Podaj literę: ") 
   used_letters.append(letter)
   found_indexes = (find_indexes(word, letter))
   if len(found_indexes) == 0:
        print("Nie ma takiej litery.")
        nomber_of_tries -= 1
   if nomber_of_tries == 0:
         print("Koniec gry.")
         sys.exit(0)
   else:
        for index in found_indexes:
            user_word[index] = letter
            if "".join(user_word) == word:
                print("Bravo! To jest slowo:", word)
                sys.exit(0)

   show_state_of_word()