from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di BibliotecaDAO e LibroDAO)
'''

class Model:
    def __init__(self):
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()

    # --- LIBRI ---
    def get_libri_filtrati(self, biblioteca:str, genere:str):
        """Restituisce la lista di tutti i libri filtrati per biblioteca e/o genere (filtri opzionali)."""
        # TODO

        if biblioteca == "Nessun Filtro" and genere == "Nessun Filtro" :
            return self._libro_dao.get_all()    #lista tutti i libri

        if biblioteca != "Nessun Filtro" :
            biblioteche = self._biblioteca_dao.get_all()    #lista con biblioteca filtrata

            if biblioteche is None:
                return None    #controllo se esiste nome biblioteca

            id_biblioteca = None

            for b in biblioteche:
                if b.nome == biblioteca:
                    id_biblioteca = b.id
                    break

            if id_biblioteca is None:
                return []    #controllo se esiste id biblioteca

            if genere == "Nessun Filtro" :
                return self._libro_dao.get_by_biblioteca(id_biblioteca)  #tutti i libri della biblioteca senza filtro genere

            return self._libro_dao.get_by_biblioteca_genere(
                id_biblioteca, genere
            )   #altrimenti li filtro per genere

        return self._libro_dao.get_by_genere(genere)  #filtro solo per genere

    def get_generi(self):
        """Restituisce la lista di tutti i generi."""
        # TODO

        libri = self._libro_dao.get_all()

        if libri is None:
            return None

        generi = []

        for libro in libri:
            if libro.genere not in generi:
                generi.append(libro.genere)

        return generi

    # --- BIBLIOTECHE ---
    def get_biblioteche(self):
        """ Restituisce la lista di tutte le biblioteche."""
        # TODO

        return self._biblioteca_dao.get_all()

