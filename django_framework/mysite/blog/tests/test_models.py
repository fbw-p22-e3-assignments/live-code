from django.test import TestCase
from blog.models import Post
from django.contrib.auth.models import User
from django.utils import timezone

class TestPostModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username="test_author", 
                                     email="testing@blog.com", 
                                     password="testingpass123")
        # user = User.objects.create(username="new_user")
        Post.objects.create(title="Testing Post", slug="testing-post",
                            author=user, body="This is a testing Post.",
                            created=timezone.now, updated=timezone.now,
                            status='published')
    
    def test_object_name_is_title(self):
        post = Post.objects.get(id=1)
        expected_name = f"{post.title}"
        # self.assertTrue(isinstance(post, Post))
        self.assertEqual(str(post), expected_name)
        
    def test_get_absolute_url(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.get_absolute_url(), '/blog/post/testing-post/')
        
    def test_slug_label(self):
        post = Post.objects.get(id=1)
        field_name = post._meta.get_field('slug').verbose_name
        self.assertEqual(field_name, 'Slug')
        
    def test_title_max_length(self):
        post = Post.objects.get(id=1)
        field_max_length = post._meta.get_field('title').max_length
        self.assertEqual(field_max_length, 200)