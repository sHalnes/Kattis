#include <iostream>

int main(){
    int min = 1;
    int max = 1000;
    int guess = max/2;
    std::cout << guess << "\n";
    std::string ans;
    while(1){
        std::cin >> ans;
        if(ans == "correct"){
            break;
        }
        if(ans == "lower"){
            max = guess - 1;
            guess = (max - min)/2 + min;
        }
        if(ans == "higher"){
            min = guess + 1;
            guess = (max - min)/2 + min;
        }
        std::cout << guess << "\n";

    }
    return 0;
}

/***Your program should output guesses for the correct number, in the form of an integer between 1
 and 1000
 on a line on its own. After making each guess, you need to make sure to flush standard out.

After each guess, there will be a response to be read from standard in. This response is a line with one of the following three words:

“lower” if the number I am thinking of is lower than your guess
“higher” if the number I am thinking of is higher than your guess
“correct” if your guess is correct
After having guessed the right answer your program should exit. If you guess incorrectly 10
 times, you won’t get any more chances and your program will be terminated.***/