from enum import Enum

class ResponseStatus(str, Enum):
    file_type_invalid = "Invalid file type"
    file_size_exceeded = "File size exceeds the maximum limit"
    file_valid = "File is valid"
    file_uploaded = "File uploaded successfully"
