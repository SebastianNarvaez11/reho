from .models import Business

def ctx_dict(request):
    return {'BUSINESS':Business.objects.get()}
