import grpc
import food_ordering_pb2
import food_ordering_pb2_grpc

def get_menu(stub):
    response = stub.GetMenu(food_ordering_pb2.GetMenuRequest())
    for item in response.items:
        print(f"ID: {item.id}, Name: {item.name}, Price: {item.price}")

def place_order(stub):
    order_response = stub.PlaceOrder(food_ordering_pb2.PlaceOrderRequest(item_ids=["1", "2"]))
    print(f"Order ID: {order_response.order_id}, Total Price: {order_response.total_price}")

def list_orders(stub):
    response = stub.ListOrders(food_ordering_pb2.ListOrdersRequest())
    for order in response.orders:
        print(f"Order ID: {order.order_id}, Total Price: {order.total_price}")
        for item in order.items:
            print(f" - Item Name: {item.name}, Price: {item.price}")

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = food_ordering_pb2_grpc.FoodOrderingStub(channel)
        print("Fetching Menu...")
        get_menu(stub)
        print("\nPlacing an Order...")
        place_order(stub)
        print("\nListing All Orders...")
        list_orders(stub)

if __name__ == '__main__':
    run()
