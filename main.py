from notion.client import NotionClient
import package.video_actions
import package.os_actions

nv = package.video_actions
no = package.os_actions

client = NotionClient(token_v2="YOUR_TOKEN_V2") # token_v2 can be found in logged in notion browser session, after developer tools open, find it in cookies menu

# needs to be in form : https://www.notion.so/organisation/page-name_page-id
page = client.get_block("NOTION_PAGE_URL")
directory = r"PATH_TO_FOLDER_WITH_VIDEOS"

no.upload_all_files_in_dir(page, directory)
