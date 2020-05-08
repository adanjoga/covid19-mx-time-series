import csv
import numpy as np

files = ["data/covid19_deaths_mx.csv","data/covid19_suspects_mx.csv"]
new_dates = list()
mx_states = list()
confirmed = list()
deaths = list()

new_confirmed = list()
new_deaths = list()

def format_date(ddmmyyyy):
    dt = ddmmyyyy.split('-')
    return dt[2]+'-'+dt[1]+'-'+dt[0]

def read_matrices_files():
    with open("data/covid19_confirmed_mx.csv", "r") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        header = next(csvreader)

        for i in range(1,len(header)):
            new_dates.append(format_date(header[i]))

        for row in csvreader:
            mx_states.append(row[0])
            for i in range (1,len(row)):
                confirmed.append(int(row[i]))
    
    with open("data/covid19_deaths_mx.csv", "r") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        header = next(csvreader)

        temp_dates = list()
        temp_states = list()
        for i in range(1,len(header)):
            temp_dates.append(format_date(header[i]))

        for row in csvreader:
            temp_states.append(row[0])
            for i in range (1,len(row)):
                deaths.append(int(row[i]))

        if len(set(mx_states).difference(temp_states)) > 0:
            print("ERROR: the state's name are inconsistent") 

        if len(set(new_dates).difference(temp_dates)) > 0:
            print("ERROR: the dates are inconsistent") 

        if len(confirmed) != len(deaths):
            print("ERROR: the number of elements are inconsistent") 

def new_vectors():
    indx = np.array(range(0,len(mx_states))) * len(new_dates)
    for i in range(0, len(confirmed)):
        if i in indx:
            new_confirmed.append(confirmed[i])
            new_deaths.append(deaths[i])
        else:
            new_confirmed.append(confirmed[i]-confirmed[i-1])
            new_deaths.append(deaths[i]-deaths[i-1])

def rename_states(mx_states):
    return [w.replace('Queretaro', 'Querétaro') for w in mx_states]


def save_covid_db(mx_states, new_dates, print_all=1):
    new_dates_ = list(new_dates)
    
    lastdate = new_dates_[len(new_dates_)-1]
    with open("data/covid19_mx_db_all"+".csv", "w") as outfile:
        csvwriter = csv.writer(outfile, delimiter=",")

        if print_all:
            csvwriter.writerow(["Estados", "Fechas", "Confirmados", "Defunciones", "Nuevos confirmados", "Nuevas defunciones"])
        else:
            csvwriter.writerow(["Estados", "Fechas", "Confirmados", "Defunciones"])
        idx = 0
        for state in mx_states:
            for date in new_dates:
                if print_all:
                    csvwriter.writerow([state, date, confirmed[idx], deaths[idx], new_confirmed[idx] ,new_deaths[idx]])
                else:
                    csvwriter.writerow([state, date, confirmed[idx], deaths[idx]])
                idx = idx + 1

if __name__ == "__main__":
    read_matrices_files()
    new_vectors()

    mx_states = rename_states(mx_states)
    save_covid_db(mx_states, new_dates)

    print("The database has been generated")