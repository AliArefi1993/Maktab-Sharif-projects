from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from django.urls import reverse
from post.models import Post, Comment, Category, Tag
from model_mommy import mommy


User = get_user_model()


class TestPost(APITestCase):

    def setUp(self):
        self.user = mommy.make(User)
        mommy.make(Post, owner=self.user, _quantity=10)
        mommy.make(Post, _quantity=5)
        mommy.make(Post, title='test here', _quantity=1)

    def test_post_list(self):
        url = reverse('post_list')
        self.client.force_authenticate(self.user)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data), 16)

    def test_post_detail(self):
        url = reverse('post_detail', args=[16])
        self.client.force_authenticate(self.user)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['title'], 'test here')


class TestComment(APITestCase):

    def setUp(self):
        self.user = mommy.make(User, username='ali909', is_staff=True)
        post1 = mommy.make(Post)
        mommy.make(Comment, _quantity=50)
        mommy.make(Comment, user=self.user, post=post1,
                   _quantity=1, text='comment test')

    def test_comment_list(self):
        url = reverse('comment_list')
        self.client.force_authenticate(self.user)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data), 51)

    def test_post_detail(self):
        url = reverse('comment_detail', args=[51])
        self.client.force_authenticate(self.user)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['user']['username'], 'ali909')


# class TestCategory(APITestCase):

#     def setUp(self):
#         post1 = mommy.make(Post)
#         mommy.make(Category, _quantity=25)
#         mommy.make(Category, post=post1,
#                    _quantity=1, name='category test')

#     def test_category_list(self):
#         url = reverse('category_list')
#         resp = self.client.get(url)
#         self.assertEqual(resp.status_code, 200)
#         self.assertEqual(len(resp.data), 26)

#     def test_category_detail(self):
#         url = reverse('category_detail', args=[26])
#         resp = self.client.get(url)
#         self.assertEqual(resp.status_code, 200)
#         self.assertEqual(resp.data['name'], 'category test')
#         url = reverse('category_detail', args=[27])
#         resp = self.client.get(url)
#         self.assertEqual(resp.status_code, 404)


# class TestPost(APITestCase):

#     def setUp(self):

#         self.user = mommy.make(User)
#         mommy.make(Post, owner=self.user, _quantity=10)
#         mommy.make(Post, _quantity=5)
#         mommy.make(Tag, _quantity=2)

#     def test_post_list(self):
#         url = reverse('post_list_create')
#         resp = self.client.get(url)
#         self.assertEqual(resp.status_code, 200)
#         self.assertEqual(len(resp.data), 15)

#     def test_create_post(self):

#         url = reverse('post_list_create')
#         tag = Tag.objects.first()
#         title = 'test title'
#         data = {
#             'title': title,
#             'tag': tag.id
#         }
#         self.client.force_authenticate(self.user)
#         resp = self.client.post(url, data=data)
#         self.assertEqual(resp.status_code, 201)
#         post = Post.objects.get(id=resp.data['id'])
#         self.assertEqual(post.owner, self.user)
#         self.assertEqual(post.title, title)

#     def test_update_post(self):
#         post = Post(owner=self.user, title='test title')
#         post.save()
#         url = reverse('post_detail_update_delete', kwargs={'id': post.id})
#         new_title = "new title"
#         data = {
#             "title": new_title,
#             "tag": Tag.objects.last().id
#         }
#         self.client.force_authenticate(self.user)
#         resp = self.client.put(url, data)
#         self.assertEqual(resp.status_code, 200)
#         updated_post = Post.objects.get(id=post.id)
#         self.assertEqual(updated_post.title, new_title)

#     def test_update_post_with_invalid_user(self):
#         post = Post(owner=self.user, title='test title')
#         post.save()
#         url = reverse('post_detail_update_delete', kwargs={'id': post.id})
#         new_title = "new title"
#         data = {
#             "title": new_title,
#             "tag": Tag.objects.last().id
#         }
#         another_user = mommy.make(User)
#         self.client.force_authenticate(another_user)
#         resp = self.client.put(url, data)
#         self.assertEqual(resp.status_code, 400)

#     def test_delete_post(self):
#         post = Post(owner=self.user, title='test title')
#         post.save()
#         url = reverse('post_detail_update_delete', kwargs={'id': post.id})
#         another_user = mommy.make(User)
#         self.client.force_authenticate(another_user)
#         resp = self.client.delete(url)
#         self.assertEqual(resp.status_code, 400)
#         self.client.force_authenticate(self.user)
#         resp = self.client.delete(url)
#         self.assertEqual(resp.status_code, 204)
#         self.assertEqual(len(Post.objects.filter(id=post.id)), 0)
