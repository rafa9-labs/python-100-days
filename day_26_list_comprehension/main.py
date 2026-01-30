#TODO 1. Create a dictionary in this format.
# {'A': 'Alfa', 'B': 'Bravo', ... }
import csv
import pandas

def readWithCsv():
    with open("C:/Users/rafa/projects/python-100-days/day_26_list_comprehension/nato_phonetic_alphabet.csv", newline="") as f:
        reader = csv.DictReader(f)
        phonetic = {row['letter']: row['code'] for row in reader}
        
def readWithPandas():
    data = pandas.read_csv("C:/Users/rafa/projects/python-100-days/day_26_list_comprehension/nato_phonetic_alphabet.csv")
    return {row.letter: row.code for (idx, row) in data.iterrows()}
        
        
# phonetic = readWithCsv()
phonetic = readWithPandas()

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def changeToNato(word: str):
    word_list = list(word.upper())
    # nato_list = [value for key, value in phonetic.items() if key and word_list]
    nato_list = [phonetic[letter.upper()] for letter in word if letter.upper() in phonetic.keys()]
    return nato_list

def main():
    word = ''
    while word != 'q':
        word = input("Enter a word: ")
        if word == 'q':
            continue
        elif word.isalpha:
            nato_list = changeToNato(word)
            print(nato_list)
        else:
            print("Enter only alphabetic characters.\n")
            

if __name__ == "__main__": 
    main()