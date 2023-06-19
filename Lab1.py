#Pre-Defined Function
#Opening the given dataset
file=open("C:/Users/Aditya Pratap Singh/Desktop/Data Analytics with Python and Mini Project/LAB WORK/bank.csv","r")  

#Printing the header
header=file.readline()
print(header)
#Count the number of  customers in each category 'marital'.  
def maritalcount():
    data=file.readlines()
    maritalstat=[]
    for i in range(1,len(data)):
        da=data[i].split(";")
        maritalstat.append(da[2])
    di={}
    for i in maritalstat:
            di[i]=di.get(i,0)+1

    print("The count of marital status of the costumer is as given below")
    print("{:<20} {:15}".format('Marital Status','Count'))
    for k, v in di.items():
     marit=v
     print("{:<20} {:<15}".format(k,marit))
maritalcount()
#Age Histogram
ag = []
for i in file:
    ag.append(i[0])
ag = ag[1:]
ages = []
for i in ag:
  j = int(i)
  ages.append(j)
def prepare_age_histogram(ages):
    age_ranges = {
        "0-10": 0,
        "11-20": 0,
        "21-30": 0,
        "31-40": 0,
        "41-50": 0,
        "51-60": 0,
        "61-70": 0,
        "71-80": 0,
        "81-90": 0,
        "91-100": 0,
        "101+": 0
    }

    for age in ages:
        if age <= 10:
            age_ranges["0-10"] += 1
        elif age <= 20:
            age_ranges["11-20"] += 1
        elif age <= 30:
            age_ranges["21-30"] += 1
        elif age <= 40:
            age_ranges["31-40"] += 1
        elif age <= 50:
            age_ranges["41-50"] += 1
        elif age <= 60:
            age_ranges["51-60"] += 1
        elif age <= 70:
            age_ranges["61-70"] += 1
        elif age <= 80:
            age_ranges["71-80"] += 1
        elif age <= 90:
            age_ranges["81-90"] += 1
        elif age <= 100:
            age_ranges["91-100"] += 1
        else:
            age_ranges["101+"] += 1

    print("Histogram for age:")
    for age_range, count in age_ranges.items():
        print(f"{age_range}: {'*' * count}")
