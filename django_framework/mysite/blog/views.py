import datetime
from django.http import HttpResponse
from django.shortcuts import reverse, render, get_object_or_404
from django.views.generic import View
from .models import Post, Contact
from .forms import CommentForm, ContactForm
# Login required decorator
from django.contrib.auth.decorators import login_required



def home(request):
    text = "Welcome to the PythonBugs Blog"
    posts = Post.objects.all()
    
    # Getting session a session value and setting a default if its not present
    num_visits = request.session.get('num_visits', 0)
    
    # Creating a session variable
    request.session['num_visits'] = num_visits + 1
    
    request.session.set_expiry(10)
    
    return render(request, 'blog/index.html', {"welcome_text": text,
                                               "all_posts": posts,
                                               "num_visits": num_visits})


# class PostDetail(View):
    
#     def get(self, request, slug):
#         blog_post = Post.objects.get(slug=slug)
#         return render(request, 'blog/post-detail.html', {"post": blog_post})


def post_detail(request, slug):
    blog_post = get_object_or_404(Post, slug=slug)
    # request.session.pop('num_visits')
    # del request.session['num_visits']
    #  List of active comments
    comments = blog_post.comments.filter(active=True)
    
    new_comment = None
    
    if request.method == "POST":
        # A comment was passed
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create the comment but dont save
            new_comment = comment_form.save(commit=False)
            # Assign post to the form
            new_comment.post = blog_post
            # Save the comment
            new_comment.save()
    else:
        # For GET request.
        comment_form = CommentForm()
    
    return render(request, 'blog/post-detail.html',
                  {"post": blog_post, "comments": comments,
                   "new_comment": new_comment, "comment_form": comment_form})
    
    
class ContactFormView(View):
    template_name = 'contact.html'
    
    def get(self, request):
        contact_form = ContactForm() 
        return render(request, self.template_name, {"contact_form": contact_form})
    
    def post(self, request):
        contact_form = ContactForm(data=request.POST)
        text = "Data not submitted!"
        if contact_form.is_valid():
            cd = contact_form.cleaned_data
            contact = Contact(name=cd['name'],
                              phone_number=cd['phone_number'],
                              message=cd["message"])
            contact.save()
            text = "Thank you!"
            return render(request, self.template_name, {"text": text})
        else: 
            # Invalid form. Reshow the form with errors
            return render(request, self.template_name, {"contact_form": contact_form})
        
            
            
    