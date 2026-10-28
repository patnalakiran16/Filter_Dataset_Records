Filter Dataset Records Using Pandas

About the Project

This project demonstrates how to filter student records using Python and Pandas. Different conditions are used to select specific records from a dataset.

Objective

The main objective is to learn how to filter rows from a dataset using single and multiple conditions.

Technologies Used

- Python
- Pandas
- Jupyter Notebook

Dataset

A sample student dataset is created with the following columns:

- Name
- Age
- Marks
- Department

Filtering Examples

1. Filter Students by Marks

Selects students who scored more than 80 marks.

df[df["Marks"] > 80]

2. Filter Students by Department

Displays students who belong to the MCA department.

df[df["Department"] == "MCA"]

3. Filter Using Multiple Conditions

Selects students who scored above 75 marks and are older than 21.

df[(df["Marks"] > 75) & (df["Age"] > 21)]

Key Learnings

- Creating a DataFrame using Pandas.
- Filtering records using Boolean conditions.
- Combining multiple conditions with the "&" operator.
- Counting filtered records using "len()".

How to Run

1. Open Jupyter Notebook.

2. Install Pandas if it is not already installed:
   
   pip install pandas

3. Copy the Python program into a notebook cell.

4. Run the cell using "Shift + Enter".

5. Check the filtered records in the output.

Conclusion

This project helped me understand how to retrieve relevant records from a dataset using Pandas. I practised applying different filtering conditions and checking the number of records returned.

Author

Kiran

Internship Task: Filter Dataset Records
Organisation: Veda Technology