# Samantha Putin, Anastacia Aguirre, Mandy Guo

#Part A: Total Length
def total_length(str_list):
    total=0
    index= 0
    while index < len(str_list):
        for word in str_list:
            length= len(str_list[index])
            total= total + length
            index= index+1
    return total

my_list1= ["queen", "rules"]
my_list2= []
my_list3= ["balloons"]
my_list4= ["", "", "", ""]

print(total_length(my_list1))
print(total_length(my_list2))
print(total_length(my_list3))
print(total_length(my_list4))


s="Tenochtitlan"
index=0
while index < len(s):
    print(s[:index])
    index= index + 1

# index=0   ->  it serves a similar function as an empty basket;
# instead of adding to it, we use it as our starting point and move from there

# index < len(s)  ->  this serves as our stopping point. since the length of
# a string is always 1 less, especially with while loops, this lets us stop
# at the very last character

# index += 1  ->  this reassignment allows us to move onto the next character.
# it would follow any function you want performed (like adding or printing) so
# that when it loops back, it'll use the character immediately after

# s[:index]  ->  using the colon allows us to use a range of characters in a
# string. before the colon would be the starting point, and since it's blank,
# it assumes the beginning. the index after the colon gives us the last letter
# to include. giving that it is "index" in this case, it would include all the
# characters from the beginning to whatever we assigned to index. 
