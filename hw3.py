import matplotlib.pyplot as plt


def partyMonth(parties, presidents, data): #takes in parameters parties,presidents,data
    main = dict()    #Create empty dictionary
    for party in parties:
        count = 0              #loop through each month
        sum = 0
        for president in presidents: #iterate through each president
            if president["party"] == party: #check if its matches current party
                for k in range(int(president["sDate"]),int(president["eDate"])):
                    for year in data: #iterate through data
                        if year[0] == str(k): #compare
                            for l in range(1, 13):
                                sum+=int(year[l])
                                count+=1
        main[party] = int(sum/count) + 1
    for party in main.keys(): #iterate and  output in proper format
        output.write("{left_aligned:<15}{right_aligned:>12}\n".format(
            left_aligned=party,
            right_aligned=main[party]
        ))

def presidentialProgress(presidents, data): #take in list of presidents/data
    progress = []
    for president in presidents: #iterate through presidents
        lName = president["name"].split(" ")[-1].strip() #strip last name
        for year in data:
            if year[0] == president["sDate"]:
                sJob = year[1].strip() #grab start date
            if year[0] == str(int(president["eDate"])-1):
                eJob = year[-1].strip() #grab end date
        difference = int(eJob)-int(sJob) #find difference
        percentage = round(difference/int(sJob)*100,1) #percentage
        progress.append((lName, sJob, eJob, difference, percentage)) #assign these values
    output.write("{lAlign:<15}{sJobs:>20}{eJobs:>20}{difference:>20}{percentage:>12}\n".format(
        lAlign="President",
        sJobs="First Month",        #output in correct format
        eJobs="Last Month",
        difference="Difference",
        percentage="Percentage"
    ))
    for pres in progress:
        output.write("{lAlign:<15}{sJobs:>20}{eJobs:>20}{difference:>20}{percentage:>12}%\n".format(
        lAlign=pres[0],
        sJobs=pres[1],  #Output in correct format
        eJobs=pres[2],
        difference=str(pres[3]),
        percentage="{percentage:.2f}".format(percentage=pres[4])
        ))


dataPrivate = []
govData = []            #Arrays to hold data
presidents = []
parties = set()

fpriv = open("private.csv")
fgov = open("gov.csv")          #opening files and asigning them to variables
fpres = open("presidents.txt")
output = open("output.txt", "w")
fpriv.readline()
fgov.readline()             #Read files

p = fpres.readlines()
for k in range(len(p)): #dictionaries for presidents
    pData = p[k].split(",") #split by comma
    pres = dict()
    pres["name"] = pData[0].strip()
    pres["sDate"] = pData[1].strip().split("-")[0]      #store name, dates, and parties
    pres["eDate"] = pData[1].strip().split("-")[1]
    pres["party"] = pData[2].strip()
    parties.add(pres["party"])
    presidents.append(pres)

dataPrivate = [k.split(",") for k in fpriv.readlines()]
govData = [k.split(",") for k in fgov.readlines()]

output.write("Private employment average per month (thousands)\n") #display employ avg
partyMonth(parties, presidents, dataPrivate)

output.write("\nGovernment employment average per month (thousands)\n") #display gov employ avg
partyMonth(parties, presidents, govData)

output.write("\nPrivate employment average by president (thousands)\n") #display private employ avg per pres
presidentialProgress(presidents, dataPrivate)

output.write("\nGovernment employment average by president (thousands)\n") #display gov employ avg by pres
presidentialProgress(presidents, govData)

output.close()

partyColors = {"Democrat": "blue", "Republican": "red"} #assign proper colors
plt.ylabel("Total employment in millions")
plt.xlabel("Year")              #labels
plt.title("Total Employment by party over the years")
partiesindata = set()
for president in presidents: #iterate through presidents
    presData = []
    presYears = [int(president["sDate"])]
    counter = 0
    for k in range(int(president["sDate"]),int(president["eDate"])):
        for line in dataPrivate: #iterate through private data
            if str(k) in line:
                for l in range(1, len(line)):
                    presData.append(int(line[l]))
                    presYears.append(presYears[-1]+(1/12))
        for line in govData: #iterate through govData
            if str(k) in line:
                for l in range(1, len(line)):
                    presData[counter]+=int(line[l])
                    counter+=1
    for k in range(len(presData)):
        presData[k]/=1000 #show data in millions
    lbl = ""
    pcolor = partyColors[president["party"]] #set colors
    if not president["party"] in partiesindata:
        lbl=president["party"]      #adding data if not in data
        partiesindata.add(president["party"])
    plt.bar(presYears[:-1], presData, color=pcolor, label=lbl) #bar graph
    plt.legend(loc="upper left") #show legend
plt.show() #show graph