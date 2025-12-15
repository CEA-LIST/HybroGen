Status au 1 Aout

* L'optimisation "reduction de constante", ne fonctionne pas: trop de calculs sont générés -> refactoring fait.
* fait beaucoup de refactoring / simplifications
* trop d'images pour l'expérimentations : réduction du nombre d'images
* il faut utilise -O3 pour les expériementation pour être crédible
  * -O3 sur RISCV (natif & qemu) crée core dump
  * -O2 aussi,
  * O1 crée une compilette non valide 'différence entre images'
