import PyPDF2
import re
import random
import os
import json
from progress.bar import IncrementalBar

#File control
data = open('bancadati1650.pdf', 'rb')
pdf = PyPDF2.PdfFileReader(data)
questionsFile = open("questions.txt", "w")
answerKeyFile = open("answer_keys.txt", "w")

database = {}

#Parsing info
delimiterQ = '[0-9][0-9][0-9][0-9]\. |[0-9][0-9][0-9]\. |[0-9][0-9]\. |[0-9]\. '  #Matching question header
delimiterA = 'A\) |B\) |C\) |D\) ' 												  #Matching answer header

blackListQ = [2364, 2408, 2590, 3853, 3949, 3964, 3971, 3980, 3981, 3982, 3983, 3984, 3985, 3986, 3987, 3988,
			  3989, 3995, 3996, 4008, 4012, 4015, 4062, 4063, 4064, 4065, 4069, 4091, 4092, 4093, 4094, 4095,
			  4096, 4097, 4098, 4099, 4100, 4120, 4123, 4136, 4137, 4138, 4139, 4140, 4141, 4142, 4143, 4144,
			  4145, 4149, 4165, 4166, 4168, 4171, 4183, 4190, 4382, 4479, 5621, 5644, 5653, 5672, 5741, 5863,
			  5867, 5868, 5933, 5934, 5959, 5966, 5967, 5990, 5994, 5995, 5996, 5990]

print("\nLoading " + os.path.basename(data.name) + " - Page count: " + str(pdf.numPages) + " - Size: " 
	+ str(round(os.stat(os.path.basename(data.name)).st_size/1000, 2)) + " KB\n")

questionsFile.write("====================INFO========================\n\n")

questionsFile.write("Input file: " + os.path.basename(data.name) + " - Page count: " + str(pdf.numPages) 
					+ " - Size: " + str(round(os.stat(os.path.basename(data.name)).st_size/1000, 2)) + " KB\n\n")

questionsFile.write("Parsed to: " + os.path.basename(questionsFile.name) + "\n")
questionsFile.write("Answer keys at: " + os.path.basename(answerKeyFile.name) + "\n\n")

questionsFile.write("Domande incluse: " + str(6000-len(blackListQ)) + "/6000\n")
questionsFile.write("Domande escluse:\n")
questionsFile.write(str(blackListQ))
questionsFile.write("\n\n")

questionsFile.write("================================================\n\n\n")

count = 1

bar = IncrementalBar("Processing", max = pdf.numPages)
bar.next()
bar.next()

skipOneMore = False

for page in range(2, pdf.numPages):

	pageObj = pdf.getPage(page).extractText()
	spiltPage = re.split(delimiterQ, pageObj)

	questionsFile.write("	  >>> Page: " + str(page) + " <<<\n\n")
	
	for question in spiltPage: 
		if (len(question) <= 20):  		#It's a section title
			questionsFile.write("             " + question + "\n")
			questionsFile.write("============================================\n\n")
		else:
			if skipOneMore:
				skipOneMore = False
				continue
			if count in blackListQ:
				skipOneMore = True
				count = count + 1
				continue
			else:
				splitQuestion = re.split(delimiterA, question)
				#print(str(count) + ") " + splitQuestion[0].replace('\n', '') + "\n")

				questionData = {}

				#Creating new order for the answers
				randomOrder = random.sample(range(1, 5), 4)

				#Q:
				temp = str(count) + ") " + splitQuestion[0].replace('\n', '')
				questionsFile.write(temp + "\n\n")
				questionData["Q"] = temp
				
				#A)
				questionsFile.write('	A: ' + splitQuestion[randomOrder[0]].replace('\n', '').replace('BANCA DATI', '') + '\n\n')
				if randomOrder[0] == 1:
					answerKeyFile.write(str(count) + ': A -> ' + splitQuestion[randomOrder[0]].replace('\n', '').replace('BANCA DATI', '') + '\n\n')
					questionData["ans"] = 'A'
				questionData["A"] = 'A: ' + splitQuestion[randomOrder[0]].replace('\n', '').replace('BANCA DATI', '')


				#B)
				questionsFile.write('	B: ' + splitQuestion[randomOrder[1]].replace('\n', '').replace('BANCA DATI', '') + '\n\n')
				if randomOrder[1] == 1:
					answerKeyFile.write(str(count) + ': B -> ' + splitQuestion[randomOrder[1]].replace('\n', '').replace('BANCA DATI', '') + '\n\n')
					questionData["ans"] = 'B'
				questionData["B"] = 'B: ' + splitQuestion[randomOrder[1]].replace('\n', '').replace('BANCA DATI', '')

				#C)
				questionsFile.write('	C: ' + splitQuestion[randomOrder[2]].replace('\n', '').replace('BANCA DATI', '') + '\n\n')
				if randomOrder[2] == 1:
					answerKeyFile.write(str(count) + ': C -> ' + splitQuestion[randomOrder[2]].replace('\n', '').replace('BANCA DATI', '') + '\n\n')
					questionData["ans"] = 'C'
				questionData["C"] = 'C: ' + splitQuestion[randomOrder[2]].replace('\n', '').replace('BANCA DATI', '')

				#D)
				questionsFile.write('	D: ' + splitQuestion[randomOrder[3]].replace('\n', '').replace('BANCA DATI', '') + '\n\n')
				if randomOrder[3] == 1:
					answerKeyFile.write(str(count) + ': D -> ' + splitQuestion[randomOrder[3]].replace('\n', '').replace('BANCA DATI', '') + '\n\n')
					questionData["ans"] = 'D'
				questionData["D"] = 'D: ' + splitQuestion[randomOrder[3]].replace('\n', '').replace('BANCA DATI', '')
					
				questionsFile.write("\n--------------------------------------------\n\n")
				database[count] = questionData
				count = count + 1
	bar.next()
bar.finish()

with open('bancaDati.json', 'w') as outfile:
            json.dump(database, outfile)

print("\nParsing completed\n")
print("Files generated:")

print(" > " + os.path.basename(questionsFile.name) + " - Size: " 
	+ str(round(os.stat(os.path.basename(questionsFile.name)).st_size/1000, 2)) + " KB")

print(" > " + os.path.basename(answerKeyFile.name) + " - Size: " 
	+ str(round(os.stat(os.path.basename(answerKeyFile.name)).st_size/1000, 2)) + " KB")

print(" > " + 'bancaDati.json' + " - Size: " 
	+ str(round(os.stat('bancaDati.json').st_size/1000, 2)) + " KB")

print()

data.close()
questionsFile.close()
answerKeyFile.close()