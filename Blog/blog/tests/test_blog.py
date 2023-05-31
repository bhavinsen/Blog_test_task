from turtle import title
from django.test import TestCase
from blog.models import Book, Author
from django.urls import reverse



class BookTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        author = Author.objects.create(name="James")
        cls.book = Book.objects.create(title="The Book", author=author)
        
    def test_model_content(self):
        self.assertEqual(self.book.title, "The Book")
        
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/book/")
        self.assertEqual(response.status_code, 200)
        
    def test_homepage(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/book_view.html")
        self.assertContains(response, "This is a test!")
        