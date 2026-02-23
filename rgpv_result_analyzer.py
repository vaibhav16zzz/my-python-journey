# RGPV Result Analyzer v1
# Created by Vaibhav Kale
# Date : 23 Feb 2026

print("===== RGPV EXAMINATION ANALYSIS - FOR SEMESTER 1st & 2nd =====")
print()

print("Course - B.Tech \nBranch - CSE \nFor Semester - 1st & 2nd \nMaximum Marks - 70 (for each subject)")
print()

subjects = ["Subject 1", "Subject 2", "Subject 3", "Subject 4", "Subject 5"]

print("Please enter the marks scored in the following subjects :- \n(Integer values only)")
print()

m1 = int(input("Subject 1 : "))
m2 = int(input("Subject 2 : "))
m3 = int(input("Subject 3 : "))
m4 = int(input("Subject 4 : "))
m5 = int(input("Subject 5 : "))
print()

marks = [m1, m2, m3, m4, m5]

max_marks = max(marks)
min_marks = min(marks)

max_index = marks.index(max_marks)
min_index = marks.index(min_marks)

strongest_subject = subjects[max_index]
weakest_subject = subjects[min_index]

total = sum(marks)

average = total / 5

percentage = (total / 350) * 100

print("\n===== RGPV RESULT =====")

print("\nTotal marks scored :", total, "out of 350")

print("\nStrongest Subject :", strongest_subject)

print("\nWeakest Subject :", weakest_subject)

print("\nAverage Marks :", average)

print("\nPercentage :", percentage, "%")