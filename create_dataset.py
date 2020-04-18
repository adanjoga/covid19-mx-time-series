import csv

files = ["data/covid19_deaths_mx.csv","data/covid19_suspects_mx.csv"]
new_dates = list()
mx_states = list()
confirmed = list()
deaths = list()

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


def save_covid_db():
    new_dates_ = list(new_dates)
    mx_states_ = list(mx_states)
    
    lastdate = new_dates_[len(new_dates_)-1]
    with open("data/covid19_db-"+lastdate+".csv", "w") as outfile:
        csvwriter = csv.writer(outfile, delimiter=",")

        csvwriter.writerow(["Estados", "Fechas", "Confirmados", "Defunciones"])
        idx = 0
        for state in mx_states:
            for date in new_dates:
                csvwriter.writerow([state, date, confirmed[idx], deaths[idx]])
                idx = idx + 1

if __name__ == "__main__":
    read_matrices_files()
    save_covid_db()
    print("The database has been generated")