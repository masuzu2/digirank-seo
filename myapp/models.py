from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name + "," + str(self.age)


class Client(models.Model):
    PACKAGE_CHOICES = [
        ('basic', 'Basic SEO'),
        ('standard', 'Standard SEO'),
        ('premium', 'Premium SEO'),
        ('enterprise', 'Enterprise SEO'),
    ]
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('pending', 'Pending'),
    ]

    company_name = models.CharField(max_length=200)
    website = models.CharField(max_length=300)
    package = models.CharField(max_length=20, choices=PACKAGE_CHOICES, default='basic')
    budget = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.company_name} - {self.get_package_display()}"
