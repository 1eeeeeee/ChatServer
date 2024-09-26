import csv
import json

# 讀取 CSV 文件並轉換為 JSON 格式
def csv_to_json(csv_file_path, json_file_path):
    data = []
    
    # 打開並讀取 CSV 文件
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        
        # 將每行數據添加到列表中
        for row in csv_reader:
            data.append(row)
    
    # 將數據寫入 JSON 文件
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)

# 主函數
if __name__ == "__main__":
    csv_file_path = 'username.csv'
    json_file_path = 'username.json'
    csv_to_json(csv_file_path, json_file_path)
    print(f"CSV 文件已成功轉換為 JSON 格式並保存到 {json_file_path}")