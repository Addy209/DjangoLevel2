from django.shortcuts import render
from django.http import JsonResponse
from Mainpage.models import CustomerDetails, Menu, Sales
from Mainpage.forms import UserInfoForm, SalesRecord
from django.core.serializers.json import DjangoJSONEncoder
import logging
import json

logging.basicConfig(filename="./logs/Myapp.logs", format="%(asctime)s %(message)s", filemode='w')
logger = logging.getLogger()
myUser = {
    'name': '',
    'phone': 0
}
id = int(Sales.objects.values_list('id', flat=True).order_by('-id')[0])
print(id)
# Create your views here


def index(request):
    global myUser
    page = 'Mainpage/index.html'
    userform = UserInfoForm()

    dictonary = {
        'value': 'Please Provide Customer Details!',
        'userform': userform,
        'Customer': "Order here",
        'Name': 'This Project is Created by Aditya Kumar',
        'find': 'Reach out to me at  adikumar209@gmail.com',
    }
    if request.method == "POST":
        form = UserInfoForm(request.POST)
        if form.is_valid():
            usrName = form.cleaned_data['name']
            usrPhone = form.cleaned_data['phone']
            form.save(commit=True)
            myUser['name'] = usrName
            myUser['phone'] = usrPhone
            cusine = 'Hello '+myUser['name']
            dictonary['cusine'] = cusine
            return render(request, page, context=dictonary)
        else:
            phone = request.POST.get('phone')
            name = CustomerDetails.objects.values_list('name', flat=True).filter(phone=phone)
            logger.warning(name[0])
            myUser['name'] = name[0]
            myUser['phone'] = phone
            cusine = 'Hello ' + myUser['name']
            dictonary['cusine'] = cusine

            return render(request, page, context=dictonary)
    return render(request, page, context=dictonary)


def FoodSearch(request):
    print("I am here")
    global valid
    if request.method == 'GET':
        searchValue = request.GET['search_food']
        name = []
        try:
            dbResp = Menu.objects.filter(dishname__istartswith=searchValue).values()
            print(dbResp)
            for i in range(0, len(dbResp)):
                print(dbResp[i].dishname)
                name.append(dbResp[i].dishname)
            if len(name) > 0:
                print("Value exist")
                print(type(dbResp.values()))
        except e:
            print("Value Doesn't exist")
        finally:
            data = {
                'name': json.dumps(list(dbResp))
            }
            return JsonResponse(data)
    else:
        print("Fill in customer Details first")


def saveSales(request):
    print('In SaveSales')
    global myUser, id
    if request.method == 'POST':
        print(1)
        if myUser['phone'] and myUser['name']:
            print(2)
            phone = int(myUser['phone'])
            print(phone)
            name = myUser['name']
            print(name)
            order = request.POST['order']
            print(order)
            amount = int(request.POST['amount'])
            print(amount)
            id = id+1
            print(id)
            sale = Sales(id, name, phone, order, amount)
            print(sale)
            sale.save()
            myUser['phone'] = 0
            myUser['name'] = ''
            return JsonResponse({'resp': 'Ok'})


def RecordGenrator(request):
    print('I am here')
    if request.method == 'POST':
        startdate = request.POST['sdate']
        enddate = request.POST['edate']
        try:
            records = Sales.objects.filter(date__range=(startdate, enddate)).values()
            for i in range(0, len(records)):
                records[i]['date'] = str(records[i]['date'])
        except e:
            print("No data Found")
        finally:
            data = {'record': json.dumps(list(records))
                    }
            return JsonResponse(data)
