#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h> 
#include <unistd.h>

void FatalError (char * msg)
{
  fprintf(stderr, "%s\n",msg);
  exit(-1);
}

#define BUFFERSIZE 1024*1024
unsigned char codeToExecute[BUFFERSIZE];
int codeSize;

int main(int argc, char * argv[])
{
    int sock;
    struct sockaddr_in server;
    int i;
    
    if (argc < 3) FatalError ("Server @ and port # to connect\n");
    server.sin_addr.s_addr = inet_addr(argv[1]);
    server.sin_family = AF_INET;
    server.sin_port = htons(atoi (argv[2]));
    i = 0;
    
    while(i < 3)
    {
      i ++;
      sock = socket(AF_INET , SOCK_STREAM , 0);
      if (sock == -1) FatalError ("Could not create socket");
      printf("Socket created");
      if (connect(sock , (struct sockaddr *)&server , sizeof(server)) < 0)
        FatalError("connect failed. Error");
      printf("Connected\n");
      bzero(codeToExecute, BUFFERSIZE*sizeof(unsigned char));
      codeSize = 0;
      if(recv(sock, &codeSize, sizeof (int), 0) < 0) FatalError("recv codeSize failed");
      printf("Receive code size %d bytes. ", codeSize);
      if(recv(sock, &codeToExecute, codeSize, 0) < 0) FatalError("recv code failed");
      printf("Received code: %s\n", codeToExecute);
      close(sock);
     }
    return 0;
}
