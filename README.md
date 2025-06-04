**Section 2: API Creation for Natural Numbers**

In this section, I implemented a class to represent the first 100 natural numbers and
provide methods to extract a number and find which number was extracted.

**Features**

- Extract a number: Remove a specific number from the set.
- Find extracted number: Determine which number was removed from the set using two different methods (summation or set difference).

**How to Use**
Save the code: Save the provided Python code as natural_numbers.py.

**Run from the command line:**

**Extract a number:**
To remove a number from the set, use the `extract` command followed by the number you want to remove.

`python3 natural_numbers.py extract 50`

Find the extracted number:
To find which number was extracted, use the `find` command. You can specify the method to use (`sum` or `alternative`). If no method is specified, it defaults to sum.


Using the `sum` method:

`python3 natural_numbers.py find --method sum`

Using the `alternative` method:

`python3 natural_numbers.py find --method alternative`
