text = """
Everyone counts.
Everyone has access to great learning.
Every person's unique talents are valued equally.
Everyone takes responsibility for themselves and their community."""

# Make a dictionary where the keys are characters and the values are the number of times that character appears in the `text` print the dicitonary
letter_counts= {} #initialization
for letter in text: #iterate through a list 
    if letter in letter_counts:
        letter_counts [letter] += 1 #update if the key exists already
else: 
    letter_counts [letter]= 1 #update by adding the key 
    print (letter_counts)