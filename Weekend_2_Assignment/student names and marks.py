#- Create a dictionary of student names and marks. Print top 3 scorers

student_marks = {
    "Alex": 88,
    "Brick": 95,
    "Cheery": 78,
    "David": 90,
    "Eva": 92
}

def get_marks(item):
    return item[1]

top_three = sorted(student_marks.items(), key=get_marks, reverse=True) [:3]

print("Top 3 Scorers:", top_three)





