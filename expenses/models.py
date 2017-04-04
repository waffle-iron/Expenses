from django.db import models
from django.contrib.auth.models import User

from pycountry import currencies
from collections import namedtuple
import webcolors


class Category(models.Model):

    def __unicode__(self):
        return '%s' % self.name

    colors_list = sorted([color for color, _ in webcolors.CSS3_NAMES_TO_HEX.iteritems()])
    colors_tuples = ((color, color) for color in colors_list)

    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50, choices=colors_tuples)


class Account(models.Model):

    def __unicode__(self):
        return '%s' % self.name

    Currency = namedtuple('Currency', 'code, name')
    currencies_list = [Currency(code=curr.alpha_3, name=curr.name) for curr in currencies]
    currencies_tuples = ((curr.code, u'{} ({})'.format(curr.code, curr.name)) for curr in currencies_list)

    user = models.ForeignKey(User)
    name = models.CharField(max_length=50)
    currency = models.CharField(max_length=3, choices=currencies_tuples)
    initial_balance = models.DecimalField(max_digits=10, decimal_places=2)
    current_balance = models.DecimalField(max_digits=10, decimal_places=2)


class Operation(models.Model):

    def get_category_color(self):
        return Category.objects.get(name=self.category).color

    types_tuples = ((-1, 'expense'), (1, 'earning'))

    user = models.ForeignKey(User)
    account = models.ForeignKey(Account)
    category = models.ForeignKey(Category)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.IntegerField(choices=types_tuples)

    color = property(get_category_color)
