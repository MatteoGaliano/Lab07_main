from pickle import NONE

from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    # TODO
    def get_all(self):
        """Recupera tutte le biblioteche dal database e restituisce una lista di oggetti Biblioteca."""

        result = []

        cnx = DBConnect.get_connection()   # appartiene a DBConnect
        if cnx is None:
            return None    # controllo che connessione sia disponibile

        cursor = cnx.cursor(dictionary=True)  # restituisce righe come dizionari
        query = """SELECT id, nome, indirizzo
                        FROM biblioteca"""

        result = []

        try:
            cursor.execute(query)  # per far eseguire cursore
            rows = cursor.fetchall() #recupero tutte le righe
            for row in rows:
                # Creo l'oggetto Biblioteca usando i dati della riga del database
                biblioteca = Biblioteca(
                    id=row["id"],
                    nome=row["nome"],
                    indirizzo=row["indirizzo"]
                )
                result.append(biblioteca)

            cursor.close()  # RICORDA
            cnx.close()
            return result

        except Exception as e:
            print(f"Errore durante la lettura delle biblioteche: {e}")
            cursor.close()
            cnx.close()
            return None

