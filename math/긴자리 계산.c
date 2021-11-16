#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#pragma warning(disable:6031)

#define BUFFER_LEN 1002
#define ZERO "0";


int ctoi(char a) {
	return a - '0';
}

char itoc(int a) {
	return a + '0';
}
 
void add(char* a, char* b) {
	int C[2345];
	int al = strlen(a) - 1;
	int bl = strlen(b) - 1;

	for (int i = 0; i < 2345; i++) {
		C[i] = 0;
	}

	int index = 0;
	int flag = 0;
	while (index <= al && index <= bl) {
		C[index] = ctoi(a[al - index]) + ctoi(b[bl - index]) + flag;
		flag = C[index] / 10;
		C[index] = C[index] % 10;
		index += 1;
	}


	while (index <= al) {
		C[index] = ctoi(a[al - index]) + flag;
		flag = C[index] / 10;
		C[index] = C[index] % 10;
		index += 1;
	}

	while (index <= bl) {
		C[index] = ctoi(b[bl - index]) + flag;
		flag = C[index] / 10;
		C[index] = C[index] % 10;
		index += 1;
	}

	if (flag) {
		C[index] = 1;
		index += 1;
	}

	while (C[index] == 0) {
		index -= 1;
	}

	for (int i = index; i >= 0; i--) {
		printf("%d", C[i]);
	}

	printf("\n");

}


// a - b ( a >= b )
char* minus(char* a, char* b) {
	
	int al = strlen(a) - 1;
	int bl = strlen(b) - 1;

	int C[2345];
	for (int i = 0; i < 2345; i++) {
		C[i] = 0;
	}

	int index = 0;
	while (index <= bl) {
		C[index] = ctoi(a[al-index]) - ctoi(b[bl-index]);
		index += 1;
	}

	while (index <= al) {
		C[index] = ctoi(a[al-index]);
		index += 1;
	}

	for (int i = 0; i <= index; i++) {
		if (C[i] < 0) {
			C[i] += 10;
			C[i + 1] -= 1;
		}
	}


	while (index > 0 && C[index] == 0) {
		index -= 1;
	}


	for (int i = index; i >= 0; i--) {
		printf("%d", C[i]);
	}

	printf("\n");
}



void multiply(char* a, char* b)
{
	int al = strlen(a) - 1;
	int bl = strlen(b) - 1;

	int C[2345];
	for (int i = 0; i < 2345; i++) {
		C[i] = 0;
	}

	for (int i = 0; i <= al; i++) {
		for (int j = 0; j <= bl; j++) {
			C[i + j] += ctoi(a[al - i]) * ctoi(b[bl - j]);
		}
	}

	for (int i = 0; i < 2002; i++) {
		C[i + 1] += C[i] / 10;
		C[i] = C[i] % 10;
	}

	int index = 2002;
	while (C[index] == 0) {
		index -= 1;
	}

	for (int i = index; i >= 0; i--) {
		printf("%d", C[i]);
	}

	return;
}



void handle_add(char* a, char* b, int flag) {
	char* add_res = NULL;
	int al = strlen(a);
	int bl = strlen(b);
	if (flag) {
		printf("-");
	}
	add(a, b);
}


int compare(char* a, char* b) {
	if (strlen(a) < strlen(b)) {
		return -1;
	}
	else if (strlen(a) == strlen(b)) {
		if (a[0] < b[0]) {
			return -1;
		}
		else if(a[0] == b[0]){
			return 0;
		}
		return 1;
	}
	else {
		return 1;
	}
}

// a - b
void handle_minus(char* a, char* b) {
	char* minus_res = NULL;
	int comp = compare(a, b);
	if (comp == -1) {
		printf("-");
		minus(b, a);
	}

	else{
		minus(a, b);
	}
}


// a * b 
void handle_multiply(char* a, char* b, int flag) {
	if (flag) {
		printf("-");
	}
	multiply(a, b);
}


int main(void) {

	//freopen("input.txt", "r", stdin);

	char A[BUFFER_LEN];
	char B[BUFFER_LEN];

	scanf("%s", A);
	scanf("%s", B);

	char* a_string = A;
	char* b_string = B;



	// a + b 
	// a - b
	// a * b
	if (A[0] != '-' && B[0] != '-') {
		handle_add(a_string, b_string, 0);

		handle_minus(a_string, b_string);

		handle_multiply(a_string, b_string, 0);
	}

	// -a - b = - ( a + b)
	// -a - (-b) = b - a
	// a * b
	else if (A[0] == '-' && B[0] == '-') {
		a_string += 1;
		b_string += 1;

		handle_add(a_string, b_string, 1);

		handle_minus(b_string, a_string);

		handle_multiply(a_string, b_string, 0);
	}

	// -a + b = b - a
	// -a - b = - ( a + b )
	// - a * b
	else if (A[0] == '-') {
		a_string += 1;
		handle_minus(b_string, a_string);

		handle_add(a_string, b_string, 1);

		handle_multiply(a_string, b_string, 1);
	}

	// a - b
	// a - (-b) = a + b
	// - a * b
	else if (B[0] == '-') {
		b_string += 1;
		handle_minus(a_string, b_string);

		handle_add(a_string, b_string, 0);

		handle_multiply(a_string, b_string, 1);
	}

	return 0;
}




