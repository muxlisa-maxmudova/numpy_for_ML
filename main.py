import numpy as np

data = np.array([
    [10, 95, 85],
    [2,  40, 30],
    [8,  80, 75],
    [5,  60, 55]
])

# Task 1:
attendance_and_study_hours = data[:4, :2]
print(attendance_and_study_hours)
#Task 2:
final_grades = data[:, -1]
print(final_grades)
#Task 3:
top_student = data[0,:]
print(top_student)










