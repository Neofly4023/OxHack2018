from DispatchStrategy import ManageSit
from GeoInfo import GeoPosition, VictimRegion, VolunteersCenter, VictimInfo

victimRegions = []
centers = []


victimRegions.append(VictimInfo(GeoPosition(44, 20, 4)))
victimRegions.append(VictimInfo(GeoPosition(46, 23, 4)))
victimRegions.append(VictimInfo(GeoPosition(44, 28, 4)))
victimRegions.append(VictimInfo(GeoPosition(47, 27, 4)))
victimRegions.append(VictimInfo(GeoPosition(45, 25, 4)))

centers.append(VolunteersCenter(GeoPosition(45.4, 21, 4), 100))
centers.append(VolunteersCenter(GeoPosition(46, 24, 4), 10232))
centers.append(VolunteersCenter(GeoPosition(44.5, 28, 4), 10232))
centers.append(VolunteersCenter(GeoPosition(47, 27.5, 4), 10232))
centers.append(VolunteersCenter(GeoPosition(44.3, 28, 4), 10232))

disp = ManageSit(victimRegions, centers)
assocs = disp.dispatch()
print(assocs)
# =======
# victims = []
# for i in range(10000):
#     victimPos0 = GeoPosition(45, 28, 1)
#     victim0 = VictimInfo(victimPos0)
#     victims.append(victim0)
#
#
# for i in range(10000):
#     victimPos0 = GeoPosition(51.5074, 0.1278, 1)
#     victim0 = VictimInfo(victimPos0)
#     victims.append(victim0)
# >>>>>>> 4a62276b1e98414817252697745e4c022de08feb

