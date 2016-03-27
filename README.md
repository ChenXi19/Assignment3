# Assignment3-Discussion on Errors of Euler Methods 
## Abstract
Numerical method has been widely used as an approximation of the exact solution of an ordinary equation. To determine how well this approximation is, it is of great significance for us to determine errors of Euler Methods-how far the Euler solution found deriate from the exact solution. In this assignments, two factors-step length and the equation itself-have been dicussed to show how they influence the deviation. Also a way to approximately estimate the errors is included and illustrated using Problem 1 and Problem 3 of chapter 1.
## Introduction
The method normally used to estimate the difference between the real solution and the Euler solution is generally based on the Taylor's Theorem and the Meanvalue Theorem, which are<br>
* Taylor's Theorem. Let k be an interger and let ![](http://latex.codecogs.com/gif.latex?f(x)) be k times differentiable at the point x=a, then there exists a function ![](http://latex.codecogs.com/gif.latex?h_k(x))such that:<br>
![](http://latex.codecogs.com/gif.latex?f%28x%29%3Df%28a%29&plus;f%27%28a%29%28x-a%29&plus;%5Cfrac%7Bf%27%27%28a%29%28x-a%29%5E2%7D%7B2%21%7D&plus;...&plus;%5Cfrac%7Bf%5E%7B%28k%29%7D%28a%29%28x-a%29%5Ek%7D%7Bk%21%7D&plus;h_k%28x%29%28x-a%29%5E%7Bk%7D)<br>
and ![](http://latex.codecogs.com/gif.latex?%5Clim_%7Bx%5Crightarrow%200%7Dh_k%28x%29%3D%200)
* Mean-value forms of the remainder. Let ![](http://latex.codecogs.com/gif.latex?f(x):R\rightarrowR)be![](http://latex.codecogs.com/gif.latex?k+1)times differentiable on the open interval with ![](http://latex.codecogs.com/gif.latex?f(x)^(k))continuous on the closed interval between a and x. Then<br>
