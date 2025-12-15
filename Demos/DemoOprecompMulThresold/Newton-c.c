#define FLT double
#define abs(x) ((x < 0) ? -(x) : (x))
FLT convergence(int a, FLT precision)
{
  FLT un = 1;
  FLT un1 = 1;
  int iterationNumber = 0;
  do {
    un = un1;
    un1 = (un + (a / un)) / 2;
	printf("%3d double : %.10f\n", iterationNumber++, un1);
  } while (abs(un1 - un) > precision);
  return un1;
}

