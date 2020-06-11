#!/usr/bin/python

'''
	File name: data_generator.py
	Author: Walton P. Coutinho
	Date created: 14/03/2017
	Date last modified: 15/03/2017
	Python Version: 2.7

	general format of instance name grtop_wl_id
	where:  w = number of waypoints
		     l = number of landing zones
		    id = number of the instance

        instance file format
        xlc ylc zlc         | coordinates of the launching point
        w                   |
        x y z r minZ maxZ   | coordinates of the waypoints
        l                   |
        xl yl zl rl         | coordinates of the landing points

        obs1: the radius defines the min radius at ground level. For example
              r = 10 means a waypoint with radius equals 10 metres at ground
              level. The distance from the apex to the xy plane is always
              considered negative. 

        obs2: Overlaps between landing sites and landing sites and waypoints
              are not allowed
             
        obs3: minZ and maxZ define the range of in which heights the waypoint 
              must be visited. Note that minZ induces a larger radius than r 
              at the base of the truncated cone.

        obs4: It is assumed that the difference between minZ and maxZ is at
              least 30 metres (minZ_max = 50 & maxZ_min = 80).

        obs5: z for waypoints is always equal 0 anz z for landing points is
              always between 0 and 5

        obs6: Max launching altitude used in Crispin 2016 pag 139 Fig 7 and 
              page 124 items E_5 to E_7 is 5km.
'''

#imports
import numpy
import random
import string
import csv
import os
from glob import glob

#############################################################################
####################### S defining global parameters ########################
#############################################################################
##instance parameters
#number_of_instances = 05;           #max number of classes of instances
#number_of_waypoints = 10;           #max number of waypoints
#number_of_landing_points = 02;      #max number of landing points

#sizeClass = "S"                     #S,M,L for small, medium and large range

##waypoint parameters
#range_m = 1000;                     #max dimension in metres
#x_wayPt = [0, range_m];             #limits for x waypoint coord
#y_wayPt = [0, range_m];             #limits for y waypoint coord
#z_wayPt = [0,0];                    #limits for z waypoint coord
#rad_wayPt = [10, 25];               #radius def min radius at ground level
#minZ_wayPt = [50, 100];             #limits for waypoint min z
#maxZ_wayPt = [200, 300];            #limits for waypoint max z

##landing sites parameters
#x_lnd = [0, range_m];               #limits for x landing coordinate
#y_lnd = [0, range_m];               #limits for y landing coordinate
#z_lnd = [0, 0];                     #limits for z landing coordinate
#rad_lnd = [10, 25];                 #limits for landing point radius

##launching points parameters
#x_lnc = [0, range_m];               #limits for x landing coordinate
#y_lnc = [0, range_m];               #limits for y landing coordinate
#z_lnc = [500, 600];                 #limits for z landing coordinate
#############################################################################
#############################################################################

#############################################################################
####################### M defining global parameters ########################
#############################################################################
#instance parameters
#number_of_instances = 05;           #max number of classes of instances
#number_of_waypoints = 10;           #max number of waypoints
#number_of_landing_points = 02;      #max number of landing points

#sizeClass = "M"                     #S,M,L for small, medium and large range

#waypoint parameters
#range_m = 5000;                     #max dimension in metres
#x_wayPt = [0, range_m];             #limits for x waypoint coord
#y_wayPt = [0, range_m];             #limits for y waypoint coord
#z_wayPt = [0,0];                    #limits for z waypoint coord
#rad_wayPt = [10, 25];               #radius def min radius at ground level
#minZ_wayPt = [50, 100];             #limits for waypoint min z
#maxZ_wayPt = [200, 300];            #limits for waypoint max z

#landing sites parameters
#x_lnd = [0, range_m];               #limits for x landing coordinate
#y_lnd = [0, range_m];               #limits for y landing coordinate
#z_lnd = [0, 0];                     #limits for z landing coordinate
#rad_lnd = [10, 25];                 #limits for landing point radius

#launching points parameters
#x_lnc = [0, range_m];               #limits for x landing coordinate
#y_lnc = [0, range_m];               #limits for y landing coordinate
#z_lnc = [1000, 2000];                 #limits for z landing coordinate
#############################################################################
#############################################################################

#############################################################################
####################### L defining global parameters ########################
#############################################################################
#instance parameters
number_of_instances = 05;           #max number of classes of instances
number_of_waypoints = 50;           #max number of waypoints
number_of_landing_points = 05;      #max number of landing points

sizeClass = "L"                     #S,M,L for small, medium and large range

#waypoint parameters
range_m = 10000;                    #max dimension in metres
x_wayPt = [0, range_m];             #limits for x waypoint coord
y_wayPt = [0, range_m];             #limits for y waypoint coord
z_wayPt = [0,0];                    #limits for z waypoint coord
rad_wayPt = [10, 25];               #radius def min radius at ground level
minZ_wayPt = [50, 100];             #limits for waypoint min z
maxZ_wayPt = [200, 300];            #limits for waypoint max z

#landing sites parameters
x_lnd = [0, range_m];               #limits for x landing coordinate
y_lnd = [0, range_m];               #limits for y landing coordinate
z_lnd = [0, 0];                     #limits for z landing coordinate
rad_lnd = [10, 25];                 #limits for landing point radius

#launching points parameters
x_lnc = [0, range_m];               #limits for x landing coordinate
y_lnc = [0, range_m];               #limits for y landing coordinate
z_lnc = [4000, 5000];                 #limits for z landing coordinate

#min and step for no of waypoints
#and landing sites
minw = 10
stepw = 10
minl = 3
stepl = 1
#############################################################################
#############################################################################

#remove old files
for files in glob(sizeClass + "/*.dat"):
    os.remove(files);

#############################################################################
############################# defining functions ############################
#############################################################################
def random_waypoint(range_m):
    x = random.uniform(x_wayPt[0],x_wayPt[1]);
    y = random.uniform(y_wayPt[0],y_wayPt[1]);
    z = random.uniform(z_wayPt[0],z_wayPt[1]);
    radius = random.uniform(rad_wayPt[0],rad_wayPt[1]);
    minZ = random.uniform(minZ_wayPt[0],minZ_wayPt[1]);
    maxZ = random.uniform(maxZ_wayPt[0],maxZ_wayPt[1]);
    waypoint = [x, y, z, radius, minZ, maxZ];
    return waypoint

def random_landing(range_m):
    x = random.uniform(x_lnd[0],x_lnd[1]);
    y = random.uniform(y_lnd[0],y_lnd[1]);
    z = random.uniform(z_lnd[0],z_lnd[1]);
    radius = random.uniform(rad_lnd[0],rad_lnd[1]);
    landing_spot = [x, y, z, radius];
    return landing_spot

def random_launching_point(range_m):
    x = random.uniform(x_lnc[0],x_lnc[1]);
    y = random.uniform(y_lnc[0],y_lnc[1]);
    z = random.uniform(z_lnc[0],z_lnc[1]);
    launching_point = [x, y, z];
    return launching_point

def circle_euc_dist(obj1,obj2):
    coord1 = numpy.array([obj1[0], obj1[1], obj1[2]]);
    coord2 = numpy.array([obj2[0], obj2[1], obj2[2]]);
    radius1 = obj1[3];
    radius2 = obj2[3];
    dist = numpy.linalg.norm(coord1 - coord2);
    dist = dist - (radius1 + radius2);
    return dist;

#############################################################################
#############################################################################

#############################################################################
###################### instance generator main loop #########################
#############################################################################
inst_id = range(1,number_of_instances+1);
waypoints = range(minw,number_of_waypoints+1,stepw);
landing_zones = range(minl,number_of_landing_points+1,stepl);

allWayPts = [];
allLandingPts = [];
overlaps = True;

#main loop for generating instances
for i in inst_id:
    for w in waypoints:
        for l in landing_zones:
            if (w >= l):
                inst_name = sizeClass + "/grtop" + sizeClass + "_" + str(w) + str(l) + "_" + str(i) + ".dat";
                print "creating ", inst_name
                with open(inst_name, "w") as myfile:
                    launching = random_launching_point(range_m);
                    myfile.write(" ".join(map(lambda x: str('%.2f' % x), launching)) + "\n")
                    myfile.write(str(w) + "\n");
                    for ww in range(1,w+1):
                        waypoint = random_waypoint(range_m);
                        allWayPts.append(waypoint);
                        myfile.write(" ".join(map(lambda x: str('%.2f' % x), waypoint)) + "\n")
                    myfile.write(str(l) + "\n");
                    for ll in range(1,l+1):
                        while(overlaps):
                            landing = random_landing(range_m);
                            overlaps = False;
                            for wpt in allWayPts:
                                dist = circle_euc_dist(landing,wpt);
                                if(dist <= 0):
                                    overlaps = True;
                            for lnd in allLandingPts:
                                dist = circle_euc_dist(landing,lnd);
                                if(dist <= 0):
                                    overlaps = True;
                        if(not overlaps):
                            myfile.write(" ".join(map(lambda x: str('%.2f' % x),landing))+"\n");
                            overlaps = True;
                myfile.close();

print "Finished creating instances!"
#############################################################################
#############################################################################







