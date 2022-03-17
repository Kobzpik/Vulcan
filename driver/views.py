from lib2to3.pgen2 import driver
from django.shortcuts import render,get_object_or_404
from pandas import PeriodIndex
from officer.models import Fine
from authenticate.models import Driver, Officer,User
from officer.models import Fine,Offence
from .models import Payment
import stripe
from django.conf import settings
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
stripe.api_key = settings.STRIPE_PRIVATE_KEY
YOUR_DOMAIN = 'http://127.0.0.1:8000'




def index(request):
        return render(request, 'driver/index_driver.htm')
        
def fine_list(request,pk):
        fined = Fine.objects.filter(driver_id = pk)     
        finedh = Driver.objects.get(user_id = pk)
        return render(request, 'driver/fines_list.htm',{'fined': fined,'finedh':finedh})

#payment gateway view 
#home view
def home(request,pk):
    fined = Fine.objects.filter(driver_id = pk)     
    finedh = Driver.objects.get(user_id = pk)
    finedm = Offence.objects.all()
    print(Offence.objects.get(id = pk))
    return render(request,'driver/checkout.htm',{'fined': fined,'finedh':finedh,'finedm':finedm})

#success view
def success(request):
    return render(request,'driver/success.htm')
    
#cancel view
def cancel(request):
    return render(request,'driver/cancel.htm')

@csrf_exempt
def create_checkout_session(request):
    checkid=request.user.id
    print(checkid)
    #amount_id = self.kwargs['pk']
    amonutd = Offence.objects.get(id=checkid)
    name=amonutd.offence
    amount2=amonutd.amount
    multyamount = amount2*100

    
    
    payment=Payment(driver=request.user,amount=amount2)
    payment.save()
    #rint(Offence.amount(id=2))
    session = stripe.checkout.Session.create(
    #client_reference_id=request.user.id if request.user.is_authenticated else None,
    payment_method_types=['card'],
    line_items=[{
      'price_data': {
        'currency': 'lkr',
        'product_data': {
          'name': name,
        },
        'unit_amount': multyamount,
      },
      'quantity': 1,
    }],
    metadata={
        "order_id":Payment.id
    },
    mode='payment',
    
    success_url=YOUR_DOMAIN + '/driver/success/',
    cancel_url=YOUR_DOMAIN + '/driver/cancel/',
    )
    print(session)
    #ID=order.id
    #order= Order.objects.filter(id=ID).update(email=customer_email,amount=price,paid=True,description=sessionID)
    #order.save()
    return JsonResponse({'id': session.id})

@csrf_exempt
def webhook(request):
    print("Webhook")
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        print("Payment was successful.")
        #session = event['data']['object']
         #creating order
       # customer_email = session["customer_details"]["email"]
       # price = session["amount_total"] /100
       # sessionID = session["id"]
       # ID=session["metadata"]["order_id"]
       # Order.objects.filter(id=ID).update(email=customer_email,amount=price,paid=True,description=sessionID)

    return HttpResponse(status=200)
