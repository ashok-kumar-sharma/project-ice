from django.shortcuts import render


def handler400(request,exception):
    return render(request,'400.html',{'path':request.path},status=400)


def handler403(request,exception):
    return render(request,'403.html',{'path':request.path},status=403)


def handler404(request,exception):
    return render(request,'404.html',{'path':request.path,'exception':exception},status=404)


def handler500(request):
    return render(request,'500.html',status=500)