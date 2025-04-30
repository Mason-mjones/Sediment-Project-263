import math
import numpy as np

def wave_speed(wavelength: float, depth: float, gravity: float = 9.81) -> float:
    """
    Calculates wave speed based on water depth and wavelength.
    
    Parameters:
    wavelength (float): The wavelength of the wave (meters).
    depth (float): The depth of the water (meters).
    gravity (float, optional): Acceleration due to gravity (default is 9.81 m/s²).
    
    Returns:
    float: The wave speed (m/s).
    
    Raises:
    ValueError: If input values are non-positive.
    """
    if wavelength <= 0 or depth <= 0:
        raise ValueError("Wavelength and depth must be positive numbers.")

    # Determine wave regime
    if depth > wavelength / 2:
        # Deep-water wave speed (fixed formula)
        return math.sqrt((gravity * wavelength) / (2 * math.pi))
    elif depth < wavelength / 20:
        # Shallow-water wave speed
        return math.sqrt(gravity * depth)
    else:
        # Intermediate-wave speed using dispersion relation approximation
        return math.sqrt((gravity * wavelength) / (2 * math.pi) * math.tanh((2 * math.pi * depth) / wavelength))

def wave_refraction_snell(initial_angle: float, depth1: float, depth2: float, wavelength: float) -> float:
    """
    Calculates the refracted wave angle using Snell's Law as a wave approaches a west-facing beach (270°).
    
    Parameters:
    - initial_angle (float): Incident wave angle (in degrees, relative to true north).
    - depth1 (float): Initial water depth (meters).
    - depth2 (float): Shallower water depth (meters, closer to shore).
    - wavelength (float): The wavelength of the wave (meters).
    
    Returns:
    - refracted_angle (float): New wave angle after refraction (degrees).
    """
    
    # Compute wave speeds dynamically using the integrated function
    c1 = wave_speed(wavelength, depth1)
    c2 = wave_speed(wavelength, depth2)

    # Convert angle to radians for calculations (relative to 270°)
    theta1_rad = np.radians(initial_angle - 270)

    # Apply Snell's Law: sin(theta1) / c1 = sin(theta2) / c2
    sin_theta2 = (c2 / c1) * np.sin(theta1_rad)
    
    # Ensure valid range for arcsin
    if abs(sin_theta2) > 1:
        theta2_rad = np.sign(sin_theta2) * np.pi / 2  # Max bending (90 degrees)
    else:
        theta2_rad = np.arcsin(sin_theta2)

    # Convert back to global angle reference
    refracted_angle = np.degrees(theta2_rad) + 270

    return refracted_angle









