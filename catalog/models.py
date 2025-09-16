from django.db import models
from django.urls import reverse
from django.db.models.functions import Lower
from django.db.models import UniqueConstraint
import uuid

# Create your models here.

""""Genre Model"""
class Genre(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(
        max_length=50,
        unique=True,
        help_text="Enter a book genre e.g Poetry, Science fiction, Adventure"
    )
    
    def get_absolute_url(self):
        """Returns a url to access details of a Genre"""
        return reverse('genre-detail', args=[str(self.id)])
    def __str__(self):
        return self.title
    
    """Constrains allows rules,and enforce intergrity for the data stored in the database"""
    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('title'),
                name='genre_case_insentive_unique',
                violation_error_message="Genre already exists"
            )
        ]
        
class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)
    author = models.ForeignKey('Author', on_delete=models.RESTRICT, null=True)
    isbn = models.CharField(
        'ISBN', 
        max_length=13, 
        unique=True, 
        help_text="The isbn number must be of 13 max characters")
    summary = models.TextField(
        max_length=200, 
        help_text="Provide a short summary about the book")
    genre = models.ManyToManyField(
        'Genre',
        help_text="Please provide the genre for this book"
    )
    
    DIFFERENT_LANGUAGES = (
        ('en', "English"),
        ('es', "Spanish"),
        ('fr', "French"),
        ('de', "German"),
        ('ja', "Japan"),
        ('zh', "Chinese"),
        ('hi', "Hindu"),
        ('ru', "Russian"),
        ('pt', "portugese"),
        ('it', "Italian"),
        ('ko', "Korean"),
        ('sh', "Swahili")
    )
    language = models.TextField(
        default="en",
        max_length=3,
        choices=DIFFERENT_LANGUAGES,
        blank=True,
        help_text="Please provide a language for the book"
    )
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        """Return an url to access details of the book"""
        return reverse('book-details', args=[str(self.id)])
    
class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    book = models.ForeignKey(
        "Book", 
        on_delete=models.RESTRICT,
        null=True
        )
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(blank=True, null=True)
    LOAN_STATUS = (
        ('l', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved')
    )
    status = models.CharField(
        max_length=3,
        choices=LOAN_STATUS,
        default='a',
        blank=True,
        help_text="Please provide a book status"
        )
    
    """Return Book-instance id and the book """
    def __str__(self):
        return f'{self.id} ({self.book})'
    
    """Order book by due_back date"""
    class Meta:
        ordering = ['due_back']
        
class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)
    
    """Return authors firstname once created"""
    def __str__(self):
        return f'{self.last_name} {self.first_name}'
    
    def get_absolute_url(self):
        """"Return teh author url for the object created"""
        return reverse('author', args=[str(self.id)])
    
    class Meta:
        ordering = ["last_name", "first_name"]