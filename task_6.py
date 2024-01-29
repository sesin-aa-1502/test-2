import csv

def create_hash(s):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    alphabet += alphabet.upper()
    alphabet += ' '
    p, m = 67, 10**9 + 9  # 1e9 + 9
    hash = 0
    dictionary = {alphabet[i]: i + 1  for i in range(len(alphabet))}
    power = 1
    for i in range(len(s)):
        hash = (hash + dictionary[s[i]] * power) % m
        power = (power * p) % m
    return hash

with open('students.csv', encoding='utf-8') as file:
    data = list(csv.DictReader(file, delimiter=','))
    for student in data:
        student['id'] = create_hash(student['Name'])
        print(student)

with open('students_with_hash.csv', 'w', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['id', 'Name', 'titleProject_id', 'class', 'score'])
    writer.writeheader()
    writer.writerows(data)
    
