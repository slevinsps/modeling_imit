import numpy as np
from scipy.special import factorial, erf
from abc import ABC, abstractmethod

from exceptions import UniformWrongRange, \
    NonSupportedArgFormat, ErlangWrongParams


class ContinuousDist(ABC):   
    @abstractmethod
    def cdf(self, x):
        pass
    
    @abstractmethod
    def pdf(self, x):
        pass 


class DiscreteDist(ABC):
    @abstractmethod
    def cdf(self, k):
        pass

    @abstractmethod
    def pmf(self, k):
        pass


class UniformDist(ContinuousDist): 
    def __init__(self, a=0, b=1): 
        if a > b:
            raise UniformWrongRange("For R[a, b] b should be greater than a")
        self.a = a
        self.b = b
        self.name = 'Uniform distribution'
        
    def _cdf_array(self, x):            
        res = (x - self.a) / (self.b - self.a)  
        res[self.b < x] = 1.
        res[self.a > x] = 0.
        
        return res
    
    def _cdf_float(self, x):
        if self.b < x:
            return 1.
        if self.a > x:
            return 0.
        return (x - self.a) / (self.b - self.a)
        
    def cdf(self, x):
        if isinstance(x, np.ndarray) or isinstance(x, list):
            return self._cdf_array(x)
        if isinstance(x, float) or isinstance(x, int):
            return self._cdf_float(x)
        raise NonSupportedArgFormat("{} type is not supported".format(type(x)))
    
    def _pdf_array(self, x):        
        res = np.ones(x.shape) / (self.b - self.a)
        res[self.b < x] = 0.
        res[self.a > x] = 0.

        return res
    
    def _pdf_float(self, x):
        if self.a <= x <= self.b:
            return 1. / (self.b - self.a)    
        return 0.
   
    def pdf(self, x):
        if isinstance(x, np.ndarray) or isinstance(x, list):
            return self._pdf_array(x)
        if isinstance(x, float) or isinstance(x, int):
            return self._cdf_float(x)
        raise NonSupportedArgFormat("{} type is not supported".format(type(x)))


    def __str__(self):
        return "R[{}, {}] distribution".format(self.a, self.b)


class ErlangDist(ContinuousDist):
    def __init__(self, k=1, lambda_=2.):
        if not isinstance(k, int):
            raise TypeError("K parameter should be int")      
        if k <= 0 or k > 50:
            raise ErlangWrongParams("K parameter should be in [1, 50] range")   
        if lambda_ < 0. or lambda_ > 50.:
            raise ErlangWrongParams("Lambda parameter should be in [0, 50] range")
        
        self.k = k
        self.lambda_ = lambda_
        self.name = 'Erlang distribution'
        
        self.lambda_power_k = np.power(lambda_, k)
        self.k_1_factorial = np.math.factorial(k-1)
        
    def pdf(self, x):
        return self.lambda_power_k * np.power(x, self.k - 1) * np.exp(-self.lambda_ * x) / self.k_1_factorial
    
    def cdf(self, x):        
        res = np.zeros((self.k, x.shape[0]))
        
        for i in range(self.k):
            res[i] = 1 / np.math.factorial(i) * np.exp(-self.lambda_ * x) * np.power(self.lambda_ * x, i)
            
        return 1 - np.sum(res, axis=0)

    def __str__(self):
        return "Erlang[k={}, lambda={}] distribution".format(self.k, self.lambda_)


class ExponentialDist(ContinuousDist):
    def __init__(self, lambda_):
        if lambda_ < 0:
            raise ValueError("Lambda parameter should be >= than 0")
        self.lambda_ = lambda_
        self.name = 'Exponential distribution'

    #TODO: pdf and cdf for one value
    def pdf(self, x):
        res = self.lambda_ * np.exp(-self.lambda_ * x)
        res[x < 0] = 0

        return res

    def cdf(self, x):
        res = 1. - np.exp(-self.lambda_ * x)
        res[x < 0] = 0

        return res

    def __str__(self):
        return "Exp[lambda={}] distribution".format(self.lambda_)


class NormalDist(ContinuousDist):
    def __init__(self, mean, variance):
        if variance < 0:
            raise ValueError("Variance parameter should be >= than 0")
        self.mean = mean
        self.variance = variance
        self.name = 'Gaussian distribution'

    def pdf(self, x):
        return 1. / np.sqrt(2 * np.pi * self.variance) * np.exp(-np.square(x - self.mean) / 2 * self.variance)

    def cdf(self, x):
        return 0.5 * (1 + erf((x - self.mean) / np.sqrt(2 * self.variance)))

    def __str__(self):
        return "N[mean={}, variance={}] distribution".format(self.mean, self.variance)


class PoissonDist(DiscreteDist):
    def __init__(self, lambda_):
        if lambda_ < 0:
            raise ValueError("Lambda parameter should be >= than 0")
        self.lambda_ = lambda_
        self.name = 'Poisson distribution'

    def pmf(self, k):
        return np.power(self.lambda_, k) * np.exp(-self.lambda_) / factorial(k)

    def _cdf_int(self, value):
        if value < 0:
                raise ValueError("K argument should be >= than 0")
        res = 0
        for i in range(value + 1):
            res += np.power(self.lambda_, i) / factorial(i)
        return res

    def _cdf_array(self, arr):
        high = np.max(arr)
        res = np.zeros((high + 1))

        for i in range(high + 1):
            res[i] = np.power(self.lambda_, i) / factorial(i) + res[i-1]
        return res[arr]

    def cdf(self, k):
        if isinstance(k, np.ndarray) or isinstance(k, list):
            return self._cdf_array(k)
        if isinstance(k, int):
            return self._cdf_int(k)
        raise NonSupportedArgFormat("{} type is not supported".format(type(k)))

    def __str__(self):
        return "Pois[lambda={}] distribution".format(self.lambda_)
