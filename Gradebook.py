# ## Create a gradebook of courses taken

#Create two-demensional list of last semester courses taken along with grades.
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]
# Create a list called 'subjects' and fill it with the classes you are taking.
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
# Create two-demensional list to combine 'subjects' and 'grades.'
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]
# add any courses completed along with grades to 'gradebook' two-demensional list
gradebook.append(["computer science", 100])
gradebook.append(["visual arts, 93"])
# Correct any mistakes and/or make preferred changes in the 'gradebook' two-demensional list
gradebook[-1][-1] = 98
gradebook[2].remove(85)
gradebook[2].append("Pass")
# Combine current courses with last semester courses
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)