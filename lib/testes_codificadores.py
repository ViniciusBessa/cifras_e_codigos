from codificadores import cod_cesar, cod_vigenere, cod_onetimepad, cod_morse, cod_tapcode, cod_autokey, cod_niilista
import unittest


class CodificadoresTeste(unittest.TestCase):
    def teste_cod_cesar(self):
        self.assertEqual(
            cod_cesar('Um teste', 3), 'XP WHVWH'
        )


    def teste_cod_vigenere(self):
        self.assertEqual(
            cod_vigenere('Um teste', 'chave'), 'WT TZWVL'
        )


    def teste_cod_onetimepad(self):
        self.assertEqual(
            cod_onetimepad('Um teste', 'umachave'), 'OYTGZTZ'
        )


    def teste_cod_morse(self):
        self.assertEqual(
            cod_morse('Um teste'), '..- -- - . ... - .'
        )


    def teste_cod_tapcode_pares(self):
        self.assertEqual(
            cod_tapcode('Um teste', 1), '4,5  3,2  4,4  1,5  4,3  4,4  1,5'
        )


    def teste_cod_tapcode_pontos(self):
        self.assertEqual(
            cod_tapcode('Um teste', 2), '.... .....  ... ..  .... ....  . .....  .... ...  .... ....  . .....'
        )


    def teste_cod_autokey(self):
        self.assertEqual(
            cod_autokey('Um teste', 'chave'), 'WT TZWNQ'
        )


    def teste_cod_niilista(self):
        self.assertEqual(
            cod_niilista('Um teste', 'chave', 'palavra'), '73 67 57 38 68 67 56'
        )


if __name__ == '__main__':
    unittest.main()
