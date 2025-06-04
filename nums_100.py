#!/usr/bin/env python3
"""
Natural Numbers API for the technical test.
Implements a class to represent the first 100
natural numbers,
with methods to extract a number and find
which number was extracted.
"""
class NaturalNumberSet:
    """
    A class representing a set of the first
    100 natural numbers.
    This class provides methods to:
    - Extract a specific number from the set
    - Find which number was extracted from
    the set
    """
    def __init__(self):
        """Initialize the set with the first
        100 natural numbers."""
        self.numbers = list(range(1, 101))
        self.original_sum = sum(self.numbers)

    def extract(self, number):
        """
        Extract a specific number from the
        set.
        Args:
            number: The number to extract.
        Returns:
            bool: True if the number was 
            extracted, False if it wasn't in the set.
        Raises:
            ValueError: If the number is not
            a valid integer between 1 and 100.
        """
        # Validate input
        if not isinstance(number, int):
            raise ValueError("Number must be an integer")
        if number < 1 or number > 100:
            raise ValueError("Number must be between 1 and 100")

        # Check if number is in the set
        if number not in self.numbers:
            return False

        # Remove the number
        self.numbers.remove(number)
        return True

    def find_extracted(self):
        """
        Find the number that was extracted
        from the set.
        Returns:
            int: The extracted number, or
            None if no number was extracted.
        """
        # Calculate the sum of the current
        current_sum = 0
        for num in self.numbers:
            current_sum += num

        # If no number was extracted, the
        # sums should be equal
        if current_sum == self.original_sum:
            return None

        # The extracted number is the
        # difference between the original sum and the
        # current sum
        return self.original_sum - current_sum

    def find_extracted_alternative(self):
        """
        Alternative method to find the
        extracted number using set operations.
        Returns:
            int: The extracted number, or
            None if no number was extracted.
        """
        # Create a set of all numbers from 1
        # to 100
        full_set = set(range(1, 101))
        # Convert the current list to a set
        current_set = set(self.numbers)

        # Find the difference between the
        # full set and the current set
        difference = full_set - current_set

        # If there's no difference, no number
        # was extracted
        if not difference:
            return None

        # Return the extracted number
        return list(difference)[0]

def main():
    """
    Main function to demonstrate the
    NaturalNumberSet class.
    """
    import argparse
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Natural Numbers API')
    subparsers = parser.add_subparsers(dest='command', help='Command to run')

    # Extract command
    extract_parser = subparsers.add_parser('extract', help='Extract a number from the set')
    extract_parser.add_argument('number', type=int, help='Number to extract')

    # Find command
    find_parser = subparsers.add_parser('find', help='Find the extracted number')
    find_parser.add_argument('--method', choices=['sum', 'alternative'],
                            default='sum',
                            help='Method to use for finding the extracted number')
    args = parser.parse_args()

    # Create the natural number set
    number_set = NaturalNumberSet()

    if args.command == 'extract':
        try:
            result = number_set.extract(args.number)
            if result:
                print(f"Number {args.number} extracted successfully")
            else:
                print(f"Number {args.number} was not in the set")
        except ValueError as e:
            print(f"Error: {e}")
    elif args.command == 'find':
        if args.method == 'sum':
            result = number_set.find_extracted()
        elif args.method == 'alternative':
            result = number_set.find_extracted_alternative()
        
        if result is None:
            print("No number has been extracted")
        else:
            print(f"The extracted number is: {result}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
