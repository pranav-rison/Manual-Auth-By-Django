from django.shortcuts import redirect, render

from .models import User, Login

from django.contrib.auth.hashers import make_password, check_password

def home(request):
    return render(request, 'home.html')

# ? Typical reasons to save login records:

# ? Show login history (last login, activity)
# ? Audit/security tracking

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email, password=password)
            # Save user id in session
            request.session['user_id'] = user.id

            return redirect('dashboard')

        except User.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid email or password'}) 

        # user = User.objects.filter(email=email, password=password).first()
        # if user:
        #     return render(request, 'dashboard.html')
        # return render(request, 'login.html', {'error': 'Invalid email or password'})
        
        # ! first method to check if user exists with this email and password
        # Check if user exists with this email and password
        # user = User.objects.filter(email=email, password=password).first()
        # if user:
        #     return render(request, 'dashboard.html')
        # return render(request, 'login.html', {'error': 'Invalid email or password'})

        #! second method to check if user exists with this email and password
        
        # ! third method to check if user exists with this email and password
        # try:
        #     user = User.objects.get(email=email, password=password)
        #     Login.objects.create(email=email, password=password)
        #     return render(request, 'dashboard.html')
        # except User.DoesNotExist:
        #     return render(request, 'login.html', {'error': 'Invalid email or password'})

        # ! fourth method to check if user exists with this email and password
        # first = User.objects.get(email=email)
        # second = User.objects.get(password=password)

        # if email == first.email and password == second.password:
        #     Login.objects.create(email=email, password=password)  # Save login details to Login model
        #     return render(request, 'dashboard.html')
        # else:
        #     return render(request, 'login.html', {'error': 'Invalid email or password'})
    
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        hash_password = make_password(password)
        confirm_password = request.POST.get('confirm_password')
        
        if password != confirm_password:
            return render(request, 'register.html', {'error': 'Passwords do not match'})
        
        # ! Check if username or email already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})
        
        if User.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': 'Email already registered'})
        
        User.objects.create(username=username, email=email, password=hash_password, conform_password=confirm_password)
        return render(request, 'register.html', {'success': 'Registration successful! Please login.'})
    
        # try:
        #     User.objects.create(username=username, email=email, password=password, conform_password=confirm_password)
        #     return render(request, 'register.html', {'success': 'Registration successful! Please login.'})
        # except Exception as e:
        #     return render(request, 'register.html', {'error': str(e)})

        # ! second try block to handle unique constraints
        # try:
        #     username = request.POST.get('username')
        #     email = request.POST.get('email')
        #     password = request.POST.get('password')
        #     confirm_password = request.POST.get('confirm_password')
        #     if password != confirm_password:
        #         return render(request, 'register.html', {'error': 'Passwords do not match'})
        #     User.objects.create(username=username, email=email, password=password, conform_password=confirm_password)
        #     return render(request, 'register.html', {'success': 'Registration successful! Please login.'})
        # except Exception as e:
        #     return render(request, 'register.html', {'error': str(e)})

        # return redirect('home')




    return render(request, 'register.html')


def logout(request):
    return render(request, 'logout.html')

def dashboard(request):
 # Assuming you have a way to identify the logged-in user
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    try:
        user = User.objects.get(id=user_id)
        return render(request, 'dashboard.html', {'user': user})

    except User.DoesNotExist:
        return redirect('login')
