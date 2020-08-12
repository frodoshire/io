from random import choices


class GenerateKey:
    _CAPSKEY = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    _SMALLKEY = "abcdefghijklmnopqrstuvwxyz"
    _NUMBER = "01234567890"
    _POPULATION = _CAPSKEY + _SMALLKEY + _NUMBER

    @staticmethod
    def generate_key(length=7):
        return "".join(choices(list(GenerateKey._POPULATION), k=length))

