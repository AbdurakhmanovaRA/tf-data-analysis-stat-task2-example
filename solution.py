import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 241769496 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    x = (x-(1/2-np.exp(1)))/np.power(80, 2)
    alpha = 1 - p
    loc = x.mean()
    scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    return loc - scale * norm.ppf(1 - alpha / 2), \
           loc - scale * norm.ppf(alpha / 2)
