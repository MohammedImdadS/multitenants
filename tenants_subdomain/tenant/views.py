from django.shortcuts import render

from .models import Member
from .utilities import get_tanant

def our_tenant(request):
    tenant = get_tanant(request)
    members = Member.objects.filter(tenant = tenant)
    return render(request, 'tenant/our_tenant.html', {'tenant': tenant, 'members': members})
