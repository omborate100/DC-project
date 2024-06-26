# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import food_ordering_pb2 as food__ordering__pb2


class FoodOrderingStub(object):
    """The food ordering service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetMenu = channel.unary_unary(
                '/foodordering.FoodOrdering/GetMenu',
                request_serializer=food__ordering__pb2.GetMenuRequest.SerializeToString,
                response_deserializer=food__ordering__pb2.MenuResponse.FromString,
                )
        self.PlaceOrder = channel.unary_unary(
                '/foodordering.FoodOrdering/PlaceOrder',
                request_serializer=food__ordering__pb2.PlaceOrderRequest.SerializeToString,
                response_deserializer=food__ordering__pb2.OrderResponse.FromString,
                )
        self.ListOrders = channel.unary_unary(
                '/foodordering.FoodOrdering/ListOrders',
                request_serializer=food__ordering__pb2.ListOrdersRequest.SerializeToString,
                response_deserializer=food__ordering__pb2.ListOrdersResponse.FromString,
                )


class FoodOrderingServicer(object):
    """The food ordering service definition.
    """

    def GetMenu(self, request, context):
        """Retrieves the menu
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PlaceOrder(self, request, context):
        """Places an order
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListOrders(self, request, context):
        """Lists all orders
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FoodOrderingServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetMenu': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMenu,
                    request_deserializer=food__ordering__pb2.GetMenuRequest.FromString,
                    response_serializer=food__ordering__pb2.MenuResponse.SerializeToString,
            ),
            'PlaceOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.PlaceOrder,
                    request_deserializer=food__ordering__pb2.PlaceOrderRequest.FromString,
                    response_serializer=food__ordering__pb2.OrderResponse.SerializeToString,
            ),
            'ListOrders': grpc.unary_unary_rpc_method_handler(
                    servicer.ListOrders,
                    request_deserializer=food__ordering__pb2.ListOrdersRequest.FromString,
                    response_serializer=food__ordering__pb2.ListOrdersResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'foodordering.FoodOrdering', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FoodOrdering(object):
    """The food ordering service definition.
    """

    @staticmethod
    def GetMenu(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/foodordering.FoodOrdering/GetMenu',
            food__ordering__pb2.GetMenuRequest.SerializeToString,
            food__ordering__pb2.MenuResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PlaceOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/foodordering.FoodOrdering/PlaceOrder',
            food__ordering__pb2.PlaceOrderRequest.SerializeToString,
            food__ordering__pb2.OrderResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListOrders(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/foodordering.FoodOrdering/ListOrders',
            food__ordering__pb2.ListOrdersRequest.SerializeToString,
            food__ordering__pb2.ListOrdersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
