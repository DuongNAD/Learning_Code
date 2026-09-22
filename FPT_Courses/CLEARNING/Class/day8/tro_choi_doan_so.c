#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(NULL)); // Khởi tạo seed cho số ngẫu nhiên
    int randomNumber = (rand() % 100) + 1; // Số ngẫu nhiên từ 1 đến 100
    int guess, attempts = 0;
    
    printf("I have generated a random number between 1 and 100. Can you guess it?\n");

    do {
        printf("Enter your guess: ");
        scanf("%d", &guess);
        attempts++;
        if (guess > randomNumber) {
            printf("Too high!\n");
        } else if (guess < randomNumber) {
            printf("Too low!\n");
        } else {
            printf("\nOUTPUT:\n");
            printf("Correct! You guessed it in %d attempts.\n", attempts);
        }
    } while (guess != randomNumber);

    return 0;
}