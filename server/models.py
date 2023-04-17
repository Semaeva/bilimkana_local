from django.db import models
from django.utils.translation import gettext as _
from parler.models import TranslatableModel, TranslatedFields, TranslatedFieldsModel


# Create your models here.

class News(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(_("Заголовк"), max_length=254, default=''),
        description=models.TextField(_('Описание'))
    )
    image = models.ImageField('Изображение', upload_to='newsImages/main/')
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Новости"
        verbose_name = "Новости"
        ordering = ['-created_date']


class NewsImage(models.Model):
    image = models.FileField(upload_to='newsImage/all/')
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name="news_images")

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name_plural = "Галерея новостей"
        verbose_name = "Галерея новостей"


class Teachers(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(_("Инициалы Учителя"), max_length=254, default=''),
        description=models.TextField(_('Описание'))
    )
    image = models.ImageField('Фотография', upload_to='teachers/main/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Учителя"
        verbose_name = "Учителя"


class Managers(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(_("Инициалы Учителя"), max_length=254, default=''),
        title=models.TextField(_('должность'))
    )
    image = models.ImageField('Фотография', upload_to='managers/main/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Руководство"
        verbose_name = "Руководство"


class OurPartner(models.Model):
    title = models.CharField('Наименование', max_length=250, default='')
    image = models.ImageField(upload_to='partners/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Партнеры"
        verbose_name = "Партнеры"


class Projects(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(_("Наименование"), max_length=254, default=''),
        description=models.TextField(_('Описание'))
    )
    image = models.ImageField('Фотография', upload_to='projects/main/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Проектная деятельность"
        verbose_name = "Проектная деятельность"


class CallBack(models.Model):
    name = models.CharField(max_length=254, default='')
    phone = models.CharField(max_length=100, default='')
    age = models.IntegerField(default=0)
    school = models.CharField(max_length=250, default="")

    def __str__(self):
        return f'ФИО: {self.name}, номер: {self.phone}'

    class Meta:
        verbose_name_plural = "Обратный звонок"
        verbose_name = "Обратный звонок"


class Contact(TranslatableModel):
    translations = TranslatedFields(
        email=models.EmailField(default=''),
        phone=models.CharField('Телефон', max_length=254, default=''),
        address=models.CharField('Адрес', max_length=254, default='')
    )
    insta = models.CharField("Ссылка на инстаграм", max_length=254, default='', blank=True, null=True)

    def __str__(self):
        return "Контакты"

    class Meta:
        verbose_name_plural = "Контакты"
        verbose_name = "Контакты"