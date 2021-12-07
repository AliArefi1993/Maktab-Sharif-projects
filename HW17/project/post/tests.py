from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from django.urls import reverse
from post.models import Post, Comment, Category
from model_mommy import mommy


User = get_user_model()


class TestPost(APITestCase):

    def setUp(self):
        user = mommy.make(User)
        mommy.make(Post, owner=user, _quantity=10)
        mommy.make(Post, _quantity=5)
        mommy.make(Post, title='test here', _quantity=1)

    def test_post_list(self):
        url = reverse('post_list')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data), 16)

    def test_post_detail(self):
        url = reverse('post_detail', args=[16])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['title'], 'test here')


class TestComment(APITestCase):

    def setUp(self):
        user1 = mommy.make(User, username='ali909')
        post1 = mommy.make(Post)
        mommy.make(Comment, _quantity=5)
        mommy.make(Comment, user=user1, post=post1,
                   _quantity=1, text='comment test')

    def test_comment_list(self):
        url = reverse('comment_list')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data), 6)

    def test_post_detail(self):
        url = reverse('comment_detail', args=[6])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['user']['username'], 'ali909')


class TestCategory(APITestCase):

    def setUp(self):
        post1 = mommy.make(Post)
        mommy.make(Category, _quantity=5)
        mommy.make(Category, post=post1,
                   _quantity=1, name='category test')

    def test_category_list(self):
        url = reverse('category_list')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data), 6)

    def test_category_detail(self):
        url = reverse('category_detail', args=[6])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['name'], 'category test')
        url = reverse('category_detail', args=[7])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 404)
