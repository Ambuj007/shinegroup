from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm, StockForm, LoginForm, DemandForm
from django.core.mail import send_mail
from django.conf import settings
from .models import Stock, Notice, Demand
from django.template.loader import get_template
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic import CreateView, FormView, ListView
from django.views import View
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import (
    authenticate,
    login,
    logout
)
from django.contrib.auth.decorators import login_required
from django.utils.http import is_safe_url
import xlwt




# Create your views here.
#DELETE View
class DeleteItem(DeleteView):
    model = Stock
    template_name = 'shop/delete_item.html'
    success_url = '../inventory_detail'


#Item Detail List View

class ItemListView(ListView):
    template_name='shop/item_detail.html'
    model = Stock
    context_object_name = 'object'


class NoticeView(CreateView):
    template_name='shop/notice.html'
    model = Notice
    fields = ['notice']
    success_url = '/'


def demand_view(request):
    form = DemandForm()
    if request.POST:
        form = DemandForm(request.POST)
        if form.is_valid():
            item = form.cleaned_data['item'] 
            quantity = form.cleaned_data['quantity']  
            context = {
            'item' : item,
            'quantity' : quantity
            }
            Demand.objects.create(**context)
            messages.success(request, 'Note kar liya hai, bagal me check kar lo')
            form = DemandForm()
    demands_all = Demand.objects.all()
    return render(request, 'shop/demand.html', {'form':form, 'object':demands_all})


def demand_download_view(request):
    response = HttpResponse(content_type = 'application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="On_Demand.xls"'
    
    wbook = xlwt.Workbook(encoding = 'utf-8')
    wbook_sheet = wbook.add_sheet('On Demand requirements')

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold=True

    columns = ['SL No.','Item', 'Quantity',]

    for col_num in range(len(columns)):
        wbook_sheet.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()


    object = Demand.objects.all().values_list('item', 'quantity')
    
    for row in object:
        row_num += 1
        new_row = [
            row_num,
            row[0],
            row[1],
        ]
        for col_num in range(len(new_row)):
            wbook_sheet.write(row_num, col_num, new_row[col_num], font_style)

    wbook.save(response)
    
    return response


#Update View
class ItemUpdateView(UpdateView):
    template_name='shop/item_update.html'
    model = Stock
    fields = ['category','brand','item','item_type','item_specification','model_no','purchase_price','selling_price']
    success_url = '../inventory_detail'


def index(request):
    object = Notice.objects.all()
    context = {
        'object' : object
    }
    return render(request, 'shop/home.html', context)


def services(request):
    return render(request, 'shop/services.html')

def thank_you(request):
    return render(request, 'shop/thank_you.html')

def about(request):
    return render(request, 'shop/about.html')

def enquiry(request):
    context= {}
    if request.GET:
        search_item = request.GET['search_item']
        result = Stock.objects.filter(
            Q(category__icontains=search_item) |
            Q(brand__icontains=search_item) |
            Q(item__icontains=search_item) |
            Q(Model_No__icontains=search_item)
        )
        context = {
            'search_item' : search_item,
            'object' : result
        }
    return render(request, 'shop/enquiry.html',context)


    #return render(request, 'shop/enquiry.html')

def search(request):
    if request.GET:
        search_item = request.GET['search_item']
        result = Stock.objects.filter(
            Q(category__icontains=search_item) |
            Q(brand__icontains=search_item) |
            Q(item__icontains=search_item) |
            Q(Model_No__icontains=search_item)
        )
        context = {
            'search_item' : search_item,
            'object' : result
        }
        return render(request, 'shop/search.html',context)
    else:
        return redirect('detail')

class LoginView(FormView):
    form_class = LoginForm
    success_url = "/"
    template_name = "shop/login.html"

    def form_valid(self, form):
        request = self.request
        next = request.GET.get("next")
        next_post = request.POST.get("next")
        redirect_path = next or next_post or None
        username= form.cleaned_data.get("username")
        password= form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login (request, user)
            #del request.session
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect("/")
        return super(LoginView, self).form_invalid(form)


def logout_view(request):
    logout(request)
    return redirect("/")


def contact(request):
    context = locals()
    form = ContactForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['name']
        subject = "%s %s" %('This email is send from Your Website ',  form.cleaned_data['subject'])
        sender = form.cleaned_data['sender']
        phone = form.cleaned_data['phone']
        message =form.cleaned_data['message']
        reciever = [settings.EMAIL_HOST_USER]

        context = {
            'name' : name,
            'subject' : subject,
            'sender' : sender,
            'phone' : phone,
            'message' : message,
            'reciever' : reciever
        }

        contact_message = get_template('shop/email.txt').render(context)
        send_mail(
            subject,
            contact_message,
            sender,
            reciever,
            fail_silently = True

        )
        return redirect('shop:thank_you')
    return render(request, 'shop/contact.html',  {'form':form})


def inventory_management(request):
    new_model = {}
    form = StockForm(request.POST or None)
    if form.is_valid():
        category_m = form.cleaned_data['item_class']
        brand_m = form.cleaned_data['brand']
        model_no_m = form.cleaned_data['model_no']
        purchase_price_m = form.cleaned_data['purchase_price']
        selling_price_m = form.cleaned_data['selling_price']
        item_m =""
        type_m= ""
        specification_m =  ""

        if form.cleaned_data['item_class'] == "CCTV":
            item_m = form.cleaned_data['cctv']
            if form.cleaned_data['cctv'] == "Camera":
                type_m = form.cleaned_data['camera']
                specification_m = form.cleaned_data['camera_spec']
            elif form.cleaned_data['cctv'] == "DVR" or form.cleaned_data['cctv'] == "SMPS":
                type_m = form.cleaned_data['dvr_smps']


        elif form.cleaned_data['item_class'] == "Computer Peripherals":
            item_m = form.cleaned_data['comp_peripherals']
            if form.cleaned_data['comp_peripherals'] == "Keyboarad" or form.cleaned_data['comp_peripherals'] == "Mouse":
                specification_m = form.cleaned_data['KB_MOUSE']
            elif form.cleaned_data['comp_peripherals'] == "RAM" or form.cleaned_data['comp_peripherals'] == "GC":
                specification_m = form.cleaned_data['small_storage']


        elif form.cleaned_data['item_class'] == "Storage":
            type_m = form.cleaned_data['storage']
            specification_m = form.cleaned_data['storage_spec']


        elif form.cleaned_data['item_class'] == "Printer":
            type_m = form.cleaned_data['printer']


        elif form.cleaned_data['item_class'] == "Ups":
            type_m = form.cleaned_data['ups']
            

        elif form.cleaned_data['item_class'] == "Speakers":
            type_m = form.cleaned_data['speaker']
            specification_m = form.cleaned_data['speaker_type']


        elif form.cleaned_data['item_class'] == "Antivirus":
            type_m = form.cleaned_data['antivirus']
            specification_m = form.cleaned_data['user']


        else:
            type_m = form.cleaned_data['item_type']
            specification_m = form.cleaned_data['item_specification']



        new_model = {
                'category' : category_m,
                'brand' : brand_m,
                'item' : item_m,
                'item_type' : type_m,
                'item_specification' : specification_m,
                'model_no' : model_no_m,
                'purchase_price' : purchase_price_m,
                'selling_price' :selling_price_m

        }

        Stock.objects.create(**new_model)
        form = StockForm()

    return render(request, 'shop/inventory_management.html', {'form':form})

