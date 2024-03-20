# dpr/models.py

# from django.db import models

# class Data(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)
#     age = models.IntegerField()

#     def save(self, *args, **kwargs):
#         self.name = ' '.join(self.name.split('_'))
#         super().save(*args, **kwargs)


from django.db import models

class Data(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    age = models.IntegerField()

    def save(self, *args, **kwargs):
        self.name = self.name.replace('_', ' ')
        super().save(*args, **kwargs)