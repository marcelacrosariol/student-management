from django.db import models

from datetime import datetime


class Student(models.Model):
    ATIVO = 0
    INATIVO = 1
    CANCELADO = 2
    TRANSFERIDO = 3

    FEMININO = 0
    MASCULINO = 1
    OUTRO = 3
    NAO_REVELADO = 4

    CHOICES_SITUACAO = (
		(ATIVO, 'Ativo'),
		(INATIVO, 'Inativo'),
		(CANCELADO, 'Cancelado'),
		(TRANSFERIDO, 'Transferido'),
	)

    CHOICES_GENERO = (
        (FEMININO, 'Feminino'),
		(MASCULINO, 'Masculino'),
		(OUTRO, 'Outro'),
		(NAO_REVELADO, 'Prefiro não dizer'),
    )

    name = models.CharField('Nome', max_length=40, null=False, blank=False)
    family_name = models.CharField('Sobrenome', max_length=40, null=False, blank=False)
    birthday = models.DateField('Aniversário', blank=False, null=False)
    gender  = models.SmallIntegerField(choices=CHOICES_GENERO, default=FEMININO)
    status = models.SmallIntegerField(choices=CHOICES_SITUACAO, default=ATIVO)
    student_id = models.CharField('RA', max_length=40, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def get_full_name(self):
        return '{} {}'.format(self.name, self.family_name)

    def get_age(self):
        date_difference = datetime.now() - self.birthday
        return int(date_difference/360)
    
    def get_gender(self):
        return self.get_gender_display()
    
    def get_status(self):
        return self.get_status_display()

    def __str__(self):
        return '{} - {}'.format(self.id, self.name, self.family_name)