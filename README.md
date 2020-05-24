# Poetry-Classification
[![Build Status](https://travis-ci.com/GesaJo/Poetry-Classification.svg?branch=master)](https://travis-ci.com/GesaJo/Poetry-Classification)

## Project to scrape poems and train a model to predict the author
This program scrapes the website www.deutschelyrik.de for poems by two or more given german poets, cleans and vectorizes the texts and trains a model to predict who of these poets is most likely to be the author of any given line of text.
The model used is a Naive Bayes model with random oversampling using SMOTE.

This project has been developed in week 5 of the Spiced-Bootcamp.

## How to use it
- Clone the repository: git clone https://github.com/GesaJo/Poetry-Classification.git
- Install the requirements: pip install -r requirements.txt
- run the main-file in your command-line interface giving two or more authors as input: python main_poems.py -p author1 -p author2
- follow the instructions in your command-line interface

## To Do:
- ~~some more cleaning up (comments)~~
- ~~Find & add first names~~
- work on translation-branch
- more tests
