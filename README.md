# calculate_orientation

calculate_orientation.py is a Python script that allows to define orientation of chain segments on imported images, and saves it to a CSV file. This script is designed to work with a variety of image file formats such as JPEG, PNG, and BMP.

# System requirements

- Python (version 3.6 or higher)
- OpenCV (version 4.5.1 or higher)
- NumPy (version 1.19.5 or higher)
- Pandas (version 1.2.4 or higher)
- Math

# Usage
Open the terminal and navigate to the directory where calculate_orientation.py is located. Run the script using the command python calculate_orientation.py Modify the following lines of the script to specify the folder containing input images (input_directory), folder for output images (output_image_directory), anf folder for output datafiles (output_data_directory):

input_directory = '/Users/---/Desktop/---/---'

output_image_directory = '/Users/---/Desktop/---/---/'

output_data_directory = '/Users/---/Desktop/---/---/'

Modify the following line of the script to specify the file extensions of your image files:

extensions = ('.jpeg','.tiff', '.jpg', '.tif')

The script will allow to define chain segments, and accodring to the chosen points, it will calculate segment orientation to horizontal axis of an image according to the law of cosines. Then, output images of tracked segments will be stored on both raw and white background images. Also, it will generate a test_data.csv file, which will contain image filename, and angle values of tracked segments in degrees. 

# Output

One output image is the one with tracked segments on raw image:
![BCKGM_0 25_TOP 071_RAW_CHAIN](https://github.com/vchibrikov/calculate_orientation/assets/98614057/8fbdb80e-6ca2-4df2-8503-5c8bb0e40cde)

The other output image is the one with tracked segments on white background:
![BCKGM_0 25_TOP 071_WHITE_CHAIN](https://github.com/vchibrikov/calculate_orientation/assets/98614057/f1160c7d-5a6c-49f3-8348-3de68d8089b2)


# License
This project is licensed under the MIT License - see the LICENSE.md file for details. Feel free to use and modify it as you wish. If you find any bugs or issues with the script, please create an issue in the GitHub repository.
