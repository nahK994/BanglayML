from django.db import models

# Create your models here.
class categoryTable(models.Model):
    categoryID = models.CharField(max_length=30, primary_key=True)
    
    def __str__(self):
        return self.categoryID

class cardTable(models.Model):
    cardID = models.AutoField(primary_key=True)
    categoryID = models.ForeignKey(
        categoryTable,
        on_delete = models.CASCADE
    )
    title = models.CharField(max_length=30)
    paragraph = models.CharField(max_length=100)
    #text = models.CharField(max_length=1000)
    
    def __str__(self):
        return str(self.categoryID) + " -> " + self.title

class cardTableNew(models.Model):
    cardID = models.AutoField(primary_key=True)
    categoryID = models.ForeignKey(
        categoryTable,
        on_delete = models.CASCADE
    )
    title = models.CharField(max_length=30)
    paragraph = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    
    def __str__(self):
        return str(self.categoryID) + " -> " + self.title