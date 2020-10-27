import cv2
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
sns.set(color_codes=True)

if __name__ == '__main__':

    image = cv2.imread('./example.png')
    pic = imageio.imread('./example.png')
    plt.figure(figsize = (15,15))
 
    plt.imshow(pic)
    plt.title('R channel')
    plt.ylabel('Height {}'.format(pic.shape[0]))
    plt.xlabel('Width {}'.format(pic.shape[1]))
    
    plt.imshow(pic[ : , : , 1])
    plt.show()
    
    print('Type of the image : ' , type(pic))
    print('Shape of the image : {}'.format(pic.shape))
    print('Image Hight {}'.format(pic.shape[0]))
    print('Image Width {}'.format(pic.shape[1]))
    print('Dimension of Image {}'.format(pic.ndim))
