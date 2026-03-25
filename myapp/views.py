from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q, Sum, Count
from myapp.models import Client


def index(request):
    total_clients = Client.objects.count()
    active_clients = Client.objects.filter(status='active').count()
    completed_projects = Client.objects.filter(status='completed').count()
    total_revenue = Client.objects.aggregate(total=Sum('budget'))['total'] or 0
    recent_clients = Client.objects.order_by('-date')[:5]
    return render(request, 'index.html', {
        'total_clients': total_clients,
        'active_clients': active_clients,
        'completed_projects': completed_projects,
        'total_revenue': total_revenue,
        'recent_clients': recent_clients,
    })


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    return render(request, 'contact.html')


def clients(request):
    all_clients = Client.objects.all().order_by('-date')
    return render(request, 'clients.html', {'all_clients': all_clients})


def client_add(request):
    if request.method == "POST":
        company_name = request.POST.get("company_name")
        website = request.POST.get("website")
        package = request.POST.get("package")
        budget = request.POST.get("budget")
        status = request.POST.get("status")

        Client.objects.create(
            company_name=company_name,
            website=website,
            package=package,
            budget=budget,
            status=status,
        )
        return redirect("/clients/")
    else:
        return render(request, "client_form.html")


def client_edit(request, id):
    client = get_object_or_404(Client, id=id)
    if request.method == "POST":
        client.company_name = request.POST.get("company_name")
        client.website = request.POST.get("website")
        client.package = request.POST.get("package")
        client.budget = request.POST.get("budget")
        client.status = request.POST.get("status")
        client.save()
        return redirect("/clients/")
    else:
        return render(request, "client_edit.html", {"client": client})


def client_delete(request, id):
    client = get_object_or_404(Client, id=id)
    client.delete()
    return redirect("/clients/")


def client_search(request):
    query_name = request.GET.get("query_name", "").strip()
    query_package = request.GET.get("query_package", "").strip()
    query_status = request.GET.get("query_status", "").strip()

    results = Client.objects.all()

    if query_name:
        results = results.filter(
            Q(company_name__icontains=query_name) | Q(website__icontains=query_name)
        )

    if query_package:
        results = results.filter(package=query_package)

    if query_status:
        results = results.filter(status=query_status)

    results = results.order_by('-date')

    return render(request, "clients.html", {
        "all_clients": results,
        "query_name": query_name,
        "query_package": query_package,
        "query_status": query_status,
    })
