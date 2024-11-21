#include <stdio.h>
#include <unistd.h>
#include <string.h>

int main(int ac, char **av) {
    printf("my_first_compilation.\n");
    return 0;
}
/*************************************************************************/
int main() {
  int person_age = 34;
  printf("%d\n", person_age);
  return 0;
}
/*************************************************************************/
int main() {
  char my_letter = 'c';
  printf("%c\n", my_letter);
  return 0;
}
/*************************************************************************/
int main() {
  char my_string[] = "Learning is growing";
  printf("%s\n", my_string);
  return 0;
}
/*************************************************************************/
int main() {
  int my_age = 34;
  char my_name[] = "Luke";
  char my_comma = ',';
  printf("Hello %s%c I'm %d years old.\n", my_name, my_comma, my_age);
  return 0;
}
/*************************************************************************/
int main() {
  int my_index = 0;
  my_index++;
  printf("%d\n", my_index);
  my_index--;
  my_index--;
  printf("%d\n", my_index);
    my_index++;
    my_index++;
    my_index++;
  printf("%d\n", my_index);
  return 0;
}
/*************************************************************************/
int main() {
  int nbr = 10;
  if (nbr > 20) {
    printf("nbr is greater than 20\n");
  }
  else {
    printf("nbr is less than 20\n");
  }
  return 0;
}
/*************************************************************************/
int main() {
  int a = 10;
  int b = 9;
  int c = 11;
  int d = 10;
  int y = 9;
  int z = 11;
  if (a > b && a < c && a == d) {
    printf("a is bigger than b AND smaller than c AND equal to d\n");
  }
  if (z > a || y > a) {
    printf("z OR y are bigger than a\n");
  }
  return 0;
}
/*************************************************************************/
int my_first_function() {
    printf("my_first_function\n");
    return 0;
}
int main() {
  my_first_function();

  return 0;
}
/*************************************************************************/
int main() {
  int index = 0;
  while (index < 100) {
    printf("I want to code\n");
    index++;
  }
  return 0;
}
/*************************************************************************/
int main() {
  int timer = 10;

  while (timer > 0) {
    printf("detonation in... %d secondes.\n", timer);
    timer--;
  }
  return 0;
}
/*************************************************************************/
int main() {
  printf("%d\n", my_get_seven(7));
  return 0;
}
int my_get_seven(int number) {
    return number;
}
/*************************************************************************/
int my_is_negative(int param_1) {
    if (param_1 < 0) {
        return 0;
    } else {
        return 1;
    }
}
/*************************************************************************/
int abs(int param_1);
int my_abs(int param_1)
{
    int final = abs(param_1);
    return final;
}
/*************************************************************************/
int my_isalpha(char param_1)
{
    if ((param_1 >= 97 && param_1 <= 122) || (param_1 >= 65 && param_1 <= 90)) {
        return 1;
    } else {
        return 0;
    }
}
/*************************************************************************/
int my_isdigit(char param_1)
{
    if ((param_1 >= 48 && param_1 <= 57)) {
        return 1;
    } else {
        return 0;
    }
}
/*************************************************************************/
int my_islower(char param_1)
{
    if (param_1 >= 97 && param_1 <= 122) {
        return 1;
    } else {
        return 0;
    }
}
/*************************************************************************/
int my_isupper(char param_1)
{
    if (param_1 >= 65 && param_1 <= 90) {
        return 1;
    } else {
        return 0;
    }
}
/*************************************************************************/
int my_isspace(char param_1)
{
    if (param_1 == 32) {
        return 1;
    } else {
        return 0;
    }
}
/*************************************************************************/
void my_putchar(char c) {
  write(1, &c, 1);
}
void my_print_alphabet()
{
    for (int c = 97; c <= 122; c++) {
        my_putchar(c);

    }
    my_putchar('\n');
}
/*************************************************************************/
void my_print_reverse_alphabet()
{
    for (int c = 122; c >= 97; c--) {
        my_putchar(c);

    }
    my_putchar('\n');
}
/*************************************************************************/
void my_initializer(int* param_1) {
    *param_1 = 0;
}
/*************************************************************************/
void my_swap(int* param_1, int* param_2)
{
    int temp = *param_1;
    *param_1 = *param_2;
    *param_2 = temp;
}
/*************************************************************************/
int my_strlen(char* param_1) {
    int count = 0;
    for (int i=0;param_1[i];i++) {
        count++;
    }
    return count;
}
/*************************************************************************/
void my_putstr(char* param_1) {
    while (*param_1) {
         write(1, &*param_1, 1);
         param_1++;

    }
    
}
/*************************************************************************/
int my_add(int param_1, int param_2)
{
    int result = param_1 + param_2;
    return result;
}
/*************************************************************************/
int my_sub(int param_1, int param_2)
{
    int result = param_1 - param_2;
    return result;
}
/*************************************************************************/
int my_mult(int param_1, int param_2)
{
    int result = param_1 * param_2;
    return result;
}
/*************************************************************************/
void my_string_formatting(char* param_1, char* param_2, int param_3)
{
    printf("Hello, my name is %s %s, I'm %d.\n", param_1, param_2, param_3);
}
/*************************************************************************/
int my_string_index(char* param_1, char param_2)
{
    int count = 0;
    
        for (int k = 0; k < strlen(param_1); k++) {
            if (param_2 == param_1[k]) {
        count++;
    } else {}
    }
    if (count > 0) {
        return count;
    } else {
        return -1;
    }
} 
/* 1. move first of param_2 through whole param_1 // for loop
   2. if match then count++;                    // count ++
   3. then if no match then move onto next letter of param_2 // nested for loop
   4. if no more matches then return count          // return count;
   */
/*************************************************************************/
char* my_upcase(char* param_1) {
    for (int i = 0; param_1[i]!='\0'; i++) {
      if(param_1[i] >= 'a' && param_1[i] <= 'z') {
         param_1[i] = param_1[i] -32;
      }
   }
    return param_1;
}
/*************************************************************************/
char* my_downcase(char* param_1) {
    for (int i = 0; param_1[i]!='\0'; i++) {
      if(param_1[i] >= 'A' && param_1[i] <= 'Z') {
         param_1[i] = param_1[i] +32;
      }
   }
    return param_1;
}
/*************************************************************************/
char* reverse_string(char* param_1) 
{  
    char temp; // define the size of str[] array  
    int i, left, right, len;  
    len = strlen(param_1); // get the length of the string  
    left = 0; // set left index at 0  
    right = len - 1; // set right index len - 1  
    // use for loop to store the reverse string  
    for (i = left; i <right; i++)  
    {  
        temp = param_1[i];  
        param_1[i] = param_1[right];  
        param_1[right] = temp;  
        right--;  
    }  
    return param_1;
}  
/*************************************************************************/
int my_strcmp(char* param_1, char* param_2)
{

    char c = param_1[0];
    int x = c;
    char d = param_2[0];
    int y = d;

    if (*param_1 == *param_2) 
    {
        return 0;
    } 
    else if (c < d) 
    {
        return -1;
    } 
    else 
    {
        return 1;
    }
}
/*************************************************************************/
char* my_strcpy(char* param_1, char* param_2)
{

    for (int i = 0; param_2[i] != '\0'; i++) 
    {
        param_1[i] = param_2[i];
    }
    
    return param_1;
}
/*************************************************************************/
char* my_strncpy(char* param_1, char* param_2, int param_3)
{
    for (int i = 0; i < param_3; i++) 
    {
        param_1[i] = param_2[i];
    }
    
    return param_1;
}
/*************************************************************************/
char* my_strchr(char* param_1, char param_2)
{   
    if (param_2 == 0) 
    {
        return NULL;
    }
    while(*param_1) 
    {  
        if (param_2 == *param_1) {
                return param_1;
        }
    param_1++;
    }
    return NULL;
}
/*************************************************************************/
char* my_strrchr(char* param_1, char param_2)
{
    if (param_2 == 0) 
    {
        return NULL;
    }
    int x = strlen(param_1);
    for (int i = 1; i < x; i++) 
    {
        param_1++;
    }
    while(*param_1) 
    {  
    if (param_2 == *param_1) 
    {
      return param_1;
    }
    param_1--;
    }
    return NULL;
}
/*************************************************************************/
char* my_strstr(char* param_1, char* param_2)
{
  if (param_1 == 0) // check valid input
  {
    return NULL;
  } else if (strlen(param_2) > strlen(param_1)) // check if param_2 bigger than param_1
  {
    return NULL;
  } else if (*param_2 == 0) 
  {
      return param_1;
  }
    while (*param_1 != '\0')
  { 
   char* p2place = param_2;        // 2nd pointer to 1st pointer
   char* p1place = param_1;        // 2nd pointer to 1st pointer
    while(*param_1)
    {                // while p1 exists run then p1++ & p1place++
        if (*param_1 == *param_2)
        {         //if value of p1 is equal to value of p2 then run 
            while(*param_2)
            {            // while p2 exists run 
                if(*param_1 != *param_2)
                {      // check to see if not matched 
                    param_1 = p1place;    // p1's value will equal to value of p1place again
                    param_2 = p2place;    // p2's value will equal to value of p2place again
                    break;            
                }
                param_1++;                //increase p1's placement
                param_2++;                //increase p2's placement
                if (!*param_2){           //if p2 does not exist
                return p1place;    //return p1place;
                }
            }
        }
    param_1++;
    p1place++;
  }
  }
  return NULL;
}
/*************************************************************************/
void my_first_struct(integer_array* param_1)
{
    printf("%d\n", param_1->size);
    for (int i = 0; i < param_1->size; i++)
    {
        printf("%d\n", *param_1->array);
        param_1->array++;
    }
}
/*************************************************************************/
#include <stdbool.h>
#ifndef STRUCT_INTEGER_ARRAY
#define STRUCT_INTEGER_ARRAY
typedef struct s_integer_array
{
    int size;
    int* array;
} integer_array;
#endif
bool my_is_sort(integer_array* param_1)
{
    int ascending_count = 0;
    int descending_count = 0;
    for (int i = 0; i < (param_1->size-1); i++) // run through array
    {
        if (param_1->array[i] > param_1->array[i+1]) //if sorted asc or desc 
        {
            ascending_count++;
        } 
        if (param_1->array[i] < param_1->array[i+1])
        {
            descending_count++;
        }
        if (param_1->array[i] == param_1->array[i+1])
        {
            descending_count++;
            ascending_count++;
        }
    }
    if (param_1->size == 0) 
    {
        return true;
    }
    if ((ascending_count == (param_1->size-1)) || (descending_count == (param_1->size-1)))
    {
        return true;
    }
    return false;
}
// Write a function that takes an integer array as a parameter (input) and returns a boolean (true/false).
// Numbers will be from -2_000_000 to 2_000_000
// Array might have duplicate(s).
/*************************************************************************/
#include <stdlib.h>
#include <stddef.h>

int* my_range(int param_1, int param_2)
{
    int range = param_2 - param_1;
    int *mallocd_array = (int*)malloc(range*sizeof(int));
    mallocd_array[0] = param_1;
    for (int i = 1; i < range; i++)
    {
        mallocd_array[i] = param_1+1;
        param_1++;
    }
    return mallocd_array;
}
/*************************************************************************/
char* my_strdup(char* param_1)
{
    int size = strlen(param_1);
    char *new_string = (char*)malloc(size*sizeof(char));
    for (int i = 0; i < size; i++)
    {
        new_string[i] = param_1[i];
    }
    return new_string;
}
/*************************************************************************/
#ifndef STRUCT_STRING_ARRAY
#define STRUCT_STRING_ARRAY
typedef struct s_string_array
{
    int size;
    char** array;
} string_array;
#endif
void my_print_words_array(string_array* param_1)
{   
    int size = param_1->size;
    char n = '\n';
    

    for (int i = 0; i < size; i++) // run through each array 
    {   
        int lil_size = strlen(param_1->array[i]);

            for (int j = 0; j < lil_size; j++) // print each char til end 
            {
                putchar(param_1->array[i][j]);
            }

        putchar(n);       
    }
}   
/*************************************************************************/
#ifndef STRUCT_STRING_ARRAY
#define STRUCT_STRING_ARRAY
typedef struct s_string_array
{
    int size;
    char** array;
} string_array;
#endif

#ifndef STRUCT_INTEGER_ARRAY
#define STRUCT_INTEGER_ARRAY
typedef struct s_integer_array
{
    int size;
    int* array;
} integer_array;
#endif


integer_array* my_count_on_it(string_array* param_1)
{
    integer_array* result = (integer_array*)malloc(result->size*sizeof(int));
    result->array = (int*)malloc(result->size*sizeof(int));
    result->size = param_1->size;

    for (int i = 0; i < param_1->size; i++) 
    {   
        result->array[i] = strlen(param_1->array[i]);
    }

    return result;
}
/*************************************************************************/
#ifndef STRUCT_STRING_ARRAY
#define STRUCT_STRING_ARRAY
typedef struct s_string_array
{
    int size;
    char** array;
} string_array;
#endif


char* my_join(string_array* param_1, char* param_2)
{   
    /* Measurements */
    int size = param_1->size;
    int param_2_total_size = strlen(param_2) * (size-1); // 3
    int param_1_total_size = 0; //9
    for (int j = 0; j < size; j++) 
    {   
        param_1_total_size += (strlen(param_1->array[j]) + 1); // (size * strlen each) + (separator * (size-1))
    }
    int full_size = param_1_total_size + param_2_total_size +1; 
    if (param_1->array == 0) { return NULL; }
    
    /* Creating String */
    char *string = (char*)malloc(full_size*sizeof(char));
    
    for (int i = 0; i < size; i ++)
    {   
            strcat(string, param_1->array[i]);
            if (i  < size-1)
            {
            strcat(string, param_2);
            }
    }
    return string;
}

struct physics {
    int x;
    int y;
    char *direction;
};
/*************************************************************************/
void turn_right(struct physics *spaceship)
{       
  if      (strcmp(spaceship->direction, "up")    == 0 ) { strcpy(spaceship->direction, "right"); }
  else if (strcmp(spaceship->direction, "right") == 0 ) { strcpy(spaceship->direction, "down" ); }
  else if (strcmp(spaceship->direction, "left")  == 0 ) { strcpy(spaceship->direction, "up"   ); }
  else if (strcmp(spaceship->direction, "down")  == 0 ) { strcpy(spaceship->direction, "left" ); }
}

void turn_left(struct physics *spaceship)
{       
  if      (strcmp(spaceship->direction, "up")    == 0 ) { strcpy(spaceship->direction, "left" ); }
  else if (strcmp(spaceship->direction, "right") == 0 ) { strcpy(spaceship->direction, "up"   ); }
  else if (strcmp(spaceship->direction, "left")  == 0 ) { strcpy(spaceship->direction, "down" ); }
  else if (strcmp(spaceship->direction, "down")  == 0 ) { strcpy(spaceship->direction, "right"); }
}

void accelerate(struct physics *spaceship) 
{
  if      (strcmp(spaceship->direction, "up")    == 0 ) { spaceship->y -= 1; }
  else if (strcmp(spaceship->direction, "right") == 0 ) { spaceship->x += 1; }
  else if (strcmp(spaceship->direction, "down")  == 0 ) { spaceship->y += 1; }
  else if (strcmp(spaceship->direction, "left")  == 0 ) { spaceship->x -= 1; }
}

char* my_spaceship(char* param_1)
{
    struct physics spaceship;
    spaceship.direction = (char*)malloc(6*sizeof(char));
    spaceship.x = 0;
    spaceship.y = 0;
    strcpy(spaceship.direction, "up");
    int i = 0;

    while (i < strlen(param_1))
    {   char instruction = param_1[i];

        if (instruction == 'A') { accelerate(&spaceship); }
        if (instruction == 'R') { turn_right(&spaceship); }
        if (instruction == 'L') { turn_left(&spaceship);  }
        i += 1;
    }
  char *landing = (char*)malloc(100*sizeof(char));
  sprintf(landing, "{x: %d, y: %d, direction: '%s'}", spaceship.x, spaceship.y, spaceship.direction);
  return landing;
}
/*************************************************************************/
int my_fibonacci(int param_1)
{
  if(param_1 <= -1)
  {
	return -1;  
  }
  if(param_1 == 0)
  {
    return 0;
  }
  if(param_1 == 1)
  {
    return 1;
  }
  else 
  {
    return (my_fibonacci(param_1-1) + my_fibonacci(param_1-2));
  }
}

// 1. 0,1,1,2,3,5,8,13,21
// 2. 0,1,2,3,4,5,6, 7, 8
// 3.     0 + 1 = 1       /    + 1 = 2      /     + 1 = 3     / + 2 = 5 / + 3 = 8 / 
// 4. n[0] + n[1] = n[2] / + n[2-1] = n[3] / + n[3-1] = n[4] /
// 5. param_1 = 4 then recursive by 4 

char* hello_name(char* param_1)
{
  	char *old_string = "Hello ";
    char *new_string = (char*) malloc(100);
  
    int i = 0, j = 0;
  
    while (old_string[i] != '\0') {
        new_string[j] = old_string[i];
        i++;
        j++;
    }
    i = 0;
    while (param_1[i] != '\0') {
        new_string[j] = param_1[i];
        i++;
        j++;
    }
    new_string[j] = '\0';
  	return new_string;
}