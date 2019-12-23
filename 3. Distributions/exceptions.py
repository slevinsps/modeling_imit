class UniformWrongRange(Exception):
    """Raises when for R[a,b] b < a"""
    
class NonSupportedArgFormat(Exception):
    """Raises when method argument isn't float/int or list/np.ndarray"""
    
class ErlangWrongParams(Exception):
    """Raises when labmda not in [0, 50] or k not in [1, 50]"""