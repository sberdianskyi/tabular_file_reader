from viewer import TabularViewer


def main():
    viewer = TabularViewer()
    file_path = input("Enter your file path: ")

    try:
        data = viewer.view_file(file_path)
        if isinstance(data, dict):  # If it's an Excel file with multiple sheets
            for sheet_name, sheet_df in data.items():
                print(f"File: {file_path}, Sheet: {sheet_name}")
                print(sheet_df.head())
        else:  # For other file types
            print(f"File: {file_path}")
            print(data.head())
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
