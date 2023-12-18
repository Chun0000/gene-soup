import pandas as pd 
file_path="/Users/lijinhong/Desktop/pyProgram/DVD_final.txt"
#genename=input ("please inut the target gene:", )
genename='ADGRV1'
#genename= genename.upper
def search_gene_data_pandas(file_path, target_gene):
    try:
        # 讀取資料到 DataFrame
        df = pd.read_csv(file_path, sep='\t', encoding='utf-8')  # 假設資料以 tab ('\t') 分隔

        # 選取符合基因名稱的資料
        result = df.loc[df['GENE'] == target_gene, ['GENE', 'FINAL_PATHOGENICITY']]
        # 檢查是否有找到符合條件的資料
        if not result.empty:
            # 按照 ClinicalSignificance 欄位進行排序
            result = result.sort_values(by='FINAL_PATHOGENICITY')
            # 將結果寫入新檔案，使用原始索引以保留與原始資料相同的格式
            result.to_csv('output.txt', header=True, encoding='utf-8', sep='\t')
            print(f'已成功找到基因 {target_gene} 的相關資料，並寫入 output.txt 檔案中。')
        else:
            print(f'找`不到基因 {target_gene} 的相關資料。')
    except FileNotFoundError:
        print(f'找不到指定的檔案：{file_path}')
    except Exception as e:
        print(f'發生錯誤：{e}')

# 使用範例
search_gene_data_pandas(file_path, genename)

import pandas as pd

def calculate_percentage(input_file, output_file):
    try:
        # 讀取輸入檔案到 DataFrame
        df = pd.read_csv(input_file, sep='\t', encoding='utf-8')  # 假設資料以 tab ('\t') 分隔

        # 檢查是否有 FINAL_PATHOGENICITY 欄位
        if 'FINAL_PATHOGENICITY' not in df.columns:
            print('找不到 FINAL_PATHOGENICITY 欄位。')
            return

        # 計算每個內容的次數
        counts = df['FINAL_PATHOGENICITY'].value_counts()

          # 對 FINAL_PATHOGENICITY 欄位進行排序
        counts = counts.sort_index()

        # 計算比例
        percentages = counts / counts.sum() * 100  # 將比例轉換成百分比形式

        # 將比例四捨五入到小數點後兩位
        percentages = percentages.round(2)

        # 在 result DataFrame 中加入 Genesymbol 欄位
        result = pd.DataFrame({'GENE': [df['GENE'].iloc[0]] * len(counts), 'FINAL_PATHOGENICITY': counts.index, 'Number': counts, 'Percentages': percentages})

        # 將結果橫向表示，並加入%符號
        result['Percentages'] = result['Percentages'].astype(str) + '%'

        # 調整欄位順序
        result = result[['GENE', 'FINAL_PATHOGENICITY', 'Number', 'Percentages']]

        # 寫入新檔案，直接覆蓋舊檔案
        result.to_csv(output_file, header=True, sep='\t', mode='w', index=False)
        print(f'統計結果已成功寫入 {output_file}。')
    except FileNotFoundError:
        print(f'找不到指定的檔案：{input_file}')
    except Exception as e:
        print(f'發生錯誤：{e}')

# 使用範例
calculate_percentage('output.txt', 'new_output.txt')


