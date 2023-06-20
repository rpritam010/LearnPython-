Student_height = input("Input a list of student height ").split()
total_height =0
total_size =0
for n in range(0,len(Student_height)):
    Student_height[n]= int(Student_height[n])
    total_height +=Student_height[n]
    total_size +=1
print(Student_height)
print(total_height)

Average = total_height/len(Student_height)
without_function = total_height/total_size
print(Average)
print(without_function)
