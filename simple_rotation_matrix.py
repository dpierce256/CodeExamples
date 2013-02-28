from math import sin
from math import cos


def OrbitPointAroundPoint(pA, pB, fAngle):
    """Rotates a 3D point (pA[3]) offset from the center of 
    rotation (pB[3]) by the supplied degrees fAngle[3], 
    and returns the new position of the point in 3D space.
    Some calculations multiplying by 0 left in for clarity."""

    fOffsetX = pA[0] - pB[0]
    fOffsetY = pA[1] - pB[1]
    fOffsetZ = pA[2] - pB[2]
    
    #Z-axis rotation matrix
    fVectorX = fOffsetX
    fVectorY = fOffsetY
    fVectorZ = fOffsetZ
    fWorkingX = (fVectorX * cos(fAngle[2])) + (fVectorY * sin(-fAngle[2])) + (fVectorZ * 0)
    fWorkingY = (fVectorX * sin(fAngle[2])) + (fVectorY * cos(fAngle[2])) + (fVectorZ * 0)
    fWorkingZ = (fVectorX * 0) + (fVectorY * 0) + (fVectorZ * 1)    
    
    #Y-axis rotation matrix
    fVectorX = fWorkingX
    fVectorY = fWorkingY
    fVectorZ = fWorkingZ
    fWorkingX = (fVectorX * cos(fAngle[1])) + (fVectorY * 0) + (fVectorZ * sin(fAngle[1]))
    fWorkingY = (fVectorX * 0) + (fVectorY * 1) + (fVectorZ * 0)
    fWorkingZ = (fVectorX * sin(-fAngle[1])) + (fVectorY * 0) + (fVectorZ * cos(fAngle[1]))
    
    #X-axis rotation matrix
    fVectorX = fWorkingX
    fVectorY = fWorkingY
    fVectorZ = fWorkingZ    
    fRotatedX = (fVectorX * 1) + (fVectorY * 0) + (fVectorZ * 0)
    fRotatedY = (fVectorX * 0) + (fVectorY * cos(fAngle[0])) + (fVectorZ * sin(-fAngle[0]))
    fRotatedZ = (fVectorX * 0) + (fVectorY * sin(fAngle[0])) + (fVectorZ * cos(fAngle[0]))
    
    #Return result
    fNewPos = [0.0, 0.0, 0.0]
    fNewPos[0] = fRotatedX
    fNewPos[1] = fRotatedY
    fNewPos[2] = fRotatedZ
    return fNewPos


#Take user input and perform rotation.
pPoint = [0.0, 0.0, 0.0]
pOrigin = [0.0, 0.0, 0.0]
fRotationAngle = [0.0, 0.0, 0.0]

print "What is the point's..."
pPoint[0] = float(raw_input('Position X?: '))
pPoint[1] = float(raw_input('Position Y?: '))
pPoint[2] = float(raw_input('Position Z?: '))

print "What is the origin's..."
pOrigin[0] = float(raw_input('Position X?: '))
pOrigin[1] = float(raw_input('Position Y?: '))
pOrigin[2] = float(raw_input('Position Z?: '))

print "What is the angle of rotation's..."
fRotationAngle[0] = float(raw_input('X value?: '))
fRotationAngle[1] = float(raw_input('Y value?: '))
fRotationAngle[2] = float(raw_input('Z value?: '))

pRotatedPoint = OrbitPointAroundPoint(pPoint, pOrigin, fRotationAngle)

print "The new point position is: X" + str(pRotatedPoint[0]) + ", Y" + str(pRotatedPoint[1]) + ", Z" + str(pRotatedPoint[2])
raw_input('Press any key to exit.')