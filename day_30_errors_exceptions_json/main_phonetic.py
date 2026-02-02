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

def generate_phonetic():
    # nato_list = [phonetic[letter.upper()] for letter in word if letter.upper() in phonetic.keys()]
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(output_list)
    return word

# phonetic = readWithCsv()
phonetic = readWithPandas()  

def main():
    word = ''
    while word != 'Q':
        word = generate_phonetic()
if __name__ == "__main__": 
    main()