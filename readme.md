# LABO-3 Jens Deryckere

Flask-folder -> Client:
- Luistert naar wijzigingen in environment-document binnen Firebase
- Stuurt wijzigingen van de matrix (kleur) door naar Firebase

Sensehat_dashboard-folder -> Server:

- Environment.py: om x-aantal minuten worden de waarden van de omgevingssensoren doorgestuurd naar Firebase
- Matrix.py: de server luistert naar wijzigingen in matrix-document binnen Firebase
