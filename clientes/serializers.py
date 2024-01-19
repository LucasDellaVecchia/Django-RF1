from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    
    def validate(self, data):
        if not check_cpf(data["cpf"]):
            raise serializers.ValidationError({"cpf":"Número de CPF inválido!"})
        if not check_nome(data["nome"]):
            raise serializers.ValidationError({"nome":"Nome não pode conter números!"})
        if not check_rg(data["rg"]):
            raise serializers.ValidationError({"rg":"O RG precisa possuir 9 dígitos!"})
        if not check_cel(data["celular"]):
            raise serializers.ValidationError({"celular":"O celular precisa seguir o seguinte formato: 00 91234-1234 (Respeitando o espaço e traço)"})
        return data
    