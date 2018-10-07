# En klass som kontrollerar virtuella TV apparater.
# Attribut:
#    namn - en sträng som anger tv'ns nanm
#    kanal - en sträng som anger tv'ns kanal
#    volym - ett heltal som anger tv'ns volym


class TV:
    # Konstruktorn, initierar attributen namn, kanal och volym
    def __init__(self, tv_namn, tv_kanal="1", tv_volym=10):
        self.namn = tv_namn
        self.kanal = tv_kanal
        self.volym = tv_volym

    # Byta kanal
    def bytKanal(self, tv_kanal):
        self.kanal = tv_kanal

    # Sänka volym
    def sankVolym(self):
        self.volym -= 1

    # Höja volym
    def hojVolym(self):
        self.volym += 1

# -------------------- Här slutar TV-klassen -------------------- #
