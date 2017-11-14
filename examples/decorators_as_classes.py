import json

class WriteOutputAsJsonToFile:

    def __init__(self, file_name):
        self.file_name = file_name

    def _write_as_json_to_file(self, object):
        with open(self.file_name, "w") as file:
            file.write(json.dumps(object))

    def __call__(self, function):

        def new_function(*args, **kwargs):
            output = function(*args, **kwargs)
            self._write_as_json_to_file(output)
            return output

        return new_function


@WriteOutputAsJsonToFile("log.json")
def merge_strings(string1, string2):
    return string1 + string2


if __name__ == "__main__":
    result = merge_strings("hi", "!")
    logged_result = json.load(open("log.json"))
    assert logged_result == result