"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
charge = 0.00 # Charge for this sign.
numChars = 18 # Number of characters.
color = "black" # Color of characters.
woodType = "oak" # Type of wood.
# Base charge for the sign
charge = 35.00

# Write assignment and if statements here as appropriate.

# Add charges for additional characters if there are more than 5
if numChars > 5: charge += (numChars - 5) * 4

# Add charge for oak wood type
if woodType == "oak": charge += 20.00

# Add charge for gold-leaf lettering
if color == "gold": charge += 15.00

# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))