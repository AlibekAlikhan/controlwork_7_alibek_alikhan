from django.db import models
from django.db.models import TextChoices
from django.utils import timezone


class StatusChoice(TextChoices):
    ACTIVE = 'active', 'Активна'
    NOT_ACTIVE = 'blocked', 'Заблокировано'


# Create your models here.
class Article(models.Model):
    status = models.CharField(verbose_name="Статус", choices=StatusChoice.choices, max_length=20,
                              default=StatusChoice.ACTIVE)
    name = models.CharField(max_length=25, null=False, verbose_name="Статус")
    email = models.EmailField(max_length=254, verbose_name="Email")
    text = models.TextField(max_length=3000, null=True, verbose_name="Текст")
    is_deleted = models.BooleanField(verbose_name="удалено", null=False, default=False)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    update_at = models.DateTimeField(verbose_name="Дата обновления", null=True, default=None)

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.status = StatusChoice.NOT_ACTIVE
        self.save()

    def update(self, using=None, keep_parents=False):
        self.update_at = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.status} - {self.text}"
