import csv
olympians = [("John Aalberg", 31, "Cross Country Skiing, 15km"),
             ("Minna Maarit Aalto", 30, "Sailing"),
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]

outfile = open("reduced_olympics2.csv", "w")
writer = csv.writer(outfile)
# .writerow expects a list , not comma separted string , and no need to write \n for new line
writer.writerow(['Name','Age','Event'])
for olympian in olympians:
    writer.writerow(olympian)
outfile.close()    