from django.db import models

class Author(models.Model):
    
    '''
    Class of entity Author
    
    Attributes
    ----------
    username : str
        Usernames(s) of author(s)
    mail : str
        Mail(s) of author(s)
    
    Methods
    -------    
    __str__()
        Provides textual username(s) of class instances in the admin panel 
    '''

    username = models.CharField(max_length=100, blank=False)
    mail = models.EmailField(primary_key=True, blank=False)
    
    def __str__(self):
        return self.username
    

class Post(models.Model):
    
    '''
    Class of entity Post 
    Include class Meta for a ordering by issued field
    
    Attributes
    ----------
    author : ForeignKeyRelationManager
        Foreign Key
    issued : Datetime
        Date and Time of post(s) 
    title : str
        Title(s) of post(s)
    content : str
        Content of post(s)
    recipe : str
        Recipe(s) of post(s)
    moderation : bool
        Check moderation of post(s)
    
    Methods
    -------
    __str__()
        Provides textual title(s) of class instances in the admin panel 
    ''' 
    
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    issued = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    recipe = models.TextField()
    moderation = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-issued']
        indexes = [
            models.Index(fields=['-issued']),
            ]
    
    def __str__(self):
        return self.title