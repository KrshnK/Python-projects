# Importing the OpenCV library
import cv2

# Setting the input and output file paths
source = "C:\\Users\\91886\\Desktop\\Python-projects\\image resizer\\KRISHNA.jpg"
destination = "newimage.jpg"

# Setting the percentage scale to resize the image
scale_percent = 50

# Reading the input image from the source path
src = cv2.imread(source, cv2.IMREAD_UNCHANGED)

# Displaying the input image
cv2.imshow("KRISHNA", src)

# Calculating the new dimensions for the output image based on the scaling percentage
new_width = int(src.shape[1] * scale_percent / 100)
new_height = int(src.shape[0] * scale_percent / 100)

# Resizing the input image to the new dimensions
output = cv2.resize(src, (new_width, new_height))

# Saving the output image to the destination path
cv2.imwrite(destination, output)

# Waiting for a key press to close the image window
cv2.waitKey(1)