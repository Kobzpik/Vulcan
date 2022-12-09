from lib2to3.pgen2 import driver
from django.shortcuts import render,get_object_or_404,redirect
from pandas import PeriodIndex
from django.contrib import messages
from officer.models import Fine
from authenticate.models import Driver, Officer,User
from officer.models import Fine,Offence
from .models import Complain, Payment
import stripe
from django.conf import settings
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
stripe.api_key = settings.STRIPE_PRIVATE_KEY
YOUR_DOMAIN = 'http://127.0.0.1:8000'
from .forms import ComplainForm




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

    
  

    
    paymentd = Payment.objects.filter(driver_id = pk )

    finedm = Offence.objects.all()

    #test
    


    
    return render(request,'driver/checkout.htm',{'fined': fined,'finedh':finedh,'finedm':finedm,'paymentd':paymentd})

#success view

def success(request):
    return render(request,'driver/success.htm')
    
#cancel view
def cancel(request):
    return render(request,'driver/cancel.htm')

@csrf_exempt
def create_checkout_session(request):

    #payment model
    checkid=request.user.id
    amonutd = Offence.objects.get(id=checkid)
    name=amonutd.offence
   
    
    

    #payment model
    fine = Fine.objects.get(driver_id=checkid)
   
    #stripe view
    fineo=fine.Nature_of_Offence_id
    offenced=Offence.objects.get(id=fineo)
    finea=offenced.amount
    name=offenced.offence
    multyamount = finea*100

    #testing
    #print("+++++++++++++++++++++")

 
    #make payment model
    payment=Payment(driver= request.user,fine=fine,amount=0,paid="False")
    payment.save()
    #print(Offence.amount(id=2))
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
        "order_id":payment.id
        
    },
    mode='payment',
   
    
    success_url= 'http://f127-123-231-85-255.ngrok.io/driver/success/',
    cancel_url='http://f127-123-231-85-255.ngrok.io/driver/cancel/',
    )
    

    #testing
    #print("+++++++++++++++++++++")
    

    #payment=Payment.objects.filter(id=ID).update(driver=request.user,fine=fine,amount=finea,paid=True)
    #print(session)
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
        
        #sessionID = session["id"]
        #ID=session["metadata"]["order_id"]
       # Order.objects.filter(id=ID).update(email=customer_email,amount=price,paid=True,description=sessionID)
        
        session = event['data']['object']
        price = session["amount_total"] /100
        ID=session["metadata"]["order_id"]
        Payment.objects.filter(id=ID).update(amount=price,paid=True)
       
       

    return HttpResponse(status=200)

#complain 
def complain_view(request):  
    form = ComplainForm()

    if request.method == 'POST':
        form = ComplainForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"successful make complain")
            return redirect('complain')
             
        else:
            messages.warning(request,"Invalid Data Enter")
    #console log
    #logger = logging.getLogger()
    #logger.propogate = True
    #logger.error(form)
    return render(request, 'driver/complain.htm', {'form': form})


#def complain_update_view(request, pk):
    fine = get_object_or_404(Complain, pk=pk)
    form = ComplainForm(instance=fine)
    if request.method == 'POST':
        form = ComplainForm(request.POST, instance=fine)
        if form.is_valid():
            form.save()
            return redirect('fine_change', pk=pk)
              
    return render(request, 'driver/complain.htm', {'form': form})


