from django.db import models

# Creating my models here.
#this table will be created at db.sqlite3 database 
class member(models.Model):
    def __str__(self):
        return self.member_name
    reference_id=models.CharField(max_length=200)
    member_name=models.CharField(max_length=200)
    member_contact=models.CharField(max_length=200)
    member_address=models.TextField()
    active=models.BooleanField(default=True)
