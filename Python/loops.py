#for
topics = ["Python", "Java", "JavaScript", "C++", "Go"]
for topic in topics:
    print(topic)

#while
count = 0
while count < 5:
    print(count)
    count += 1  

#range
for i in range(5):
    print(i)    

#nested loops
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")    

#break
for i in range(10):
    if i == 5:
        break
    print(i)    

#continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)    