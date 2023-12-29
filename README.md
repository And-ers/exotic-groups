# thompson-group-f
This package implements _Thompson's Group F_, from this point simply referred to as "_F_", as a Python class. For the necessary background information on _F_, please see José Burillo's _Introduction to Thompson's Group F_, available from the UPC webpage [here](https://web.mat.upc.edu/pep.burillo/book_en.php).

Elements of *F* are implemented using the following group presentation:

    F = 〈 x₀,x₁,x₂,…,xₙ,… | xᵢ⁻¹xⱼxᵢ = xⱼ₊₁, for i < j 〉.

Each element in *F* is represented as a product of the generators xᵢ. Much of the theory behind certain features, most notably the representation of elements by "forest diagrams", as well as calculating the word length of elements, come from the paper _Forest Diagrams for Elements of Thompson's Group F_ (2005) by James M. Belk and Kenneth S. Brown of Cornell University, available on arXiv [here](https://arxiv.org/abs/math/0305412). 

Current features include:
- Multiplication and division of abstract elements in $F$.
- Finding normal forms of elements.
- Representing elements by forest diagrams
- Calculating the word length of elements in terms of generators \{x₀,x₁\}.

Requirements:
- Python 3.10 or newer.
