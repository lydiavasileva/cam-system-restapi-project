import requests

server = "http://localhost:5000"

# get list of parameters
url = "%s/streaming/parameters"%(server, )
print "Getting from", url
r = requests.get(url)
print "- return code", r.status_code
print "- data:", r.json()
print ""

# get value for width
url = "%s/streaming/parameters/width"%(server, )
print "Getting from", url
r = requests.get(url)
print "- return code", r.status_code
getData = r.json()
print "- data:", getData
print ""

# # set (using put) value for A0
# putData = {'data': str(int(getData['value'])+2) }
# print "Putting data", putData, "to", url
# r = requests.put(url, json=putData)
# print "- return code", r.status_code
# print ""

# # get newvalue for A0
# print "Getting from", url
# r = requests.get(url)
# getData = r.json()
# print "- return code", r.status_code
# print "- data:", getData
# print ""


