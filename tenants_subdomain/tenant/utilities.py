from .models import Tenant

def get_hostname(request):
    print(request.get_host)
    return request.get_host().split(':')[0].lower()

def get_tanant(request):
    hostname = get_hostname(request)
    subdomain = hostname.split('.')[0]
    return Tenant.objects.filter(subdomain = subdomain).first()