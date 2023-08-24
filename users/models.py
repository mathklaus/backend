from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator
# Create your models here.


class Profile(models.Model):
    school_level = (('초등학교', '초등학교'), ('중학교', '중학교'),
                    ('고등학교', '고등학교'), ('일반', '일반'))
    level = (('1학년', '1'), ('2학년', '2'), ('3학년', '3'),
             ('4학년', '4'), ('5학년', '5'), ('6학년', '6'), ('일반', '0'))
    job = (('선생님', '선생님'), ('학생', '학생'), ('학부모님', '학부모님'))
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    초중고 = models.CharField(max_length=4, choices=school_level, blank=False)
    학년 = models.CharField(max_length=3, choices=level, blank=False)
    직업 = models.CharField(max_length=4, choices=job, default='학생', blank=False)
    본인핸드폰번호 = models.CharField(
        validators=[phoneNumberRegex], max_length=16, blank=True)
    부모님핸드폰번호 = models.CharField(
        validators=[phoneNumberRegex], max_length=16, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
