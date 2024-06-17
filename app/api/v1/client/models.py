from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Client(models.Model):
    id = fields.IntField(pk=True)
    lastname = fields.CharField(max_length=100)
    firstname = fields.CharField(max_length=100)
    fathername = fields.CharField(max_length=100)
    birthday = fields.CharField(max_length=50)
    inn = fields.IntField(unique=True)
    user_fio = fields.ForeignKeyField('models.User',
                                      related_name='clients', to_field='fio', on_delete=fields.CASCADE)
    is_working = fields.CharField(max_length=50, default='Not in work')

    class Meta:
        table = "clients"


Client_Pydantic = pydantic_model_creator(Client, name="Client")
ClientIn_Pydantic = pydantic_model_creator(Client, name="ClientIn", exclude_readonly=True)
ClientOut_Pydantic = pydantic_model_creator(Client, name="ClientOut", include=(
    'id',
    'lastname',
    'firstname',
    'fathername',
    'birthday',
    'is_working',
    'user_fio'
))
