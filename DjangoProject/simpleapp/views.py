from django.views.generic import View, ListView, DetailView  # импортируем класс получения деталей объекта
from django.shortcuts import render
from django.core.paginator import Paginator  # импортируем класс, позволяющий удобно осуществлять постраничный вывод
from datetime import datetime

from .models import Product


class ProductsList(ListView):
    model = Product  # указываем модель, объекты которой мы будем выводить
    template_name = 'products.html'  # указываем имя шаблона, в котором будет лежать html, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'products'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через html-шаблон
    queryset = Product.objects.order_by('-id')

    # # метод get_context_data нужен нам для того, чтобы мы могли передать переменные в шаблон. В возвращаемом словаре context будут храниться все переменные. Ключи этого словари и есть переменные, к которым мы сможем потом обратиться через шаблон
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
    #     context['value1'] = None  # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
    #     return context

    def get(self, request):
        products = Product.objects.order_by('-price')
        p = Paginator(products, 1)  # создаём объект класса пагинатор, передаём ему список наших товаров и их количество для одной страницы

        products = p.get_page(request.GET.get('page', 1))  # берём номер страницы из get-запроса. Если ничего не передали, будем показывать первую страницу.
        # теперь вместо всех объектах в списке тsоваров хранится только нужная нам страница с товарами

        data = {
            'products': products,
        }
        return render(request, 'products.html', data)


class ProductDetail(DetailView):
    model = Product  # модель всё та же, но мы хотим получать детали
    # конкретно отдельного товара
    template_name = 'product.html'  # название шаблона будет product.html
    context_object_name = 'product'  # название объекта. в нём будет


# В отличиe от дженериков, которые мы уже знаем, код здесь надо писать
# самому, переопределяя типы запросов (например, get- или post-, вспоминаем
# реквесты из 19-го модуля)
class Products(View):
    model = Product
    template_name = 'products_list.html'
    context_object_name = 'products_list'
    ordering = ['-price']
    paginate_by = 1  # поставим постраничный вывод в один элемент

    def get(self, request):
        products = Product.objects.order_by('-price')
        p = Paginator(products, 1)  # создаём объект класса пагинатор, передаём ему список наших товаров и их количество для одной страницы

        products = p.get_page(request.GET.get('page', 1))  # берём номер страницы из get-запроса. Если ничего не передали, будем показывать первую страницу.
        # теперь вместо всех объектах в списке товаров хранится только нужная нам страница с товарами

        data = {
            'products_list': products,
        }
        return render(request, 'products_list.html', data)
