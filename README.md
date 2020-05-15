# eigenvalue_identity
Implementation of a "new" linear algebra identity from a paper by Peter Denton, Stephen Parke, Terrance Tao, and Xining Zhang

https://arxiv.org/pdf/1908.03795.pdf

If A is an n×n Hermitian matrix with eigenvalues λ1(A), . . . , λn(A) and i, j = 1, . . . , n, then the jth component vi,j of a unit eigenvector vi associated to the eigenvalue λi(A) is related to the eigenvalues λ1(Mj ), . . . , λn−1(Mj ) of the minor Mj of A formed by removing the jth row and column

Mostly done to brush up on numpy and linear algebra.

Current issues:
When using complex numbers, the matrices are about a hundredth of a place off. No idea why this is happening...
