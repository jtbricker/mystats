import numpy as np

def mean(data, weights=None, trimmed=None):
    """ Calculates the average of a set of data
    
    Arguments:
        data {array-like} -- [data to be summarized (float or int)]
    
    Keyword Arguments:
        weights {array-like} -- [If provided, weights will be used to calculate the weighted average] (default: {None})
        trimmed {int} -- [If provided, mean will be calculated without the highest and lowest `x` values where `x` is parameter passed] (default: {None})
    """
    
    if data is None:
        raise ValueError("Parameter `data` must be provided")

    if len(data) == 0:
        return None

    if trimmed:
        data = sorted(data)[trimmed:len(data)-trimmed]

        if weights:
            weights = sorted(weights)[trimmed:len(weights)-trimmed]
    
    num = np.sum(data)
    denom = len(data)

    if weights:
        if len(weights) != len(data):
            raise ValueError('Parameters `data` and `weights` must have the same number of elements')

        num = np.sum(np.array(data) * np.array(weights))
        denom = np.sum(weights)

    return num / denom