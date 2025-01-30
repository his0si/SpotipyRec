# SpotipyRec

## 프로젝트 소개
_**2024 Winter HoPy project**_<br>

딥러닝을 활용한 Spotipy 음악 추천 프로그램 



<details>
<summary> 시현 영상 </summary>
<div markdown="1">    


https://github.com/user-attachments/assets/1235020f-4c69-49af-95f9-85b511a6326f

  
</div>
</details>


![image](https://github.com/user-attachments/assets/7453c3db-03f9-42c7-92c9-e22153cd23c0)

## ✨ 기능
**SpotipyRec**가 제공하는 기능은 다음과 같습니다.
###### &nbsp;&nbsp;&nbsp;&nbsp;v1.0
- 사용자가 좋아하는 곡 입력 시 비슷한 곡 추천

<br>

### 프로젝트 시작
```
git clone https://github.com/his0si/SpotipyRec.git

cd SpotipyRec
pip install -r requirements.txt --user

cd client
npm run dev
```


##  팀원 소개
|     김희서     |     구지원     |     이연재     |
|:--------------:|:--------------:|:--------------:|
| 팀장, FE , BE , ML | ML | ML |

<br>

## 기술 스택

- Frontend: React
- Backend: Flask
- API: OpenAI API, Spotipy API

<br>


## 📂 Directory Structure

```
📦 SpotipyRec
├─ 📂 data                           # Spotify dataset
├─ 📄 data.csv
├─ 📄 data_by_genres.csv
├─ 📄 data_by_year.csv
│
├─ 📂 client                         # React 프론트엔드 디렉토리
│  ├─ 📦 node_modules
│  ├─ 📂 public
│  │  └─ 📄 index.html
│  └─ 📂 src
│     ├─ 📄 App.js
│     ├─ 📄 index.js
│     └─ 📂 components
│        ├─ 📂 images
│        ├─ 📂 style
│        ├─ 📂 utils                 # 유틸리티 함수들을 모아둔 디렉토리
│        └─ 📂 views                 # 페이지 단위의 컴포넌트 디렉토리
│           └─ 📄 Main.jsx           # 채팅 관련 메인 컴포넌트
│ 
├─ 🐍 app.py                         # Flask 백엔드 메인 애플리케이션
├─ 🐍 chat_model.py                  # ChatGPT API 연동 로직
├─ 🐍 EDA.py                         # data 폴더의 데이터 시각화
├─ 🐍 model.py                       # KNN 모델
├─ 📄 package.json                   # 프로젝트 의존성 및 스크립트 정의
├─ 📄 .env                           # 환경 변수 파일 (API 키 등)
├─ 📄 .gitignore
├─ 📄 requirements.txt               # 패키지 설치
├─ 📄 LICENSE
└─ 📄 README.md 
```


