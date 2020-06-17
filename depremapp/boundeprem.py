import pandas as pd
from bs4 import BeautifulSoup
import urllib.request
def vericek():

    adress = 'http://www.koeri.boun.edu.tr/scripts/lst9.asp'
    response = urllib.request.urlopen(adress)
    html = response.read()

    soup = BeautifulSoup(html,"lxml")
    table = soup.find("pre").contents[0]

    table = str(table)

    with open("depremler.txt","w",encoding="utf-8") as file:
        file.write(table)
        file.close
    depremler = []

    with open("depremler.txt", "r",encoding="utf-8") as file2:
        for line in file2:
            #print(line)
            if line[0].isnumeric() == True:
                data = line.split()
                data[-1] = " "


                depremler.append([])
                depremler[-1].append(f"{data[0]},{data[1]}")
                depremler[-1].append(f"{data[2]}")
                depremler[-1].append(f"{data[3]}")
                depremler[-1].append(f"{data[4]}")
                depremler[-1].append(f"{data[6]}")

                strm = ""
                i = 8
                while data[i] != " ":
                    strm += data[i] + " "
                    i += 1

                depremler[-1].append(strm.rstrip())
    return depremler
