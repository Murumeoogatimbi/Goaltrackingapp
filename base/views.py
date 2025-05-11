from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Goal

class GoalListView(ListView):
    model = Goal
    template_name = 'base/goal_list.html'

class GoalDetailView(DetailView):
    model = Goal
    template_name = 'base/goal_detail.html'

class GoalCreateView(CreateView):
    model = Goal
    fields = "__all__"
    template_name = 'base/goal_form.html'
    success_url = reverse_lazy('goal_list')

class GoalUpdateView(UpdateView):
    model = Goal
    fields = "__all__"
    template_name = 'base/goal_form.html'
    success_url = reverse_lazy('goal_list') 

class GoalDeleteView(DeleteView):
    model = Goal
    template_name = 'base/goal_confirm_delete.html'
    success_url = reverse_lazy('goal_list')   