from flask import Flask, render_template, flash, url_for, redirect, request, jsonify, send_file
import os
import qrcode
from PIL import Image
import datetime
import time

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'qrcodes')


@app.route('/', methods=['GET', 'POST'])
def qrgen():
    if request.method == 'POST':
        prefix = request.form['prefix']
        start = request.form['start']
        end = request.form['end']
        item_name = request.form['item_name']
        category = request.form['category']
        rate = request.form['rate']
        f = []

        for i in range(int(start), int(end)+1):
            data = (prefix + "-" + str(i).zfill(len(end)) + "-" + item_name + "-" + category + "-" + rate)
            qr = qrcode.make(data)
            folder = os.path.join(app.config['UPLOAD_FOLDER'])
            filename = data+".png"
            file_path = os.path.join(folder, filename)
            qr.save(os.path.join(folder, filename))
            f.append(os.path.join(folder, filename))
        return render_template('qr.html', f=f)
    return render_template("qrgen.html")

# Older version
@app.route('/api/v0.1/json/item=<string:item>&category=<string:category>&code=<string:code>&price=<int:price>&format=<string:format>', methods=['GET', 'POST'])
def api(item, category, code, price, format):
    if request.method == "POST":
        dict = {}
        dict.update({"item": item,
                     "category": category,
                     "code": code,
                     "price": price,
                     "format": format})
        qr = qrcode.make(dict)
        folder = os.path.join(app.config['UPLOAD_FOLDER'])
        filename = item+"_"+category+"_"+code+"."+format
        qr.save(os.path.join(folder, filename))
        file_path = os.path.join(folder, filename)
        dict.update({"image": "https://localhost:5001/"+file_path})

        invalid = {"Format": "Invalid"}
        return jsonify(dict)

    else:
        return render_template("index.html")

# Current version
@app.route('/api/v1/qr_data=<string:qr_data>&mar=<int:mar>&fmt=<string:fmt>', methods=['GET', 'POST'])
def api_json(qr_data, mar, fmt):
    folder = os.path.join(app.config['UPLOAD_FOLDER'])
    file_name = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S_%f")+"."+fmt
    file_path = os.path.join(folder, file_name)
    invalid = {"Format": "Invalid"}
    result = {}

    qr = qrcode.QRCode(
        version=3,
        box_size=mar,
        border=mar)

    qr.add_data(qr_data)
    qr.make()
    img = qr.make_image()

    if fmt == 'jpg':
        for i in os.listdir(folder):
            os.remove(os.path.join(folder, i))
        img.save(file_path)
        im = Image.open(file_path)
        rgb_im = im.convert("RGB")
        rgb_im.save(file_path)
        result.update({"qr_data": qr_data,
                       "file_path": file_path})
        return send_file(file_path, as_attachment=True)
    elif fmt == 'png':
        for i in os.listdir(folder):
            os.remove(os.path.join(folder, i))
        img.save(file_path)
        result.update({"qr_data": qr_data,
                       "file_path": file_name})
        return send_file(file_path, as_attachment=True)
    else:
        return jsonify(invalid)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
