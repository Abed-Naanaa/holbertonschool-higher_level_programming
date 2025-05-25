from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json(filename='products.json'):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except Exception:
        return []

def read_csv(filename='products.csv'):
    products = []
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Convert id and price types correctly
                try:
                    row['id'] = int(row['id'])
                    row['price'] = float(row['price'])
                except ValueError:
                    continue
                products.append(row)
        return products
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
    else:
        return render_template('product_display.html', error="Wrong source", products=[])

    # Filter by id if provided
    if id_param:
        try:
            id_val = int(id_param)
        except ValueError:
            return render_template('product_display.html', error="Invalid id parameter", products=[])
        filtered = [p for p in data if p.get('id') == id_val]
        if not filtered:
            return render_template('product_display.html', error="Product not found", products=[])
        data = filtered

    return render_template('product_display.html', products=data, error=None)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
