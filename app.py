from flask import Flask, jsonify, request
import grpc
import food_ordering_pb2
import food_ordering_pb2_grpc
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

def get_grpc_stub():
    channel = grpc.insecure_channel('localhost:50051')
    stub = food_ordering_pb2_grpc.FoodOrderingStub(channel)
    return stub

@app.route('/menu', methods=['GET'])
def get_menu():
    stub = get_grpc_stub()
    response = stub.GetMenu(food_ordering_pb2.GetMenuRequest())
    items = [{'id': item.id, 'name': item.name, 'price': item.price} for item in response.items]
    return jsonify(items)

@app.route('/order', methods=['POST'])
def place_order():
    stub = get_grpc_stub()
    item_ids = request.json.get('item_ids', [])
    order_response = stub.PlaceOrder(food_ordering_pb2.PlaceOrderRequest(item_ids=item_ids))
    return jsonify({'order_id': order_response.order_id, 'total_price': order_response.total_price})

@app.route('/orders', methods=['GET'])
def list_orders():
    stub = get_grpc_stub()
    response = stub.ListOrders(food_ordering_pb2.ListOrdersRequest())
    orders = []
    for order in response.orders:
        items = [{'id': item.id, 'name': item.name, 'price': item.price} for item in order.items]
        orders.append({'order_id': order.order_id, 'total_price': order.total_price, 'items': items})
    return jsonify(orders)

if __name__ == '__main__':
    app.run(debug=True)
