![CI Status](https://github.com/irinamoise/lab_tss/actions/workflows/python-ci.yml/badge.svg)

## Descriere Proiect
Acesta este un proiect de laborator pentru disciplina TSS, care implementeaza si testeaza o metoda de cautare a unei chei intr-un vector de lungime 5.

## Instructiuni Rulare Locala
1. Activeaza mediul virtual: `.\venv\Scripts\activate`
2. Instaleaza dependintele: `pip install coverage mutatest`
3. Rulează testele: `coverage run --branch -m unittest discover`
4. Vezi raportul: `coverage report -m`

## Semnificatie Badge
Badge-ul de sus indică dacă ultima versiune de cod (push) a trecut toate testele și a respectat pragul minim de coverage de 80%.
