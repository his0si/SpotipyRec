import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

try:
    # Spotify 앱의 상세 정보 설정
    spotify_details = {
        "client_id": os.getenv("SPOTIFY_CLIENT_ID"),      # 환경 변수에서 가져오기
        "client_secret": os.getenv("SPOTIFY_CLIENT_SECRET"), # 환경 변수에서 가져오기
        "redirect_uri": "http://localhost:8080"
    }

    # Spotify API 접근 권한 (scope)
    scope = "user-library-read"

    # Spotipy 클라이언트 생성
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=spotify_details['client_id'],
            client_secret=spotify_details['client_secret'],
            redirect_uri=spotify_details['redirect_uri'],
            scope=scope,
            open_browser=True
        )
    )

    # 아티스트 검색 예제
    result = sp.search('iu', limit=2, type='artist')
    pprint.pprint(result)

except Exception as e:
    print(f"에러가 발생했습니다: {str(e)}")
