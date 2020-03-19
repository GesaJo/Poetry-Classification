# Poetry-Classification

[![Build Status](https://travis-ci.com/GesaJo/Poetry-Classification.svg?branch=master)](https://travis-ci.com/GesaJo/Poetry-Classification)

## Project to scrape poems and train a model to predict the author
This program scrapes the website www.deutschelyrik.de for poems by two or more given german poets, cleans and vectorizes the texts and trains a model to predict who of these poets the author of any given line of text is.

The model used is a Naive Bayes model with random oversampling.

## How to use it
- Clone the repository: git clone https://github.com/GesaJo/Poetry-Classification.git
- Install the requirements: pip install -r requirements.txt
- run the main-file in your command-line interface giving two or more authors as input: python main_poems.py -p author1 -p author2
- follow the instructions in your command-line interface

## Tests
Two of the tests are still under construction (commented out).

![alt text](https://images.unsplash.com/reserve/uZYSV4nuQeyq64azfVIn_15130980706_64134efc6e_o.jpg?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1947&q=80)
