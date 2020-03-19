#include <stdio.h>
#include <string.h>

/*

SSM{y0u_are_4_mastr_of_d1ffs}

S 83   0
S 83   0
M 77  -6
{ 123  46
y 121 -2
0 48  -73
u 117  69
_ 95  -22
a 97   2
r 114  17
e 101 -13
_ 95  -6
4 52  -43
_ 95   43
m 109  14
a 97  -12
s 115  18
t 116  1
r 114 -2
_ 95  -19
o 111  16
f 102 -9
_ 95  -7
d 100  5
1 49  -51
f 102  53
f 102  0
s 115  13
} 125  10
NULL  -125

*/

#define MIN(A,B) (A < B ? A : B )

int passcomp(char *pass) {
	signed char a[30] = { 0, 0, -6, 46, -2, -73, 69, -22, 2, 17, -13, -6, -43, 43, 14, -12, 18, 1, -2, -19, 16, -9, -7, 5, -51, 53, 0, 13, 10, -125 };

	unsigned int len = strlen(pass);

	if (len > 0) {
		if (pass[0] == 'S') {
			for (unsigned int i = 1; i < MIN(len + 1, sizeof(a)); i++) {
				if (pass[i] - pass[i - 1] != a[i])
					return 0;
			}
			return 1;
		}
	}

	return 0;
}

int main(int argc, char **argv) {
	char pass[100];

	printf("Enter password: ");
	scanf("%s", pass);

	if (passcomp(pass))
		printf("correct\n");
	else
		printf("incorrect, try again\n");

	return 0;
}
