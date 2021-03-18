from simpleapp.models import Product, Category


category1 = Category.objects.create(name='Средства личной гигиены')
category2 = Category.objects.create(name='Игрушкм')
category3 = Category.objects.create(name='Музыкальные инструменты')

product1 = Product.objects.create(name='Зубная щетка', description='Классно чистит зубы', quantity=10, category=category1, price=78.90)
product2 = Product.objects.create(name='Мочалка', description='Очень хорошо моет', quantity=15, category=category1, price=155.50)
product3 = Product.objects.create(name='Солдатик', description='Зеленый солдатик, 10 см', quantity=27, category=category2, price=276.0)
product4 = Product.objects.create(name='Гитара', description='Шестиструнная, акустическая гитара', quantity=3, category=category3, price=3590.0)







Product.objects.all()

category1 = Category.objects.get(id=1)
category1.name = 'Гигиена'
category1.save()

