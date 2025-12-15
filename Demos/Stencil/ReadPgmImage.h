
typedef struct
{
  int width, height;
  int **pixelsArray;
} imgStruct_t;

void parseError (char * reference, char * inputLine, int defaultLen);
imgStruct_t * readPgmImage (char * fileName);
imgStruct_t * createImage (int height, int width);
void writePgmImage (imgStruct_t * img, char * fileName);
