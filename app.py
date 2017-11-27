from flask import Flask, render_template, request
import getfbPage as fb
import getComments as gc
import csvHandling2 as cs
import csv
pgid = ''
app = Flask(__name__)

@app.route("/")
def main():
	return render_template('home.html')
@app.route('/',methods=['POST'])
def getValues():

	fb.page_id = request.form['pageid']
	#
	global pgid
	pgid = fb.page_id
	#
	fb.since_date = request.form['startdate']

	fb.until_date = request.form['enddate']
	#illi nodu tegi
	l = fb.scrapeFacebookPageFeedStatus(fb.page_id, fb.access_token, fb.since_date, fb.until_date)
	print fb.page_id
	print fb.since_date
	print fb.until_date
	print l
	#strq = 'DOne '
	if fb.success:

		strq= render_template('proc.html',success=fb.success,pageid=fb.page_id,num_processed=l[0],timetaken=l[1])
	else:
		strq= render_template('proc.html')
	return strq

@app.route("/stats/")
def pchart():
	global pgid
	cs.extractData(pgid + '_facebook_statuses.csv')
	cs.reactStats()
	cs.growthStats()
	#abcd = "<script type=\"text/javascript\">window.onload = function(){ alert(\"Hi there\"));}</script>"
	return "<html><body>The piechart and bargraph of <b><i><u>" + pgid +"</u></i></b> has been downloaded into your local repository</body></html>"


@app.route("/displaydata/")
def displayData():
	global pgid
	dataFile = open(pgid+"_facebook_statuses.csv","r")
	r = csv.reader(dataFile)
	P = '<html><style> body{background-color:rgba(255,127,80,0.3)} table {font-family: arial, sans-serif;border-collapse: collapse;width: 100%;}'
	P +="td, th {border: 1px solid #dddddd;text-align: left;padding: 8px;}tr:nth-child(even) {background-color: #dddddd;}</style><body><h3>Scraped Statuses</h3><table>"

	for row in r:
		P += "<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td><td>{5}</td><td>{6}</td><td>{7}</td><td>{8}</td><td>{9}</td><td>{10}</td></tr>".format(row[1],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14])
		P += "</tr>"
	P+= "</table></body></html>"
	#print P
	return P

@app.route("/displaycomments")
def displyComments():
	global pgid
	#gc.scrapeFacebookPageFeedComments(pgid+"_facebook_statuses.csv", gc.access_token)
	dataFile = open(pgid+"_facebook_comments.csv","r")
	r = csv.reader(dataFile)
	P = '<html><style> body{background-color:rgba(255,127,80,0.3)} table {font-family: arial, sans-serif;border-collapse: collapse;width: 100%;}'
	P +="td, th {border: 1px solid #dddddd;text-align: left;padding: 8px;}tr:nth-child(even) {background-color: #dddddd;}</style><body><h3>Comments</h3><table>"

	for row in r:
		P += "<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td></tr>".format(row[3],row[4],row[5],row[6])
		P += "</tr>"
	P+= "</table></body></html>"
	#print P
	return P



if __name__ == "__main__":
	app.run()
