import csv
f=open("reader.csv")
reader = csv.reader(f)
for question,answer in reader:
    print(question)
    print(answer)



