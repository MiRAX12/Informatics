import xmltodict, csv

with open("Laboratornaya №4.5.xml", encoding='utf-8') as xmlfile:
    xml = xmltodict.parse(xmlfile.read())

csv_file = open("Laboratornaya №4.5.csv", 'w', newline='', encoding='utf-8')
csv_write = csv.writer(csv_file)
csv_write.writerow(["time", "week", "location", "room", "lesson"])
i = 0
line = [" "] * 3
for subject in xml["timetable"]["subject"]:
    line[i] = [subject["time"], subject["week"], subject["location"], subject["room"], subject["lesson"]]
    print(line[i])
    i += 1
csv_write.writerows(line)