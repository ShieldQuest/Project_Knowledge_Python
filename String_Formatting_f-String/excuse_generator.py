name = "Treasure"
color = "blue"
restaurant = "Beau Thai"

about_me = f"My name is {name}, my favorite color is {color}, and my favorite place to eat is {restaurant}."

print (about_me)

# Challenge: Excuse Generator

# Don't feel like going out tonight? Write a program that generates excuses for why you have 
# to stay in.

#   1. Define these variables: first_name, event, number, noun, and verb. Use whatever values you
#      want, as long as they match the format.
#   2. Write an f-string using your variables that generates a one-sentence excuse. Here's an example
#      of what your output should look like:
#          "Sorry [Ted], I can't go to [the movies] - I have [345] [bees] to [crochet] and honestly 
#           it's taking longer than expected."
#   3. Print it! Change some or all of the values to create a new excuse. Print again.

first_name = "Laura"
event = "hiking"
number = 7
noun = "mountain"
verb = "cook"

excuse = f"Sorry {first_name}, I can't go {event} this weekend. I have to {verb} for a dinner party for {7} guests."
print(excuse)
