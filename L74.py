# Samantha Putin, Anastacia Aguirre, Mandy Guo

# Part D: until_dot (using while)

# index < len(s)  ->  ensuring we go from first character to last
# s[index] != " "  ->  tells the program to stop at the first space
# index += 1  ->  moves to the next character
# print(s[:index])  ->  prints the first letter to whatever non-space character
# it should print the first word: Mind

index=0 
s= "Mind the gap!"
while index < len(s) and s[index] != " ":
    index += 1
print(s[:index])

def until_dot(string):
    index= 0
    while index < len(string) and string[index] != ".":
        index = index + 1
    print(string[:index])

until_dot("This is a sentence. This is another.")
until_dot("192.168.200.2")
until_dot("No dots here")


# Break on through
def find_512():
    for x in range(100):
        for y in range(100):
            if x*y == 512:
                break 
    return f"{x} * {y} == 512"

print(find_512())


def find_512():
    for x in range(100):
        for y in range(100):
            if x*y == 512:
                return f"{x} * {y} == 512"

print(find_512())
