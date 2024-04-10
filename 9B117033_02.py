import os
import json

def search_search(data,student_id):
    #學號查詢學生資料，有查到回傳資料，查無則回傳None
    for d in data:                                                      #依序取出資料
        if(d.get("student_id") ==student_id):                           #使用字典.get()取出資料，值是否等於查詢的學號
            return d                                                    #找到資料後退出函式
    return None                                                         #找不到資料回傳None

def get_student_info(data, student_id):
    #根據學號返回該學生的個人資料字典
    #如果找不到該學生，則手動拋出 ValueError 與錯誤訊息供上層呼叫程式處理。
    search_data = search_search(data,student_id)                           #自訂函式搜尋學生資料，查無資料會回傳None
    if(search_data!=None):
        print(json.dumps(search_data,ensure_ascii=False,indent=4))         #印出資料，使用json.dumps格式化內容，ensure_ascii=False為照原始資料顯示，indent=4為縮排空格的數量
    else:
        raise ValueError("發生錯誤: 學號 {} 找不到.".format(student_id))     #未找到資料，拋出ValueError錯誤

def add_course(data, student_id, course_name, course_score):
    #為指定學生添加一門課程及其分數
    #如果找不到該學生，則手動拋出 ValueError與錯誤訊息
    #確保課程名稱與課程分數不可為空字串
    assert not (not course_name or str(course_name).isspace() or not course_score),"其它例外: 課程名稱或分數不可空白."          #判斷輸入課程名稱、分數不是空字串和不是空格，錯誤提示訊息
    try:
        dic = {"name":course_name, "score":float(course_score) }        #建立字典並將使用者的輸入存入字典，分數轉換為浮點數
    except ValueError:
        raise ValueError("輸入錯誤!課程的分數請輸入數字!")                 #無法轉換，發生錯誤並傳回警告

    search_data = search_search(data,student_id)                        #自訂函式搜尋學生資料，查無資料會回傳None
    if(search_data!=None):
        search_data["courses"].append(dic)                              #將課程和分數加入至該學生資料中
    else:
        raise ValueError("發生錯誤: 學號 {} 找不到.".format(student_id))  #未找到資料，拋出ValueError錯誤

def calculate_average_score(student_data):
    #計算並返回一位學生所有課程的平均分數，如果該學生沒有課程，則返回 0.0。
    #如果找不到該學生，則手動拋出 ValueError與錯誤訊息
    score_sum = 0.0
    if(len(student_data["courses"])>0):                                 #檢查學生是否有成績
        for d in student_data["courses"]:
            score_sum += d["score"]                                     #將每一項成績加總
        score_sum = score_sum/len(student_data["courses"])              #將成績除科目數量
        print("各科平均分數 : {:.2f}".format(score_sum))                 #顯示平均分數，顯示至小數點第二位
    else:
        print("各科平均分數 : 0.0")                                      #沒有成績，顯示0.0分

#主程式
def main():
    file_name = 'students.json'                                         #儲存json檔案名稱

    if (os.path.isfile(file_name)):                                     #確認是否有json檔案
        with open(file_name,'r', encoding="utf-8") as file:             #開啟檔案，唯讀，編碼指定utf-8
             data = json.load(file)                                     #讀取資料
    else:
        print("找不到檔案!")
        return                                                          #跳出函式，結束程式

    while(True):                                                        #使用無窮迴圈
        print("***************選單***************")
        print("1. 查詢指定學號成績")
        print("2. 新增指定學號的課程名稱與分數")
        print("3. 顯示指定學號的各科平均分數")
        print("4. 離開")

        choose = input("請選擇操作項目：")                                #等待使用者輸入選擇項目
        match choose:
            case "1":
                student_id = input("請輸入學號: ")
                try:
                    get_student_info(data, student_id)
                except ValueError as e:
                    print(e.args[0])                                    #印出錯誤訊息
            case "2":
                try:
                    student_id = input("請輸入學號 : ")
                    course_name = input("請輸入要新增課程的名稱 : ")
                    course_score = input("請輸入要新增課程的分數 : ")
                    add_course(data, student_id, course_name, course_score)
                except ValueError as e:
                    print(e.args[0])                                    #印出錯誤訊息
                except AssertionError as e:
                    print(e.args[0])                                    #印出錯誤訊息

            case "3":
                student_id = input("請輸入學號 : ")
                search_data = search_search(data,student_id)                           #自訂函式搜尋學生資料，查無資料會回傳None
                if(search_data!=None):
                    calculate_average_score(search_data)                               #呼叫函式計算平均成績
                else:
                    print("發生錯誤: 學號 {} 找不到.".format(student_id))                #未找到資料，顯示錯誤
            case "4":
                print("程式結束。")
                return
            case default:
                print("請輸入有效的選項。")

if __name__ == "__main__":
    main()
