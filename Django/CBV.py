
class AuthorView(ListView):
    model = Author
    template_name = 'main/index_authors.html'
    context_object_name = 'authors'
    extra_context = {
        'title': 'Authors',
    }


class AuthorInfo(DetailView):
    model = Author
    template_name = 'main/index_author.html'
    slug_url_kwarg = 'author_slug'
    context_object_name = 'author'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        books = Book.objects.filter(author__slug=self.kwargs[self.slug_url_kwarg])
        context['books'] = books
        context['title'] = 'Info'
        return context


class UpdateAuthor(UpdateView):
    model = Author
    template_name = 'main/index_update_author.html'
    slug_url_kwarg = 'author_slug'
    fields = ('name', 'surname')
    success_url = reverse_lazy('authors_page')
    extra_context = {
        'title': 'Update',
    }


class DeleteAuthor(DeleteView):
    model = Author
    template_name = 'main/index_delete_author.html'
    success_url = reverse_lazy('authors_page')
    slug_url_kwarg = 'author_slug'
    extra_context = {
        'title': 'Delete',
    }


class AddAuthor(CreateView):
    form_class = AddAuthorForm
    template_name = 'main/index_add_author.html'
    success_url = reverse_lazy('authors_page')
    extra_context = {
        'title': 'Add Author',
    }
