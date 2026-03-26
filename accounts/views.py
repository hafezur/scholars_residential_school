from django.shortcuts import render, redirect
from scholars_main.models import NewsEvent, okgs_photo, scientest,singleUnique 

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout



from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import UserProfile
from scholars_main.models import NewsEvent


@login_required
def custom_admin(request):
    #get user profile safely
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":

        form_type = request.POST.get("form_type")
        # ================= NEWS / EVENT =================
        if form_type == "news":

            title = request.POST.get("title")
            description = request.POST.get("description")
            type_ = request.POST.get("type")
            start_date = request.POST.get("start_date")
            end_date = request.POST.get("end_date")

            image = request.FILES.get("image")
            video = request.FILES.get("video_file")

            NewsEvent.objects.create(
                title=title,
                description=description,
                type=type_,
                start_date=start_date if start_date else timezone.now().date(),
                end_date=end_date if end_date else None,
                image=image,
                video_file=video
            )

            messages.success(request, "News/Event added successfully!")
            return redirect('news&event')

        # ================= GALLERY =================
        elif form_type == "gallery":

            title = request.POST.get("title", "").strip()
            description = request.POST.get("description", "").strip()
            picture1 = request.FILES.get("picture1")
            picture2 = request.FILES.get("picture2")

            

            # save to database
            okgs_photo.objects.create(
                title=title,
                description=description,
                picture1=picture1,
                picture2=picture2,
            )

            messages.success(request, "Gallery added successfully!")
            return redirect('galary_function')
        
        elif form_type == "scientest":

            name = request.POST.get("name", "").strip()
            description = request.POST.get("description", "").strip()
            scientest_pic = request.FILES.get("scientest_pic")

            # validation (optional but recommended)
            if not name:
                messages.error(request, "Scientist name is required!")
                return redirect('admin_panel')

            # save to database
            scientest.objects.create(
                name=name,
                description=description,
                scientest_pic=scientest_pic
            )

            messages.success(request, "Scientist added successfully!")
            return redirect('home_function')
        
        elif form_type == "logo":

            title = request.POST.get("title", "").strip()
            description = request.POST.get("description", "").strip()
            logo_pic = request.FILES.get("logo_pic")

            # validation
            if not title:
                messages.error(request, "Logo title is required!")
                return redirect('admin_panel')

            if not logo_pic:
                messages.error(request, "Logo image is required!")
                return redirect('admin_panel')

            # save to database
            singleUnique.objects.create(
                title=title,
                description=description,
                image=logo_pic   # make sure model field name matches
            )

            messages.success(request, "Logo updated successfully!")
            return redirect('home_function')
        
        elif form_type == "principal_logo":

            title = request.POST.get("title", "").strip()
            description = request.POST.get("description", "").strip()
            logo_pic = request.FILES.get("principal_pic")

            # validation
            if not title:
                messages.error(request, "Logo title is required!")
                return redirect('admin_panel')

            if not logo_pic:
                messages.error(request, "Logo image is required!")
                return redirect('admin_panel')

            # save to database
            singleUnique.objects.create(
                title=title,
                description=description,
                image=logo_pic   # make sure model field name matches
            )

            messages.success(request, "Logo updated successfully!")
            return redirect('home_function')
    logo = singleUnique.objects.filter(title='school_logo').latest('created_at')
    context = {
        "profile": profile,
        'logo':logo,
    }

    return render(request, 'base.html', context)
from.models import UserProfile
def sign_up(request):
    logo = singleUnique.objects.filter(title='school_logo').latest('created_at')
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # Check password match
        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

        # Check username
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('sign_up')

        # Check email
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('sign_up')

        # Create user
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        UserProfile.objects.get_or_create(user=user)
        messages.success(request, "Account created successfully! Please login.")
        return redirect('get_login')
    context={
        'logo':logo,
    }
    return render(request, "signup.html",context)

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import UserProfile


def user_login(request):
    logo = singleUnique.objects.filter(title='school_logo').latest('created_at')
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome {user.username}!")

            # Correct way
            profile, created = UserProfile.objects.get_or_create(user=user)

            # Role-based redirect 
            if profile.is_secondary_admin:
                return redirect('admin_panel')   
            else:
                return redirect('userDashboard') 

        else:
            messages.error(request, "Invalid username or password!")
            return redirect('get_login')
    context={
        'logo':logo,
    }
    return render(request, "login.html" ,context)


# ------------------ LOGOUT ------------------
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('get_login')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile


@login_required
def userDashboard(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    #  Role check
    if profile.is_secondary_admin:
        return redirect('admin_panel')   # custom admin page
    logo = singleUnique.objects.filter(title='school_logo').latest('created_at')
    #  Normal user dashboard
    context = {
        "profile": profile,
        'logo':logo,
    }

    return render(request, "user_dashboard.html", context)


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile


@login_required
def profile_update(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    logo = singleUnique.objects.filter(title='school_logo').latest('created_at')
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone = request.POST.get("phone")

        # update user
        request.user.username = username
        request.user.email = email
        request.user.save()

        # update profile
        profile.phone = phone

        if request.FILES.get("profile_pic"):
            profile.profile_pic = request.FILES.get("profile_pic")

        profile.save()

        messages.success(request, "Profile updated successfully!")
        return redirect('userDashboard')

    return render(request, "updateUserProfile.html", {"profile": profile,'logo':logo})