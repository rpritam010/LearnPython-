student_scores = input("Input the list of student score").split()
heighest_score =0;
for n in range(0,len(student_scores)):
    student_scores[n] = int(student_scores[n])
    if heighest_score < student_scores[n]:
        heighest_score = student_scores[n]
print(heighest_score)
    