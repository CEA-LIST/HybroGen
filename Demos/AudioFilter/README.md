# Audio Pass Band filter demonstration


## HybroLang demonstrator

This demonstrator implement a code generator which embed the audio
filter parameter inside the binary code which avoid the necesity to
reload the parameter at each iterations

## Interesting URLS:

* What is a biquad filter :
  https://en.wikipedia.org/wiki/Digital_biquad_filter
* Source code implementation in :
  https://sourceforge.net/projects/sox/files/sox/14.4.2/ 
  ** File biqiad.c function int lsx_biquad_flow
  ** L'expression suivante :   double o0 = *ibuf*p->b0 + p->i1*p->b1 +
  p->i2*p->b2 - p->o1*p->a1 - p->o2*p->a2; utilise les parametres du
  filtre b0, b1, b2, a1, a2 qui sont "constant" durant le traitement
  du filtre.
*  Source code example: 

```C

  
int lsx_biquad_flow(sox_effect_t * effp, const sox_sample_t *ibuf,
    sox_sample_t *obuf, size_t *isamp, size_t *osamp)
{
  priv_t * p = (priv_t *)effp->priv;
  size_t len = *isamp = *osamp = min(*isamp, *osamp);
  while (len--) {
    double o0 = *ibuf*p->b0 + p->i1*p->b1 + p->i2*p->b2 - p->o1*p->a1 - p->o2*p->a2;
    p->i2 = p->i1, p->i1 = *ibuf++;
    p->o2 = p->o1, p->o1 = o0;
    *obuf++ = SOX_ROUND_CLIP_COUNT(o0, effp->clips);
  }
  return SOX_SUCCESS;
}

```
