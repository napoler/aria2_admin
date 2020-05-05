from config import *
import json
from pprint import pprint
# Purge completed, removed or failed downloads from the queue.
# 自动清理完成的 失败 删除的
# aria2.autopurge()

a=aria2.get_stats()

def dictojson(a):
    """
    对象转换为json
    """
    js = json.dumps(a.__dict__)
    js=json.loads(js)
    # print(type(js))
    return js

stats=dictojson(a)
print(stats['_struct'])
# print(a.__dict__)
# print(a.num_stopped)

# # list downloads
downloads = aria2.get_downloads()
# print(downloads.__dict__)

num_available=10-int(stats['_struct']['numActive'])
if int(stats['_struct']['numActive'])<10:
    print("剩余可启动进程：",num_available)

for download in downloads:
    # print(download.name, download.download_speed,download.status, download.dir)
    if download.is_torrent:
        print("##"*20)
        print("name:",download.name)
        print("状态：",download.status)
        print("进度",download.progress)
        if (download.is_paused or download.has_failed) and download.progress <100:
            print("11111111")
        # pprint(download.__dict__)

        # if download.total_length==0:
        #     complete=0
        # else:
        #     complete=download.completed_length/download.total_length
        # print("完成率：",complete)
        # print(download.files)

        # for it_file in download.files:
        #     print(it_file)
        #     print(it_file.is_metadata)
        #     print(it_file.selected)
        #     print(it_file.length)


        # print(download.bittorrent())
        # print(download.bittorrent)
        # download.move_up
        
        # print(download._struct.completedLength)
        # pprint(download.__dict__)
        #  if download.is_complete =="complete"
        if download.is_complete:
            print("已完成，删除:",download.name)
            # download.remove()
            
        elif download.status=="error" and num_available>0:
            pass
            download.resume
            download.move_to_top
            num_available=num_available-1
            print("自动恢复")
            # tell_status(
            # download.resume()
            # print(download.completed_length())
            # try:
            #     print(download.total_length())

            #     complete=int(download.total_length())-int(download.completed_length())
            #     print("完成率：",complete)
            # except:
            #     pass

        # elif download.status=="error":
        #     print("error")
    

    # pprint(download.__dict__)

    