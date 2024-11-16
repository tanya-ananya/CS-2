# Test.py
from FileProcessor import FileProcessor

def test_merge():
    """Test the merge functionality"""
    print("Testing merge function...")
    FileProcessor.merge("text1.txt", "text2.txt", "result.txt")

def test_copy():
    """Test the copy functionality"""
    print("Testing copy function...")
    FileProcessor.copy("text1.txt", 3)  # Example: Create 3 copies

def test_convert_to_csv():
    """Test the convert_to_csv functionality"""
    print("Testing convert_to_csv function...")
    FileProcessor.convert_to_csv("text1.txt", "text1.csv")

def test_file_statistics():
    """Test the file_statistics functionality"""
    print("Testing file_statistics function...")
    FileProcessor.file_statistics("text1.txt")

# Run the tests
if __name__ == "__main__":
    test_merge()
    test_copy()
    test_convert_to_csv()
    test_file_statistics()
