@echo off

echo There are 5 types of statistics: 
echo 1 total rebounds (TRB)
echo 2 assists (AST), 
echo 3 steals (STL), 
echo 4 blocks (BLK), 
echo 5 points (PTS). 
echo please input your interested types of statistics as array. 
echo eg: you can input 2,5 if you are interested in 'assist' and 'points'.
set /p inputArray1=Please input the statistics:
echo %inputArray1% > input_type.txt
echo please input the number of the top players you would like to know:
echo eg: you can input 10 if you would like to know the statistics results of top 10 players.
set /p inputArray2=Please input the number of the top players:
echo %inputArray2% > input_k.txt
pip install pandas
pip install numpy
pip install os

python code.py

pause

