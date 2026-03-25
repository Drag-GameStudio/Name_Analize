import base64

encoded = "Z2hzX05xRFlJTzVhVEtLdXI0MnQyNjk5M0Ewc3FCZGJ4WTF1cGZscwo="
decoded = base64.b64decode(encoded).decode("utf-8")
print(decoded)