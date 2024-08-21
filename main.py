from flask import Flask, jsonify, request
import firebase_admin
from firebase_admin import credentials, db
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from io import BytesIO
import base64
from flask_cors import CORS


# Initialize Flask app
app = Flask(__name__)
CORS(app)
# Initialize Firebase Admin SDK
cred = credentials.Certificate('/Users/2003s/financetech-1459b-firebase-adminsdk-t6ykd-c1537e355b.json')  # Update path
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://financetech-1459b-default-rtdb.asia-southeast1.firebasedatabase.app/'  # Your database URL
})


@app.route('/data/_analysis/chart', methods=['GET'])
def get_chart():
    chart_type = request.args.get('type')

    df = fetch_data()

    if df.empty:
        return jsonify({"message": "No data available"}), 404

    # 1. Fraud Count by Age and Gender (Plotly)
    if chart_type == 'fraud_age_gender':
        fraud_by_age_gender = df[df['fraud'] == 1].groupby(['age', 'gender']).size().reset_index(name='fraud_count')
        fig = px.bar(fraud_by_age_gender, x='age', y='fraud_count', color='gender', barmode='group',
                     title='Fraud Count by Age and Gender')

    # 2. Fraud Count by Age and Gender (Matplotlib)
    elif chart_type == 'fraud_age_gender_mpl':
        fraud_by_age_gender = df[df['fraud'] == 1].groupby(['age', 'gender']).size().reset_index(name='fraud_count')
        fig, ax = plt.subplots()
        fraud_by_age_gender.pivot("age", "gender", "fraud_count").plot(kind='bar', ax=ax)
        ax.set_title('Fraud Count by Age and Gender')

    # ... Add other chart types similarly

    # Convert the figure to a PNG image and encode in base64
    img_bytes = io.BytesIO()
    fig.savefig(img_bytes, format='png')
    img_bytes.seek(0)
    img_base64 = base64.b64encode(img_bytes.read()).decode('utf-8')

    plt.close(fig)  # Close the figure after saving

    return jsonify({'chart': img_base64})


@app.route('/api/data', methods=['GET'])
def get_data():
    # Fetch or process your data
    data = {"message": "Hello from Flask!"}
    return jsonify(data)

def fetch_data():
    # Fetch data from Firebase Firestore
    collection_ref = db.collection('databaseURL')
    docs = collection_ref.stream()

    data = []
    for doc in docs:
        data.append(doc.to_dict())

    return pd.DataFrame(data)

def matplotlib_to_base64(fig):
    """Converts a Matplotlib figure to a Base64 encoded image."""
    buf = BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()
    return img_base64

@app.route('/data/_analysis', methods=['GET'])
def analyze_data():
    df = fetch_data()

    if df.empty:
        return jsonify({"message": "No data available"}), 404

    _analysis_results = {}

    # 1. Fraud Detection Analysis with Plotly
    fraud_by_age_gender = df[df['fraud'] == 1].groupby(['age', 'gender']).size().reset_index(name='fraud_count')
    fig_fraud_age_gender = px.bar(fraud_by_age_gender, x='age', y='fraud_count', color='gender', barmode='group',
                                  title='Fraud Count by Age and Gender')
    img_bytes_fraud_age_gender = fig_fraud_age_gender.to_image(format='png')
    img_base64_fraud_age_gender = base64.b64encode(img_bytes_fraud_age_gender).decode('utf-8')

    # 2. Fraud Detection Analysis with Matplotlib
    fig, ax = plt.subplots()
    fraud_by_age_gender.pivot(index='age', columns='gender', values='fraud_count').plot(kind='bar', ax=ax)
    ax.set_title('Fraud Count by Age and Gender (Matplotlib)')
    img_base64_fraud_age_gender_mpl = matplotlib_to_base64(fig)
    plt.close(fig)

    # 3. Customer Segmentation by Age Distribution with Plotly
    fig_age_distribution = px.histogram(df, x='age', title='Age Distribution of Customers')
    img_bytes_age_distribution = fig_age_distribution.to_image(format='png')
    img_base64_age_distribution = base64.b64encode(img_bytes_age_distribution).decode('utf-8')

    # 4. Customer Segmentation by Age Distribution with Matplotlib
    fig, ax = plt.subplots()
    df['age'].plot(kind='hist', bins=10, ax=ax)
    ax.set_title('Age Distribution of Customers (Matplotlib)')
    img_base64_age_distribution_mpl = matplotlib_to_base64(fig)
    plt.close(fig)

    # 5. Transaction Amount Analysis with Plotly
    avg_amount_by_category = df.groupby('category')['amount'].mean().reset_index()
    fig_avg_amount_by_category = px.bar(avg_amount_by_category, x='category', y='amount', title='Average Amount by Category')
    img_bytes_avg_amount_by_category = fig_avg_amount_by_category.to_image(format='png')
    img_base64_avg_amount_by_category = base64.b64encode(img_bytes_avg_amount_by_category).decode('utf-8')

    # 6. Transaction Amount Analysis with Matplotlib
    fig, ax = plt.subplots()
    avg_amount_by_category.plot(kind='bar', x='category', y='amount', ax=ax)
    ax.set_title('Average Amount by Category (Matplotlib)')
    img_base64_avg_amount_by_category_mpl = matplotlib_to_base64(fig)
    plt.close(fig)

    # 7. Fraud by Merchant with Plotly
    fraud_by_merchant = df[df['fraud'] == 1].groupby('merchant').size().reset_index(name='fraud_count')
    fig_fraud_by_merchant = px.bar(fraud_by_merchant, x='merchant', y='fraud_count', title='Fraud Count by Merchant')
    img_bytes_fraud_by_merchant = fig_fraud_by_merchant.to_image(format='png')
    img_base64_fraud_by_merchant = base64.b64encode(img_bytes_fraud_by_merchant).decode('utf-8')

    # 8. Fraud by Merchant with Matplotlib
    fig, ax = plt.subplots()
    fraud_by_merchant.plot(kind='bar', x='merchant', y='fraud_count', ax=ax)
    ax.set_title('Fraud Count by Merchant (Matplotlib)')
    img_base64_fraud_by_merchant_mpl = matplotlib_to_base64(fig)
    plt.close(fig)

    # Return all analysis results and charts
    return jsonify({
        'analysis': {
            'avg_amount_by_category': avg_amount_by_category.to_dict(),
            'fraud_by_age_gender': fraud_by_age_gender.to_dict(),
            'fraud_by_merchant': fraud_by_merchant.to_dict(),
        },
        'charts': {
            'fraud_age_gender': img_base64_fraud_age_gender,
            'fraud_age_gender_mpl': img_base64_fraud_age_gender_mpl,
            'age_distribution': img_base64_age_distribution,
            'age_distribution_mpl': img_base64_age_distribution_mpl,
            'avg_amount_by_category': img_base64_avg_amount_by_category,
            'avg_amount_by_category_mpl': img_base64_avg_amount_by_category_mpl,
            'fraud_by_merchant': img_base64_fraud_by_merchant,
            'fraud_by_merchant_mpl': img_base64_fraud_by_merchant_mpl,
        }
    })
# Fetch all data with pagination
@app.route('/data', methods=['GET'])
def get_paginated_data():
    limit = request.args.get('limit', default=1000, type=int)
    start_after = request.args.get('start_after', default=None)

    ref = db.reference('/')  # Adjust with your actual top-level node name
    query = ref.order_by_key().limit_to_first(limit + 1)

    if start_after:
        query = query.start_after(start_after)

    data = query.get()

    if isinstance(data, dict):
        keys = list(data.keys())
        if len(keys) > limit:
            next_start_after = keys[-1]
            data = {k: data[k] for k in keys[:-1]}
        else:
            next_start_after = None
    elif isinstance(data, list):
        if len(data) > limit:
            next_start_after = data[-1]
            data = data[:-1]
        else:
            next_start_after = None
    else:
        data = {}
        next_start_after = None

    return jsonify({
        'data': data,
        'next_start_after': next_start_after
    })

# Fetch data by customer
@app.route('/data/customer/<customer_id>', methods=['GET'])
def get_data_by_customer(customer_id):
    ref = db.reference('/')  # Adjust with your actual top-level node name if needed
    query = ref.order_by_child('customer').equal_to(customer_id).get()

    if not query:
        return jsonify({"error": "No data found for the specified customer."}), 404

    return jsonify(query)
# Add new data
@app.route('/data', methods=['POST'])
def add_data():
    new_data = request.json
    ref = db.reference('/')
    ref.push(new_data)
    return jsonify({"status": "Data added successfully!"}), 201

# Update existing data
@app.route('/data/<key>', methods=['PUT'])
def update_data(key):
    updated_data = request.json
    ref = db.reference(f'/{key}')
    ref.update(updated_data)
    return jsonify({"status": "Data updated successfully!"})

# Delete data
@app.route('/data/<key>', methods=['DELETE'])
def delete_data(key):
    ref = db.reference(f'/{key}')
    ref.delete()
    return jsonify({"status": "Data deleted successfully!"})

# Run Flask app
if __name__ == '__main__':
    app.run(debug=True)
