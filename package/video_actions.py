from notion.client import NotionClient
from notion.block import VideoBlock
from notion.block import SubheaderBlock

def create_subh(page, title):
    page.children.add_new(SubheaderBlock, child_list_key=None, title=title)
    print("added subheader block with title " + title)

def create_vidblock(page, full_width, height, type, url_path):
    video = page.children.add_new(VideoBlock, height=height, full_width=full_width)
    print("added video block")
    if type == 1:
        video.set_source_url(url_path)
        print("set the video block's url to " + url_path)
    if type == 2:
        print("started video upload ... ")
        video.upload_file(url_path)
        print("uploaded video with path: " + url_path)
    else:
        print("type not found")

def video_w_url(page, title_video_yt, url_video_yt):
    create_subh(page, title_video_yt)
    create_vidblock(page, 0, 400, 1, url_video_yt)

def video_w_file(page, title_video_file, path_video_file):
    create_subh(page, title_video_file)
    create_vidblock(page, 0, 400, 2, path_video_file)
