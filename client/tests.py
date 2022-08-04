from msauce.lib import infine_fix_echeancier
from models.titleModel import title
import datetime

titreTest = title()
titreTest.dateJouissance = datetime.datetime(2020, 7, 22)
titreTest.dateEcheance = datetime.datetime(2022, 7, 22)
titreTest.periodicite = 'Q'

infine_fix_echeancier(titreTest)
