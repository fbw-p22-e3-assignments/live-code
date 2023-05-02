from django.test import TestCase
from blog.models import Post, Comment
from django.utils import timezone
from django.contrib.auth.models import User
from http import HTTPStatus


class PostListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        
        user = User.objects.create(username="test_author",
                                   email="testing@blog.com",
                                   password="testingpass123")
         
        num_of_posts = 10
        
        for post_num in range(num_of_posts):
            Post.objects.create(
                title=f"Testing Post {post_num}", 
                slug=f"testing-post-{post_num}",
                author=user,
                body="This is a testing Post.",
                created=timezone.now,
                updated=timezone.now,
                status='published')
            
    def test_view_url(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/index.html')
    
    def test_list_all_posts(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['all_posts']), 10)
        

class PostDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user1 = User.objects.create(username="test_author1",
                                   email="testing1@blog.com",
                                   password="testingpass123")
        
        user2 = User.objects.create(username="test_author2",
                                   email="testing2@blog.com",
                                   password="testingpass123")
        
        post = Post.objects.create(
                title=f"Testing Post", 
                slug=f"testing-post",
                author=user1,
                body="This is a testing Post.",
                created=timezone.now,
                updated=timezone.now,
                status='published')
        
        Comment.objects.create(
            post=post,
            name="Test Commenter",
            email="commneter@blog.com",
            body="Test comment",
            # created=str(timezone.now),
            # updated=timezone.now,
            # active=True,
        )
        

    def test_redirect_if_not_authenticated(self):
        response = self.client.get('/blog/post/testing-post/')
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/account/login/'))
    
    def test_logged_in_url(self):
        user = User.objects.get(id=2)
        logged_in = self.client.force_login(user)
        response = self.client.get('/blog/post/testing-post/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post-detail.html')
    
    
    def test_view_uses_correct_template(self):
        response = self.client.get('/blog/post/testing-post/')
        self.assertEqual(response.status_code, 302)
        # self.assertTemplateUsed(response, 'blog/post-detail.html')
         
    def test_comments_exist(self):
        user = User.objects.get(id=2)
        post = Post.objects.get(id=1)
        logged_in = self.client.force_login(user)
        response = self.client.get('/blog/post/testing-post/')
        self.assertEqual(len(response.context['comments']), 1)
        
    def test_comment_submission(self):
        user = User.objects.get(id=2)
        post = Post.objects.get(id=1)
        logged_in = self.client.force_login(user)
        response = self.client.post('/blog/post/testing-post/', kwargs=
                                    {"post":post,
                                     "name": "Second Commenter",
                                     "email":"commenter2@blog.com",
                                     "body":"2nd Test comment."})
        self.assertEqual(response.status_code, HTTPStatus.OK)
        
        
