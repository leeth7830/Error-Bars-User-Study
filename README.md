# Error Bars User Study
Replicated experiment for the paper "Error Bars Considered Harmful: Exploring Alternate Encodings for Mean and Error" by Michael Correll and Michael Gleicher 

The goal of this user study is to evaluate the performance of different type of error bars (bar chart, box plot, gradient plot, and violin plot). This experiment was originally conducted in 2014 when the paper was written. This replicated experiment was redone on December of 2018 to see if the results from the original experiment still holds true.

Refer to the write-up and powerpoint for more detailed information/instruction.

## Prerequisite 
* Python
* Jupyter Notebook
* Google Forms 
## Getting Started
1. Read the paper mentioned above and understand how the experiment is done.
2. Create a survey on google forms and use the chart images provided in /original_paper/data/ and questions mentioned in the paper (or refer to /analysis/project2_error_bars.pdf)  
Example of the survey: https://docs.google.com/forms/d/1FIoGS1vknNvywocRjzBl7Jap6BEW0e1pi00tLP1wpws/edit?usp=sharing
3. Deploy on a surveying platform (Mechanical Turk, etc)
4. Collect the results and put it in the input folder
5. run transform.py 
6. Check the quality of data and participants by looking through outputted files in the output folder
7. open and run Error Bars ANCOVA.ipynb to perform statistical analysis.
8. Compare the results to the results from the original experiment.

## Original Data
The original data is available on http://graphics.cs.wisc.edu/Vis/ErrorBars/
