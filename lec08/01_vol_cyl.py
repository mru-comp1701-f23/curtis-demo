import math
def vol_cyl(radius: float, height: float) -> float:
    """Calculates the volume of a regular cylinder."""
    vol = radius**2 * math.pi * height
    return vol

def main() -> None:
    rad = 1.0
    height = 25
    vol = 78.5 # equivalent to vol_cyl call
    vol = vol_cyl(rad, height)
    print(f"The volume of the cylinder is: {vol}")
    
main()