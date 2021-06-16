import csv
#open the csv file
with open('mempool.csv') as csvfile:
 data = csv.DictReader(csvfile)
 
 for row in data:
     #print the tx id ,fee and weight
   print(row['tx_id'], row['fee'],row['weight']) 