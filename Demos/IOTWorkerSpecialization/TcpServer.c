#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <netdb.h>
#include <netinet/in.h>
#include <signal.h>
#include <string.h>
#include <arpa/inet.h> 
#include <sys/socket.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

void FatalError (char * msg)
{
  fprintf(stderr, "%s\n",msg);
  exit(-1);
}

char codeGenerated[] = "Generated code\n";
int codeLen;

/* https://beej.us/guide/bgnet/html//index.html#a-simple-stream-server */
int main(int argc, char * argv[])
{
  int sockfd, new_fd;  // listen on sock_fd, new connection on new_fd
  struct addrinfo hints, *servinfo, *p;
  struct sockaddr_storage their_addr; // connector's address information
  socklen_t sin_size;
  struct sigaction sa;
  int yes=1;
  char s[INET6_ADDRSTRLEN];
  int rv;

  if (argc != 2)
    {
      FatalError("Give port #");
    }
  memset(&hints, 0, sizeof hints);
  hints.ai_family = AF_UNSPEC;
  hints.ai_socktype = SOCK_STREAM;
  hints.ai_flags = AI_PASSIVE; // use my IP

  if ((rv = getaddrinfo(NULL, argv[1], &hints, &servinfo)) != 0) {
        fprintf(stderr, "getaddrinfo: %s\n", gai_strerror(rv));
        return 1;
    }
  // loop through all the results and bind to the first we can
  for(p = servinfo; p != NULL; p = p->ai_next)
    {
      if ((sockfd = socket(p->ai_family, p->ai_socktype, p->ai_protocol)) == -1)
        {
          perror("server: socket");
          continue;
        }
      if (setsockopt(sockfd, SOL_SOCKET, SO_REUSEADDR, &yes, sizeof(int)) == -1) 
        FatalError("setsockopt");
      
      if (bind(sockfd, p->ai_addr, p->ai_addrlen) == -1)
        {
          close(sockfd);
          perror("server: bind");
          continue;
        }
      break;
    }
  freeaddrinfo(servinfo); // all done with this structure
  if (p == NULL)  FatalError("server: failed to bind\n");
  if (listen(sockfd, 2) == -1) FatalError("listen");   /* 2 pending connection */
  printf("server: waiting for connections...\n");
  codeLen = strlen(codeGenerated);
  while(1)
    {
      sin_size = sizeof their_addr;
      new_fd = accept(sockfd, (struct sockaddr *)&their_addr, &sin_size);
      if (new_fd == -1)
        {
          perror("accept");
          continue;
        }
      if (send(new_fd, &codeLen, sizeof (int), 0) == -1)
        perror("send");
      if (send(new_fd, codeGenerated, codeLen, 0) == -1)
        perror("send");
      printf("Code sent\n");
      close(new_fd);
    }

  return 0;
}
