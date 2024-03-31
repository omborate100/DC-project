from concurrent import futures
import grpc
import food_ordering_pb2
import food_ordering_pb2_grpc
import uuid

# Example data
menu_items = [
    food_ordering_pb2.MenuItem(id="1", name="Pizza", price=90.99),
    food_ordering_pb2.MenuItem(id="2", name="Burger", price=88.99),
    food_ordering_pb2.MenuItem(id="3", name="Salad", price=100),
     food_ordering_pb2.MenuItem(id="4", name="Chicken", price=111),
]

orders = []

class FoodOrderingService(food_ordering_pb2_grpc.FoodOrderingServicer):

    def GetMenu(self, request, context):
        return food_ordering_pb2.MenuResponse(items=menu_items)

    def PlaceOrder(self, request, context):
        ordered_items = [item for item in menu_items if item.id in request.item_ids]
        total_price = sum(item.price for item in ordered_items)
        order_id = str(uuid.uuid4())
        orders.append(food_ordering_pb2.Order(order_id=order_id, items=ordered_items, total_price=total_price))
        return food_ordering_pb2.OrderResponse(order_id=order_id, total_price=total_price)

    def ListOrders(self, request, context):
        return food_ordering_pb2.ListOrdersResponse(orders=orders)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    food_ordering_pb2_grpc.add_FoodOrderingServicer_to_server(FoodOrderingService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
