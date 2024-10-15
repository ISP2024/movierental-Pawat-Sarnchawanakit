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
5.2. I think the method should be in the Movie class for the following reasons:  
 - Informatiion Expert: The movie class contains all the information needed in this method.  
 - High Cohesion: The movie class deals with movie stuff such as genre and release year.  
   Putting the method here means it will keep releated functionalities such as pricing logic for movie of such properties together.  
 - Single resposibility principle: While one may think that putting this method inside the Movie class violates this principle, I disagree. I think that this method has its focus on movie-related information and doesn't introduce any responsibility other than dealing with movie related stuff.  
 - Low coupling: By putting the method here, it minimizes dependencies that Rental or PriceStrategy would otherwise have with Movie.  
