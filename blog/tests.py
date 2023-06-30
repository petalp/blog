from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post

# Create your tests here.



class BlogTests(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
                    username = 'jamestoma',
                    email = 'testtoma@gmail.com',
                    password = 'toma'
                )
        self.post = Post.objects.create(
                title = 'A good title',
                body = 'Nice body content',
                author = self.user
                )
    
    def test_string_represtation(self):
        post = Post(title="A sample title")
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.author}', 'jamestoma')
        self.assertEqual(f'{self.post.body}', 'Nice body content')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_reponse = self.client.get('/post/1000000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_reponse.status_code, 404)
        self.assertContains(response, "A good title")
        self.assertTemplateUsed(response, 'post_detail.html')