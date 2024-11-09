from flask import Flask, jsonify, request
from models import Point
from database import SessionLocal, init_db

app = Flask(__name__)

print("Flask app is starting...")  # This should appear in Docker logs

@app.before_first_request
def create_tables():
    print("Initializing database...")
    init_db()

@app.route('/points', methods=['POST'])
def create_points():
    print("POST /points endpoint was called")
    return {"message": "Points created successfully"}, 201

@app.route('/points', methods=['GET'])
def get_points():
    print("GET /points endpoint was called")
    session = SessionLocal()

    # Get customer_id and order_id from query parameters
    customer_id = request.args.get('customer_id')
    order_id = request.args.get('order_id')

    try:
        print("getting points")
        points = session.query(Point)
        query = session.query(Point)
        if customer_id:
            query = query.filter(Point.customer_id == customer_id)
        if order_id:
            query = query.filter(Point.order_id == order_id)
        points = query.all()
        print("Points retrieved:", points)  # This will print only if the query is successful
    except Exception as e:
        print("An error occurred:", e)  # Print the error if one occurs
        session.close()
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()

    total_points = 0
    for point in points:
        total_points += point.points

    # Convert query results to a list of dictionaries for JSON response
    points_data = [
        {"customer_id": customer_id, "points": total_points}
    ]

    return jsonify(points_data), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
    logging.basicConfig(level=logging.DEBUG)
