import numpy as np


def compute_gradient(y, tx, w):
    """
    Compute the gradient.
    :param y:
    :param tx:
    :param w:
    :return:
    """
    e = y - np.dot(tx, w)
    return (-1 / tx.shape[0]) * np.dot(tx.T, e)


def compute_stoch_gradient(y, tx, w):
    """
    Compute a stochastic gradient from just few examples n and their corresponding y_n labels.
    :param y:
    :param tx:
    :param w:
    :return:
    """
    e = y - np.dot(tx, w)
    return (-1 / tx.shape[0]) * np.dot(tx.T, e)


def compute_loss(y, tx, w):
    """
    Calculate the loss by MSE.
    :param y:
    :param tx:
    :param w:
    :return:
    """
    e = y - np.dot(tx, w)
    return np.dot(e.T, e) / (2*tx.shape[0])


def compute_loss_mae(y, tx, w):
    """
    Calculate the loss by MAE.
    :param y:
    :param tx:
    :param w:
    :return:
    """
    e = y - np.dot(tx, w)
    return np.sum(np.absolute(e)) / (tx.shape[0])
