import json

from django.views import View
from django.http  import JsonResponse

from order.models   import OrderList
from user.models    import User
from user.utils     import authorize

class OrderListView(View):
    @authorize
    def get(self,request):
        user          = request.user
        order_list_id = request.GET.get('order_id', None)
        quantity      = request.GET.get('quantity', 1)

        if order_list_id and quantity:
            order_product          = OrderList.objects.get(id=order_list_id)
            order_product.quantity = quantity
        
        orders = list(User.order)
        order_list        = [OrderList.objects.get(order=order) for order in orders]
        order_products    = []
        total_order_price = 0
        for order in order_list: 
            order_product = OrderList.objects.get(order=order).product
            order_products = [
                {
                    'id'          : order_product.id,
                    'english_name': order_product.english_name,
                    'korean_name' : order_product.korean_name,
                    'sub_category': order_product.sub_category,
                    'price'       : order_product.price
                }
                for order_product in list(OrderList.objects.get(order=order).product)
            ]
            total_order_price += order_product.price * order_product.quantity
        return JsonResponse({'order_list':order_list , 'total_order_price':total_order_price}, status=200)
    