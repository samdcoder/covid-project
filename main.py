import re

message = 'Hi, I wanted to know if remdesivir syringe is available in the city Mumbai through you or any contact of yours. The city is Mumbai and the patient is admitted in Palghar. Thank you.'

message_file = open('messages.txt', 'r')
lines = message_file.readlines()
unique_contact_numbers = set()


for line in lines:
	r = re.findall(r'(?:\+?\d{2}[ -]?)?\d{10}', line)
	for number in r:
		unique_contact_numbers.add(number)


outF = open("contact_numbers.txt", "w")
for number in unique_contact_numbers:
  outF.write(number)
  outF.write("\n")
outF.close()