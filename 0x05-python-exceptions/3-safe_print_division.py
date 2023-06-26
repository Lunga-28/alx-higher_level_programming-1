#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    except Exception as e:
        print("An error occurred:", str(e))
        return None
    finally:
        print("Inside result: {}".format(result) if 'result' in locals() else "Inside result: None")
        return result if 'result' in locals() else None

