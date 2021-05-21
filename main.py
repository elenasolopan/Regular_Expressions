import csv
import re

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


def get_phone(lines: str):
    phone_number = r'(\+7|8)\s?\(?(\d{3})\)?\s?\-?(\d{3})\s?\-?(\d{2})\s?\-?(\d+)\s?(\(?(доб\.)\s(\d{4})\)?)?'
    substitution = r'+7(\2)\3-\4-\5 \7\8'
    correct_phone = re.sub(phone_number, substitution, lines)
    return correct_phone


surname_list = list()
correct_phonebook = list()
correct_phonebook.append(contacts_list[0])

for line in contacts_list[1:]:
    correct_name = []
    surname = line[0].split()[0]
    if surname not in surname_list:
        surname_list.append(surname)

        phone = get_phone(line[5])

        correct_name = line[0].split() + line[1].split() + line[2].split()

        organization, position, email = line[3], line[4], line[6]

        correct_name.extend([organization, position, phone, email])
        correct_phonebook.append(correct_name)

    else:
        number = surname_list.index(surname)

        organization, position, email = line[3], line[4], line[6]
        phone = get_phone(line[5])
        if organization:
            correct_phonebook[number + 1][3] = organization
        if position:
            correct_phonebook[number + 1][4] = position
        if email:
            correct_phonebook[number + 1][6] = email
        if phone:
            correct_phonebook[number + 1][5] = phone

with open("phonebook.csv", "w", newline="", encoding='utf-8') as f:
    r = csv.writer(f, delimiter=',')
    r.writerows(correct_phonebook)
