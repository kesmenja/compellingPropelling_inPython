import math

# Assuming Mass Flow Inlet = Mass Flow Exhaust
# Function Input is Degrees, Converts to Radians From Within
def reverseThrust(massFlow, inletAngle, velocityInlet, exhaustAngle, velocityExhaust):
    
    print('Mass Flow: '          + str(round(massFlow,2))        + ' [kg/s]' + '\n'
          + 'Inlet Angle: '      + str(round(inletAngle,2))      + ' [deg]'  + '\n'
          + 'Inlet Velocity: '   + str(round(velocityInlet,2))   + ' [m/s]'  + '\n'
          + 'Exhaust Angle: '    + str(round(exhaustAngle,2))    + ' [deg]'  + '\n'
          + 'Exhaust Velocity: ' + str(round(velocityExhaust,2)) + ' [m/s]'  + '\n')
    
    velocityInlet   = velocityInlet * math.cos(inletAngle*(math.pi/180))
    velocityExhaust = velocityExhaust * math.cos(exhaustAngle*(math.pi/180))
    thrustValue     = massFlow * (velocityExhaust - velocityInlet)

    print('Exhaust Force: '
          + str(round(thrustValue,2))
          + '\n')
    
    return thrustValue

############################################################################################

dmdt          = 50                # [kg/s]
theta_Inlet   = 0                 # [deg]
v_Inlet       = 150 * (1000/3600) # [m/s]
theta_Exhaust = 0                 # [deg]
v_Exhaust     = 150               # [m/s]

print('--- Part a -----------------')
reverseThrust(dmdt, theta_Inlet, v_Inlet, theta_Exhaust, v_Exhaust)
############################################################################################

dmdt          = 50                # [kg/s]
theta_Inlet   = 0                 # [deg]
v_Inlet       = 150 * (1000/3600) # [m/s]
theta_Exhaust = 90                 # [deg]
v_Exhaust     = 0 * (1000/3600)   # [m/s]

print('--- Part b -----------------')
reverseThrust(dmdt, theta_Inlet, v_Inlet, theta_Exhaust, v_Exhaust)

############################################################################################
dmdt          = 50                # [kg/s]
theta_Inlet   = 0                 # [deg]
v_Inlet       = 0 * (1000/3600) # [m/s]
theta_Exhaust = 90                 # [deg]
v_Exhaust     = 0 * (1000/3600)   # [m/s]

print('--- Part c -----------------')
reverseThrust(dmdt, theta_Inlet, v_Inlet, theta_Exhaust, v_Exhaust)
