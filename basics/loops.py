# A for loop is used for iterating over a sequence

people = ['john', 'paul', 'sara', 'susan']

# for person in people:
#     print(f'Current person: {person}')

# break out of loop
for person in people:
    if person == 'sara':
        break
    print(f'Current person: {person}')

# continue
for person in people:
    if person == 'sara':
        continue
    print(f'Current person: {person}')

# range
for i in range(len(people)):
    print(people[i])

for i in range(0, 11):
    print(f'Number: {i}')

# while loops execute a set of statements as long as a condition is true

count = 0
while count <= 10:
    print(f"count: {count}")
    count += 1
