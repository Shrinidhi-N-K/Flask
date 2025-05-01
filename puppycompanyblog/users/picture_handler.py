import os
from PIL import Image
from flask import current_app

def add_profile_pic(pic_upload, username):
    # Get the file extension
    filename = pic_upload.filename
    ext_type = filename.split('.')[-1]  # Extract file extension
    storage_filename = str(username) + '.' + ext_type  # New filename with extension

    # Create the full filepath including the file name
    filepath = os.path.join(current_app.root_path, 'static', 'profile_pics', storage_filename)

    # Resize image
    output_size = (200, 200)
    pic = Image.open(pic_upload)
    pic.thumbnail(output_size)

    # Save the image to the correct path
    pic.save(filepath)

    return storage_filename
