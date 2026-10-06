from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .models import Food, Order
from .forms import RegisterForm, FoodForm

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import FoodSerializer


# ---------------- REGISTER ----------------

def register(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect('home')

    else:

        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


# ---------------- LOGIN ----------------

def login_user(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('home')

        else:

            return render(
                request,
                'login.html',
                {'error': 'Invalid username or password'}
            )

    return render(request, 'login.html')


# ---------------- LOGOUT ----------------

def logout_user(request):

    logout(request)

    return redirect('login')


# ---------------- HOME ----------------

@login_required
def home(request):

    foods = Food.objects.all()

    return render(
        request,
        'home.html',
        {'foods': foods}
    )


# ---------------- ADD FOOD ----------------

@login_required
def add_food(request):

    if request.method == 'POST':

        form = FoodForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('home')

    else:

        form = FoodForm()

    return render(
        request,
        'add_food.html',
        {'form': form}
    )


# ---------------- EDIT FOOD ----------------

@login_required
def edit_food(request, id):

    food = get_object_or_404(Food, id=id)

    if request.method == 'POST':

        form = FoodForm(
            request.POST,
            instance=food
        )

        if form.is_valid():

            form.save()

            return redirect('home')

    else:

        form = FoodForm(instance=food)

    return render(
        request,
        'edit_food.html',
        {'form': form}
    )


# ---------------- DELETE FOOD ----------------

@login_required
def delete_food(request, id):

    food = get_object_or_404(Food, id=id)

    if request.method == 'POST':

        food.delete()

        return redirect('home')

    return render(
        request,
        'delete_food.html',
        {'food': food}
    )

# ---------------- ORDER FOOD ----------------

@login_required
def order_food(request, id):

    food = get_object_or_404(Food, id=id)

    if request.method == 'POST':

        quantity = int(request.POST['quantity'])

        total_price = food.price * quantity

        Order.objects.create(
            customer=request.user,
            food=food,
            quantity=quantity,
            total_price=total_price
        )

        return redirect('my_orders')

    return render(
        request,
        'order_food.html',
        {'food': food}
    )


# ---------------- MY ORDERS ----------------

@login_required
def my_orders(request):

    orders = Order.objects.filter(
        customer=request.user
    ).order_by('-ordered_at')

    return render(
        request,
        'my_orders.html',
        {'orders': orders}
    )



@api_view(['GET', 'POST'])
def food_api(request):

    if request.method == 'GET':
        foods = Food.objects.all()
        serializer = FoodSerializer(foods, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = FoodSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def food_detail_api(request, id):

    try:
        food = Food.objects.get(id=id)
    except Food.DoesNotExist:
        return Response({'error': 'Food not found'}, status=404)

    if request.method == 'GET':
        serializer = FoodSerializer(food)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = FoodSerializer(food, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    if request.method == 'DELETE':
        food.delete()
        return Response({'message': 'Food deleted successfully'})