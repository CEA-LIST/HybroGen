// Read a PGM image file. ASCII format, 1 pixel per line
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include "ReadPgmImage.h"

void parseError (char * reference, char * inputLine)
{
  int len = strlen (reference);
  if (0 != strncmp (reference, inputLine, len))
    {
      printf("Pgm parse error, should be (%s) : %s\n", reference, inputLine);
      exit(-1);
    }
}
/* Read PGM image in memory */
short_image_struct * readPgmImage (char * fileName)
{
  FILE * theFile;
  char inputLine[80], line[80];
  short_image_struct *theImage;
  int height, width, lineNo, columnNo, pixel;

  theFile = fopen (fileName, "r");
  if (NULL == theFile)
	{
	  printf("Error for the file %s\n", fileName);
	  exit(-1);
	}
  fgets (inputLine, sizeof (line), theFile); // P2 format
  parseError("P2", inputLine);
  fgets (inputLine, sizeof (line), theFile); // Gimp comment
  parseError("# Created by GIMP version", inputLine);
  fgets (inputLine, sizeof (line), theFile);
  sscanf (inputLine, "%d %d\n", &height, &width); // LxH
  fgets (inputLine, sizeof (line), theFile);
  sscanf (inputLine, "%d\n", &pixel); // Max grey value
  parseError("255", inputLine);
  printf("Read image file %s (%dx%d)\n", fileName, height, width);
  theImage = malloc (sizeof (short_image_struct));
  printf("malloc image struct %d bytes\n", sizeof (short_image_struct));
  theImage->height = height;
  theImage->width = width;
  theImage->pixelsArray = malloc ((size_t) (height * width * sizeof (short)));
  printf("malloc image buffer %d bytes\n", (size_t) (height * width * sizeof (short)));
  for (lineNo = 0; lineNo < height; lineNo ++)
    {
      for (columnNo = 0; columnNo < width; columnNo ++)
        {
          fgets (inputLine, sizeof (line), theFile);
          sscanf (inputLine, "%hd ", &theImage->pixelsArray[lineNo*width+columnNo]);
        }
    }
  fclose (theFile);
  return theImage;
}
