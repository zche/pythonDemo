import os
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
downloadPath ='/Users/zhaoruifei/Downloads/tmp/pictures/imgs'
def downloadPic(url,imgName):
    try:
        urllib.request.urlretrieve(url, filename=downloadPath + '/'+ imgName)
    except Exception as e:
        print("Error occurred when downloading file, error message:")
        print(e)

if __name__ == '__main__':
    with open(r'/Users/zhaoruifei/Downloads/tmp/pictures/urls.txt', 'r+', encoding='utf-8') as f_read:
        while True:
            line = f_read.readline()
            if not line:
                break
            arr = line.replace('\'','').split(',')
            flag = 1
            for url in arr:
                downloadPic(url,str(flag)+'.jpg')
                flag = flag + 1
            print('over')
            # url = re.findall(PATTERN,line)
            # if len(url) > 0:
            #     imgsUrl.append(url[0])
# def get_pic_by_url(folder_path, lists):
#     if not os.path.exists(folder_path):
#         print("Selected folder not exist, try to create it.")
#         os.makedirs(folder_path)
#     for url in lists:
#         print("Try downloading file: {}".format(url))
#         filename = url.split('/')[-1]
#         filepath = folder_path + '/' + filename
#         if os.path.exists(filepath):
#             print("File have already exist. skip")
#         else:
#             try:
#                 urllib.request.urlretrieve(url, filename=filepath)
#             except Exception as e:
#                 print("Error occurred when downloading file, error message:")
#                 print(e)
