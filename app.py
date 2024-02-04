from flask import Flask, render_template, request, jsonify
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
from PIL import Image
import io

app = Flask(__name__, template_folder='templates')

def compare_images_np(image1_np, image2_np):
    try:
        # Resize images to the same dimensions if needed
        if image1_np.shape[:2] != image2_np.shape[:2]:
            image2_np = cv2.resize(image2_np, (image1_np.shape[1], image1_np.shape[0]))

        # Convert the images to grayscale for Mean Squared Error calculation
        signature1_gray = cv2.cvtColor(image1_np, cv2.COLOR_RGB2GRAY)
        signature2_gray = cv2.cvtColor(image2_np, cv2.COLOR_RGB2GRAY)

        # Calculate Mean Squared Error
        mse_value = np.mean((signature1_gray.astype("float") - signature2_gray.astype("float")) ** 2)
        print("Mean Squared Error: ", mse_value)

        # Calculate Structural Similarity Index
        ssim_value = ssim(signature1_gray, signature2_gray)
        print("Structural Similarity Index: ", ssim_value)

        return jsonify({'mse': mse_value, 'ssim': ssim_value, 'image1': image1_np.tolist(), 'image2': image2_np.tolist()})

    except Exception as e:
        print("Error: ", str(e))
        return jsonify({'error': str(e)})

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/compare-images', methods=['POST'])
def compare_images_route():
    try:
        # Read the images directly from memory
        image1_file = request.files['image1']
        image2_file = request.files['image2']

        image1_np = np.asarray(Image.open(image1_file).convert('RGB'))
        image2_np = np.asarray(Image.open(image2_file).convert('RGB'))

        # Perform image comparison
        result = compare_images_np(image1_np, image2_np)

        return result
    
       
        

    except Exception as e:
        print("Error: ", str(e))
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
