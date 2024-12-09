from PIL import Image
import math



def pixel():
    file = input("What's the name of your image? ")
    image = Image.open(file)
    size = width, height = image.size
    
    num = int(input("How many pixels do you want total? "))
    num = 1/num
    pix = int(math.sqrt(((width*height)*num)))
    right = low = pix
    left = up = 0
   
    for i in range(int(height/pix)+1):
        for i in range(int(width/pix)+1):
            average = average_color(image, (left,up,right,low))
            image.paste(average, (left,up,right,low)) 
            right += pix
            
            left += pix
           
        left = 0
        right = pix
        up += pix
        low += pix

    image.show()


    
def average_color (image, box):
    cropimg = image.crop(box)
    R = 0
    G = 0
    B = 0
    data = list(cropimg.getdata())
    for color in data:
        r, g, b = color
        R += r/len(data)
        B += b/len(data)
        G += g/len(data)
    RGB = (int(R), int(G), int(B))
    return RGB



pixel()
    
