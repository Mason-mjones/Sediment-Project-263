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




