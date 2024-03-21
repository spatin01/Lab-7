# Samantha Putin, Anastacia Aguirre, Mandy Guo

#Part C: Count Characters (using while)
def count_characters(string, target):
    total=0
    index=0
    while index < len(string):
        if string[index] == target:
            total = total +1
        index= index + 1
    return total

print(count_characters("bonobos", "o"))
print(count_characters("abracadabra", "a"))
