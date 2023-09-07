from django.test import TestCase
from django.db.models import CharField, EmailField, ForeignKey, DateTimeField, BooleanField, TextField
from .models import Author, Post


def create_user_and_post():
    
    user = Author.objects.create(username = 'User', mail = 'test@gmail.com')
    Post.objects.create(author = user, 
                        title = 'The Perfect Steak', 
                        content = 'Beaf', 
                        recipe = 'Eat it raw', 
                        moderation = True)
    

class AuthorModelTest(TestCase):
    
    '''
    Class of testing Author model
    
    Methods
    -------    
    test_data_str()
        Check if it converts to textual data    
    
    test_len_of_fields()
        Check len of fields
    
    test_type_of_fields()
        Check type of fields
    '''
    
    @classmethod
    def setUpTestData(cls):
        create_user_and_post()
    
    def test_data_str(self):
        author = Author.objects.get(username = 'User')
        expected_name = f'{author.username}'
        expected_mail = f'{author.mail}'
        self.assertEquals(expected_name, str(author.username))
        self.assertEquals(expected_mail, str(author.mail))
    
    def test_len_of_fields(self):
        author = Author.objects.get(username = 'User')
        max_len = author._meta.get_field('username').max_length
        self.assertEquals(max_len, 100)
    
    def test_type_of_fields(self):
        author = Author.objects.get(username = 'User')
        expected_field_username = author._meta.get_field('username')
        expected_field_mail = author._meta.get_field('mail')
        self.assertTrue(isinstance(expected_field_username, CharField))
        self.assertTrue(isinstance(expected_field_mail, EmailField))


class PostModelTest(TestCase):
    
    '''
    Class of testing Post model
    
    Methods
    -------    
    test_data_str()
        Check if it converts to textual data    
    
    test_len_of_fields()
        Check len of fields
    
    test_type_of_fields()
        Check type of fields
    '''
    
    @classmethod
    def setUpTestData(cls):
        create_user_and_post()
    
    def test_data_str(self):
        post = Post.objects.get(title = 'The Perfect Steak')
        expected_title = f'{post.title}'
        expected_content = f'{post.content}'
        expected_recipe = f'{post.recipe}'
        self.assertEquals(expected_title, str(post.title))
        self.assertEquals(expected_content, str(post.content))
        self.assertEquals(expected_recipe, str(post.recipe))
    
    def test_len_of_fields(self):
        post = Post.objects.get(title = 'The Perfect Steak')
        max_len_title = post._meta.get_field('title').max_length
        max_len_content = post._meta.get_field('content').max_length
        self.assertEquals(max_len_title, 100)
        self.assertEquals(max_len_content, 1000)
    
    def test_type_of_fields(self):
        post = Post.objects.get(title = 'The Perfect Steak')
        expected_field_author = post._meta.get_field('author')
        expected_field_issued = post._meta.get_field('issued')
        expected_field_title = post._meta.get_field('title')
        expected_field_content = post._meta.get_field('content')
        expected_field_recipe = post._meta.get_field('recipe')
        expected_field_moderation = post._meta.get_field('moderation')
        self.assertTrue(isinstance(expected_field_author, ForeignKey))
        self.assertTrue(isinstance(expected_field_issued, DateTimeField))
        self.assertTrue(isinstance(expected_field_title, CharField))
        self.assertTrue(isinstance(expected_field_content, CharField))
        self.assertTrue(isinstance(expected_field_recipe, TextField))
        self.assertTrue(isinstance(expected_field_moderation, BooleanField))