from django.db import models

class Categories(models.Model):
    category_title = models.CharField(max_length=35, primary_key=True)
    
    def __str__(self):
        return self.category_title

class CardsInfo(models.Model):
    card_info_ID = models.AutoField(primary_key=True)
    category_title = models.ForeignKey(
        Categories,
        on_delete = models.CASCADE
    )
    card_serial_NO = models.IntegerField(default=0)
    card_title = models.CharField(max_length=35)
    card_paragraph = models.CharField(max_length=200)
    card_text = models.TextField()
    
    def __str__(self):
        return str(self.category_title) + " -> " + self.card_title + " -> Serial No: " + str(self.card_serial_NO)

class Images(models.Model):
    image_title = models.CharField(max_length=35)
    card_info_ID = models.ForeignKey(
        CardsInfo,
        on_delete = models.CASCADE
    )
    image_serial_NO = models.IntegerField(default=0)
    image_height = models.IntegerField(default=0)
    image_width = models.IntegerField(default=0)
    image_upload = models.ImageField()

    def __str__(self):
        return self.card_info_ID.card_title + " -> " + self.image_title + " -> Serial No: " + str(self.image_serial_NO)

class The_All_New_Images_From_GoogleDrive(models.Model):
    Title = models.CharField(max_length=35)
    card_info_ID = models.ForeignKey(
        CardsInfo,
        on_delete = models.CASCADE
    )
    Serial_NO = models.IntegerField(default=0)
    Height = models.IntegerField(default=0)
    Width = models.IntegerField(default=0)
    Upload_Link = models.CharField(max_length=100)

    def __str__(self):
        return self.card_info_ID.card_title + " -> " + self.Title + " -> Serial No: " + str(self.Serial_NO)

class Codes(models.Model):
    code_title = models.CharField(max_length=35)
    card_info_ID = models.ForeignKey(
        CardsInfo,
        on_delete = models.CASCADE
    )
    code_serial_NO = models.IntegerField(default=0)
    code = models.TextField()

    def __str__(self):
        return self.card_info_ID.card_title + " -> " + self.code_title + " -> Serial No: " + str(self.code_serial_NO)

class Recommendations(models.Model):
    recommendation_title = models.CharField(max_length=30)
    card_info_ID = models.ForeignKey(
        CardsInfo,
        on_delete = models.CASCADE
    )
    recommendation_serial_NO = models.IntegerField(default=0)
    recommendation_link = models.CharField(max_length=300)

    def __str__(self):
        return self.card_info_ID.card_title + " -> " + self.recommendation_title + " -> Serial No: " + str(self.recommendation_serial_NO)