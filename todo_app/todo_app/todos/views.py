from django.shortcuts import render
from rest_framework import generics as api_views, permissions
from rest_framework import serializers

from todo_app.todos.models import Todo, Category
from todo_app.todos.serializers import TodoForListSerializer, TodoFullSerializer, CategoryForListSerializer


class TodosListAndCreateView(api_views.ListCreateAPIView):
    queryset = Todo.objects.all()
    list_serializer_class = TodoForListSerializer
    create_serializer_class = TodoFullSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get_queryset(self):
        queryset = super().get_queryset()

        queryset = queryset.filter(user=self.request.user)

        category_id = self.request.query_params.get('category', None)
        if category_id:
            queryset = queryset.filter(category_id=category_id)

        return queryset

    def get_serializer_class(self):
        if self.request.method.lower() == 'post':
            return self.create_serializer_class
        return self.list_serializer_class


class TodoDetailsAndUpdateView(api_views.RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoFullSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )


class CategoryListView(api_views.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryForListSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.filter(todo__user=self.request.user)
    #     return queryset
