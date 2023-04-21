
typedef struct
{
  int width, height;
  short *pixelsArray;
} short_image_struct;

void parseError (char * reference, char * inputLine);
short_image_struct * readPgmImage (char * fileName);
