from django.db import models

class Material(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название")
    content = models.TextField(verbose_name="Содержимое")
    views_count = models.IntegerField(default=0, verbose_name="Просмотры")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    slug = models.CharField(max_length=150, verbose_name="slug", null=True, blank=True)



    class Meta:
        verbose_name = "Материал"
        verbose_name_plural = "Материалы"

    def __str__(self):
        return f"{self.title}"