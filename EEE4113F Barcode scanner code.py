#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install Pillow')
get_ipython().system('pip install opencv-python')
get_ipython().system('pip install python-barcode')
get_ipython().system('pip install pyzbar')
import cv2
from pyzbar import pyzbar


# In[2]:


def read_barcodes(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y , w, h = barcode.rect
        
        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
        
        font = cv2.FONT_HERSHEY_SIMPLEX    # font
        org = (x + 6, y - 6)               # org
        fontScale = 1                      # fontScale
        color = (255, 255, 255)            # white in BGR
        thickness = 2                      # Line thickness of 2 px

        cv2.putText(frame, barcode_info, org, font, fontScale, color, thickness)
        
        print("Barcode scan sucessful")                        #prints if scan is sucessful
        print("The product barcode is: ", barcode_info)        #print results
        
    return frame


# In[3]:


def main():
    #1
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    #2
    while ret:
        ret, frame = camera.read()
        frame = read_barcodes(frame)
        cv2.imshow('Barcode/QR code reader', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    #3
    camera.release()
    cv2.destroyAllWindows()


# In[11]:


#4
if __name__ == '__main__':
    main()


# In[ ]:




