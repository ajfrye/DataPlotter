
#from math import pi, sin, cos, tan, acos, atan
from functools import reduce
import numpy as np

def orbital_params_to_r_v(satellite):
    """
    Use Orbital Parameters to convert to R and V in ECI

    Inputs:
            Satellite data struct (directly populated from TLE data)
    Outputs:
            R vector in ECI
            V vector in ECI
    """
    mu = 398600.4418  # km3/s2

    mean_motion_revs = float(satellite.mean_motion_revs)
    P = (mean_motion_revs / (24*3600))**-1
    a = (P * mu**0.5 / (2*np.pi))**(2/3)

    mean_anomaly_rad = np.deg2rad( float(satellite.mean_anomaly_deg) )
    eccentricity = float(satellite.eccentricity)
    theta_deg = mean_anomaly_to_theta(mean_anomaly_rad, eccentricity)

    rp = -a * (eccentricity - 1)
    h = orbit_equation('h', mu, eccentricity, 0, rp)

    r_peri = find_r_peri(h, mu, eccentricity, theta_deg)
    v_peri = find_v_peri(h, mu, eccentricity, theta_deg)

    raan_rad = np.deg2rad(float(satellite.raan_deg))
    inc_rad = np.deg2rad(float(satellite.inclination_deg))
    ap_rad = np.deg2rad(float(satellite.arg_perigee_deg))
    dcm = get_dcm('313', [raan_rad, inc_rad, ap_rad])

    r_eci = np.matmul(np.transpose(dcm), r_peri)
    v_eci = np.matmul(np.transpose(dcm), v_peri)

    return r_eci, v_eci

def mean_anomaly_to_theta(me_rad, ecc):
    """
    Use Newton's Method to approximate the Eccentric Anomaly
    and then convert that to the True Anomaly in degree

    Inputs:
            me_rad is the Mean Anomaly in radians
            ecc is the orbit eccentricity
    Outputs:
            theta_deg is the True Anomaly in degrees
    """
    # make an educated guess for value of E
    if me_rad < np.pi:
        E = me_rad - ecc/2
    else:
        E = me_rad + ecc/2
    
    # iterate until tolerance is reached
    for i in range(100):
        fE = -me_rad + E - ecc * np.sin(E)
        dfE = 1 - ecc * np.cos(E)
        E_new = E - (fE / dfE)
        tol = abs(E_new - E)
        E = E_new
        if tol < 1e-8:
            break
        if i == 99:
            print('mean_anomaly_to_theta - MAX ITERATION LIMIT REACHED')
    
    # find True Anomaly in degrees
    theta_deg = np.rad2deg( (2*np.atan(((1+ecc)/(1-ecc))**0.5 * np.tan(E/2))) )

    return theta_deg

def orbit_equation(h, mu, ecc, theta_deg, r):
    """
    Use the Orbital Equation to solve for the missing variable.
    Use a string for the missing variable
    """
    if isinstance(h, str):
        th = np.deg2rad(theta_deg)
        return (r * mu * (1+ecc*np.cos(th)))**0.5
    elif isinstance(mu, str):
        th = np.deg2rad(theta_deg)
        return (h**2/r * (1+ecc*np.cos(th))**-1)
    elif isinstance(ecc, str):
        th = np.deg2rad(theta_deg)
        return h**2/(mu*r*np.cos(th)) - 1/np.cos(th)
    elif isinstance(theta_deg, str):
        return np.rad2deg( np.acos(h**2/(mu*r*ecc)- 1/ecc) )
    elif isinstance(r, str):
        th = np.deg2rad(theta_deg)
        return h**2/mu * (1+ecc*np.cos(th))**-1

def find_r_peri(h, mu, ecc, theta_deg):
    """
    Finds the perifocal radius by using the Orbit Equation
    and multiplying it by the matrix
    """
    theta_rad = np.deg2rad(theta_deg)
    vector_peri = np.array([np.cos(theta_rad), np.sin(theta_rad), 0])
    
    r = orbit_equation(h, mu, ecc, theta_deg, 'r')
    r_peri = vector_peri * r
    return r_peri

def find_v_peri(h, mu, ecc, theta_deg):
    """
    Finds the perifocal velocity
    """
    theta_rad = np.deg2rad(theta_deg)
    vector_peri = np.array([-np.sin(theta_rad), ecc+np.cos(theta_rad), 0])

    v_peri = mu/h * vector_peri
    return v_peri


def get_dcm(axis, angles):
    """
    Use the Direction Cosine Matrix for Principal Rotations
    Specify the axis rotation sequence ('xyx', 'xzxyxz', '123', etc)
    """
    dcm = []
    for i in range(len(axis)):
        ang = angles[i]
        if axis[i] == '1' or axis[i] == 'x':
            cx = np.matrix([[1, 0, 0],
                            [0, np.cos(ang), np.sin(ang)],
                            [0, -np.sin(ang), np.cos(ang)]])
            dcm.append(cx)
        elif axis[i] == '2' or axis[i] == 'y':
            cy = np.matrix([[np.cos(ang), 0, -np.sin(ang)],
                            [0, 1, 0],
                            [np.sin(ang), 0, np.cos(ang)]])
            dcm.append(cy)
        elif axis[i] == '3' or axis[i] == 'z':
            cz = np.matrix([[np.cos(ang), np.sin(ang), 0],
                            [-np.sin(ang), np.cos(ang), 0],
                            [0, 0, 1]])
            dcm.append(cz)

    mat = reduce(np.matmul, reversed(dcm))
    return mat