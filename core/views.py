from django.shortcuts import render
from decimal import Decimal

def index(request):
    
    if request.method=="GET":
        return render(request,'index.html')
    
    if request.method=="POST" and request.POST.get('count') and not request.POST.get('weight'):
        request.session['gate']=request.POST.get('gate')
        arr=[]
        for i in range(int(request.POST.get('count'))):
            arr.append(0)
        # response = render(request,'index.html',context={'count':arr,'gate':request.COOKIES.get('gate')})
        # response.set_cookie(key='gate',value=request.POST.get('gate'))
        return render(request,'index.html',context={'count':arr,"gate":request.session['gate']})

    elif request.method=="POST" and request.POST.get('weight'):
        data=request.POST
        gate=request.session.get('gate')
        # gate=request.COOKIES['gate']
        weight=request.POST.getlist('weight')
        value=request.POST.getlist('value')
        sum_of_weight=0
        sum=0
        sum_of_value=0
        for i in range(len(weight)):
            sum_of_value+=int(value[i])
            sum_of_weight+=Decimal(weight[i])
            sum+=Decimal(weight[i]) * int(value[i])
        result=0
        # OR
        if gate=='or':
            if sum>0:
                result = 1

        if gate=='and':
            if sum_of_weight==sum:
                result = 1

        if gate=='nor':
            if sum>0:
                result = 0

        if gate=='nand':
            if sum_of_weight==sum:
                result = 0

        # request.POST['result']=result
        context={
            'count':request.POST.getlist('count'),
            'value':request.POST.getlist('value'),
            'weight':request.POST.getlist('weight'),
            'result':result,
            'gate':gate
        }
        return render(request,'result.html',context=context)