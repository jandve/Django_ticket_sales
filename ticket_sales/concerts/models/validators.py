from django.core.exceptions import ValidationError

def validate_capacity(value):
    if value<=0:
        raise ValidationError(
        f"{value} Debe ingresar un numero mayor a 0" ,
        params={'value':value},
)

def validate_password(value):
    if  len(value)<6:
        raise ValidationError(
        f"{value} La contraseña debe tener un minimo 6 caracteres" ,
        params={'value':value},
)

def validate_price(value):
    if value<10:
        raise ValidationError(
        f"{value} Debe ingresar un numero mayor o igual a 10" ,
        params={'value':value},
)
