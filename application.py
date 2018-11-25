from flask import Flask, render_template,jsonify
app = Flask(__name__,static_url_path='/static')
import time
import threading
from DispatchStrategy import ManageSit
import VictumInfo as vi
from GeoInfo import VolunteersCenter, GeoPosition
import json


thousand = 1
centers = []
centers.append(VolunteersCenter(GeoPosition(45.4, 21, 4), thousand))
centers.append(VolunteersCenter(GeoPosition(46, 24, 4), thousand))
centers.append(VolunteersCenter(GeoPosition(44.5, 28, 4), thousand))
centers.append(VolunteersCenter(GeoPosition(47, 27.5, 4), thousand))
centers.append(VolunteersCenter(GeoPosition(44.3, 28, 4), thousand))

disp = -1
assocs = -1

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/getTweets")
def getTweets():
    return json.dumps(vi.getUpdateTweets())


@app.route("/getDispatches")
def getDispatches():
    global assocs
    if assocs == -1:
        return "[]"
    data = []
    for dispatch in assocs:
        thisData = []
        thisData.append( {"lat":dispatch[0].latitude,"lon":dispatch[0].longitude} )
        thisData.append( {"lat":dispatch[1].latitude,"lon":dispatch[1].longitude} )
        thisData.append(dispatch[2])
        data.append(thisData)


    return json.dumps(data)

@app.route("/getIdleCenters")
def getIdleCenters():
    global disp
    if disp == -1:
        return "[]"
    data = []
    for center in disp.centers:
        data.append( [{"lat":center.location.latitude,"lng":center.location.longitude},center.responderNumbers] )
    return json.dumps(data)


@app.route("/getUnresolvedRegions")
def getUnresolvedRegions():
    global disp
    if disp == -1:
        return "[]"
    data = []
    for region in disp.affectedRegions:
        data.append( [{"lat":region.location.latitude,"lng":region.location.longitude},region.populationCount] )
    return json.dumps(data)


def worker():
    while(True):
        victims = vi.getVictims()
        global disp
        global assocs
        disp = ManageSit(victims, centers)
        assocs = disp.dispatch()
        print(assocs)
        time.sleep(1)



if __name__ == '__main__':
    t = threading.Thread(target=worker)
    t.start()

    app.debug=True
    app.run()