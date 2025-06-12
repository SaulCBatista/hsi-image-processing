# 🎨 RGB to HSI Conversion with Intensity Channel Adjustments
This project implements the conversion of images from the RGB color space to HSI, allowing operations on the Intensity (I) channel such as brightness adjustment, contrast enhancement, and histogram equalization. The system was developed as part of Practical Assignment 4 for the Digital Image Processing course at the Federal University of Alagoas (UFAL).
## 📸 Features
- RGB to HSI and HSI to RGB conversion.
- Increase and decrease brightness (on the I channel).
- Contrast adjustment (on the I channel).
- Histogram equalization (on the I channel).
- Simple web interface for uploading and processing images.
## 🧰 Technologies Used
- Python 3
- Flask
- OpenCV
- NumPy
- HTML (for the web interface)
## ▶️ How to Run the Project
1. Clone the repository:
```bash
git clone https://github.com/SaulCBatista/hsi-image-processing
cd hsi-image-processing
```
2. Install the dependencies:
```bash
pip install flask opencv-python numpy
```
3. Run the server:
```bash
python app.py
```
4. Open in your browser:
```bash
http://127.0.0.1:5000/
```
## 💼 Available Operations
- Increase Brightness – Adds a value to the intensity channel.
- Decrease Brightness – Subtracts a value from the intensity channel.
- Adjust Contrast – Enhances or softens image contrast.
- Equalize Histogram – Equalizes the I channel to improve intensity distribution.
