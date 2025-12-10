import numpy as np
import matplotlib.pyplot as mp 
import  cv2
path=r"D:\OpenCV_build\assets\BBK.jpg"
img=cv2.imread(path)
img_rgb=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  #BGR converted to RBG because matplotlib requires such format

median=img_rgb.copy()
median=cv2.medianBlur(median, 5) #Applying median blur

def create_lut(n):
    lut=np.zeros(256, dtype=np.uint8)

    step=256//n
    for i in range(256):            
        bucket_index=i//step
        if bucket_index>=n:
            bucket_index=n-1
        lut[i]=bucket_index*255/(n-1)
    return lut

n=int(input("Enter number of colours required to group pixels (can't be 1): "))

if n==1:
    print("All pixels will be mapped to one colour, image won't be posterized")
elif n<1:
    print("Invalid input")
else:
    new_img=cv2.LUT(median, create_lut(n))
    new_img_bgr=cv2.cvtColor(new_img, cv2.COLOR_RGB2BGR) #image converted back to bgr to save 
    #Displaying
    mp.figure()
    
    #Displaying original image
    mp.subplot(1,2,1)
    mp.imshow(img_rgb)
    mp.title("Original")

    #Displaying posterized image
    mp.subplot(1,2,2)
    mp.imshow(new_img)
    mp.title("Posterized image")
    
    cv2.imwrite(r"D:\OpenCV_build\results\posterized.png", new_img_bgr)
    mp.show()


