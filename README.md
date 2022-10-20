# QRGen

In Stores and supermarkets every item has a QR code. These QR codes are created for unique identification for the products. When we enter the billing section the person in billing counter would scan the QR code for the information hidden in the QR code. 

QRgen is a qr code generation web application developed using python flask framework. This application runs in browser. Using qrgen we could create qr codes for an item in a bulk order sequentially.

This would be helpful to track the stock inventory whenever we execute the billing.

## Usage

qrgen has two functionalities. 

1. QR code generation in bulk
2. API to generate QR code based on request


### QR Code generation in bulk

1. Run the python file `index.py` with below command

```
$ python3 index.py
    * Serving Flask app 'index'
    * Debug mode: on
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
    * Running on all addresses (0.0.0.0)
    * Running on http://127.0.0.1:5001
    * Running on http://192.168.29.138:5001
    Press CTRL+C to quit
    * Restarting with stat
    * Debugger is active!
    * Debugger PIN: 134-050-709
```

2. Open up the given URL in the browser and enter the details. Refer the below screenshot

![homepage](https://i.imgur.com/uqEGofv.png)

3. Once clicked on the "Generate QR" button the page would load and redirect to another page with QR codes listed.

![qr codes](https://i.imgur.com/Ggjb1Zy.png)

4. If you scroll down to the bottom you could see two buttons like the below image. To print all the qr codes or go back to home

![print](https://i.imgur.com/6hMHrh3.png)

5. You can print to these qr codes to stickers and stick them to the product

