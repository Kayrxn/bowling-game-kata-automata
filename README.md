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

- Simplifiqué el diseño para que toda la lógica de cálculo resida en una única clase: `ScoreCard`.
- `ScoreCard` ahora se encarga de parsear la cadena de lanzamientos y calcular la puntuación total mediante el método `score()`.

**Estructura del código**

- `src/ScoreCard.py`: contiene la clase `ScoreCard` con la lógica de parsing y cálculo de puntuación.
- `src/automaton.py`: eliminado (la lógica se integró en `ScoreCard`). Si alguien intenta importarlo, lanzará un error con la orientación a usar `ScoreCard`.
- `test/test_automaton.py`: actualizado para usar directamente `ScoreCard` (se mantiene el nombre del archivo por compatibilidad).

**Decisiones de diseño**

- Centralicé la lógica en `ScoreCard` para reducir la complejidad y facilitar las pruebas y el mantenimiento.
- Mantengo tests que documentan el comportamiento esperado (casos simples, spares, strikes y perfect game).


