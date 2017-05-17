#include <stdio.h>
#include <math.h>
#include <assert.h>

#define OK              0
#define NO_INPUT_DATA  -1
#define INVALID_ARGS   -2
#define FILE_NOT_FOUND -3

int expected_value(FILE *f, float *ex_val, int *n)
{   
    float data;
	float summ;  
	*n = 0;       
	*ex_val = 0;    
    if (fscanf(f, "%f", &data) != 1)
        return NO_INPUT_DATA;
    *n += 1;
    summ = data;
    while (fscanf(f, "%f", &data) == 1)
    {
    	*n += 1;
    	summ += data;
    }
    *ex_val = summ / *n;
    rewind(f);
    //printf("[debug!] ex_val = %f\n",*ex_val);
    return OK;
}

float dispersion(FILE *f, float ex_val, int n)
{   
    float data;  
    float delta;
	float delta_summ = 0;
    float disp;       
    assert(n > 0);
    while (fscanf(f, "%f", &data) == 1 )
    {
        delta = data - ex_val;
        delta_summ += delta * delta;
        //printf("[debug!] delta = %f\n",delta);
    }
    //printf("[debug!] delta_summ = %f\n",delta_summ);
    disp = delta_summ/ (n-1);
    return disp;
}

int main(int argc, char** argv)
{
	FILE *f;
	if (argc == 2)
	{
		f = fopen(argv[1],"r");
	}
	else
	{
		printf("Invalid number of arguments");
		return INVALID_ARGS;
	}
	if (f == NULL)
	{
		printf("File not found");
		return FILE_NOT_FOUND;
	}
    int n = 0;
	int result;
	float ex_val;
	float disp;
    result = expected_value(f, &ex_val, &n);
    if (result == NO_INPUT_DATA)
    {
        printf("The file does not contain numbers");
        return NO_INPUT_DATA;
    }
    disp = dispersion(f,ex_val,n);
    printf("Dispersion: %f\n ", disp);
    fclose(f);
    return OK;
}


