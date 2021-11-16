from django.core.management.base import BaseCommand
from users.models import Users
from django.contrib.auth.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        Users.objects.all().delete()

        suser = Users.objects.create_superuser('suser',
                                                'rtretyakov@outlook.com',
                                                'zaq1@WSX',
                                                is_staff=True,
                                                first_name='Roman',
                                                last_name='Tretyakov')

        user01 = Users.objects.create_user('user01', 'user01@localhoct', 'zaq1@WSX', first_name='user01')
        user02 = Users.objects.create_user('user02', 'user02@localhoct', 'xsw2#EDC', first_name='user02')
        user03 = Users.objects.create_user('user03', 'user03@localhoct', 'cde3$RFV', first_name='user03')
        user04 = Users.objects.create_user('user04', 'user04@localhoct', 'vfr4%TGB', first_name='user04')
