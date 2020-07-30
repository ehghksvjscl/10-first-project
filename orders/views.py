import  json

from django.http    import JsonResponse
from django.views   import View

from products.models    import Product
from orders.models      import Order,OrderStatus,OrderItem
from users.utils        import login_decorator

class CartAddView(View):
    @login_decorator
    def post(self,request):
        data = json.loads(request.body)
        try:
            # data = {}
            # data["product_id"] = 2
            product_id = data['product_id']
            user_id = request.user.id
            try:
                order = Order.objects.get(user_id=user_id,order_status_id=1)
            except Order.DoesNotExist:
                order = Order.objects.create(
                    user_id  = user_id,
                    order_status_id  = 1
                )
            try:
                order_item = OrderItem.objects.get(order_id=order.id,product_id=data['product_id']) 
                order_item.quantity += 1
                order_item.save()
        
                price_orginal = 0
                price_sale = 0
                product = Product.objects.prefetch_related("product_detail").get(id=data['product_id'])
                price_orginal += product.product_detail.price*order_item.quantity
                price_sale += product.product_detail.price_sale*order_item.quantity

            except OrderItem.DoesNotExist:
                order_item = OrderItem.objects.create (
                    order_id = order.id,
                    product_id = data['product_id'],
                    quantity = 1,
                )
                price_orginal = 0
                price_sale = 0
                product = Product.objects.prefetch_related("product_detail").get(id=data['product_id'])
                price_orginal += product.product_detail.price*order_item.quantity
                price_sale += product.product_detail.price_sale*order_item.quantity
                print(price_orginal,price_sale)
            return JsonResponse({'quantity':order_item.quantity,"price":price_orginal,"price_sale":price_sale}, status=200)
        except KeyError:
            return JsonResponse({'message': "Invalid key"}, status=400)

class CartMinusView(View):
    @login_decorator
    def post(self,request):
        data = json.loads(request.body)
        try:
            product_id = data['product_id']
            user_id = request.user.id
            try:
                order = Order.objects.get(user_id=user_id,order_status_id=1)
            except Order.DoesNotExist:
                order = Order.objects.create(
                    user_id  = user_id,
                    order_status_id  = 1
                )
            try:
                order_item = OrderItem.objects.get(order_id=order.id,product_id=data['product_id']) 
                if order_item.quantity <= 1:
                    order_item.quantity=1
                else:
                    order_item.quantity -=1

                order_item.save()

                price_orginal = 0
                price_sale = 0
                product = Product.objects.prefetch_related("product_detail").get(id=data['product_id'])
                price_orginal += product.product_detail.price*order_item.quantity
                price_sale += product.product_detail.price_sale*order_item.quantity

            except OrderItem.DoesNotExist:
                order_item = OrderItem.objects.create (
                    order_id = order.id,
                    product_id = data['product_id'],
                    quantity = 1,
                )

                price_orginal = 0
                price_sale = 0
                product = Product.objects.prefetch_related("product_detail").get(id=data['product_id'])
                price_orginal += product.product_detail.price*order_item.quantity
                price_sale += product.product_detail.price_sale*order_item.quantity
            return JsonResponse({'quantity':order_item.quantity,"price":price_orginal,"price_sale":price_sale}, status=200)
        except KeyError:
            return JsonResponse({'message': "Invalid key"}, status=400)

class CartDeletView(View):
    @login_decorator
    def post(self,request):
        data = json.loads(request.body)
        try:
            product_id = data['product_id']
            user_id = request.user.id
            try:
                order = Order.objects.get(user_id=user_id,order_status_id=1)
                order_item = OrderItem.objects.get(order_id=order.id,product_id=data['product_id']) 
                order_item.delete()
            except OrderItem.DoesNotExist:
                return JsonResponse({'message': "Don't find Products"}, status=400)

            return JsonResponse({'message':"SUCCESS"}, status=200)
        except KeyError:
            return JsonResponse({'message': "Invalid key"}, status=400)

class CartList(View):
    @login_decorator
    def post(self,request):
        try:
            user_id    = request.user.id
            # user_id = 5
            order = Order.objects.get(
                user_id = user_id,
                order_status_id = 1
            )
            product_list  = OrderItem.objects.prefetch_related("product","product__product_detail").filter(order_id=order.id)
            datas = []
            for item in product_list:
                data_dic ={
                    'id'           :item.product.id,
                    'image_url'     : item.product.main_image_url,
                    'name'         : item.product.name,
                    'quantity'         : item.quantity,
                    "price"       : int(item.product.product_detail.price)*int(item.quantity),
                    "price_sale"     : int(item.product.product_detail.price_sale)*int(item.quantity)
                }
                print(data_dic)
                print(int(item.product.product_detail.price_sale)*int(item.quantity))
                datas.append(data_dic)

            return JsonResponse({'data':datas}, status=200)

        except KeyError:
            return JsonResponse({'message': 'Invalid key'}, status=400)