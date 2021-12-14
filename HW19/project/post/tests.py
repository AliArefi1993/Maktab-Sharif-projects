from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from django.urls import reverse
from post.models import Post, Comment, Category, Tag
from model_mommy import mommy


User = get_user_model()


class TestPost(APITestCase):

    def setUp(self):
        self.user = mommy.make(User)
        mommy.make(Post, owner=self.user, _quantity=2)
        mommy.make(Post, _quantity=1)
        mommy.make(Post, title='test here', _quantity=1)
        mommy.make(Tag, _quantity=2)

    def test_post_list(self):
        url = reverse('post_list')
        self.client.force_authenticate(self.user)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data), 4)

    def test_post_detail(self):
        url = reverse('post_detail', args=[4])
        self.client.force_authenticate(self.user)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['title'], 'test here')

    def test_create_post(self):

        url = reverse('post_list')
        tag = Tag.objects.first()
        title = 'test title'
        data = {
            'title': title,
            'tag': tag.id,
            'description': 'test DESCS',
            'published': True,
            'owner': 1
        }
        self.client.force_authenticate(self.user)
        resp = self.client.post(url, data=data)
        self.assertEqual(resp.status_code, 201)
        post = Post.objects.get(id=resp.data['id'])
        self.assertEqual(post.owner, self.user)
        self.assertEqual(post.title, title)

    def test_update_post(self):
        post = Post(owner=self.user, title='test title')
        post.save()
        url = reverse('post_detail', kwargs={'pk': post.id})
        new_title = "new title"
        data = {
            "title": new_title,
            "tag": Tag.objects.last().id,
            'description': 'test DESCS',
            'owner': 1

        }
        self.client.force_authenticate(self.user)
        resp = self.client.put(url, data)
        self.assertEqual(resp.status_code, 200)
        updated_post = Post.objects.get(id=post.id)
        self.assertEqual(updated_post.title, new_title)

    def test_update_post_with_invalid_user(self):
        post = Post(owner=self.user, title='test title')
        post.save()
        url = reverse('post_detail', kwargs={'pk': post.id})
        new_title = "new title"
        data = {
            "title": new_title,
            "tag": Tag.objects.last().id,
            'description': 'test DESCS',
            'owner': 1
        }
        another_user = mommy.make(User)
        self.client.force_authenticate(another_user)
        resp = self.client.put(url, data)
        self.assertEqual(resp.status_code, 404)

    def test_delete_post(self):
        post = Post(owner=self.user, title='test title')
        post.save()
        url = reverse('post_detail', kwargs={'pk': post.id})
        another_user = mommy.make(User)
        self.client.force_authenticate(another_user)
        resp = self.client.delete(url)
        self.assertEqual(resp.status_code, 404)
        self.client.force_authenticate(self.user)
        resp = self.client.delete(url)
        self.assertEqual(resp.status_code, 204)
        self.assertEqual(len(Post.objects.filter(id=post.id)), 0)


class TestComment(APITestCase):

    def setUp(self):
        self.user = mommy.make(User, username='ali909', is_staff=True)
        post1 = mommy.make(Post)
        mommy.make(Comment, _quantity=5)
        mommy.make(Comment, user=self.user, post=post1,
                   _quantity=1, text='comment test')

    def test_comment_list(self):
        url = reverse('comment_list')
        self.client.force_authenticate(self.user)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data), 6)

    def test_post_detail(self):
        url = reverse('comment_detail', args=[6])
        self.client.force_authenticate(self.user)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['user']['username'], 'ali909')


class TestCategory(APITestCase):

    def setUp(self):
        self.user = mommy.make(User, username='ali909', is_staff=True)
        post1 = mommy.make(Post)
        mommy.make(Category, _quantity=2)
        mommy.make(Category, post=post1,
                   _quantity=1, name='category test')

    def test_category_list(self):
        url = reverse('category_list')
        self.client.force_authenticate(self.user)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data), 3)

    def test_category_detail(self):
        url = reverse('category_detail', args=[3])
        self.client.force_authenticate(self.user)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['name'], 'category test')
        url = reverse('category_detail', args=[4])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 404)

    def test_create_category(self):

        url = reverse('category_list')
        name = 'test cat'
        data = {
            'name': name,
        }
        self.client.force_authenticate(self.user)
        resp = self.client.post(url, data=data)
        self.assertEqual(resp.status_code, 201)
        post = Category.objects.get(id=resp.data['id'])
        self.assertEqual(post.name, name)

    def test_update_category(self):
        my_category = Category(name='test cat')
        my_category.save()
        url = reverse('category_detail', kwargs={'pk': my_category.id})
        new_name = "new name"
        data = {
            "name": new_name,
        }
        self.client.force_authenticate(self.user)
        resp = self.client.put(url, data)
        self.assertEqual(resp.status_code, 200)
        updated_category = Category.objects.get(id=my_category.id)
        self.assertEqual(updated_category.name, new_name)

    def test_update_category_with_invalid_user(self):
        post = Post(owner=self.user, title='test title')
        post.save()
        url = reverse('category_detail', kwargs={'pk': post.id})
        new_name = "new name"
        data = {
            "name": new_name,
        }
        another_user = mommy.make(User)
        self.client.force_authenticate(another_user)
        resp = self.client.put(url, data)
        self.assertEqual(resp.status_code, 403)

    def test_delete_category(self):
        category = Category(name='test name')
        category.save()
        url = reverse('category_detail', kwargs={'pk': category.id})
        another_user = mommy.make(User)
        self.client.force_authenticate(another_user)
        resp = self.client.delete(url)
        self.assertEqual(resp.status_code, 403)
        self.client.force_authenticate(self.user)
        resp = self.client.delete(url)
        self.assertEqual(resp.status_code, 204)
        self.assertEqual(len(Category.objects.filter(id=category.id)), 0)


class TestTag(APITestCase):

    def setUp(self):
        self.user = mommy.make(User, username='ali909', is_staff=True)
        post1 = mommy.make(Post)
        mommy.make(Tag, _quantity=2)
        mommy.make(Tag, post=post1,
                   _quantity=1, name='tag test')

    def test_t_list(self):
        url = reverse('tag_list')
        self.client.force_authenticate(self.user)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data), 3)

    def test_tag_detail(self):
        url = reverse('tag_detail', args=[3])
        self.client.force_authenticate(self.user)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['name'], 'tag test')
        url = reverse('tag_detail', args=[4])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 404)

    def test_create_tag(self):

        url = reverse('tag_list')
        name = 'test tag'
        data = {
            'name': name,
        }
        self.client.force_authenticate(self.user)
        resp = self.client.post(url, data=data)
        self.assertEqual(resp.status_code, 201)
        tag = Tag.objects.get(id=resp.data['id'])
        self.assertEqual(tag.name, name)

    def test_update_category(self):
        my_tag = Tag(name='test cat')
        my_tag.save()
        url = reverse('tag_detail', kwargs={'pk': my_tag.id})
        new_name = "new name"
        data = {
            "name": new_name,
        }
        self.client.force_authenticate(self.user)
        resp = self.client.put(url, data)
        self.assertEqual(resp.status_code, 200)
        updated_tag = Tag.objects.get(id=my_tag.id)
        self.assertEqual(updated_tag.name, new_name)

    def test_update_tag_with_invalid_user(self):
        post = Tag(name='test title')
        post.save()
        url = reverse('tag_detail', kwargs={'pk': post.id})
        new_name = "new name"
        data = {
            "name": new_name,
        }
        another_user = mommy.make(User)
        self.client.force_authenticate(another_user)
        resp = self.client.put(url, data)
        self.assertEqual(resp.status_code, 403)

    def test_delete_tag(self):
        tag = Tag(name='test name')
        tag.save()
        url = reverse('tag_detail', kwargs={'pk': tag.id})
        another_user = mommy.make(User)
        self.client.force_authenticate(another_user)
        resp = self.client.delete(url)
        self.assertEqual(resp.status_code, 403)
        self.client.force_authenticate(self.user)
        resp = self.client.delete(url)
        self.assertEqual(resp.status_code, 204)
        self.assertEqual(len(Tag.objects.filter(id=tag.id)), 0)
