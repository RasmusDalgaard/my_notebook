import matplotlib.pyplot as plt

student_attendance = {'day1':33, 'day2':34,'day3':29,'day4':31,'day5':28,'day6':26,'day7':30}

plt.plot(list(student_attendance.keys()), list(student_attendance.values()), color='red', marker='o')
plt.title('Student Attendance')
plt.xlabel('Days')
plt.ylabel('Attendance')
plt.grid(True)
plt.show()