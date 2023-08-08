import requests
import pandas as pd
import sys
def main():
    api_key = 'Your-API-Key'
    #After giving a permission for each endpoint by administrator:
    for endpoint in ['research-outputs','persons','journals','publishers','organizations','external-organizations']:
        url = f"https://cris.haifa.ac.il/ws/api/{endpoint}?apiKey=" + api_key
        header = {"Accept": "application/json"} 
        query_params = {'size': 100, 'offset': 0}
        response_decoded_json = requests.get(url, headers=header, params=query_params)
        json_data = response_decoded_json.json()
        df = pd.json_normalize(json_data["items"])
        df_list = []
        size = 1000
        offset = 0
        while True:
            query_params = {'size': size, 'offset': offset}
            response_decoded_json = requests.get(url, headers=header, params=query_params)
            if response_decoded_json.status_code == 200:
                json_data = response_decoded_json.json()
                df = pd.json_normalize(json_data["items"])  
                df_list.append(df)
                total = json_data['count']
                print(f'Retrieved {len(df)} items, Total retrieved so far: {offset+len(df)} out of {total}')
                if offset + len(df) >= total:
                    break
                offset += size
            else:
                print('Error:', response_decoded_json.status_code)
                break
        full_df = pd.concat(df_list, ignore_index=True)
        full_df.to_excel(fr"C:\vsprojects\cris_output\raw_data\{endpoint}_cris.xlsx",index=False)       
        
if __name__ == "__main__":
    main()
    sys.exit()