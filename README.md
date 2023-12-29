# thompsons-group-f

This package implements _Thompson's Group $F$_, from this point simply referred to as "$F$", as a Python class. For the necessary background information on $F$, please see José Burillo's _Introduction to Thompson's Group $F$_, available from the UPC webpage [here](https://web.mat.upc.edu/pep.burillo/book_en.php).

Elements of $F$ are implemented using the following group presentation:

$$F = \left\langle x_0, x_1, x_2, \ldots, x_n, \ldots \mid x_i^{-1}x_jx_i = x_{j+i}, \text{ for } i < j \right\rangle.$$

Each element in $F$ is represented as a product of the generators $x_i$. Much of the theory behind certain features, most notably the representation of elements by "forest diagrams", as well as calculating the word length of elements, come from the paper _Forest Diagrams for Elements of Thompson's Group $F$_ (2005) by James M. Belk and Kenneth S. Brown of Cornell University, available on [arXiv here](https://arxiv.org/abs/math/0305412). 

Proper documentation (WIP) is available on [ReadTheDocs here.](http://exotic-groups.rtfd.io/)

## Current Features:
- Multiplication and division of abstract elements in $F$.
- Finding normal forms of elements.
- Representing elements by forest diagrams (in the form of strings).
- Calculating the word length of elements in terms of generators $x_0$ and $x_1$.

## Planned Features:
- Drawing of forest diagrams for elements.
- Representing of elements as pairs of binary trees.

## Requirements:
- Python 3.10 or newer.
