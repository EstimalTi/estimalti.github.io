#include <stdio.h>

int main(int args, char* argv[])
{
    float cels = 30, fhar, step = -1;
    printf("Таблица перевода С в F.\n");
    printf("   -----------------\n");
        while (cels >= -30)
        {
            printf("   | %3.0f°C = %3.0f°F |\n", cels, fhar = cels*9./5.+32);
            cels = cels + step;
        }
    printf("   -----------------\n");
return 0;
}
