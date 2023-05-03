from django.test import TestCase
from users.models import User
from addresses.models import Address
from django.db import IntegrityError


class UserModelTest(TestCase):
    # @classmethod
    # def setUpTestData(cls) -> None:
    #     # cls.user_data = {
    #     #     "username": "rogerinho_do_grau",
    #     #     "first_name": "Rogério",
    #     #     "last_name": "do Grau",
    #     #     "email": "rogerinho171@mail.com",
    #     #     "is_seller": False,
    #     # }

    #     # cls.user_data_2 = {
    #     #     "username": "miltinho_do_corre",
    #     #     "first_name": "Milton",
    #     #     "last_name": "do Corre",
    #     #     "email": "miltinho171@mail.com",
    #     #     "is_seller": False,
    #     # }

    #     # cls.address = {
    #     #     "street": "Rua dos loucos",
    #     #     "number": 171,
    #     #     "city": "Diadema",
    #     #     "state": "SP",
    #     #     "zipcode": "01234-567"
    #     # }

    #     # cls.user = User.objects.create(**cls.user_data)
    #     # cls.user_2 = User.objects.create(**cls.user_data_2)      
    def test_email_properties(self):
        expected = 127
        result = User._meta.get_field("email").max_length
        msg = f"Verifique se a propriedade `max_length` de `email` foi definida como `{expected}`"
        self.assertEqual(expected, result, msg)

        result = User._meta.get_field("email").unique
        msg = f"Verifique se o atributo `email` foi definido como unico"
        self.assertTrue(result, msg)

        result = User._meta.get_field("email").null
        msg = f"Verifique se o atributo `email` foi definido como obrigatório"
        self.assertFalse(result, msg)

    def test_first_name_properties(self):
        expected = 50
        result = User._meta.get_field("first_name").max_length
        msg = f"Verifique se a propriedade `max_length` de `first_name` foi definida como `{expected}`"
        self.assertEqual(expected, result, msg)

        result = User._meta.get_field("first_name").null
        msg = f"Verifique se o atributo `first_name` foi definido como obrigatório"
        self.assertFalse(result, msg)

    def test_last_name_properties(self):
        expected = 50
        result = User._meta.get_field("last_name").max_length
        msg = f"Verifique se a propriedade `max_length` de `last_name` foi definida como `{expected}`"
        self.assertEqual(expected, result, msg)

        result = User._meta.get_field("last_name").null
        msg = f"Verifique se o atributo `last_name` foi definido como obrigatório"
        self.assertFalse(result, msg)

    def test_username_properties(self):
        expected = 50
        result = User._meta.get_field("username").max_length
        msg = f"Verifique se a propriedade `max_length` de `username` foi definidade como `{expected}`"
        self.assertEqual(expected, result, msg)

        result = User._meta.get_field("username").unique
        msg = f"Verifique se o atributo `username` foi definido como unico"
        self.assertTrue(result, msg)

        result = User._meta.get_field("username").null
        msg = f"Verifique se o atributo `birthdate` foi definido como obrigatório"
        self.assertFalse(result, msg)

    def test_is_seller_properties(self):
        result = User._meta.get_field("is_seller").default
        msg = f"Verifique se o valor padrão de `is_seller` foi definido como `False`"
        self.assertFalse(result, msg)

    def test_image_user_properties_null_or_blank(self):
        result_nullable = User._meta.get_field("image_user").null
        result_blankable = User._meta.get_field("image_user").blank
        msg = f"Verifique se o atributo `image_user` foi definido como opcional"
        self.assertTrue(result_nullable, msg)
        self.assertTrue(result_blankable, msg)

    # def test_user_address_relations(self):
    #     created_address = Address.objects.create(**self.address)
    #     msg = f"Verifica se o atributo `address` foi criado com sucesso"
    #     self.user.address = created_address
    #     self.user.save()

    #     self.assertIs(self.user.address, created_address, msg)
    #     self.assertIs(self.user, created_address.user, msg)

    # def test_if_raise_error_when_address_already_have_in_user(self):
    #     created_address = Address.objects.create(**self.address)
    #     self.user.address = created_address
    #     self.user.save()

    #     with self.assertRaises(IntegrityError):
    #         self.user_2.address = created_address
    #         self.user_2.save()