import pynmea2


#/home/abhinav/Schreibtisch/NMEA/NmeaTest1.nmea
f=open("/home/abhinav/Schreibtisch/NMEA/NmeaTest1.nmea", "r")
#contents =f.read()

#reader2 = pynmea2.parse(f.readline().decode('ascii',errors='replace'))
#reader2 = pynmea2.parse(f.readline())

streamreader = pynmea2.NMEAStreamReader(f)
while 1:
    for msg in streamreader.next():
        print (msg)
