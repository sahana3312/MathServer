from django.shortcuts import render
def gst_calculate(request):
    price = int(request.POST.get('price', '0'))
    gst = int(request.POST.get('gst', '1'))
    total_amount=price+(price*gst/100) if request.method == 'POST' else 0
    print("Price=",price)
    print("GST=",gst)
    print("Total Amount=",total_amount)
    return render(request, 'mathapp/math.html', {'Price': price, 'GST': gst, 'Total Amount': total_amount})
