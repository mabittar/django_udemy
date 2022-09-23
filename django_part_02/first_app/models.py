from django.db import models
from django.urls import reverse


class Topic(models.Model):
    id = models.AutoField(primary_key=True)
    top_name = models.CharField(max_length=264, unique=True)
    

    class Meta:
        verbose_name = "topic"
        verbose_name_plural = "topics"

    def __str__(self):
        return self.top_name

    def get_absolute_url(self):
        return reverse("topic_detail", kwargs={"pk": self.pk})
    
class Webpage(models.Model):
    id = models.AutoField(primary_key=True)
    topic = models.ForeignKey(Topic, related_name="webpages", on_delete=models.CASCADE)
    name = models.CharField(max_length=264, unique=True, db_index=True)
    url = models.URLField(unique=True)
    

    class Meta:
        verbose_name = "webpage"
        verbose_name_plural = "webpages"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("topic_detail", kwargs={"pk": self.id}, args=[str(self.id)])


class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField()
    
    def __str__(self) -> str:
        return str(self.date)
