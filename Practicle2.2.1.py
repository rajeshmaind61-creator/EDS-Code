arr = list(map(int, input().split()))
key = int(input())

found = False

for i in range(len(arr)):
	if arr[i] == key:
		print(i)
		found = True
		break

if not found:
	print("Not found")