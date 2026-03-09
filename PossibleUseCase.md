% Hybrogen Possible Use Cases
% HP Charles

# Introduction

# OpenCV https://opencv.org/

* Possible optimisation : based on filters values
* Initial implementation : Demos/Stencil
    
# Mesa OpenGL https://gitlab.freedesktop.org/mesa/mesa

* Possible optimisaion : based on transformation matrix value
  * Matrix which is "constant" during 1 image génération
  * https://gitlab.freedesktop.org/mesa/mesa/-/blob/main/src/mesa/math/m_matrix.c
* Initial implementation : Demos/VectorMatrix    

# Variable precision number library

* Possible optimisation : based on code specialisation for
  optimization by a given number
* Memoise binary code based on input parameters
    
# BPF
                    
* Possible optimisation : compile expression based on IP addresses

# SGBD

* Possible optimisation : JIT prepared query

# High performance computing

* Possible optimisation : identify possible optimization (kernel BigDfT)    