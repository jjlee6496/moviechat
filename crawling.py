
## 2024년 1월 4일 다음영화 서비스 종료..

# import random
# import time
# import re
# import os
# import argparse
# import pandas as pd
# from datetime import datetime
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options

# # 다음 영화 사이트 크롤링 수행 함수
# def crawl_daum_movie():
#     # Selenium 웹 드라이버 설정
#     driver = webdriver.Chrome()
#     options = Options()

#     #지정한 user-agent로 설정합니다.
#     user_agent = "Mozilla/5.0 (Linux; Android 9; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.83 Mobile Safari/537.36"
#     options.add_argument('user-agent=' + user_agent)
#     options.add_argument('headless') # headless모드 브라우저가 뜨지 않고 실행됩니다.
#     options.add_argument('--blink-settings=imagesEnabled=false') # 브라우저에서 이미지 로딩을 하지 않습니다.
#     options.add_argument('incognito') # 시크릿 모드의 브라우저가 실행됩니다.

#     # 웹 페이지 열기
#     url = 'https://movie.daum.net/premovie/theater'
#     driver.get(url)
#     print('영화 정보 크롤링 중...')
#     # 페이지가 완전히 로딩되도록 3초동안 기다림
#     time.sleep(3)

#     # 해당 경로의 요소 가져오기
#     ol_element = driver.find_element(By.XPATH, '//*[@id="mainContent"]/div/div[2]/ol')
#     # ol 아래의 모든 li 요소 가져오기
#     li_elements = ol_element.find_elements(By.TAG_NAME, 'li')
#     infos = []

#     # 가져온 li 요소 출력
#     for li in li_elements:
#         li.click()
#         # 0.4에서 0.6 사이의 랜덤한 값을 선택하여 sleep에 적용
#         random_sleep_time = random.uniform(0.4, 0.6)
#         time.sleep(random_sleep_time)
#         infos.append(li.text)

#     # 웹 드라이버 종료
#     driver.quit()
#     return infos

# # 크롤링한 정보 파싱
# def parse_movie_info(movie_info_list):
#     print('영화 정보 파싱 중...')
#     parsed_info = []
#     for info in movie_info_list:
#         split_info = info.split('\n')
#         if len(split_info) == 5:
#             if len(split_info[3].split())!=2: # 평점 또는 예몌율이 없는 경우 건너뜀
#                 continue
#             age_limit = split_info[0]
#             plot = split_info[1]
#             title = split_info[2]
#             rating, booking_rate = (split_info[3].split())
#             rating = re.findall(r'\d+\.\d+', rating)
#             booking_rate = re.findall(r'예매율(\d+\.\d+)%', booking_rate)            
#             release_date = re.sub(r'\D', '', split_info[4])
#             release_date_formatted = datetime.strptime('20'+release_date, '%Y%m%d').strftime('%y-%m-%d')
            
#             parsed_info.append({
#                 '관람가': age_limit,
#                 '제목' : title,
#                 '평점': rating,
#                 '예매율': booking_rate,
#                 '개봉일': release_date_formatted,
#                 '줄거리': plot,
#             })
#     return pd.DataFrame(parsed_info)

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#     parser.add_argument('path', type=str, help='데이터 경로 입력')
#     args = parser.parse_args()
    
#     movie_info_list = crawl_daum_movie()
#     movie_list = parse_movie_info(movie_info_list)
#     output_dir = f'./{args.path}/daum_movie'
#     if not os.path.exists(output_dir):
#         os.makedirs(output_dir)
#     movie_list.to_csv(os.path.join(output_dir,'movie_list.csv'), encoding='utf-8', index=False)
#     print('저장 완료')