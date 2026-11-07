import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    # TODO
    def popola_dropdown(self):

        biblioteche = self._model.get_biblioteche()  # recupero biblioteche da Model

        self._view.dd_biblioteca.options = [ft.dropdown.Option("Nessun Filtro")]

        if biblioteche is not None:
            for biblioteca in biblioteche:
                self._view.dd_biblioteca.options.append(ft.dropdown.Option(biblioteca.nome))

        generi = self._model.get_generi()

        self._view.dd_genere.options = [ft.dropdown.Option("Nessun Filtro")]

        if generi is not None:
            for genere in generi:
                self._view.dd_genere.options.append(ft.dropdown.Option(genere))

        self._view.update()  #RICORDA IMPORTANTE!!!!!

    # CALLBACKS DROPDOWN
    # TODO

    def seleziona_biblioteca(self,e):
        self.biblioteca_selezionata = e.control.value

    def seleziona_genere(self,e):
        self.genere_selezionato = e.control.value

    # AZIONE: MOSTRA LIBRI
    # TODO

    def mostra_libri(self, e):

        libri = self._model.get_libri_filtrati(
            self.biblioteca_selezionata,
            self.genere_selezionato
        )

        self._view.lv_libri.controls.clear()

        if libri is None:
            self._view.show_alert("Errore durante il recupero dei libri.")
            return

        if len(libri) == 0:
            self._view.show_alert("Nessun libro trovato.")
            self._view.update()
            return

        for libro in libri:
            self._view.lv_libri.controls.append(
                ft.Text(str(libro))
            )

        self._view.update()