from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from food.forms import FoodCreationForm, FoodChangeForm
from food.models import Food
from accounts.models import Profile

class FoodListView(ListView):
    model = Food

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            profile = Profile.objects.get(user=user)
            food_list = Food.objects.filter(profile=profile)
        else:
            food_list = Food.objects.all()
            food_list = Food.objects.none()
        return food_list


class FoodCreateView(LoginRequiredMixin, CreateView):
    model = Food
    fields = ['profile', 'name']
    template_name_suffix = '_create'
    success_url = reverse_lazy('food:list')

    def get_initial(self):
        user = self.request.user
        profile = Profile.objects.get(user=user)
        return {'profile': profile}


class FoodDetailView(LoginRequiredMixin, DetailView):
    model = Food


class FoodUpdateView(LoginRequiredMixin, UpdateView):
    model = Food
    fields = ['name']
    template_name_suffix = '_update'


class FoodDeleteView(LoginRequiredMixin, DeleteView):
    model = Food
    success_url = reverse_lazy('food:list')


def list_food(request):
    user = request.user

    if user.is_authenticated:
        profile = Profile.objects.get(user=user)
        food_list = Food.objects.filter(profile=profile)
    else:
        food_list = Food.objects.none()
    return render(request, 'food/food_list.html', {'food_list': food_list})


def detail_food(request, pk):
    food = Food.objects.get(pk=pk)
    return render(request, 'food/food_detail.html', {'food': food})


def delete_food(request, pk):
    if request.method == 'POST':
        food = Food.objects.get(pk=pk)
        food.delete()
        return redirect('food:list')
    else:
        food = Food.objects.get(pk=pk)
        return render(request, 'food/food_confirm_delete.html', {'food': food})


@login_required
def create_food(request):
    if request.method == 'POST':
        form = FoodCreationForm(request.POST)

        if form.is_valid():
            new_food = form.save(commit=False)
            new_food.profile = Profile.objects.get(user=request.user)
            new_food.save()
            return redirect('food:list')
    else:
        form = FoodCreationForm()
    return render(request, 'food/food_create.html', {'form': form})


@login_required
def modify_food(request, pk):
    if request.method == 'POST':
        form = FoodChangeForm(request.POST)
        if form.is_valid():
            food = Food.objects.get(pk=pk)
            food_name = form.cleaned_data.get('name')
            food.save()
            return redirect('food:list')
    else:
        food = Food.objects.get(pk=pk)
        form = FoodChangeForm(instance=food)
    return render(request, 'food/food_update.html', {'form': form})