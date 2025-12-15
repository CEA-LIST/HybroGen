#include "colors.inc"  
#include "stones.inc"    // pre-defined scene elements

background { color White }

camera { location <3, 3, -15>    look_at  <0, 0,  0>  }
// camera { location <0, 0, -10>    look_at  <0, 0,  0>  }


#macro B (X, Y, Z, Color)
    box { <-.5, -.5, -.5>,  < .5, .5, .5> texture { pigment {color Color}} translate <X, Y, Z> }
#end

plane {<0, 1, 0>, -4  pigment {checker color Gray, color White  }}

union {
// H left bar
B(-2, -2, 0, Blue)
B(-2, -1, 0, Blue)
B(-2,  0, 0, Blue)
B(-2,  1, 0, Blue)
B(-2,  2, 0, Blue)
// H right bar
B(+2, -2, 0, Blue)
B(+2, -1, 0, Blue)
B(+2,  0, 0, Blue)
B(+2,  1, 0, Blue)
B(+2,  2, 0, Blue)
// H middle
B(-1,  0, 0, Blue)    
B( 1,  0, 0, Blue)    
B( 0,  0, 0, Blue)

}


union {
// G left bar
B(-2, -2, 0, Red)
B(-2, -1, 0, Red)
B(-2,  0, 0, Red)
B(-2,  1, 0, Red)
B(-2,  2, 0, Red)
// G top bar
B(-1,  2, 0, Red)
B( 0,  2, 0, Red)
B( 1,  2, 0, Red)
B( 2,  2, 0, Red)
// G bottom bar
B(-1, -2, 0, Red)
B( 0, -2, 0, Red)
B( 1, -2, 0, Red)
B( 2, -2, 0, Red)
// G Right part
B( 2, -1, 0, Red)
B( 2,  0, 0, Red)
B( 1,  0, 0, Red)
translate <3, 0, -3>
rotate -90*y
}
