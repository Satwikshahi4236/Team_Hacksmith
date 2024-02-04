import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
from skimage import io

def compare_images(image1_path, image2_path):
    # Load the two signature images
    try:
        signature1 = cv2.imread(image1_path)
        signature2 = cv2.imread(image2_path)
    except Exception as e:
        print("Error loading images: ", str(e))
        return

    # Check if the images have the same dimensions
    if signature1.shape != signature2.shape:
        print("Error: Images have different dimensions")
        return

    # Convert the images to grayscale for Mean Squared Error calculation
    signature1_gray = cv2.cvtColor(signature1, cv2.COLOR_BGR2GRAY)
    signature2_gray = cv2.cvtColor(signature2, cv2.COLOR_BGR2GRAY)

    # Calculate Mean Squared Error
    mse = np.mean((signature1_gray.astype("float") - signature2_gray.astype("float")) ** 2)
    print("Mean Squared Error: ", mse)

    # Calculate Structural Similarity Index
    s = ssim(signature1_gray, signature2_gray)
    print("Structural Similarity Index: ", s)

    # Display the images (optional)
    cv2.imshow("Signature 1", signature1)
    cv2.imshow("Signature 2", signature2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Replace with your signature image paths
image1_path = r"C:\Users\satvi\OneDrive\Documents\Documents\Satwik Signature Blue.jpg"
image2_path = r"C:\Users\satvi\OneDrive\Documents\Documents\satwik signature Black.jpg"

compare_images(image1_path, image2_path)
