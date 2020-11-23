import random

when = ['A few years ago ', 'Yesterday', 'Last night', 'A long time ago', 'years ago']

who = [' Dad ', ' Mother ', ' Son ', ' young son ', 'maid']

name = ['Felipe', 'Marcela', 'Naruto', 'Tulho', 'Reno']

residence = ['Brazil', 'Italy', 'Paraiba', 'França', '']

went = ['Backyard', 'Field', 'lake', 'kitchen', '']

happened = ['made a lot of friends', 'found a secret key', 'solved a mistery', 'wrote a book', 'Almost die']

print(random.choice(when) + ' a ' + random.choice(who) + ' named ' + random.choice(name) + ' in ' + random.choice(residence) + ' go to ' + random.choice(went) + ' and ' + random.choice(happened)+ ' And then the story begin')