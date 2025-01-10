import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler

# 데이터 로드
data = pd.read_csv("data/data.csv")

# 추천 모델에 사용할 특성 선택
features = ['acousticness', 'danceability', 'energy', 'instrumentalness',
            'liveness', 'loudness', 'speechiness', 'tempo', 'valence']

# 특성 행렬 준비
X = data[features]

# 특성 표준화
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# KNN 모델 초기화
knn = NearestNeighbors(n_neighbors=5, algorithm='ball_tree')

# 모델 학습
knn.fit(X_scaled)

def recommend_songs(song_name, n_recommendations=5):
    """
    주어진 곡 이름을 기반으로 곡을 추천합니다.

    매개변수:
    - song_name: str, 추천의 기준이 될 곡 이름
    - n_recommendations: int, 반환할 추천 곡의 수

    반환값:
    - recommendations: 추천 곡 이름의 리스트
    """
    # 데이터셋에서 곡의 인덱스 찾기
    song_index = data[data['name'] == song_name].index[0]

    # 곡의 특성 벡터 가져오기
    song_vector = X_scaled[song_index].reshape(1, -1)

    # 가장 가까운 이웃 찾기
    distances, indices = knn.kneighbors(song_vector, n_neighbors=n_recommendations + 1)

    # 추천 곡 인덱스 가져오기 (첫 번째는 입력 곡이므로 제외)
    recommended_indices = indices.flatten()[1:]

    # 추천 곡 이름 가져오기
    recommendations = data.iloc[recommended_indices]['name'].tolist()

    return recommendations

# 예제 사용법
if __name__ == "__main__":
    song_to_recommend = "Payphone"  # 데이터셋에 있는 실제 곡 이름으로 대체
    recommendations = recommend_songs(song_to_recommend)
    print(f"Recommendations for '{song_to_recommend}': {recommendations}") 