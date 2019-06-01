class Scenario(object):
    def scenario_happy(self):
        return (
        "Scenariusz: \n"
        "   1. Sytem wyświetla formularz logowania zawierający pola (Nr karty, Imię użytkownika, Nazwisko użytkownika)\n"
        "   2. Użytkownik wypełnia pola swoimi danymi i zatwierdza formularz\n"
        "   3. System prekierowuje na stronę powitalną\n")

    def scenario_sad(self):
        return (
            "Scenariusz: \n"
            "   1. Sytem wyświetla formularz logowania zawierający pola (Nr karty, Imię użytkownika, Nazwisko użytkownika)\n"
            "   2. Użytkownik wypełnia pola nieprawidłowymi danymi\n"
            "   3. Użytkownik zatwierdza formularz\n"
            "   4. Pojawiają się informacje o błednie wypełnionym formularzu\n")

    def scenario_blank(self):
        return (
            "Scenariusz: \n"
            "   1. Sytem wyświetla formularz logowania zawierający pola (Nr karty, Imię użytkownika, Nazwisko użytkownika)\n"
            "   2. Użytkownik  nie wypełnia pól danymi\n"
            "   3. Użytkownik zatwierdza formularz\n"
            "   4. Pojawiają się informacje o błednie wypełnionym formularzu\n")

