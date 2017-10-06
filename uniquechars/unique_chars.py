# Create a function called `unique_characters` that takes a string as parameter
# and returns a list with the unique letters of the given string
# Create basic unit tests for it with at least 3 different test cases
# Should print out:
# ["n", "g", "r", "m"]

def unique_characters(string):
    list_of_letters = []
    if string == "":
        return "no string given"
    for i in string:
        if i != "a":
            list_of_letters.append(i) 
    return list_of_letters


print(unique_characters("anagram"))