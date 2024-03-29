import pandas as pd
import fiona
import shapely
from shapely.geometry import shape, Polygon, Point, MultiPoint
import utm
import collections
from geopandas.tools import geocode

# function to be used by Twilio texting interface
def zoneResponse(inputAddress):

    # container for all zones
    allZones = []

    # read shp dataset through fiona library
    zones = fiona.open("Garbage__Recycling_Collection_Zone_Boundaries.shp")

    # get next polygon data
    poly = zones.next()
    print(poly)

    # function to convert UML coordinates to lat/long coordinates
    def toLatLong(original):

        # list to hold tuples of coordinates
        latLong = []
        print("Converting UTM coordinates to Latitude and Longitude.")
        for coor in original:

            # append converted tuple to latLong

            latLong.append(utm.to_latlon(coor[0], coor[1], 17, 'T'))

        return latLong

    for zone in range(0,len(zones) - 2):
        print('##########################################')

        # get next zone in list
        poly = zones.next()

        # check for MultiPolygon
        if 'MultiPolygon' in str(poly):     # if poly.geom_type == 'MultiPolygon':
            pass
            # formatting
            """
            sector = poly['properties']['Collection']
            geom = shape(poly['geometry'])
            poly_data = poly['geometry']['coordinates'][0]
            """
            # print(poly_data)
        else:

            # formatting
            sector = poly['properties']['Collection']
            geom = shape(poly['geometry'])
            poly_data = poly['geometry']['coordinates'][0]
            # print(poly_data)
            final = Polygon(poly_data)

            # get coordinates to extract
            ex = final.exterior.coords

            # convert from UML to lat and long
            converted = Polygon(toLatLong(ex))

            # add zones to container
            allZones.append((converted, sector))

            print('Zone ' + str(zone + 1) + ' complied into polygon.')

    # use pandas to read csv for all london addresses
    londonAddresses = pd.read_csv('LondonAddressesDatabase.csv', sep='\s*,\s*', header=0, encoding='ascii', engine='python')
    # print(londonAddresses)

    addressCoor = londonAddresses.loc[londonAddresses['UnitFullAddress'] == inputAddress]['Latitude'].values[0], londonAddresses.loc[londonAddresses['UnitFullAddress'] == inputAddress]['Longitude'].values[0]

    # retrieve point object from coordinates
    point = Point(addressCoor)
    # print(point)

    # iterate through all zones for an address, return zone address is located in
    isWithin = False
    count = 0
    zone = 'Your zone is not supported yet.'
    while not isWithin and count < len(allZones):
        isWithin = point.within(allZones[count][0])

        # record zone assignment
        if isWithin:
            zone = allZones[count][1]
        count += 1
    for i in range(0, len(allZones)-1):
        print(allZones[i][1])
    print("Zone Region: " + str(zone))

    # return zone and boolean
    return (zone, isWithin)

