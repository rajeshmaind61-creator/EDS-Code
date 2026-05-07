import numpy as np

# 9. print average marks of each student
avg = np.mean(a[:,1:],axis=1)
print(np.round(avg,1))

# 10. print average marks of each subject
print("Average Marks of each subject", np.mean(a[:,1:],axis=0)      )

# 11. print average marks of S1 and S2
print("Average Marks of S1 and S2",     np.mean(a[:,1:3],axis=0)     )

# 12. print average marks of S1 and S3
print("Average Marks of S1 and S3",      np.mean(a[:,[1,3]],axis=0)          )

# 13. print Roll number who got maximum marks in Subject 3
i = np.argmax(a[:,3])
print("Roll no who got maximum marks in Subject 3",   a[i,0]        )

# 14. print Roll number who got minimum marks in Subject 2
mn = np.argmin(a[:,2])
print("Roll no who got minimum marks in Subject 2",  a[mn,0]    )

# 15. print Roll number who got 24 marks in Subject 2
whr = np.where(a[:,2]==24)
print("Roll no who got 24 marks in Subject 2",    a[whr,0]             )

# 16. print count of students who got marks in Subject 1 < 40
ct = np.count_nonzero(a[:,1]<40)
print("Count of students who got marks in Subject 1 < 40",      ct         )

# 17. print count of students who got marks in Subject 2 > 90
ct = np.count_nonzero(a[:,2]>90)
print("Count of students who got marks in Subject 2 > 90:",     ct         )

# 18. print count of students in each subject who got marks >= 90
print("Count of students in each subject who got marks >= 90:",      np.count_nonzero(a[:,1:]>=90,axis = 0)         )

# 19. print count of subjects in which each student got marks >= 90
print("Roll no:",  a[:,0]    )
print("Count of subjects in which student got marks >= 90:",   np.count_nonzero(a[:,1:]>=90,axis = 1)     )

# 20. Print S1 marks in ascending order

str = np.sort(a[:,1])
print(str)

# 21. Print S1 marks >= 50 and <= 90

print(a[(a[:,1]>=50)& (a[:,1]<=90)])

# 22. Print the index position of marks 79
print(a)
ip = np.where(a[:,1]==79)
print(ip)