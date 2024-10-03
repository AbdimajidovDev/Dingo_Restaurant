from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, View

from blogapp.models import Comments
from dingoapp.models import *
from dingoapp.forms import *


def index(request):
    exfoods = FoodModel.objects.filter(exclusive=True)[:3]
    category = CategoryModel.objects.all()
    cat = request.GET.get('cat')
    chefs = ChefModel.objects.filter(level__ch_level='Chef Master')[:3]
    form = BookingForm()
    best = Comments.objects.filter(best_comment=True)

    if cat is None:
        cat = 'Special'

    foods = FoodModel.objects.filter(category__category_name=cat)[:6]
    tags = FoodModel.objects.filter(tags__tag='Food News')[:3]

    if request.method == 'POST':
        form = BookingForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'home_menu': 'home_menu',
        'foods3': foods[:3],
        'foods6': foods[3:6],
        'exfoods': exfoods[:3],
        'categories': category,
        'cat': cat,
        'chefs': chefs,
        'form': form,
        'tags': tags,
        'best': best,
    }
    return render(request, 'index.html', context)


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        my_context = super().get_context_data(**kwargs)
        my_context['chefs'] = ChefModel.objects.filter(level__ch_level='Chef Master')[:3]
        return my_context


class MenuView(TemplateView):
    template_name = 'food_menu.html'

    def get_context_data(self, **kwargs):
        cat = self.request.GET.get('cat')
        if cat is None:
            cat = 'Special'

        foods = FoodModel.objects.filter(category__category_name=cat)[:6]
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryModel.objects.all()
        context['foods3'] = foods[:3]
        context['foods6'] = foods[3:6]
        return context


class ChefsView(TemplateView):
    template_name = 'chefs.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['chefs'] = ChefModel.objects.all()
        return context


class ElementsView(TemplateView):
    template_name = 'elements.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


class LoginPageView(View):
    template_name = 'login.html'
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, {'form': form, 'message': message})

    def post(self, request):
        request.user.is_authenticated
        form = self.form_class(request.POST)
        user = authenticate(
            username=self.request.POST.get('username'),
            password=self.request.POST.get('password'),
            )
        if user is not None:
            login(request, user)
            return redirect('home')

        message = 'Login failed!'
        return render(request, self.template_name, {'form': form, 'message': message})


# def login_user(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request,
#                             username=username,
#                             password=password)
#         if user is not None:
#                 login(request, user)
#                 return redirect('home')
#         else:
#             context = {'form': LoginForm,
#                        'error': 'Error login'}
#             return render(request, 'login.html', context)
#     else:
#         context = {'form': LoginForm}
#         return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('login')
