from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Reservation
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import AnonymousUser, User
from django.contrib.auth.decorators import login_required
from .forms import ReservationForm
from datetime import date, timedelta


def index(request):
    d0 = date.today()
    d1 = date.today() + timedelta(days=1)
    d2 = date.today() + timedelta(days=2)
    d3 = date.today() + timedelta(days=3)
    d0come = Reservation.objects.filter(dateFrom=d0).filter(type="Bungalov")
    d0go = Reservation.objects.filter(dateTo=d0).filter(type="Bungalov")
    d1come = Reservation.objects.filter(dateFrom=d1).filter(type="Bungalov")
    d1go = Reservation.objects.filter(dateTo=d1).filter(type="Bungalov")
    d2come = Reservation.objects.filter(dateFrom=d2).filter(type="Bungalov")
    d2go = Reservation.objects.filter(dateTo=d2).filter(type="Bungalov")
    d3come = Reservation.objects.filter(dateFrom=d3).filter(type="Bungalov")
    d3go = Reservation.objects.filter(dateTo=d3).filter(type="Bungalov")
    context = {"d0come": d0come, "d0go": d0go,
               "d1come": d1come, "d1go": d1go,
               "d2come": d2come, "d2go": d2go,
               "d3come": d3come, "d3go": d3go,
               "d0": d0, "d1": d1, "d2": d2, "d3": d3,}
    print(len(d1come))
    print(d1go)
    print(d2come)
    print(d2go)
    print(d3come)
    print(d3)
    return render(request, 'index.html', context)


def loginView(request):
    return redirect('index')


def logoutView(request):
    user = getattr(request, "user", None)
    if not getattr(user, "is_authenticated", True):
        user = None
    user_logged_out.send(sender=user.__class__, request=request, user=user)
    request.session.flush()
    if hasattr(request, "user"):
        request.user = AnonymousUser()
    return redirect('index')


@login_required
def add(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST, request.FILES)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.madeBy = request.user
            form.save()
            return redirect('list')
    else:
        form = ReservationForm()

    context = {"form": form}
    return render(request, 'add.html', context)


@login_required
def list(request):
    allReservations = Reservation.objects.all().order_by('dateFrom')
    context = {"allReservations": allReservations}
    return render(request, 'list.html', context)


@login_required
def delete(request, reservation_id):
    reservations = Reservation.objects.all()
    reservation = reservations.filter(pk=reservation_id)
    reservation.delete()
    return redirect('list')


@login_required
def edit(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST, request.FILES)
        if form.is_valid():
            resForm = form.save(commit=False)
            resForm.madeBy = request.user
            if resForm.image == None:
                resForm.image = reservation.image
            reservation.delete()
            form.save()
            return redirect('list')
    else:
        form = ReservationForm()

    context = {"form": form, "reservation": reservation, "reservation_id": reservation_id}
    return render(request, 'edit.html', context)


@login_required
def users(request):
    allUsers = User.objects.all()
    context = {"users": allUsers}
    return render(request, 'users.html', context)


@login_required
def b6(request):
    allReservations = Reservation.objects.filter(bNumber='6').order_by('dateFrom')
    context = {"allReservations": allReservations}
    return render(request, 'bng/b6.html', context)


@login_required
def b7(request):
    allReservations = Reservation.objects.filter(bNumber='7').order_by('dateFrom')
    context = {"allReservations": allReservations}
    return render(request, 'bng/b7.html', context)


@login_required
def b8(request):
    allReservations = Reservation.objects.filter(bNumber='8').order_by('dateFrom')
    context = {"allReservations": allReservations}
    return render(request, 'bng/b8.html', context)


@login_required
def b9(request):
    allReservations = Reservation.objects.filter(bNumber='9').order_by('dateFrom')
    context = {"allReservations": allReservations}
    return render(request, 'bng/b9.html', context)


@login_required
def b10(request):
    allReservations = Reservation.objects.filter(bNumber='10').order_by('dateFrom')
    context = {"allReservations": allReservations}
    return render(request, 'bng/b10.html', context)


@login_required
def b11(request):
    allReservations = Reservation.objects.filter(bNumber='11').order_by('dateFrom')
    context = {"allReservations": allReservations}
    return render(request, 'bng/b11.html', context)


@login_required
def b12(request):
    allReservations = Reservation.objects.filter(bNumber='12').order_by('dateFrom')
    context = {"allReservations": allReservations}
    return render(request, 'bng/b12.html', context)


@login_required
def b13(request):
    allReservations = Reservation.objects.filter(bNumber='13').order_by('dateFrom')
    context = {"allReservations": allReservations}
    return render(request, 'bng/b13.html', context)


@login_required
def b14(request):
    allReservations = Reservation.objects.filter(bNumber='14').order_by('dateFrom')
    context = {"allReservations": allReservations}
    return render(request, 'bng/b14.html', context)


@login_required
def b15(request):
    allReservations = Reservation.objects.filter(bNumber='15').order_by('dateFrom')
    context = {"allReservations": allReservations}
    return render(request, 'bng/b15.html', context)
