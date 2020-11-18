from django.db import models
# Create your models here.
from datetime import datetime, timedelta
import pytz
class Subject(models.Model):
    subject_name = models.TextField('Название предмета')
    class Meta:
        verbose_name = "Дисциплина"
        verbose_name_plural = "Дисциплины"

    def __str__(self):
        return self.subject_name
class Task(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    task_text = models.TextField('Текст дз')
    expire = models.DateTimeField('Дедлайн')
    def isSoon(self):
        time = self.expire
        time = str(time)
        time = time[:19]
        t1 = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
        date_format = "%Y-%m-%d %H:%M:%S"
        old_format = '%Y-%m-%d %H:%M:%S %:z'
        # dt_tz = pytz.utc.localize(time)
        time = datetime.strptime(time, date_format)
        # time = time.replace(tzinfo = None)
        # time = dt_tz.replace(tzinfo=None)
        # t1 = datetime.strptime(str(time), old_format).strftime(date_format)
        t2 = datetime.now()
        delta = t1 - t2
        print(delta.days)
        if delta.days <= 3:
            return True
    class Meta:
        verbose_name = "Задание"
        verbose_name_plural = "Задания"
    def __str__(self):
        return self.task_text
