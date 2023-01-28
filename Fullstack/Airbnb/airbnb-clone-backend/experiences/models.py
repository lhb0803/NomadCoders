from django.db import models
from common.models import CommonModel

class Experience(CommonModel):
    """
    Experience Model Definition
    """
    name = models.CharField(max_length=180, default="")
    country = models.CharField(max_length=50, default="한국")
    city = models.CharField(max_length=80, default="서울")
    host = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="experiences",)
    price = models.PositiveIntegerField()
    address = models.CharField(max_length=250)
    description = models.TextField(max_length=250, blank=True, null=True)

    start_at = models.TimeField()
    end_at = models.TimeField()
    perks = models.ManyToManyField("experiences.Perk", related_name="experiences",)
    
    category = models.ForeignKey(
        "categories.Category", 
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="experiences",
    )

    def __str__(self) -> str:
        return self.name
    
class Perk(CommonModel):
    """
    What is included on an Experience
    """
    name = models.CharField(max_length=180)
    details = models.CharField(max_length=250, blank=True, null=True)
    explanation = models.TextField()

    def __str__(self) -> str:
        return self.name