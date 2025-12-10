<h1>**Posterization Tool (OpenCV + Python)**</h1>
A simple image posterization tool built using OpenCV.
The program reduces the number of colors in an image based on user input and saves the result.

**Project structure**
/assets            → Input images  
/results           → Output posterized images  
/src
    posterization.py  → Main posterization script
README.md
requirements.txt

**Features**

* Converts an image to RGB
* Applies median blur
* Uses a custom Lookup Table (LUT) for posterization
* Lets the user choose number of color groups
* Displays original + posterized image
* Saves output to /results/

**How to Run**
1.Clone this repository
2.Navigate into the project folder
3.Install the required libraries using pip install -r requirements.txt
4.Run the posterization script
5.Enter the number of color groups when prompted
6.Original image and posterized image will be displayed side by side 
7.Posterized image will be saved in results/posterized.png (ensure that the folder exists)

The program:
* Loads the original image
* Converts BGR → RGB
* Applies median blur
* Creates a LUT that compresses pixel intensities into buckets
* Uses cv2.LUT() to remap all pixel values
* Displays both images
* Saves the posterized image

**Sample Output**
Output for n=5
<img width="1919" height="1022" alt="image" src="https://github.com/user-attachments/assets/82313853-0c15-4cf1-abde-f4cffa179309" />
