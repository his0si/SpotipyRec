#################### 1. Read Data ####################
# 필요한 라이브러리 임포트
import os
import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px 
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
from sklearn.metrics import euclidean_distances
from scipy.spatial.distance import cdist

# 경고 메시지 숨기기
import warnings
warnings.filterwarnings("ignore")

# 데이터 파일 읽기
data = pd.read_csv("data/data.csv")              # 개별 곡들의 특성 데이터
genre_data = pd.read_csv('data/data_by_genres.csv')  # 장르별 집계 데이터
year_data = pd.read_csv('data/data_by_year.csv')     # 연도별 집계 데이터

# 각 데이터셋의 기본 정보 출력
print(data.info())
print(genre_data.info())
print(year_data.info())

# 특성과 인기도 간의 상관관계 분석
from yellowbrick.target import FeatureCorrelation

# 분석할 특성 목록 정의
feature_names = ['acousticness', 'danceability', 'energy', 'instrumentalness',
       'liveness', 'loudness', 'speechiness', 'tempo', 'valence','duration_ms','explicit','key','mode','year']

# 특성(X)과 타겟(y, 인기도) 분리
X, y = data[feature_names], data['popularity']
features = np.array(feature_names)

# 상관관계 시각화
visualizer = FeatureCorrelation(labels=features)
plt.rcParams['figure.figsize']=(20,20)
visualizer.fit(X, y)     
visualizer.show()


#################### 2. Music Over Time ####################
# 연도를 십년단위로 변환하는 함수 정의
def get_decade(year):
    period_start = int(year/10) * 10
    decade = '{}s'.format(period_start)
    return decade

# 데이터에 십년단위 열 추가
data['decade'] = data['year'].apply(get_decade)

# 십년단위별 곡 수 분포 시각화
sns.set(rc={'figure.figsize':(11 ,6)})
sns.countplot(data['decade'])

# 연도별 음악 특성 변화 추적
sound_features = ['acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'valence']
fig = px.line(year_data, x='year', y=sound_features)
fig.show()


#################### 3. Characteristics of Different Genres ####################
# 인기도 기준 상위 10개 장르 선택
top10_genres = genre_data.nlargest(10, 'popularity')

# 상위 10개 장르의 주요 특성 비교
fig = px.bar(top10_genres, x='genres', y=['valence', 'energy', 'danceability', 'acousticness'], 
             barmode='group',
             title='Top 10 Genres and Their Musical Characteristics')
fig.show()


#################### 4. Clustering Genres with K-Means ####################
# K-Means 클러스터링을 사용하여 장르 군집화
cluster_pipeline = Pipeline([('scaler', StandardScaler()), ('kmeans', KMeans(n_clusters=10, n_jobs=-1))])
X = genre_data.select_dtypes(np.number)
cluster_pipeline.fit(X)
genre_data['cluster'] = cluster_pipeline.predict(X)

# t-SNE를 사용하여 클러스터 시각화
tsne_pipeline = Pipeline([('scaler', StandardScaler()), ('tsne', TSNE(n_components=2, verbose=1))])
genre_embedding = tsne_pipeline.fit_transform(X)
projection = pd.DataFrame(columns=['x', 'y'], data=genre_embedding)
projection['genres'] = genre_data['genres']
projection['cluster'] = genre_data['cluster']

fig = px.scatter(
    projection, x='x', y='y', color='cluster', hover_data=['x', 'y', 'genres'])
fig.show()


#################### 5. Clustering Songs with K-Means ####################
# K-Means 클러스터링을 사용하여 곡 군집화
song_cluster_pipeline = Pipeline([('scaler', StandardScaler()), 
                                  ('kmeans', KMeans(n_clusters=20, 
                                   verbose=False, n_jobs=4))
                                 ], verbose=False)

X = data.select_dtypes(np.number)
number_cols = list(X.columns)
song_cluster_pipeline.fit(X)
song_cluster_labels = song_cluster_pipeline.predict(X)
data['cluster_label'] = song_cluster_labels

# PCA를 사용하여 클러스터 시각화
pca_pipeline = Pipeline([('scaler', StandardScaler()), ('PCA', PCA(n_components=2))])
song_embedding = pca_pipeline.fit_transform(X)
projection = pd.DataFrame(columns=['x', 'y'], data=song_embedding)
projection['title'] = data['name']
projection['cluster'] = data['cluster_label']

fig = px.scatter(
    projection, x='x', y='y', color='cluster', hover_data=['x', 'y', 'title'])
fig.show()