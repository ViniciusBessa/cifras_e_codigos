from decodificadores import decod_cesar, decod_vigenere, decod_onetimepad, decod_morse, decod_tapcode, decod_autokey, decod_niilista
import unittest


class CodificadoresTeste(unittest.TestCase):
    def teste_decod_cesar(self):
        self.assertEqual(
            decod_cesar('XP WHVWH', 3), 'UM TESTE'
        )


    def teste_decod_vigenere(self):
        self.assertEqual(
            decod_vigenere('WT TZWVL', 'chave'), 'UM TESTE'
        )


    def teste_decod_onetimepad(self):
        self.assertEqual(
            decod_onetimepad('OYTGZTZ', 'umachave'), 'UMTESTE'
        )


    def teste_decod_morse(self):
        self.assertEqual(
            decod_morse('..- -- - . ... - .'), 'UMTESTE'
        )


    def teste_decod_tapcode_pares(self):
        self.assertEqual(
            decod_tapcode('4,5  3,2  4,4  1,5  4,3  4,4  1,5', 1), 'UMTESTE'
        )


    def teste_decod_tapcode_pontos(self):
        self.assertEqual(
            decod_tapcode('.... .....  ... ..  .... ....  . .....  .... ...  .... ....  . .....', 2), 'UMTESTE'
        )


    def teste_decod_autokey(self):
        self.assertEqual(
            decod_autokey('WT TZWNQ', 'chave'), 'UM TESTE'
        )


    def teste_decod_niilista(self):
        self.assertEqual(
            decod_niilista('73 67 57 38 68 67 56', 'chave', 'palavra'), 'UMTESTE'
        )


if __name__ == '__main__':
    unittest.main()
