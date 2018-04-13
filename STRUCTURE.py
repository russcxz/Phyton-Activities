#russel john cortez
#STRUCTURES

letters = ['r','r','u','s','s','s','r','r',
                's','u','u','u','u','u','s','s',
                'r','s','s','r','u','u','u',
                's','u','s','u','u','r','r','s',
                'u','r','s','u','s','s','r']


from collections import Counter
letters_counts = Counter(letters)
repeat = letters_counts.most_common(3)
print ("letters repeated")
print(repeat)
