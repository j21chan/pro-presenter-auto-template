import subprocess

# global variable
MAX_TEMPLATE_LEN = 300


# get clipboard data
def get_clipboard_data():
    p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
    retcode = p.wait()
    content = p.stdout.read()
    return content


# set clipboard data
def set_clipboard_data(_str):
    p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
    p.stdin.write(_str)
    p.stdin.close()
    retcode = p.wait()


# log
def log(_log_info):
    print _log_info


# get clipboard data process
def get_clipboard_data_process():
    log("get copied string from clipboard...")
    try:
        clipboard_data = get_clipboard_data()

        if type(clipboard_data) == str:
            log("clipboard is " + clipboard_data[0:80] + "...")
        else:
            log("clipboard is not string")
            raise Exception

    except Exception as e:
        log("Error :: during get clipboard data")
        log(e)

    clipboard_data = str(clipboard_data)
    clipboard_data = clipboard_data.replace("\n", " ")

    return clipboard_data


# generate template string
def generate_template(_clipboard_data):
    log("generate template string...")

    clipboard_data_list = _clipboard_data.split(' ')
    template_string_list = []
    temp_str = ""    

    for clipboard_str in clipboard_data_list:
        clipboard_str_len = len(clipboard_str)
        temp_str_len = len(temp_str)

        # It is max length of template page
        if temp_str_len > MAX_TEMPLATE_LEN:
            template_string_list.append(temp_str)
            temp_str = clipboard_str
        # Add string when clipboard length longger than 0
        elif clipboard_str_len > 0:
            temp_str = temp_str.strip() + " " + clipboard_str.strip()

    template_string_list.append(temp_str)
    template_string = "\n\n\n".join(template_string_list)
    return template_string


# set clipboard data process
def set_clipboard_data_process(_template_str):
    log("set template string to clipboard")
    set_clipboard_data(_template_str)
    return


# main
if __name__ == "__main__":
    log("### Auto propresenter template generator program start ###\n")

    clipboard_data = get_clipboard_data_process()
    template_string = generate_template(clipboard_data)
    set_clipboard_data_process(template_string)

    log("\n### Auto propresenter template generator program end ###")