from bing_image_downloader import downloader
# 설치할때는 bing-image-downloader 검색

# query_string = ['dog','cat','tiger']
# 리스트는 안되고 한개씩만 가능하다.
downloader.download('dog', limit=100,  output_dir='bing_dataset',
                    adult_filter_off=True, force_replace=False,
                    timeout=60, verbose=True)
