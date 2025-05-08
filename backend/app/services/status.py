_status = {
    "processing": False,
    "comments_found": False,
    "file_created": False,
    "error": False,
    "prev_url": ""
}

def get_status():
    return _status

def update_status(**kwargs):
    _status.update(kwargs)
