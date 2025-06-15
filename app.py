from flask import Flask, render_template, request

app = Flask(__name__)

def cek_isbn13(isbn):
    isbn = isbn.replace("-", "").replace(" ", "")
    if len(isbn) != 13 or not isbn.isdigit():
        return False

    total = 0
    for i in range(12):
        angka = int(isbn[i])
        if i % 2 == 0:
            total += angka
        else:
            total += angka * 3

    cek_digit = (10 - (total % 10)) % 10
    return cek_digit == int(isbn[-1])

@app.route('/', methods=['GET', 'POST'])
def index():
    hasil = ''
    if request.method == 'POST':
        isbn = request.form['isbn']
        if cek_isbn13(isbn):
            hasil = f"✅ ISBN {isbn} valid!"
        else:
            hasil = f"❌ ISBN {isbn} tidak valid."
    return render_template('index.html', hasil=hasil)

if __name__ == '__main__':
    app.run(debug=True)
