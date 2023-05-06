#Import packages

import numpy as np
import os
import cv2
import pandas as pd
import math

# Define dataframe to write data filename of output data file
df = pd.DataFrame(columns=['file_name', 'segment_angle_deg'])
output_filename = 'test_data.csv'

# Define the function to create white image with same size as input image
def create_white_image(image):
    white_image = np.ones(image.shape, dtype=np.uint8) * 255
    return white_image

# Define the function to handle mouse events
def mouse_callback(event, x, y, flags, params):

    # Condition if left mouse button is pressed
    if event == cv2.EVENT_LBUTTONDOWN and len(params['points']) < 6000:
        
        # Append the point to the list
        params['points'].append((x, y))

        # Mark point as a circle
        cv2.circle(params['image'], (x, y), 5, (255, 0, 0), -1)

        # Mark point as a circle on white image
        cv2.circle(white_image, (x, y), 5, (255, 0, 0), -1)

        # Update the display
        cv2.imshow('image', params['image'])

        # If the list of points contains at least 2 points, draw a line
        if event == cv2.EVENT_LBUTTONDOWN and len(params['points']) > 1:

            # Define the coordinates of the last chain segment
            point1 = params['points'][-2]
            point2 = params['points'][-1]

            # Draw segment
            cv2.line(params['image'], point1, point2, (0, 0, 255), 2)

            # Draw segment on white image
            cv2.line(white_image, point1, point2, (0, 0, 255), 3)

            # Mark point as a circle
            cv2.circle(params['image'], (x, y), 5, (255, 0, 0), -1)

            # Mark point as a circle on white image
            cv2.circle(white_image, (x, y), 5, (255, 0, 0), -1)

            # Write chains at white image
            cv2.imwrite(os.path.join(output_image_directory, filename_short + '_WHITE_CHAIN.tiff'), white_image)
 
            # Write chains at original image
            cv2.imwrite(os.path.join(output_image_directory, filename_short + '_RAW_CHAIN.tiff'), params['image'])

            # Update the display
            cv2.imshow('image', params['image'])

            # Define an angle between the last chain segment and y-axis according to law of cosines
            # Define the point with higher value of y coordinate
            if point1[1] <= point2[1]:

                # Define edge coordinates of triangle
                A = params['points'][-2]
                B = params['points'][-1]
                C = (B[0],  B[1] + 10)

                # Check coordinates
                # print('A = ', A, ' | B = ', B, ' | C = ', C)

                # Define length of triangle's sides
                AB = ((A[0] - B[0])**2 + (A[1] - B[1])**2)**0.5
                BC = ((B[0] - C[0])**2 + (B[1] - C[1])**2)**0.5
                CA = ((C[0] - A[0])**2 + (C[1] - A[1])**2)**0.5

                # Check length values
                # print('AB = ', AB, ' | BC = ', BC, ' | CA = ', CA)

                # Define angle ABC in rad
                ABC = math.acos((BC**2 + AB**2 - CA**2)/(2*BC*AB))

                # Define angle ABC in deg
                ABC = round(math.degrees(ABC), 0)

                # Track the procedure
                print('Filename: ', filename ,' | Click number: ', len(params['points']), ' | Angle = ', ABC, 'degrees')

            else:
                # Define edge coordinates of triangle
                A = params['points'][-2]
                B = params['points'][-1]
                C = (A[0],  A[1] + 10)  

                # Check coordinates
                # print('A = ', A, ' | B = ', B, ' | C = ', C)   

                # Define length of triangle's sides
                AB = ((A[0] - B[0])**2 + (A[1] - B[1])**2)**0.5
                BC = ((B[0] - C[0])**2 + (B[1] - C[1])**2)**0.5
                CA = ((C[0] - A[0])**2 + (C[1] - A[1])**2)**0.5

                # Check length values
                # print('AB = ', AB, ' | BC = ', BC, ' | CA = ', CA)

                # Define angle ABC in rad
                ABC = math.acos((CA**2 + AB**2 - BC**2)/(2*CA*AB))

                # Define angle ABC in deg
                ABC = round(math.degrees(ABC), 0)

                # Track the procedure
                print('Filename: ', filename ,' | Click number: ', len(params['points']), ' | Angle = ', ABC, 'degrees')                       

            # Write data to dataframe
            df.loc[len(df)] = [filename_short, ABC]
            df.to_csv(output_data_directory + output_filename, index = False)

        # If right mouse button is pressed, than draw a separate point
    if event == cv2.EVENT_RBUTTONDOWN and len(params['points']) < 6000:

        # Add the point to the list
        params['points'].append((x, y))

        # Track the procedure
        print('Fiber changed. Filename: ', filename ,' | Click number: ', len(params['points']))

        # Mark point as a circle
        cv2.circle(params['image'], (x, y), 5, (255, 0, 0), -1)

        # Update the display
        cv2.imshow('image', params['image'])

# Define the folder containing the images
input_directory = '/Users/---/Desktop/---/---/---/' 
output_image_directory = '/Users/---/Desktop/---/---/---/'
output_data_directory = '/Users/---/Desktop/---/---/---/'

# Define the extensions of the image files
extensions = ('.jpeg','.tiff', '.jpg', '.tif')

# Iterate over the images in the folder
for filename in os.listdir(input_directory):
    if filename.lower().endswith(extensions):

	# Modify filename
        filename_short = filename.replace('.tiff', '')

        # Load the image
        image = cv2.imread(os.path.join(input_directory, filename))

        # Create a copy of the image for display purposes
        image_copy = image.copy()

        # Create a white image to draw lines on
        white_image = create_white_image(image)

        # Define the dictionary of parameters to be passed to the mouse callback function
        params = {'image': image_copy, 'filename': filename, 'points': []}

        # Create a window to display the image
        cv2.namedWindow("image", cv2.WINDOW_FULLSCREEN)

        # Set the mouse callback function
        cv2.setMouseCallback("image", mouse_callback, params)

        # Show the image and wait for user to select points
        cv2.imshow("image", image)
        cv2.setMouseCallback("image", mouse_callback, params)
        cv2.waitKey(0)