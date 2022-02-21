from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import NewsStory, Category, Comment
from .forms import StoryForm, CommentForm, UpdateStoryForm
from django.shortcuts import get_object_or_404, render
from django.contrib import messages


class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
        context['all_stories'] = NewsStory.objects.all().order_by('-pub_date')
        return context


class StoryView(generic.DetailView):
    model = NewsStory
    template_name = "news/story.html"
    context_object_name = 'story'

class AddStoryView(LoginRequiredMixin, generic.CreateView):
    login_url = '/users/login/'
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CategoryView(generic.DetailView):
    model = Category
    template_name = "news/categoryDetail.html"
    context_object_name = 'category'

class UpdateStoryView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    login_url = 'users/login/'
    model = NewsStory
    form_class = UpdateStoryForm
    context_object_name = 'storyForm'
    template_name = 'news/updateStory.html'

    def get_success_url(self):
        """Get the story_id from the request object to pass to the success url"""
        slug = self.kwargs['slug']
        success_url = reverse_lazy('news:story', kwargs={'slug': slug})
        return success_url

    def test_func(self):
        """Only let the user access this page if they are the author of the object being updated"""
        return self.get_object().author == self.request.user

def story_detail(request, slug):
    template_name = 'news/story.html'
    story = get_object_or_404(NewsStory, slug=slug)
    comments = story.comments.all()
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid() and request.user.is_authenticated:
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current story to the comment
            new_comment.story = story
            new_comment.name = request.user
            # Save the comment to the database
            new_comment.save()
        else:
            messages.error(request, 'Please login or register to leave a comment.')
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'story': story,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

class DeleteStoryView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    login_url = 'users/login/'
    model = NewsStory
    template_name = 'news/deleteStory.html'
    success_url = reverse_lazy('news:index')
    
    def test_func(self):
        """Only let the user access this page if they are the author of the object being deleted"""
        return self.get_object().author == self.request.user                                          

def handler404(request, exception):
    return render(request, '404.html', status=404)