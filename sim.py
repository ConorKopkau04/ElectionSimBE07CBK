import csv
import random
longoutlist = []
shortoutlist = []
done = False
run = 0



while (not done):
    wonvotes = 0
    totalvotepop = 0
    with open('cleandata.csv') as inputfile:
        filereader = csv.reader(inputfile)
        for row in filereader:
            swonvotes = 0
            state = row[0]
            spop = int(row[1])
            elecvotes = int(row[2])
            wmenmax = int(row[3])
            wmenmin = int(row [4])
            wwomax = int(row[5])
            wwomin = int(row[6])
            mmenmax = int(row[7])
            mmenmin = int(row[8])
            mwomax = int(row[9])
            mwomin = int(row[10])
            wmenper = int(row[11])/100
            wwoper = int(row[12])/100
            mmenper = int(row[13])/100
            mwoper = int(row[14])/100
            wmenvoteper= random.randrange(wmenmin,wmenmax)/100
            wwovoteper = random.randrange(wwomin,wwomax)/100
            mmenvoteper= random.randrange(mmenmin,mmenmax)/100
            mwovoteper= random.randrange(mwomin,mwomax)/100
            statevotepop =  spop*wmenvoteper*wmenper + spop*wwovoteper*wwoper + spop*mmenvoteper*mmenper + spop*mwovoteper*mwoper
            totalvotepop += spop*wmenvoteper*wmenper + spop*wwovoteper*wwoper + spop*mmenvoteper*mmenper + spop*mwovoteper*mwoper
            if(statevotepop/spop>.5):
                wonvotes += elecvotes
                swonvotes = elecvotes
            longoutlist.append([run, state, wmenvoteper,wwovoteper, mmenvoteper, mwovoteper,statevotepop,swonvotes])
        shortoutlist.append([run, wonvotes,totalvotepop/256662010])
    run += 1
    print(run)



            
    if (wonvotes>=270 and (totalvotepop/256662010)<=.5):
        
        done = True
with open('shortout.csv', 'w',) as outputfile:
    shortwriter = csv.writer(outputfile, delimiter=',')
    csv.QUOTE_NONE
    for row in shortoutlist:
        shortwriter.writerow(row)

#Records Data 
with open('longout.csv', 'w',) as outputfile:
    longwriter = csv.writer(outputfile, delimiter=',')
    csv.QUOTE_NONE
    for row in longoutlist:
        longwriter.writerow(row)




        #STATE,A Pop.,Electoral Votes,WMen Max,WMen Min,WWomen Max,WWomen Min,MMen Max,MMen Min,MWomen Max,MWomen Min,WMen,WWomen,MMen,MWomen
        #min and max voter randomized between output result done
        #num of elec votes for givin state output result did majority?
        #state name output result done
        #voter group percentages of whole for one party output result done
