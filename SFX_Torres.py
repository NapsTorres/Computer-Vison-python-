import cv2
import os
import numpy as np

def apply_filters(image, brightness_level):
    blur = cv2.GaussianBlur(image, (21, 21), 0)
    
    brightness = cv2.convertScaleAbs(image, beta=brightness_level)
    
    emboss_kernel = np.array([[-2, -1, 0],
                               [-1, 1, 1],
                               [0, 1, 2]], dtype=np.float32)
    emboss = cv2.filter2D(image, -1, emboss_kernel)
    emboss = cv2.convertScaleAbs(emboss, alpha=0.5, beta=-50)  # Darken the emboss
    
    sepia = apply_sepia(image)
    
    warm = increase_red_channel(image)
    
    cold = increase_blue_channel(image)
    
    return blur, brightness, emboss, sepia, warm, cold

def save_images(original_image, edited_images, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    cv2.imwrite(os.path.join(output_folder, "original.jpg"), original_image)
    
    filters = ['blur', 'brightness', 'emboss', 'sepia', 'warm', 'cold']

    for i, edited_image in enumerate(edited_images):
        cv2.imwrite(os.path.join(output_folder, f"{filters[i]}.jpg"), edited_image)

def apply_sepia(image):
    sepia_filter = cv2.transform(image, np.array([[0.272, 0.534, 0.131],
                                                  [0.349, 0.686, 0.168],
                                                  [0.393, 0.769, 0.189]]))
    return cv2.convertScaleAbs(sepia_filter, alpha=1.5, beta=50)  # Brighten the sepia

def increase_red_channel(image):
    warm = image.copy()
    warm[:, :, 2] +=  20  
    warm[:, :, 1] += 5   
    return warm

def increase_blue_channel(image):
    cold = image.copy()
    cold[:, :, 0] += 20 
    cold[:, :, 1] += 5  
    return cold

if __name__ == "__main__":
    input_image_path = "test.jpg"
    image = cv2.imread(input_image_path)
    
    brightness_level = -50
    adjusted_brightness_image = apply_filters(image, brightness_level)[1]
    
    blur, _, emboss, sepia, warm, cold = apply_filters(image, brightness_level)
    
    output_folder = "output_images"
    save_images(image, [blur, adjusted_brightness_image, emboss, sepia, warm, cold], output_folder)
