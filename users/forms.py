from django.db import models

class UserName(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Имя пользователя',
        unique=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    
    class Meta:
        verbose_name = 'Имя пользователя'
        verbose_name_plural = 'Имена пользователей'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name
