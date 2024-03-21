# Samantha Putin, Anastacia Aguirre, Mandy Guo

#Part B: Abracadabra (using while)
def letter_tree(string):
    index= len(string)
    while index >= 0:
        print(string[:index])
        index= index - 1

letter_tree("abracadabra")
