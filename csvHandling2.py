import csv
import sys
import matplotlib.pyplot as plt
import bargraph
import piechart
react = {"likes":0,"loves":0,"wows":0,"hahas":0,"sads":0,"angry":0,"thanks":0}
growth = {}
def extractData(filename):
	f = open(filename,'rb')
	reader = csv.reader(f)
	headerline = f.next()
	#react = {"likes":0,"loves":0,"wows":0,"hahas":0,"sads":0,"angry":0,"thanks":0}
	reactions = []
	comments = []
	shares = []
	#growth = {}
	for row in reader:
    		growth[row[5]]=int(row[6])+2*int(row[7])+5*int(row[8])
    		reactions.append(int(row[6]))
    		comments.append(int(row[7]))
    		shares.append(int(row[8]))
    		react["likes"] += int(row[9])
    		react["loves"] += int(row[10])
    		react["wows"] += int(row[11])
    		react["hahas"] += int(row[12])
    		react["sads"] += int(row[13])
    		react["angry"] += int(row[14])
    		react["thanks"] += int(row[15])
    	f.close()
#bargraph.drawGraph(react.keys(),react.values(),"Rections Stats")
def reactStats():
	piechart.drawPieChart(react)

def growthStats():
	bargraph.drawGraph([' ' for x in range(1,len(growth)+1)],growth.values(),"Quality Stats")

'''extractData(sys.argv[1] + "_facebook_statuses.csv")
reactStats()
growthStats()'''
