import csv
import numpy as np

new_dates = list()
mx_states = list()
confirmed = list()
deaths = list()

new_confirmed = list()
new_deaths = list()

nlevels_total = list() 
nlevels_paid = list() 

def read_matrices_files():
    levelc = 0
    level1 = 0
    level2 = 0
    level3 = 0
    Flevelc = 0
    Flevel1 = 0
    Flevel2 = 0
    Flevel3 = 0
    Mlevelc = 0
    Mlevel1 = 0
    Mlevel2 = 0
    Mlevel3 = 0
    area1 = 0
    area2 = 0
    area3 = 0
    area4 = 0
    area5 = 0
    area6 = 0
    area7 = 0

    area_c = [0,0,0,0,0,0,0]
    area_1 = [0,0,0,0,0,0,0]
    area_2 = [0,0,0,0,0,0,0]
    area_3 = [0,0,0,0,0,0,0]
    with open("data2/Vigentes_Enero_2019.csv", "r") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        header = next(csvreader)
        print(header)
        
        for row in csvreader:
            level = row[5]
            ads = row[11]
            title = row[1]
            area = row[6]
            fm = ""
            if title == "M. EN C." or title == "MTRO." or title == "DR.":
                fm = "M"
            elif title == "DRA.":
                fm = "F"
            
            if ads != "":
                if area == "1":
                    area1 = area1 + 1
                elif area == "2":
                    area2 = area2 + 1
                elif area == "3":
                    area3 = area3 + 1
                elif area == "4":
                    area4 = area4 + 1
                elif area == "5":
                    area5 = area5 + 1
                elif area == "6":
                    area6 = area6 + 1
                elif area == "7":
                    area7 = area7 + 1

                if level == "C":
                    levelc = levelc + 1
                    if fm == "M":
                        Flevelc = Flevelc + 1
                    else:
                        Mlevelc = Mlevelc + 1

                    if area == "1":
                        area_c[0] = area_c[0] + 1
                    elif area == "2":
                        area_c[1] = area_c[1] + 1
                    elif area == "3":
                        area_c[2] = area_c[2] + 1
                    elif area == "4":
                        area_c[3] = area_c[3] + 1
                    elif area == "5":
                        area_c[4] = area_c[4] + 1
                    elif area == "6":
                        area_c[5] = area_c[5] + 1
                    elif area == "7":
                        area_c[6] = area_c[6] + 1
                    
                elif level == "1":
                    level1 = level1 + 1
                    if fm == "M":
                        Flevel1 = Flevel1 + 1
                    else:
                        Mlevel1= Mlevel1 + 1

                    if area == "1":
                        area_1[0] = area_1[0] + 1
                    elif area == "2":
                        area_1[1] = area_1[1] + 1
                    elif area == "3":
                        area_1[2] = area_1[2] + 1
                    elif area == "4":
                        area_1[3] = area_1[3] + 1
                    elif area == "5":
                        area_1[4] = area_1[4] + 1
                    elif area == "6":
                        area_1[5] = area_1[5] + 1
                    elif area == "7":
                        area_1[6] = area_1[6] + 1

                elif level == "2":
                    level2 = level2 + 1
                    if fm == "M":
                        Flevel2 = Flevel2 + 1
                    else:
                        Mlevel2 = Mlevel2 + 1

                    if area == "1":
                        area_2[0] = area_2[0] + 1
                    elif area == "2":
                        area_2[1] = area_2[1] + 1
                    elif area == "3":
                        area_2[2] = area_2[2] + 1
                    elif area == "4":
                        area_2[3] = area_2[3] + 1
                    elif area == "5":
                        area_2[4] = area_2[4] + 1
                    elif area == "6":
                        area_2[5] = area_2[5] + 1
                    elif area == "7":
                        area_2[6] = area_2[6] + 1

                elif level == "3":
                    level3 = level3 + 1
                    if fm == "M":
                        Flevel3 = Flevel3 + 1
                    else:
                        Mlevel3 = Mlevel3 + 1
                    
                    if area == "1":
                        area_3[0] = area_3[0] + 1
                    elif area == "2":
                        area_3[1] = area_3[1] + 1
                    elif area == "3":
                        area_3[2] = area_3[2] + 1
                    elif area == "4":
                        area_3[3] = area_3[3] + 1
                    elif area == "5":
                        area_3[4] = area_3[4] + 1
                    elif area == "6":
                        area_3[5] = area_3[5] + 1
                    elif area == "7":
                        area_3[6] = area_3[6] + 1
    print(levelc,level1,level2,level3)
    print(Flevelc,Flevel1,Flevel2,Flevel3)
    print(Mlevelc,Mlevel1,Mlevel2,Mlevel3)
    print(area1,area2,area3,area4,area5,area6,area7)
    print(area_c)
    print(area_1)
    print(area_2)
    print(area_3)

def read_matrices_files2():
    levelc = 0
    level1 = 0
    level2 = 0
    level3 = 0
    with open("data2/Vigentes_Enero_2019.csv", "r") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        header = next(csvreader)
        print(header)
        
        for row in csvreader:
            level = row[5]
            ads = row[11]
            if level == "C":
                levelc = levelc + 1
            elif level == "1":
                level1 = level1 + 1
            elif level == "2":
                level2 = level2 + 1
            elif level == "3":
                level3 = level3 + 1
    print(levelc, level1,level2,level3)

def save_covid_db(mx_states, new_dates, print_all):
    new_dates_ = list(new_dates)
    
    lastdate = new_dates_[len(new_dates_)-1]
    with open("data/covid19_mx_db_all"+".csv", "w") as outfile:
        csvwriter = csv.writer(outfile, delimiter=",")

        csvwriter.writerow(["Estados", "Fechas", "Confirmados", "Defunciones", "Nuevos confirmados", "Nuevas defunciones"])
        
        for state in mx_states:
            for date in new_dates:
                if print_all:
                    csvwriter.writerow([state, date, confirmed[idx], deaths[idx], new_confirmed[idx] ,new_deaths[idx]])
                else:
                    csvwriter.writerow([state, date, confirmed[idx], deaths[idx]])
                idx = idx + 1

if __name__ == "__main__":
    read_matrices_files()

    print("The database has been generated")