from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json():
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except Exception:
        return []

def read_csv():
    data = []
    try:
        with open('products.csv', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    row['id'] = int(row['id'])
                    row['price'] = float(row['price'])
                except ValueError:
                    continue
                data.append(row)
    except Exception:
        pass
    return data

def read_sql():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        conn.close()
        return [{'id': r[0], 'name': r[1], 'category': r[2], 'price': r[3]} for r in rows]
    except Exception:
        return []

@app.route('/products')
def products():
    source = request.args.get('source', '').lower()
    id_param = request.args.get('id')

    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    elif source == 'sql':
        data = read_sql()
    else:
        return render_template('product_display.html', error='Wrong source', products=[])

    if id_param:
        try:
            id_val = int(id_param)
        except ValueError:
            return render_template('product_display.html', error='Invalid id parameter', products=[])
        filtered = [p for p in data if p.get('id') == id_val]
        if not filtered:
            return render_template('product_display.html', error='Product not found', products=[])
        data = filtered

    return render_template('product_display.html', products=data, error=None)

if __name__ == '__main__':
    app.run(debug=True)
