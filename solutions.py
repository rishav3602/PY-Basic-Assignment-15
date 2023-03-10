##  Questions...

"""
1.How many seconds are in an hour? Use the interactive interpreter as a calculator and 
multiply thenumber of seconds in a minute (60) by the number of minutes in an hour (also 60).
sol. 60
2. Assign the result from the previous task (seconds in an hour) to a variable called
seconds_per_hour.
3. How many seconds do you think there are in a day? Make use of the variables seconds per hour
and minutes per hour.
4. Calculate seconds per day again, but this time save the result in a variable called 
seconds_per_day
5. Divide seconds_per_day by seconds_per_hour. Use floating-point (/) division.
6. Divide seconds_per_day by seconds_per_hour, using integer (//) division. Did this number
 agree with the floating-point value from the previous question, aside from the final .0?
7. Write a generator, genPrimes, that returns the sequence of prime numbers on successive 
calls to its next() method: 2, 3, 5, 7, 11, ...

"""

## Answers....

"""
1. There are 3600 seconds in an hour (60 seconds/minute * 60 minutes/hour = 3600 seconds/hour).

------------------------------------------------------------------------------------------

2. seconds_per_hour = 3600

------------------------------------------------------------------------------------------

3. There are 86,400 seconds in a day 
(60 seconds/minute * 60 minutes/hour * 24 hours/day = 86,400 seconds/day).

------------------------------------------------------------------------------------------

4. seconds_per_day = seconds_per_hour * 24 = 3600 * 24 = 86,400

------------------------------------------------------------------------------------------

5. seconds_per_day / seconds_per_hour = 86,400 / 3600 = 24.0

------------------------------------------------------------------------------------------

6. seconds_per_day // seconds_per_hour = 86,400 // 3600 = 24
The result is the same as the floating-point division, but without the decimal point.

------------------------------------------------------------------------------------------

7.

def genPrimes():
    primes = []
    n = 2
    while True:
        if all(n % p != 0 for p in primes):
            primes.append(n)
            yield n
        n += 1

"""