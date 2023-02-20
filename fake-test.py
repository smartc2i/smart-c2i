import random
from django.contrib.auth.models import User
from django.utils import timezone
from faker import Faker

from myapp.models import Customer, Product, Sale, Cashier, Order, Admin, Cart, OrderItem, CATEGORY

fake = Faker()

# Create a few users
for i in range(5):
    username = f'user{i}'
    email = f'{username}@example.com'
    password = 'password'
    user = User.objects.create_user(username=username, email=email, password=password)

    # Create a customer for each user
    customer = Customer.objects.create(
        user=user,
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        boarding_pass=fake.uuid4(),
        email=email,
    )

    # Create a few products
    for j in range(3):
        product = Product.objects.create(
            reference=fake.uuid4(),
            name=fake.word(),
            category=random.choice(CATEGORY)[0],
            description=fake.sentence(),
            price=random.randint(10, 1000),
            stock=random.randint(1, 100),
            volume=random.randint(100, 1000),
        )

        # Create a few sales
        for k in range(2):
            sale = Sale.objects.create(
                customer=customer,
                product=product,
                quantity=random.randint(1, 5),
                total_price=random.randint(10, 1000),
                sale_date=timezone.now(),
            )

    # Create a cashier for each user
    cashier = Cashier.objects.create(
        user=user,
        first_name=fake.first_name(),
        last_name=fake.last_name(),
    )

    # Create an order for each user
    order = Order.objects.create(
        customer_name=fake.name(),
        customer_email=email,
        order_total=random.randint(10, 1000),
        order_status=random.choice(['New', 'In Progress', 'Shipped']),
    )

    # Create a few order items
    for l in range(3):
        product = Product.objects.create(
            reference=fake.uuid4(),
            name=fake.word(),
            category=random.choice(CATEGORY)[0],
            description=fake.sentence(),
            price=random.randint(10, 1000),
            stock=random.randint(1, 100),
            volume=random.randint(100, 1000),
        )
        OrderItem.objects.create(
            product=product,
            user=user,
            quantity=random.randint(1, 5),
        )

    # Create a few carts
    for m in range(3):
        product = Product.objects.create(
            reference=fake.uuid4(),
            name=fake.word(),
            category=random.choice(CATEGORY)[0],
            description=fake.sentence(),
            price=random.randint(10, 1000),
            stock=random.randint(1, 100),
            volume=random.randint(100, 1000),
        )
        Cart.objects.create(
            product=product,
            quantity=random.randint(1, 5),
            price=product.price,
        )

# Create an admin
admin = Admin.objects.create(
    first_name=fake.first_name(),
    last_name=fake.last_name(),
    username='admin',
    password='admin',
)
