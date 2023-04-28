from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from university.forms import StudentForm
from university.models import Student


# Create your views here.


def index(request):
    return HttpResponse("OK")


def student_view(request, id: int):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return HttpResponseRedirect(reverse("index"))
    if request.method == "GET":
        form = StudentForm(instance=student)
        context = {"form": form}
        return render(request, "student.html", context)
    elif request.method == "POST":
        # Updating student with data from form
        form = StudentForm(request.POST, instance=student)
        if not form.is_valid():
            return HttpResponse(reverse("new_student"))
        form.save()
        context = {"form": form}
        return render(request, "student.html", context)


def new_student(request):
    if request.method == "GET":
        form = StudentForm()
        context = {"form": form}
        return render(request, "new_student.html", context)
    elif request.method == "POST":
        form = StudentForm(request.POST)
        if not form.is_valid():
            return HttpResponse(reverse("new_student"))
        form.save()
        return HttpResponseRedirect(reverse("student_view", args=[form.instance.id]))
