#include<stdio.h>
#include<string.h>

char* deCiffer(char* pass1, char* pass2) {

  for (int i = 0; pass1[i] != 0; i++) {
      
    if((int)pass1[i] + 10 > 126)
      pass1[i] = (char)((int)pass1[i] + 10 - 126 + 32);
    
    else
      pass1[i] = (char)((int)pass1[i] + 10);
  }

  for (int i = 0; pass1[i] != 0; i++) {
      
    if((int)pass2[i] + 10 > 126)
      pass2[i] = (char)((int)pass2[i] + 10 - 126 + 32);
    
    else
      pass2[i] = (char)((int)pass2[i] + 10);
    
  }
  
  strcat(pass1, pass2);

  return pass1;
}

int checkPasswords(char* userInput) {
      
  char secret1[] = "O)iUJ^'iU'iUm";
  char secret2[] = "^*jUo&kUd))Zu";
    
  if ( strcmp(userInput, deCiffer(secret1, secret2)) == 0 )
    printf("SSM{%s}\n", userInput);
  return 1;
}

int main(void) {
  char password1[30];
  char password2[30];

  printf("Enter password 1: ");
  scanf("%s", password1);
  
  printf("Enter password 2: ");
  scanf("%s", password2);
  
  deCiffer(password1, password2);
  checkPasswords(password1);

  return 0;
}
