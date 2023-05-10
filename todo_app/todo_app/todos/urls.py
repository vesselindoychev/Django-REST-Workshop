from django.urls import path

from todo_app.todos.views import TodosListAndCreateView, CategoryListView, TodoDetailsAndUpdateView

urlpatterns = (
    path('', TodosListAndCreateView.as_view(), name='api list or create todos'),
    path('categories/', CategoryListView.as_view(), name='list categories'),
    path('<int:pk>/', TodoDetailsAndUpdateView.as_view(), name='api details or update todo'),

)

