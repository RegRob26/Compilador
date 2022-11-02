int main,0;
int first_number = 0, second_number = 1, third_number, i, number;
printf "Enter the number for fibonacci series:";
printf "Fibonacci Series for a given number:";
printf first_number, second_number; //To print 0 and 1
for i = 2; i < number; ++i //loop will starts from 2 because we have printed 0 and 1 before

third_number = first_number + second_number;
printf third_number;
first_number = -second_number;
second_number = third_number;

return 0;
