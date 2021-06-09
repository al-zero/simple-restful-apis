from django.db import models


class TestModel(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    phone_number = models.PositiveIntegerField()
    is_live = models.BooleanField()
    amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = " Test Model"


class ModelX(models.Model):
    test_content = models.ForeignKey(TestModel, on_delete=models.CASCADE, related_name="test_content")
    mileage = models.FloatField()

    def __str__(self):
        return f"{self.test_content.name} - {self.mileage}"

    class Meta:
        verbose_name_plural = "ModelX"




