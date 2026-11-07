from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    # TODO
    def get_all(self):
        """Recupera tutti i libri dal database e restituisce una lista di oggetti Libro."""

        cnx = DBConnect.get_connection()   # appartiene a DBConnect
        if cnx is None:
            return None    # controllo che connessione sia disponibile

        cursor = cnx.cursor(dictionary=True)  # restituisce righe come dizionari
        query = """SELECT id, titolo, autore, genere, anno_pubblicazione, id_biblioteca
                        FROM libro"""

        result = []

        try:
            cursor.execute(query)  # per far eseguire cursore
            for row in cursor:
                result.append(Libro(row["id"],row["titolo"], row["autore"], row["genere"], row["anno_pubblicazione"], row["id_biblioteca"]))
            cursor.close()  # RICORDA
            cnx.close()
            return result

        except Exception as e:
            print(f"Errore durante la lettura dei libri: {e}")
            cursor.close()
            cnx.close()
            return None

    def get_by_biblioteca(self, id_biblioteca):
        """Recupera tutti i libri di una biblioteca."""
        result = []
        cnx = DBConnect.get_connection()
        if cnx is None:
            return None
        cursor = cnx.cursor(dictionary=True)
        query = """
            SELECT id, titolo, autore, genere,
                   anno_pubblicazione, id_biblioteca
            FROM libro
            WHERE id_biblioteca = %s
        """
        try:
            cursor.execute(query, (id_biblioteca,))
            for row in cursor:
                result.append(Libro(
                    row["id"],
                    row["titolo"],
                    row["autore"],
                    row["genere"],
                    row["anno_pubblicazione"],
                    row["id_biblioteca"]
                ))
            cursor.close()
            cnx.close()
            return result

        except Exception as e:
            print(f"Errore durante la lettura dei libri: {e}")
            cursor.close()
            cnx.close()
            return None

    def get_by_genere(self, genere):
        """Recupera tutti i libri di un determinato genere."""

        result = []

        cnx = DBConnect.get_connection()
        if cnx is None:
            return None

        cursor = cnx.cursor(dictionary=True)

        query = """
            SELECT id, titolo, autore, genere,
                   anno_pubblicazione, id_biblioteca
            FROM libro
            WHERE genere = %s
        """

        try:
            cursor.execute(query, (genere,))

            for row in cursor:
                result.append(Libro(
                    row["id"],
                    row["titolo"],
                    row["autore"],
                    row["genere"],
                    row["anno_pubblicazione"],
                    row["id_biblioteca"]
                ))

            cursor.close()
            cnx.close()
            return result

        except Exception as e:
            print(f"Errore durante la lettura dei libri: {e}")
            cursor.close()
            cnx.close()
            return None

    def get_by_biblioteca_genere(self, id_biblioteca, genere):
        """Recupera i libri di un genere in una biblioteca specifica."""

        result = []

        cnx = DBConnect.get_connection()
        if cnx is None:
            return None

        cursor = cnx.cursor(dictionary=True)

        query = """
            SELECT id, titolo, autore, genere,
                   anno_pubblicazione, id_biblioteca
            FROM libro
            WHERE id_biblioteca = %s
            AND genere = %s
        """

        try:
            cursor.execute(query, (id_biblioteca, genere))

            for row in cursor:
                result.append(Libro(
                    row["id"],
                    row["titolo"],
                    row["autore"],
                    row["genere"],
                    row["anno_pubblicazione"],
                    row["id_biblioteca"]
                ))

            cursor.close()
            cnx.close()
            return result

        except Exception as e:
            print(f"Errore durante la lettura dei libri: {e}")
            cursor.close()
            cnx.close()
            return None

