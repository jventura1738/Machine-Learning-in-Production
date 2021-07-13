Financial-Models-Numerical-Methods 
==================================


This is a collection of [Jupyter notebooks](https://jupyter.org/) based on different topics in the area of quantitative finance.


### Is this a tutorial?

Almost! :) 

This is just a collection of topics and algorithms that in my opinion are interesting.     

It contains several topics that are not so popular nowadays, but that can be very powerful. 
Usually, topics such as PDE methods, Lévy processes, Fourier methods or Kalman filter are not very popular among practitioners, who prefers to work with more standard tools.     
The aim of these notebooks is to present these interesting topics, by showing their practical application through an interactive python implementation.


### Who are these notebooks for?

Not for absolute beginners. 

These topics require a basic knowledge in stochastic calculus, financial mathematics and statistics. A basic knowledge of python programming is also necessary.

In these notebooks I will not explain what is a call option, or what is a stochastic process, or a partial differential equation.     
However, every time I will introduce a concept, I will also add a link to the corresponding wiki page or to a reference manual.
In this way, the reader will be able to immediately understand what I am talking about. 

These notes are for students in science, economics or finance who have followed at least one undergraduate course in financial mathematics and statistics.       
Self-taught students or practicioners should have read at least an introductiory book on financial mathematics. 


### Why is it worth to read these notes?  

First of all, this is not a book!      
Every notebook is (almost) independent from the others. Therefore you can select only the notebook you are interested in!

```diff
- Every notebook contains python code ready to use!     
```

It is not easy to find on internet examples of financial models implemented in python which are ready to use and well documented.    
I think that beginners in quantitative finance will find these notebooks very useful!  

Moreover, Jupyter notebooks are interactive i.e. you can run the code inside the notebook. 
This is probably the best way to study!

If you open a notebook with Github or [NBviewer](https://nbviewer.ipython.org), sometimes mathematical formulas are not displayed correctly. 
For this reason, I suggest you to clone/download the repository. 


### Is this series of notebooks complete?

**No!**    
I will upload more notebooks from time to time. 

At the moment, I'm interested in the areas of stochastic processes, Kalman Filter, statistics and much more. I will add more interesting notebooks on these topics in the future. 

If you have any kind of questions, or if you find some errors, or you have suggestions for improvements, feel free to contact me.      



### Contents

1.1) **Black-Scholes numerical methods**
*(lognormal distribution, change of measure, Monte Carlo, Binomial method)*.

1.2) **SDE simulation and statistics**
*(paths generation, Confidence intervals, Hypothesys testing, Geometric Brownian motion, Cox-Ingersoll-Ross process, Euler Maruyama method, parameters estimation)*

1.3) **Fourier inversion methods**
*(inversion formula, numerical inversion, option pricing, FFT, Lewis formula)*

1.4) **SDE, Heston model**
*(correlated Brownian motions, Heston paths, Heston distribution, characteristic function, option pricing)*

1.5) **SDE, Lévy processes** 
*(Merton, Variance Gamma, NIG, path generation, parameter estimation)*

2.1) **The Black-Scholes PDE** 
*(PDE discretization, Implicit method, sparse matrix tutorial)*

2.2) **Exotic options**
*(Binary options, Barrier options, Asian options)*

2.3) **American options**
*(PDE, Early exercise, Binomial method, Longstaff-Schwartz, Perpetual put)*

3.1) **Merton Jump-Diffusion PIDE**
*(Implicit-Explicit discretization, discrete convolution, model limitations, Monte Carlo, Fourier inversion, semi-closed formula )*

3.2) **Variance Gamma PIDE**
*(approximated jump-diffusion PIDE, Monte Carlo, Fourier inversion, Comparison with Black-Scholes)*

3.3) **Normal Inverse Gaussian PIDE** 
*(approximated jump-diffusion PIDE, Monte Carlo, Fourier inversion, properties of the Lévy measure)*

4.1) **Pricing with transaction costs** 
*(Davis-Panas-Zariphopoulou model, singular control problem, HJB variational inequality, indifference pricing, binomial tree, performances)*

4.2) **Volatility smile and model calibration**
*(Volatility smile, root finder methods, calibration methods)*

5.1) **Linear regression and Kalman filter** 
*(market data cleaning, Linear regression methods, Kalman filter design, choice of parameters)*

5.2) **Kalman auto-correlation tracking - AR(1) process** 
*(Autoregressive process, estimation methods, Kalman filter, Kalman smoother, variable autocorrelation tracking)*

5.3) **Volatility tracking** 
*(Heston simulation, hypothesis testing, distribution fitting, estimation methods, GARCH(1,1), Kalman filter, Kalman smoother)*

6.1) **Ornstein-Uhlenbeck process and applications**
*(parameters estimation, hitting time, Vasicek PDE, Kalman filter, trading strategy)*

7.1) **Classical MVO**
*(mean variance optimization, quadratic programming, only long and long-short, closed formula)*

A.1) **Appendix: Linear equations** 
*(LU, Jacobi, Gauss-Seidel, SOR, Thomas)*
  
A.2) **Appendix: Code optimization** 
*(cython, C code)*

A.3) **Appendix: Review of Lévy processes theory**
*(basic and important definitions, derivation of the pricing PIDE)*



## How to run the notebooks 

You have several options:

1) **Docker:** Install [docker](https://www.docker.com/) following the instructions in [install link](https://docs.docker.com/install/) 

At this point, you just need to run the script `docker_start_notebook.py`, i.e enter in the shell the following code:

```bash
python docker_start_notebook.py
```

The script will download the data-science docker image [scipy-notebook](https://hub.docker.com/r/jupyter/scipy-notebook), that will be used every time you run the script (the script will take about 10-15 minutes to download the image, ONLY the first time). You can also download a different image by modifying the script. For a list of images see [here](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html).

2) **Virtual environment:**
Here I explain how to create a virtual environment with [Anaconda](https://www.anaconda.com/distribution/). A possible alternative could be to use the python module [venv](https://docs.python.org/3.7/tutorial/venv.html). 

```bash
conda create -n FMNM python=3.7.3
source activate FMNM
pip install --requirement requirements.txt
```

3) If you prefer to use the python version already installed in your system, you just need to check that all the packages listed in `requirements.txt` are installed, and then enter in the shell the code:

```bash
jupyter-notebook
```

However, if you are using old versions, there could be compatibility problems.


#### If you wish to use a different python version or a different docker image, you will probably need to recompile the Cython code!

If you are using the data science image, you can open the shell in the notebooks directory, and run the script 
```bash
python docker_start_notebook.py
```

after that, paste the following code into the shell:

```bash 
docker exec -it Numeric_Finance bash
cd work/functions/cython
python setup.py build_ext --inplace
exit
``` 
(`Numeric_Finance` is the name of the docker container)

If you are not using docker, just copy in the shell the following:

```bash 
cd functions/cython
python setup.py build_ext --inplace
``` 


### Enjoy!