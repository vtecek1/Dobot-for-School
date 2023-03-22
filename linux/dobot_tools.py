from pathlib import Path

def find_port():
    check_1_path = Path('dev/ttyACM0')
    check_1_result = check_1_path.is_file()
    print(check_1_result)
    return '/dev/ttyACM0'

find_port()
