<h1>Posterization Tool</h1>

A simple image posterization tool built using **OpenCV**, **NumPy** and **matplotlib.pyplot**
<br>The program reduces the number of colors in an image based on user input and saves the result.

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
<ol>
<li>Clone this repository</li>
<li>Navigate into the project folder</li>
<li>Install the required libraries using pip install -r requirements.txt</li>
<li>Specify path of image used in the code </li>
<li>Run the posterization script</li>
<li>Enter the number of color groups when prompted</li>
<li>Original image and posterized image will be displayed side by side </li>
<li>Posterized image will be saved in results/posterized.png (ensure that the folder exists)</li>
</ol>

The program:

* Loads the original image
* Converts BGR → RGB
* Applies median blur
* Creates a LUT that compresses pixel intensities into buckets
* Uses cv2.LUT() to remap all pixel values
* Displays both images
* Saves the posterized image

**Sample Output**
<br>Output for n=5
<img width="1919" height="1022" alt="image" src="https://github.com/user-attachments/assets/82313853-0c15-4cf1-abde-f4cffa179309" />
