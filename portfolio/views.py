from django.shortcuts import render
from django.views.generic.base import View

from .models import side_bar, intro, services, portfolio, clients, about_me, contact_me, footer

class base(View):
    def get(self, request):
        sidebar = side_bar.objects.all()
        int = intro.objects.all()
        serv = services.objects.all()
        portf = portfolio.objects.all()
        cl = clients.objects.all()
        about = about_me.objects.all()
        contact = contact_me.objects.all()
        foot = footer.objects.all()

        return render(request, "portfolio/index.html", {'bar': sidebar,
                                                        'intro': int,
                                                        'services': serv,
                                                        'portfolio': portf,
                                                        'clients': cl,
                                                        'about_me': about,
                                                        'contact_me': contact,
                                                        'footer': foot
                                                        })
