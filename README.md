# difsorting

What is this program for?
=========================

1) It allows to rename files in one chosen directory by modification date by adding decent number before its name

For example:\
 We created files in this order:

Test1; Test2; Test3; Test4

After usage names will be:

1\. Test1; 2. Test2; 3. Test3; 4. Test4

2) It allows to rename files in one chosen directory by taking their xxhash

For example:\
 We have file named "Test.txt"

After usage name will be:

22fd2e703d0645255770cd7a08cf3ec6.txt

Installation
============

pip install --r requirements.txt

Usage
=====

Open terminal in program directory and enter:

python main.py

Choose actions and enter absolute directory path where files you want to rename located

For example:

/home/theuser/Pictures/

All files in directory Pictures will be placed in program directory "SortedFiles"
