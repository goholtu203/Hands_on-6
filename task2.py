"""
Problem: Temperature Converter

Function signature
def convert_temperature(value, scale):
    pass

Requirements:

If scale = "C", the given value is in Celsius. Convert it to Kelvin using:

𝐾=𝐶+273.15

If scale = "K", the given value is in Kelvin. Convert it to Celsius using:
𝐶=𝐾−273.15
If the user enters an invalid scale (not "C" or "K"), return the message: "Invalid scale. Use 'C' for Celsius or 'K' for Kelvin."

Example Usage:
print(convert_temperature(25, "C"))  
298.15 (25°C = 298.15 K)

print(convert_temperature(300, "K"))  
26.85 (300 K = 26.85°C)

print(convert_temperature(100, "F"))  
# "Invalid scale. Use 'C' for Celsius or 'K' for Kelvin."
"""

def convert_temperature(value, scale):
	K = 0
	C = 0
	if scale == "C":
		K = value + 273.15
		print(f"{K:.2f} ({scale}= {K:.2f})")
	elif scale == "K":
		C = value-273.15
		print(f"{C:.2f} ({scale}= {C:.2f})")
	else:
		print("Invalid Scale: ")
	
(convert_temperature(300, "K"))




















