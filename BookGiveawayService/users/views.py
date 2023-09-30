

from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookForm
from django.core.mail import send_mail

from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer



class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



class MyLoginView(LoginView):
    template_name = 'login.html'




def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Sending the email verification link
            send_mail(
                'Verify your email for BookGiveawayService',
                f'Click the link to verify your email: http://127.0.0.1:8000/verify_email/{user.email_verification_token}',
                'noreply@bookgiveawayservice.com',
                [user.email],
            )

            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})



@login_required
def profile(request):
    return render(request, 'profile.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.owner = request.user
            book.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})


def set_recipient(request, book_id, user_id):
    book = Book.objects.get(id=book_id)
    if request.user == book.owner:
        book.recipient = User.objects.get(id=user_id)
        book.save()



# Update an existing book
def update_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'update.html', {'form': form})



def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('book_list')


def add_author(request):
    pass

def add_genre(request):
    pass

def add_condition(request):
    pass
