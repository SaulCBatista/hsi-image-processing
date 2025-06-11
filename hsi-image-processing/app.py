from flask import Flask, render_template, request, send_file, jsonify
import os
import cv2
import numpy as np
from utils import rgb_to_hsi, hsi_to_rgb, ajustar_brilho, ajustar_contraste, equalizar_histograma

app = Flask(__name__)
UPLOAD_FOLDER = 'static'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files['image']
    op = request.form.get("operation")
    factor = float(request.form.get("factor", "0.2"))
    print("processando..")

    filename = file.filename
    input_path = os.path.join(UPLOAD_FOLDER, filename)
    output_path = os.path.join(UPLOAD_FOLDER, "result_" + filename)
    
    file.save(input_path)

    img = cv2.imread(input_path)
    H, S, I = rgb_to_hsi(img)

    if op == "brilho_mais":
        print('rodando operação..')
        I_mod = ajustar_brilho(I, factor)
    elif op == "brilho_menos":
        I_mod = ajustar_brilho(I, -factor)
    elif op == "contraste":
        I_mod = ajustar_contraste(I, factor)
    elif op == "equalizar":
        I_mod = equalizar_histograma(I)
    else:
        I_mod = I

    result = hsi_to_rgb(H, S, I_mod)
    cv2.imwrite(output_path, result)

    return jsonify({
        "original": f"/static/{filename}",
        "processed": f"/static/result_{filename}"
    })
if __name__ == "__main__":
    app.run(debug=True)
