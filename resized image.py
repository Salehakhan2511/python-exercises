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


img = Image.open('chandelier.png')  # Open your image file
img.show()



img_resized = img.resize((100, 100))

# Save the image to a new file
img_resized.save("chandelier.png")  # Save the new image
print("Image saved successfully!")
img.show()
