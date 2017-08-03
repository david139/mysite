from django.db import models
from ckeditor.fields import RichTextField


class Recipe(models.Model):
    class Meta:
        verbose_name = "Recept"
        verbose_name_plural = "Receptek"

    created = models.DateTimeField(verbose_name="Dátum", auto_now_add=True)
    title = models.CharField(verbose_name="Cím", max_length=1024)
    content = RichTextField(verbose_name="Tartalom")

    def __str__(self):
        return str(self.title) + ' - ' + self.created.strftime('%Y.%m.%d. %H:%M')
