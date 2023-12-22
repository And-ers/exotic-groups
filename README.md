# exotic-groups
Python package used to study more exotic groups.

This package implements Thompson's Group F, from this point simply referred to as "F", as a Python class. For an introduction on F, please see José Burillo's "Introduction to Thompson's Group F", available from his UPC webpage below.

https://web.mat.upc.edu/pep.burillo/book_en.php

Elements of Thompson's Group are implemented using the following group presentation:

    〈 x₀,x₁,x₂,x₃,…,xₙ,… | xᵢxⱼxᵢ = xⱼ₊₁, for i < j 〉.

Each element is represented as a

Requirements:
- Python 3.10 or above
- NetworkX (Written using version 3.2.1)
