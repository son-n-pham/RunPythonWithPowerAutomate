def save_string_to_text_file(string_to_save, file_path):
    """_summary_

    Args:
        string_to_save (string): string to insert into text file
        file_path (string): filepath with file name
    """
    import datetime
    current_time = str(datetime.datetime.now())
    current_time = current_time.replace(' ', '_').replace(':', '-')
    file_path = file_path + '_' + current_time + '.txt'
    with open(file_path, 'w') as file:
        file.write(string_to_save)
    return

if __name__ == '__main__':
    save_string_to_text_file('Hello World!', 'HelloWorld')