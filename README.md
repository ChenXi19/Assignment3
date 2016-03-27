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


To estimate how well Euler solution approaches the real solution, a comparison between the Euler solution and the exact solution is made in this assignment.

To display how step legth influence the difference, several runs of the same equation are made with respect to different step length.

To show how the function itself can affect the accuracy, a comparison was made between problem 1 and problem 3.

## Methods 
### Numerical Methods
Numerical Method is a perticularly useful approach to solve an initial value problem. Take the free falling problem as an example, which is<br>
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%20v%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3D-g)
with g being the Gravitational constant and the initial velocity ![](http://latex.codecogs.com/gif.latex?v_0%3D0)<br>
The numerical approach to this problem is based on the Taylor expansion for v(t) at t=0,<br>
![](http://latex.codecogs.com/gif.latex?v%28t%29%3Dv%280%29&plus;v%27%280%29t&plus;%5Cfrac%7Bv%27%27%28t%29%7D%7B2%21%7Dt%5E2&plus;...)<br>If we take t to be small enough, it is always a good approximation to simply consider only the first two terms, leaving us with<br>
![](http://latex.codecogs.com/gif.latex?v%28t%29%5Capprox%20v%280%29&plus;v%27%280%29t)<br>
Similarlly by expanding v(t) at time t, we can esitimate the value ![](http://latex.codecogs.com/gif.latex?v%28t&plus;%5CDelta%20t%29) at ![](http://latex.codecogs.com/gif.latex?t%27%3Dt&plus;%5CDelta%20t) to be,<br>
![](http://latex.codecogs.com/gif.latex?v%28t&plus;%5CDelta%20t%29%3Dv%28t%29&plus;v%27%28t%29%5CDelta%20t)<br>
Therefore by repeatedly applying this method, we can estimate the value of the velcity at time ![](http://latex.codecogs.com/gif.latex?t%3D%5CDelta%20t%2C2%5CDelta%20t%2C3%5CDelta%20t...)<br>
From latter discussion, we will see that the Euler solution of the free falling problem is actually the exact solution, which is the result of the first derivative of v(t) being constant or equally the second derivative of it being zero.
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
where ![](http://latex.codecogs.com/gif.latex?M%3Dmax%5Cleft%20%7C%20f%27%27%28%5Cxi%20%29%20%5Cright%20%7C) and ![](http://latex.codecogs.com/gif.latex?dx) is the step length.<br>
Therefore, it is easy to see that two factors contribute to the errors result from Euler Method, which are step length and the value of the function's second derivetive. The second derivaive illustrates how rapidly a function change; if a function changes rapidly, the using tangent lines at each point as an approximation can result in a large error.

## Result
### Accuracy of the Euler solution
#### Problem 1: the free falling problem
![](https://raw.githubusercontent.com/ChenXi19/Assignment3/master/free%20falling10.png)<br>
The error is estimated by substracting the Euler solution and the real solution and taking the maximum of the absolute value, which is <br>
![](https://raw.githubusercontent.com/ChenXi19/Assignment3/master/Free10%20error.png)<br>
The error is almost zero but not exact zero, which is what we expected. And the non zero error can be explained by omission made during compuitation.

#### Problem 3: frictional force problem
The two solutions get from different methods are,
![](https://raw.githubusercontent.com/ChenXi19/Assignment3/master/friction100.png)<br>
where the interval is divided into 100 parts.<br>
The error is estimated by substracting the Euler solution and the real solution and taking the maximum of the absolute value, which is <br>
![](https://raw.githubusercontent.com/ChenXi19/Assignment3/master/friction100error.png)<br>
Although it is not zero, it is still small enough to guarantee the accuracy of Eulor solution.

When we took the step length smaller by dividing the interval into 1000 parts, the error became even smaller.<br>
![](https://raw.githubusercontent.com/ChenXi19/Assignment3/master/friction1000.png)<br>
with the error being<br>
![](https://raw.githubusercontent.com/ChenXi19/Assignment3/master/friction1000error.png)

### How step length affects errors 
Since the Euler solution is the exact solution of problem 1, only problem 3 will be discussed in this part. Define N as the number of times the interval is divided to indicate different step length.
#### case 1: N=10
![](https://raw.githubusercontent.com/ChenXi19/Assignment3/master/friction10.png)<br>
with the error being<br>
![](https://raw.githubusercontent.com/ChenXi19/Assignment3/master/fricton10%20error.png)

#### case 2: N=100
![](https://raw.githubusercontent.com/ChenXi19/Assignment3/master/friction100.png)<br>
with the error being<br>
![](https://raw.githubusercontent.com/ChenXi19/Assignment3/master/friction100error.png)<br>

#### case 3: N=1000
![](https://raw.githubusercontent.com/ChenXi19/Assignment3/master/friction1000.png)<br>
with the error being<br>
![](https://raw.githubusercontent.com/ChenXi19/Assignment3/master/friction1000error.png)<br>
To view code please click here [free falling problem](https://github.com/ChenXi19/Assignment3/blob/master/plot%20of%20free%20falling%20problem.py) and [frictional force problem](https://github.com/ChenXi19/Assignment3/blob/master/friction%20force%20problem.py)

## Reference and Acknowledgement 
In finishing this assignment, I would like to express my gratitude to my classmate [CaoYi](https://github.com/breakingDboy) who helped me with coding and taught me how to write them step by step. Furthermore, I also want to thank Wikipedia, the free encyclopedia for information on Taylor's Theorem.












