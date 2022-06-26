from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from .forms import CategoryForm
from .models import Category, Product

'''Client views'''


def homepage_view(request):
    request.user.is_superuser
    return render(request, "homepage.html", {})



class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_details.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        products = Product.objects.filter(category=context[self.context_object_name])
        context['products'] = products
        return context


# def category_details_view(request, pk):
#    category = Category.objects.get(pk=pk)
#    products = Product.object.filter(category=category)
#    return render(request, 'category_details.html', {'category':category, 'products':products})

'''Administration view'''


class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'category'
    queryset = Category.objects.all()


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_create.html'
    success_url = reverse_lazy('category_list')


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_create.html'
    success_url = reverse_lazy('category_list')


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category_delete.html'
    success_url = reverse_lazy('category_list')



