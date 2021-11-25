from rest_framework import serializers
# from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Projects, Roles, ProjectUsers, Todo
from users.serializers import UsersModelSerializer


class ProjectsSerializer(serializers.ModelSerializer):
    name_user = UsersModelSerializer()
    # И вот тут я засомневался, в api/projects html-форма стала выглядеть иначе. В остальных класса не стал делать,
    # сначала хочу разобраться

    class Meta:
        model = Projects
        fields = '__all__'


class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'


class ProjectUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectUsers
        fields = '__all__'


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
