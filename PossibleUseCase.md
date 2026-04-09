% Hybrogen Possible Use Cases
% HP Charles

## Introduction

## OpenCV
* Reference code : https://opencv.org/
* Possible optimisation : based on filters values
* Initial implementation : Demos/Stencil

## Mesa OpenGL
* Reference code : https://gitlab.freedesktop.org/mesa/mesa
* Possible optimisaion : based on transformation matrix value
  * Matrix which is "constant" during 1 image génération
  * https://gitlab.freedesktop.org/mesa/mesa/-/blob/main/src/mesa/math/m_matrix.c
* High level applications:;
  * https://www.opengl.org/archives/resources/code/samples/glut_examples/examples/examples.html
  * https://www.opengl.org/archives/resources/code/samples/glut_examples/demos/demos.html
* Initial implementation : Demos/VectorMatrix

## GMP integer / rational & FP numbers

* Reference code :  https://gmplib.org/
* Possible optimisation : based on code specialization
* Possible usage
  * CADO-NFS for big numbers factorization

## Variable precision floating point number library

* Reference code : https://mpfr.loria.fr/mpfr-current/
* Possible optimisation : based on code specialisation for
  optimization by a given number
* Memoise binary code based on input parameters

## BPF

* Possible optimisation : compile expression based on IP addresses

## SGBD

* Possible optimisation : JIT prepared query

## High performance computing

* Possible optimisation : identify possible optimization (kernel BigDfT)

## Heterogeneous environment

* Generate binary code on a node X, send it over the air on a IOT node Y

## Trigonometry function for embedded systems

* See ST micro library from ENS-Lyon article
