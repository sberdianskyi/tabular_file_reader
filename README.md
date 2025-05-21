# Tabular Viewer

**Tabular Viewer** is a universal tool for viewing tabular data from files of various formats. The program automatically detects the file format and displays its content in a user-friendly way.

## Supported File Formats
- `.xlsx` (Excel)
- `.csv` (CSV)
- `.sas7bdat` (SAS)
- `.xpt` (SAS Transport XPORT)

Note: CPORT SAS files are not supported.

## Installation

1. Ensure you have Python version 3.8 or higher installed.
2. Open a terminal and run the following command to clone the project from GitHub:
   ```shell
   git clone https://github.com/sberdianskyi/tabular_file_reader.git
   ```   
3. Create and activate virtual environment:

   ```shell
   python -m venv venv
   venv\Scripts\activate # for Windows
   source vevn/bin/activate # for MacOS/Linux
   ```

4. Install the required dependencies:
   ```shell
   pip install -r requirements.txt
    ```

## Usage

1. Run the program:
   ```shell
   python main.py
    ```
2. Enter the file path you want to view.
3. The program will automatically detect the file format and display its content:
   * For Excel files with multiple sheets, the content of each sheet will be displayed.
   * For other formats, the file content will be displayed.

### Example

Input example:
```
Enter your file path: C:\Users\Sergiy\Downloads\example.xlsx
```

Output example:
```
File: C:\Users\Sergiy\Downloads\example.xlsx, Sheet: Sheet1
   Column1  Column2
0       10       20
1       30       40
```

### Extensibility
The project architecture allows for easy addition of support for new file formats. To add a new format:


1. Create a new class inheriting from TabularReader.
2. Implement the read_file method.
3. Add the new reader to the self.readers dictionary in the TabularViewer class
