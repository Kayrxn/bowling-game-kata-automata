# Bowling Game Kata 🎳

Este repositorio contiene una resolución del "Bowling Game Kata". El objetivo del kata es calcular la puntuación total de una partida de bolos de 10 frames, aplicando las reglas para tiros normales, spares y strikes.

<br>

## Reglas 

- Una partida consta de 10 frames.
- Un frame normal suma la cantidad de bolos derribados en sus dos lanzamientos.
- **Spare**: cuando en un frame se derriban los 10 bolos entre ambos lanzamientos; el frame suma 10 + el número de bolos del siguiente lanzamiento.
- **Strike**: cuando en el primer lanzamiento se derriban los 10 bolos; el frame suma 10 + los bolos de los dos siguientes lanzamientos.
- En el décimo frame se conceden lanzamientos extra en caso de spare o strike para calcular los bonus.

<br>

## Enfoque

**Enfoque principal**

- Simplifiqué el diseño de lógica en una única clase: `ScoreCard`.
- `ScoreCard` se encarga de parsear la cadena de lanzamientos y calcular la puntuación total mediante `score()`.

**Estructura del código**

- `src/ScoreCard.py`: contiene la clase `ScoreCard` con la lógica de parsing y cálculo de puntuación.
- `tests/test_score_card.py`: contiene pruebas unitarias para validar el código.

