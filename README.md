## Movie Rental Refactoring

A classic refactoring problem from Chapter 1 of
_Refactoring: Improving the Design of Existing Code_ by Martin Fowler.  

This repository contains Python code translated from the Java version.

The runnable `main.py` creates a customer and prints a statement.


## Instructions

See [Movie Rental Refactoring, Part 1](https://cpske.github.io/ISP/assignment/movierental/movierental-part1) for description of the code and what to do.

Before and after each refactoring you should **run the unit tests**.

## Resources

See [Resources](https://cpske.github.io/ISP/assignment/movierental/movierental-part1#resources) in the assignment description.

## Rationale
2.1. Feature Envy
2.2. Single Responsibility Principle. The Movie class should only know about the movie itself. How to price is is not a property of a movie and may differ in different store and thus isn't the responsibility of the Movie class. Having it store the price strategy adds an additional responsibility on how to price the movie onto the Movie class violating the single resposibility principle.  
