
# find all officers
def findOfficers(archive,officers):
    for i in range(0,len(archive),1):
        if len(archive[i]) == 1:
            officers.append(i+1)
        
# find people who have at least two signatures from officers 
def findNonSuspects(archive,officers,non_suspects,suspects):
    for i in range(0,len(archive),1):
        count = 0
        if len(archive[i]) > 1:
            for j in range(1,archive[i][0]+1,1):
                for k in officers:
                    if archive[i][j] == k:
                        count += 1
            if count >= 2:
                non_suspects.append(i+1)
                archive[i] = [-1]
            else:
                suspects.append(i+1)

# find others who are not spies and find spies
def findSuspects(archive,suspects,non_suspects):
    for s in range(0,len(suspects),1):
        
        for i in range(0,len(archive),1):
            check = 0
            if len(archive[i]) > 1:
                for j in range(1,archive[i][0]+1,1):
                    for k in non_suspects:
                        if archive[i][j] == k:
                            check += 1
                if check == len(archive[i])-1:
                    non_suspects.append(i+1)
                    archive[i] = [-1]
                    suspects.remove(i+1)

def createOutputFile(suspects):
    try:
        file = open("output.txt", "w")
        file.write("")
        file.close()
    except FileNotFoundError:
        msg = "Sorry, the output text file does not exist"
        print(msg)

    try:
        oFile = open("output.txt", "a")
        if len(suspects) > 0:
            for i in suspects:
                oFile.write(str(i) + "\n")
        else:
            oFile.write("brak podejrzanych")
        oFile.close()
        print("Pomyslnie zapisano wynik do output.txt")
    except FileNotFoundError:
        msg = "Sorry, the output text file does not exist"
        print(msg)



def createSite(suspects):
    with open('index.html', 'w',encoding="utf-8") as r:
        r.write("""<!DOCTYPE html>\n<html>\n\t<head>\n\t\t\t<meta charset="UTF-8">\n\t
</head>\n\t<body>\n\t\t<h2 style="text-align: center;">Zadanie "Podpisy"</h2>\n\t\t
<h3 style="text-align: center;"><span style="color: #911111;"><strong>! Ściśle tajne !</strong></span></h3>
\n\t\t<table style="border-collapse: collapse; height: 230px; border: 1px solid black; width: 50%; margin-left: auto; margin-right: auto;" border="1">
\n\t\t<tbody>\n\t\t<tr style="text-align: center;">\n\t\t<td style="width: 100%; height: 24px; text-align: center;">Urzędnicy UOB podejrzani o szpiegostwo</td>
\n\t\t</tr>\n\t\t<tr style="height: 206px;">\n\t\t<td style="width: 100%; height: 206px;">""")
        for i in suspects:
            r.write(f"""\n\t\t<p style="text-align: center;">Urzędnik nr {i}</p>""")
        r.write("""\n\t\t</td>\n\t\t</tr>\n\t\t</tbody>\n\t\t</table>\n\t</body>\n</html>""")



def main():
    archive = []
    try:
        with open('input.txt') as file:
            archiveSize = int(file.readline())
            #print(archiveSize)
            archive = [[int(num) for num in line.split(' ')] for line in file]
            file.close()
            print("Pomyslnie odczytano plik input.txt")
    except FileNotFoundError:
        msg = "Sorry, the input text file does not exist"
        print(msg)
        
    
    officers = []
    non_suspects = []
    suspects = []
    
    findOfficers(archive,officers)
    findNonSuspects(archive,officers,non_suspects,suspects)
    findSuspects(archive,suspects,non_suspects)
    createOutputFile(suspects)
    createSite(suspects)


if __name__ == "__main__":
    main()