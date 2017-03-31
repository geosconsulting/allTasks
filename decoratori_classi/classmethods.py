class BorsaSpesa:

    numero_borse = 1

    # @staticmethod
    # def _calcola_numero_borse():
    #     numero_borse_attive = BorsaSpesa.numero_borse
    #     BorsaSpesa.numero_borse += 1
    #     return numero_borse_attive

    @classmethod
    def _calcola_numero_borse(cls):
        numero_borse_attive = cls.numero_borse
        cls.numero_borse += 1
        return numero_borse_attive

    @classmethod
    def crea_borsa_vuota(cls,famiglia):
        return cls(famiglia, contenuto = None)

    @classmethod
    def crea_borsa_piena(cls, famiglia,componenti):
        return cls(famiglia, contenuto=componenti)

    def __init__(self, famiglia, contenuto):
        self.famiglia = famiglia
        self.contenuto = contenuto
        self.numero_borse = BorsaSpesa._calcola_numero_borse()

    def __str__(self):
        return '({}, {})'.format(self.famiglia,self.contenuto)

    def __repr__(self):
        return 'BorsaSpesa(famiglia={},lista={})'.format(self.famiglia, self.contenuto)

borsa_rossi = BorsaSpesa('Rossi',['pasta','pane','zucchero'])
print(borsa_rossi.contenuto)
print borsa_rossi.numero_borse

borsa_bianchi = BorsaSpesa('Bianchi',['uova','pane','zucchero','sale'])
print(borsa_bianchi.contenuto)
print borsa_bianchi.numero_borse

borsa_neri = BorsaSpesa('Bianchi',['uova','pane','zucchero','sale'])
print borsa_neri.numero_borse
