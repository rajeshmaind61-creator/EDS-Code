# write your code here
n=int(input())
marks=list(map(int,input().split()))

if any(mark < 40 for mark in marks):
	print("Fail")
else:
	aggrper=sum(marks)/n
	print("Aggregate Percentage: "+'%.2f'%aggrper)
	if aggrper>75:
		grade="Distinction"
	elif 60<=aggrper<75:
		grade = "First Division"
	elif 50<=aggrper<60:
		grade = "Second Division"
	elif 40<=aggrper<50:
		grade = "Third Division"

	print("Grade:",grade)