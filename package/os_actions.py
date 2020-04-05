import os
import package.video_actions

nv = package.video_actions

def upload_all_files_in_dir(page, directory):
    d = directory
    for path in os.listdir(d):
        full_path = os.path.join(d, path)
        file_name = path[:-4]
        if os.path.isfile(full_path):
            nv.video_w_file(page, file_name, full_path)
