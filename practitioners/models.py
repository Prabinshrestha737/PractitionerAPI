from django.db import models


class Practitioner(models.Model):
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=255)
    telecom = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    birth_date = models.DateField()
    deceased = models.BooleanField(default=False)
    address = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='practitioner/photos/', null=True, blank=True)

    def __str__(self):
        return self.name


class Qualification(models.Model):
    practitioner = models.ForeignKey(
        Practitioner,
        on_delete=models.CASCADE,
        related_name='qualifications'
    )
    code = models.CharField(max_length=50)
    period_start = models.DateField()
    period_end = models.DateField(null=True, blank=True)
    issuer = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.practitioner.name}"


class Communication(models.Model):
    practitioner = models.ForeignKey(
        Practitioner,
        on_delete=models.CASCADE,
        related_name='communications'
    )
    language = models.CharField(max_length=50)
    preferred = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.practitioner.name}"
