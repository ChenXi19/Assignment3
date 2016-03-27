# Assignment3-Discussion on Errors of Euler Methods 
## Abstract
Numerical method has been widely used as an approximation of the exact solution of an ordinary equation. To determine how well this approximation is, it is of great significance for us to determine errors of Euler Methods-how far the Euler solution found deriate from the exact solution. In this assignments, two factors-step length and the equation itself-have been dicussed to show how they influence the deviation. Also a way to approximately estimate the errors is included and illustrated using Problem 1 and Problem 3 of chapter 1.
## Introduction
A generally used method to estimate the difference between the real solution and the Euler solution is based on the Taylor's Theorem and the Mean-value forms of the remainder, which are<br>
* Taylor's Theorem. Let k be an interger and let ![](http://latex.codecogs.com/gif.latex?f(x)) be k times differentiable at the point x=a, then there exists a function ![](http://latex.codecogs.com/gif.latex?R_k(x))such that:<br>
![](http://latex.codecogs.com/gif.latex?f%28x%29%3Df%28a%29&plus;f%27%28a%29%28x-a%29&plus;%5Cfrac%7Bf%27%27%28a%29%28x-a%29%5E2%7D%7B2%21%7D&plus;...&plus;%5Cfrac%7Bf%5E%7B%28k%29%7D%28a%29%28x-a%29%5Ek%7D%7Bk%21%7D&plus;R_k%28x%29)<br>
and ![](http://latex.codecogs.com/gif.latex?%5Clim_%7Bx%5Crightarrow%20a%7DR_k%28x%29%3Do%28%5Cleft%20%7C%20x-a%20%5Cright%20%7C%5Ek%29)
* Mean-value forms of the remainder. Let ![](http://latex.codecogs.com/gif.latex?f%28x%29%3A%7BR%5Crightarrow%20R%7D) be ![](http://latex.codecogs.com/gif.latex?k+1)times differentiable on the open interval with ![](http://latex.codecogs.com/gif.latex?f(x)^{(k)})continuous on the closed interval between a and x. Then<br>
![](http://latex.codecogs.com/gif.latex?R_k%28x%29%3D%5Cfrac%7Bf%5E%7B%28k&plus;1%29%7D%28%5Cxi%20%29%7D%7B%28k&plus;1%29%21%7D%28x-a%29%5E%7Bk&plus;1%7D)<br>where![](http://latex.codecogs.com/gif.latex?%5Cxi) is between x and a.


To estimate how well it can determine the errors resulting from Euler Methods, a comparison is made in this assignment between what is got directly from substraction between the exact solutin and the Eural solution and the the value got from applying Taylor's theorem.

To display how step legth influence the difference, several runs of the same equation are made with respect to different step length.

## Methods 
### Numerical Methods
Numerical Method is a perticularly useful approach to solve an initial value problem. Take the free falling problem as an example, which is<br>
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%20v%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3D-g)
with g being the Gravitational constant and the initial velocity ![](http://latex.codecogs.com/gif.latex?v_0%3D0)<br>
The numerical approach to this problem is based on the Taylor expansion for v(t) at t=0,<br>
![](http://latex.codecogs.com/gif.latex?v%28t%29%3Dv%280%29&plus;v%27%280%29t&plus;%5Cfrac%7Bv%27%27%28t%29%7D%7B2%21%7Dt%5E2&plus;...)<br>If we take t to be small enough, it is always a good approximation to simply consider only the first two terms, leaving us with<br>
![](http://latex.codecogs.com/gif.latex?v%28t%29%5Capprox%20v%280%29&plus;v%27%280%29t)<br>
Similarlly by expanding v(t) at time t, we can esitimate the value ![](http://latex.codecogs.com/gif.latex?v%28t&plus;%5CDelta%20t%29) at ![](http://latex.codecogs.com/gif.latex?t%27%3Dt&plus;%5CDelta%20t) to be,<br>
![](http://latex.codecogs.com/gif.latex?v%28t&plus;%5CDelta%20t%29%3Dv%28t%29&plus;v%27%28t%29%5CDelta%20t)
### estimation of errors based on Taylor's Theorem
* Taylor's Theorem. Let k be an interger and let ![](http://latex.codecogs.com/gif.latex?f(x)) be k times differentiable at the point x=a, then there exists a function ![](http://latex.codecogs.com/gif.latex?R_k(x))such that:<br>
![](http://latex.codecogs.com/gif.latex?f%28x%29%3Df%28a%29&plus;f%27%28a%29%28x-a%29&plus;%5Cfrac%7Bf%27%27%28a%29%28x-a%29%5E2%7D%7B2%21%7D&plus;...&plus;%5Cfrac%7Bf%5E%7B%28k%29%7D%28a%29%28x-a%29%5Ek%7D%7Bk%21%7D&plus;R_k%28x%29)<br>
and ![](http://latex.codecogs.com/gif.latex?%5Clim_%7Bx%5Crightarrow%20a%7DR_k%28x%29%3Do%28%5Cleft%20%7C%20x-a%20%5Cright%20%7C%5Ek%29)
* Mean-value forms of the remainder. Let ![](http://latex.codecogs.com/gif.latex?f%28x%29%3A%7BR%5Crightarrow%20R%7D) be ![](http://latex.codecogs.com/gif.latex?k+1)times differentiable on the open interval with ![](http://latex.codecogs.com/gif.latex?f(x)^{(k)})continuous on the closed interval between a and x. Then<br>
![](http://latex.codecogs.com/gif.latex?R_k%28x%29%3D%5Cfrac%7Bf%5E%7B%28k&plus;1%29%7D%28%5Cxi%20%29%7D%7B%28k&plus;1%29%21%7D%28x-a%29%5E%7Bk&plus;1%7D)<br>where![](http://latex.codecogs.com/gif.latex?%5Cxi) is between x and a.

Therefore the differece between the first order approxiamtion and the real solution will be:<br>
![](http://latex.codecogs.com/gif.latex?f%28x%29-P_1%28x%29%3D%5Cfrac%7Bf%27%27%28%5Cxi%20%29%7D%7B2%21%7D%28x-a%29%5E2)<br>
where f(x)is the exact solution and ![](http://latex.codecogs.com/gif.latex?P_1%28x%29%3Df%28a%29&plus;%7Bf%27%28a%20%29%7D%28x-a%29) is the solution found through the Euler Method with ![]( http://latex.codecogs.com/gif.latex?e%3D%5Cfrac%7Bf%27%27%28%5Cxi%20%29%7D%7B2%21%7D%28x-a%29%5E2) being the error between them. Therefore an apporoxiamtion can be made:<br>
![](http://latex.codecogs.com/gif.latex?e%5Cleqslant%20%5Cleft%20%7C%20%5Cfrac%7Bf%27%27%28%5Cxi%20%29%7D%7B2%21%7D%28x-a%29%5E2%20%5Cright%20%7C%5Cleqslant%20%5Cfrac%7BM%7D%7B2%21%7D%28dx%29%5E2)<br>
where ![](http://latex.codecogs.com/gif.latex?M%3Dmax%5Cleft%20%7C%20f%27%27%28%5Cxi%20%29%20%5Cright%20%7C) and ![](http://latex.codecogs.com/gif.latex?dx) is the step length.

















