import FreeSimpleGUI as sg

from .app_layout import appLayout
from entiteit.top30 import Top30
from bin.imagetkhelper import ImageTKHelper

class App:
    def __init__(self):
        self._top30 = Top30()

    def toon(self):
        venster = sg.Window(
            title = 'TOP 30',
            layout = appLayout(),
            resizable = False,
            disable_close = True,
            disable_minimize = True,
            finalize = True
        )

        venster['-LBX-TOP30-'].update(values = self._top30.lijst())
        self._update(venster, self._top30.lijst()[0])

        while True:
            evt, vals = venster.read()

            match evt:
                case sg.WIN_CLOSED | '-BTN-AFSLUITEN-':
                    break

                case '-LBX-TOP30-':
                    liedje = vals['-LBX-TOP30-'][0]
                    self._update(venster, liedje)

        venster.close()

    def _update(self, venster, liedje):
        venster['-TXT-PERFORMER-'].update(liedje.performer)
        venster['-TXT-TITEL-'].update(liedje.titel)
        foto = ImageTKHelper.schaal(f'data/afbeeldingen/{liedje.foto}', grootte=(250,250))
        venster['-IMG-FOTO-'].update(data = foto)