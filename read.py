data = []
with open ('reviews.txt','r') as f:
	for line in f:
		data.append(line)
print(len(data))

new = []

for d in data:
	if len(d) < 100:
		new.append(d)

print(len(d))