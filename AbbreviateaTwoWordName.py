"""
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.
"""

def abbrevName(name):
	name=name.title()
	name=name.split()
	name_one=name[0]
	name_two=name[1]
	return name_one[0]+"."+name_two[0]


print(abbrevName("andrea dejean"))

