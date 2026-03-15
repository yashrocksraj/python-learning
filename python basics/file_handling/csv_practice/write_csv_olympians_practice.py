olympians = [("John Aalberg", 31, "Cross Country Skiing, 15km"),
             ("Minna Maarit Aalto", 30, "Sailing"),
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]
outfile = open("reduced_olympics.csv", "w")
# write head row
outfile.write('Name,Age,Sport')
outfile.write('\n')
# write each row
for i in olympians:
    row_string = ('{},{},{}'.format(i[0],i[1],i[2]))
    outfile.write(row_string)
    outfile.write('\n')
outfile.close()    