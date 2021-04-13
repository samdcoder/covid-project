import re

message = 'Hi, I wanted to know if remdesivir syringe is available in the city Mumbai through you or any contact of yours. The city is Mumbai and the patient is admitted in Palghar. Thank you.'

#todo 

#paste messages somewhere, in a file or some place to extract numbers from it => done

#extract phone numbers through regex or some pattern => done 

#figure out a way to save contact numbers with a generic pattern or sending messages without saving the numbers through api.whatsapp or something simlar

#emergencycontact 1, emergencycontact 2 and so on could be a pattern for sending texts 

message_file = open('messages.txt', 'r')
lines = message_file.readlines()
#contact_numbers = []
unique_contact_numbers = set()

#print lines

for line in lines:
	#print line
	r = re.findall(r'(?:\+?\d{2}[ -]?)?\d{10}', line)
	#print "r is ", r
	#print "\n\n"
	for number in r:
		unique_contact_numbers.add(number)



outF = open("contact_numbers.txt", "w")
for number in unique_contact_numbers:
  # write line to output file
  outF.write(number)
  outF.write("\n")
outF.close()