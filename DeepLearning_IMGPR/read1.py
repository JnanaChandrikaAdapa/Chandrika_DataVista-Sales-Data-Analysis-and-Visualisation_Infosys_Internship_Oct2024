import cv2
import os
# Path to the folder containing images
folder_path ="D:/INTERNSHIP/image1"
# Get list of image files in the folder
image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
# Check if there are at least 10 images in the folder
if len(image_files) < 10:
    print("The folder contains fewer than 10 images.")
else:
    # Loop through each image and display it
    for img_file in image_files:
        # Read the image
        img_path = os.path.join(folder_path, img_file)
        img = cv2.imread(img_path)

        if img is None:
            print(f"Could not open or find the image {img_file}")
            continue
        
        # Display the image
        cv2.imshow('Image', img)

        # Wait for user input or 2000ms (2 seconds)
        if cv2.waitKey(2000) & 0xFF == 27:  # Press 'Esc' to exit early
            break
        
    # Destroy all the windows after displaying images
    cv2.destroyAllWindows()