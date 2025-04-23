#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      HADI
#
# Created:     10/04/2025
# Copyright:   (c) HADI 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from PIL import Image

# Open an existing image
img = Image.open('chandelier.png')  # Open your image file

# Perform any operations you want (optional)
# For example, resizing or converting format
img_resized = img.resize((1000, 1000))  # Resize image to 200x200 pixels

# Save the image to a new file
img_resized.save("chandelier.png")  # Save the new image
print("Image saved successfully!")
img.show()
