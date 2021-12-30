#!/usr/bin/env python
# coding: utf-8

# In[3]:


def triangleformation(file):
    '''a Generator that returns a triangle one at a time from an STL file '''
    tri = []
    trianglenumber = 0
    x=[]
    with open(file,"r") as f:
        for i in f:
            if trianglenumber == 3:
                yield tri
                trianglenumber = 0
                tri=[]
            elif  "vertex" in i:
                trianglenumber += 1
                temp = (str(i).rstrip("\n'")).strip("'\tvertex ")
                y = temp.split()
                x.append(float(y[0]))
                x.append(float(y[1]))
                x.append(float(y[2]))
                tri.append(tuple(x))
                x = []


# In[4]:


def intersection3D2(h,g):
    ''' calculates the intersection of a triangle with a horizontal plane. The input
    is a list of 3D points and returns a list of 3D points.'''
    vector =[]

    #2 points
    if (h == g[0][2] and h ==  g[1][2] and  h != g[2][2]):
        x1 = (g[0][0],g[0][1],g[0][2])
        x2 = (g[1][0],g[1][1],g[1][2]) 
        vector.append(x1)
        vector.append(x2)
        return vector

    elif (h == g[2][2] and h ==  g[1][2] and  h != g[0][2]):
        x1 = (g[2][0],g[2][1],g[2][2])
        x2 = (g[1][0],g[1][1],g[1][2]) 
        vector.append(x1)
        vector.append(x2)
        return vector

    elif (h == g[2][2] and h ==  g[0][2] and  h != g[1][2]):
        x1 = (g[2][0],g[2][1],g[2][2])
        x2 = (g[0][0],g[0][1],g[0][2]) 
        vector.append(x1)
        vector.append(x2)
        return vector


    #line through h 
    elif ((h < g[0][2] and (h > g[1][2] and  h > g[2][2])) or (h > g[0][2] and (h < g[1][2] and  h < g[2][2]))):
            vAB = [(g[1][0] -  g[0][0], g[1][1] -  g[0][1], g[1][2] -  g[0][2])] #A-B
            #A=g[0]
            #B = g[1]

            x2 =g[0][0] + ((h-g[0][2])/(vAB[0][2]))*vAB[0][0]
            y2 =g[0][1] + ((h-g[0][2])/(vAB[0][2]))*vAB[0][1]
            z2 =g[0][2] + ((h-g[0][2])/(vAB[0][2]))*vAB[0][2]
            T2 = (x2,y2,z2)
            vector.append(T2)
            #A=g[0]
            #C =g[2]
            vAC = [(g[2][0] -  g[0][0], g[2][1] -  g[0][1], g[2][2] -  g[0][2])] #A-C

            x1 =g[0][0] + ((h-g[0][2])/(vAC[0][2]))*vAC[0][0]
            y1 =g[0][1] + ((h-g[0][2])/(vAC[0][2]))*vAC[0][1]
            z1 =g[0][2] + ((h-g[0][2])/(vAC[0][2]))*vAC[0][2]
            T1 = (x1,y1,z1)
            vector.append(T1)

            return vector
            #g00 is p0
            
    elif ((h < g[1][2] and (h > g[0][2] and  h > g[2][2])) or (h > g[1][2] and (h < g[0][2] and  h < g[2][2]))):
            vAB = [(g[0][0] -  g[1][0], g[0][1] -  g[1][1], g[0][2] -  g[1][2])] #A-B
            #A=g[1]
            #B = g[0]


            x2 =g[1][0] + ((h-g[1][2])/(vAB[0][2]))*vAB[0][0]
            y2 =g[1][1] + ((h-g[1][2])/(vAB[0][2]))*vAB[0][1]
            z2 =g[1][2] + ((h-g[1][2])/(vAB[0][2]))*vAB[0][2]
            T2 = (x2,y2,z2)
            vector.append(T2)

            #A=g[1]
            #C =g[2]
            vAC = [(g[2][0] -  g[1][0], g[2][1] -  g[1][1], g[2][2] -  g[1][2])] #A-C
            x1 =g[1][0] + ((h-g[1][2])/(vAC[0][2]))*vAC[0][0]
            y1 =g[1][1] + ((h-g[1][2])/(vAC[0][2]))*vAC[0][1]
            z1 =g[1][2] + ((h-g[1][2])/(vAC[0][2]))*vAC[0][2]
            T1 = (x1,y1,z1)
            vector.append(T1)

            #g[1] is p0
            return vector


    elif ((h < g[2][2] and (h > g[1][2] and  h > g[0][2])) or (h > g[2][2] and (h < g[1][2] and  h < g[0][2]))):
            vAB = [(g[0][0] -  g[2][0], g[0][1] -  g[2][1], g[0][2] -  g[2][2])] #A-B
            #A=g[2]
            #B = g[0]

            x2 =g[2][0] + ((h-g[2][2])/(vAB[0][2]))*vAB[0][0]
            y2 =g[2][1] + ((h-g[2][2])/(vAB[0][2]))*vAB[0][1]
            z2 =g[2][2] + ((h-g[2][2])/(vAB[0][2]))*vAB[0][2]
            T2 = (x2,y2,z2)
            vector.append(T2)

            #A=g[2]
            #C =g[1]
            vAC = [(g[1][0] -  g[2][0], g[1][1] -  g[2][1], g[1][2] -  g[2][2])] #A-C

            x1 =g[2][0] + ((h-g[2][2])/(vAC[0][2]))*vAC[0][0]
            y1 =g[2][1] + ((h-g[2][2])/(vAC[0][2]))*vAC[0][1]
            z1 =g[2][2] + ((h-g[2][2])/(vAC[0][2]))*vAC[0][2]
            T1 = (x1,y1,z1)
            vector.append(T1)

            #g[2] is p0
            return vector 
    else:
        return None


# In[5]:


def convert3Dto2D(vect):
    '''Project a list of list of tuples from 3D points to 2D points '''
    points2D = []
    temp = []
    for i in vect:
        for x in i:
            temp.append(tuple(x[0:2]))
        points2D.append(temp)
        temp = []
    return points2D


# In[6]:


import math
         
def convertor(list1):
    '''Convert a list of list of tuples into a list of pair 2D points'''
    value=[]
    y=[]
    pointlist=[]
    for i in list1:
        for g in i:
            pointlist.append(g)
            y.append(g[1])


    maxinumy = max(y)
    yindex = y.index(maxinumy)
    value.append(list1[yindex // 2][yindex % 2])
    if yindex % 2 != 0: 
        endpoint = (list1[yindex // 2][yindex % 2 -1])
        value.append(endpoint)
        pointlist.pop(yindex)
        pointlist.pop(yindex - 1)
    else: 
        endpoint = (list1[yindex // 2][yindex % 2 + 1])
        value.append(endpoint)
        pointlist.pop(yindex)
        pointlist.pop(yindex + yindex % 2)

    while len(pointlist) >= 2:
        distance = []
        for i in pointlist:
            distance.append(math.sqrt((endpoint[0] - i[0])**2 + (endpoint[1] - i[1])**2))
        mindistance = min(distance)
        indexvalue = distance.index(mindistance)

        if indexvalue % 2 != 0:
            endpoint = pointlist[indexvalue - 1]
            value.append(endpoint)
            pointlist.pop(indexvalue)
            pointlist.pop(indexvalue - 1)
        else: 
            endpoint = pointlist[indexvalue + 1]
            value.append(endpoint)
            pointlist.pop(indexvalue)
            pointlist.pop(indexvalue)
    return value


# In[7]:


def imperative(points,rate,movement,height,elength):
    '''Accepts the x and y points, extrude speed,movement speed, present slice height, extruder length and writes a file to convert the
    coordinates to gcode using imperative programming  and returns the present extrude length by the height'''
    distance = []
    for i in range(0,len(points) - 1):
        distance.append(math.sqrt(((points[i + 1][0] + 100) - (points[i][0]+ 100))**2 + ((points[i + 1][1] + 100) - (points[i][1] + 100))**2))
    distance.append(math.sqrt(((points[len(points) - 1][0] + 100) - (points[0][0] + 100))**2 + ((points[len(points) - 1][1] + 100) - (points[0][1] + 100))**2))
    
    with open("Julia_Vase_TF.gcode","a") as f:
        f.write(f"G0 F6000 X{points[0][0] + 100} Y{points[0][1] + 100} Z{round(height,2)}\n")
        f.write(f"G1 F{movement} X{points[0][0] + 100} Y{points[0][1] + 100} Z{round(height,2)} E{elength}\n")
        for i in range(1,len(points)):
            f.write(f"G1 X{points[i][0] + 100} Y{points[i][1] + 100 } E{distance[i -1]*rate + elength}\n")
            elength = distance[i - 1]*rate + elength
        f.write(f"G1 X{points[0][0] + 100} Y{points[0][1] + 100} E{distance[-1]*rate + elength}\n")
    return distance[-1]*rate + elength


# In[8]:


def combiner(stl,height,temp, extrude,movement):
    '''takes in a stl file, printer temperatures,extruder speed and movement speed and
    its ouput is the walls of the stl file in gcode'''
    with open("Julia_Vase_TF.gcode","w") as f:     
        f.write(f";Startup Procedure\n")
        f.write(f"G21\n")
        f.write(f"M140 S60\n")
        f.write(f"M105\n")
        f.write(f"M190 S60\n")
        f.write(f"M104 S{temp}\n")
        f.write(f"M105\n")
        f.write(f"M109 S{temp}\n")
        f.write(f"M106 S200\n")
        f.write(f"M82\n\n")

        f.write(f"; Ender 3 Custom Start G-code from cura\n")
        f.write(f"G92 E0 ; Reset Extruder\n")
        f.write(f"G28 ; Home all axes\n")
        f.write(f"G1 Z2.0 F3000 ; Move Z Axis up little to prevent scratching of Heat Bed\n")
        f.write(f"G1 X0.1 Y20 Z0.3 F5000.0 ; Move to start position\n")
        f.write(f"G1 X0.1 Y200.0 Z0.3 F1500.0 E15 ; Draw the first line\n")
        f.write(f"G1 X0.4 Y200.0 Z0.3 F5000.0 ; Move to side a little\n")
        f.write(f"G1 X0.4 Y20 Z0.3 F1500.0 E30 ; Draw the second line\n")
        f.write(f"G92 E0 ; Reset Extruder\n")
        f.write(f"G1 Z2.0 F3000 ; Move Z Axis up little to prevent scratching of Heat Bed\n")
        f.write(f"G1 X5 Y20 Z0.3 F5000.0 ; Move over to prevent blob squish\n\n")
        
        f.write(f";Printing Vase\n")
        f.write(f"G90\n")
        f.write(f"G28 x0 Y0 Z0; go to the home location\n")
        f.write(f"G92 E0\n")
        f.write(f"G92 E0\n")
        f.write(f"G1 F2700 E-5\n")

        
        
        
    sliceheight = height
    length = 0.0
    for x in range(0,619): #changes based on the height of the stl file
        vect = []
        triangle = triangleformation(stl)
        for i in triangle:
            tri = intersection3D2(round(sliceheight,2),next(triangle))
            if tri != None:
                vect.append(tri)
        elength = imperative(convertor(convert3Dto2D(vect)),extrude,movement,round(sliceheight,2),length)
        sliceheight += 0.2
        length = elength
        
        
    with open("Julia_Vase_TF.gcode","a") as f:
        f.write(f"\n;Shutting Down procedure \n")
        f.write(f"; Ender 3 Custom end G-code from cura\n")
        f.write(f"G91 ;Relative positioning\n")
        f.write(f"G1 E-2 F2700 ;Retract a bit\n")
        f.write(f"G1 E-2 Z0.2 F2400 ;Retract and raise Z\n")
        f.write(f"G1 X5 Y5 F3000 ;Wipe out\n")
        f.write(f"G1 Z10 ;Raise Z more\n")
        f.write(f"G90 ;Absolute positionning\n")

        f.write(f"G1 X0 Y235 ;Present print\n")
        f.write(f"M106 S0 ;Turn-off fan\n")
        f.write(f"M104 S0 ;Turn-off hotend\n")
        f.write(f"M140 S0 ;Turn-off bed\n")

        f.write(f"M84 X Y E ;Disable all steppers but Z\n")    


# In[9]:


combiner("Julia_Vase.stl",0.2,230,0.0332819082,1200)


# In[ ]:




