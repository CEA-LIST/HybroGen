// Read a PGM image file. ASCII format, 1 pixel per line
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include "ReadPgmImage.h"

void parseError (char * reference, char * inputLine, int defaultLen)
{
  int len;
  len = (defaultLen == 0)?strlen (reference):defaultLen;
  if (0 != strncmp (reference, inputLine, len))
    {
      printf("Pgm parse error, should be (%s) : %s\n", reference, inputLine);
      exit(-1);
    }
}

/* Write pgm image */
void writePgmImage (imgStruct_t * img, char * fileName)
{

  FILE *out = fopen(fileName, "w");
  fprintf(out, "P2\n%d %d\n255\n", img->width, img->height);

  for (int i = 0; i < img->height; i++) {
    for (int j = 0; j < img->width; j++) {
        fprintf(out, "%d ", img->pixelsArray[i][j]);
    }
    fprintf(out, "\n");
  }
  fclose (out);
}

/* Create image in memory
 * Allocate the structure
 * Allocate the pointer column
 * Then allocate all lines
 */
imgStruct_t * createImage (int height, int width)
{
  imgStruct_t *theImage;
  int line;
  theImage = malloc (sizeof (imgStruct_t));
  theImage->height = height;
  theImage->width = width;
  theImage->pixelsArray = calloc (height, sizeof (int*));
  for (line = 0; line < height; line++){
     theImage->pixelsArray[line] = calloc (width, sizeof (int));
     memset(theImage->pixelsArray[line],0,sizeof(int) * width);
  }

  return theImage;
}

// Lit le prochain entier dans le fichier en sautant les commentaires
// Retourne valeur lue en cas de succès, -1 si erreur ou fin de fichier
int readNextInt(FILE *file) {
#define MAX_LINE_LENGTH 1024
    char line[MAX_LINE_LENGTH];
    long pos;
	int value;
    if (!file)
        return -1; // Paramètres invalides
    while (1)
	  {
        pos = ftell(file);         // Sauvegarde la position actuelle

        if (fgets(line, MAX_LINE_LENGTH, file) == NULL) // Lit une ligne
		  return -1; // Fin de fichier ou erreur

        if (line[0] == '#' || line[0] == '\n') // Vérifie si c'est un commentaire ou une ligne vide
            continue;


        if (sscanf(line, "%d", &value) == 1) { // Tente de lire un entier
            // Repositionne le curseur après l'entier lu
            fseek(file, pos, SEEK_SET);
            fscanf(file, "%d", &value);
            return value;
        }
        // Si la ligne ne commence pas par # mais n'est pas un entier valide,
        // on continue à la ligne suivante
    }
    return -1;
}

/* Read PGM image in memory */
imgStruct_t * readPgmImage (char * fileName)
{
  FILE * theFile;
  char inputLine[80], line[80];
  imgStruct_t *theImage;
  int height, width, lineNo, columnNo, pixel;
  // printf("%s\n",fileName);
  theFile = fopen (fileName, "r");
  if (NULL == theFile)
	{
	  printf("Error for the file %s\n", fileName);
	  exit(-1);
	}
  fgets (inputLine, sizeof (line), theFile); // P2 format
  parseError("P2", inputLine, 0);
  fgets (inputLine, sizeof (line), theFile); // Comment  (Gimp?)
  //parseError("# Created by GIMP version", inputLine, 2);
  fgets (inputLine, sizeof (line), theFile);
  sscanf (inputLine, "%d %d\n", &width, &height); // LxH
  fgets (inputLine, sizeof (line), theFile);
  sscanf (inputLine, "%d\n", &pixel); // Max grey value
  parseError("255", inputLine, 0);
  theImage = createImage (height, width);
  //  printf("malloc image buffer %ld bytes\n", (size_t) (height * width * sizeof (short)));
  for (lineNo = 0; lineNo < height; lineNo++)
    {
      for (columnNo = 0; columnNo < width; columnNo++)
        {
          fscanf(theFile,"%i",&theImage->pixelsArray[lineNo][columnNo]);
          
		  //          fscanf (theFile, "%hd ", &theImage->pixelsArray[lineNo][columnNo] );
#ifdef DEBUG
		  //printf ("%3dx%3d=%3d\n", lineNo, columnNo, theImage->pixelsArray[lineNo][columnNo]);
#endif
        }
	  // printf ("\n");
    }
  fclose (theFile);
  return theImage;
}
