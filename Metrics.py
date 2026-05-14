# Import required dependencies
import numpy as np

def MAE(y_true: np.ndarray, y_pred: np.ndarray) -> np.float64:
    """ Implementation of the Mean Absolute Error (MAE) """
    ### TO BE COMPLETED BY THE STUDENTS ###
    
    errors = np.abs(y_true - y_pred)
    mae = np.mean(errors)
    return mae

def MSE(y_true: np.ndarray, y_pred: np.ndarray) -> np.float64:
    """ Implementation of the Mean Squared Error (MSE) """
    ### TO BE COMPLETED BY THE STUDENTS ###
    
    sq_errors = (y_true - y_pred) ** 2
    mse = np.mean(sq_errors)
    return mse

def R2(y_true: np.ndarray, y_pred: np.ndarray) -> np.float64:
    """ Implementation of the R2 metric """
    ### TO BE COMPLETED BY THE STUDENTS ###
    
    ss_total = np.sum((y_true - np.mean(y_true)) ** 2)
    ss_res = np.sum((y_true - y_pred) ** 2)
    if ss_total == 0:
        return 0.0

    r2 = 1 - (ss_res / ss_total)
    return r2

def Corr(y_true: np.ndarray, y_pred: np.ndarray) -> np.float64:
    """ Implementation of the Pearson's Correlation Coefficient """
    ### TO BE COMPLETED BY THE STUDENTS ###
    
    yt = y_true - np.mean(y_true)
    yp = y_pred - np.mean(y_pred)
    cov = np.sum(yt * yp)
    d = np.sqrt(np.sum(yt**2) * np.sum(yp**2))
    if d == 0:
        return 0.0
    corr = cov / d
    return corr
