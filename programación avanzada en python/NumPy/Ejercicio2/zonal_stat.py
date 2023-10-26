import numpy as np


def read_data(fname: str, tipo: type) -> np.ndarray:
    """
    lee los datos de un fichero y devuelve un array de numpy
    :param fname: str
        ruta del fichero
    :param tipo: type
        tipo de datos del array devuelto
    :return: np.ndarray
        array con datos del fichero
    Examples:
    --------
    >>> read_data("./datos/zonas.txt", int)
    array([[1, 1, 1, 1, 3, 3],
           [1, 1, 1, 1, 3, 1],
           [2, 2, 3, 3, 3, 4],
           [2, 2, 3, 3, 3, 4],
           [2, 2, 3, 3, 2, 2],
           [3, 3, 3, 3, 3, 2]])
    >>> read_data("./datos/valores.txt", float)
    array([[5., 3., 4., 4., 4., 2.],
           [2., 1., 4., 2., 6., 3.],
           [8., 4., 3., 5., 3., 1.],
           [4., 2., 4., 3., 2., 2.],
           [6., 3., 3., 7., 4., 2.],
           [5., 5., 2., 3., 1., 3.]])
    """
    # Escribe aquí tu código
    # No olvides documentar la función
    datos = np.loadtxt(fname, dtype=tipo)
    return datos


def set_of_areas(zonas: np.ndarray) -> set[int]:
    """
    determina las zonas distintas que existen en un array
    :param zonas: np.ndarray
        array con distintas zonas
    :return: set[int]
        conjunto de las zonas que se encuentran en el array
    Examples:
    --------
    >>> set_of_areas(np.arange(10).reshape(5, 2))
    {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    >>> set_of_areas(np.zeros(10, dtype=np.int_).reshape(5, 2))
    {0}
    >>> set_of_areas(np.array([2, 3, 4, 2, 3, 4], dtype=np.int_).reshape(3, 2))
    {2, 3, 4}
    >>> set_of_areas(np.zeros(3, dtype=np.float_))
    Traceback (most recent call last):
        ...
    TypeError: The elements type must be int, not float64
    """
    # Escribe aquí tu código
    # No olvides documentar la función
    if zonas.dtype != int:
        raise TypeError("The elements type must be int, not float64")

    return set(np.unique(zonas))


def mean_areas(zonas: np.ndarray, valores: np.ndarray) -> np.ndarray:
    """
    calcula la media de los valores en cada zona
    :param zonas: np.ndarray
        array con distintas zonas
    :param valores: np.ndarray
        array que representan los valores en cada zona
    :return: np.ndarray
        array con la media de valores en cada zona
    Examples:
    --------
    >>> mean_areas(np.array([[1, 2], [1, 2]]), np.array([[5, 6], [7, 12]]))
    array([[6., 9.],
           [6., 9.]])
    >>> mean_areas(np.array([[1, 2, 3], [1, 2, 3]]), np.array([[5, 6], [7, 12]]))
    Traceback (most recent call last):
        ...
    IndexError: Zonas: (2, 3) != Valores: (2, 2)
    """
    # Escribe aquí el código de la función mean_areas
    # No olvides documentar la función y escribir las anotaciones de tipos
    # Añade más ejemplos para doctest

    if zonas.shape != valores.shape:
        raise IndexError(f"Zonas: {zonas.shape} != Valores: {valores.shape}")

    areas = set_of_areas(zonas)
    result = np.zeros(zonas.shape)
    for area in areas:
        mean = round(valores[zonas == area].sum() / len(valores[zonas == area]), 1)
        mask = zonas == area
        result[mask] = mean

    return result


# ------------ test  --------#
import doctest


def test_doc() -> None:
    """
    The following instructions are to execute the tests of same functions
    If any test is fail, we will receive the notice when executing
    :return: None
    """
    doctest.run_docstring_examples(read_data, globals(), verbose=True)  # vemos los resultados de los test que fallan
    doctest.run_docstring_examples(set_of_areas, globals(), verbose=True)  # vemos los resultados de los test que fallan
    doctest.run_docstring_examples(mean_areas, globals(), verbose=True)  # vemos los resultados de los test que fallan


if __name__ == "__main__":
    test_doc()   # executing tests
