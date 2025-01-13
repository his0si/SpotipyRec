from flask import Flask, request, jsonify
from ChatModel import ChatModel  # ChatModel을 Chat.py에서 임포트
from flask_cors import CORS

app = Flask(__name__)  # Flask 애플리케이션 인스턴스 생성
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/chat', methods=['POST'])  # '/chat' 경로에 POST 요청을 처리하는 라우트 추가
def chat():
    user_message = request.json.get('message')  # JSON에서 사용자 메시지 추출
    if not user_message:
        return jsonify({"error": "No message provided"}), 400  # 메시지가 없을 경우 오류 반환

    chat_model = ChatModel()  # ChatModel 인스턴스 생성
    response = chat_model.get_response(user_message)  # 챗봇 응답 생성
    return jsonify({"response": response})  # JSON 형식으로 응답 반환

@app.route('/recommend', methods=['POST'])
def recommend():
    song_name = request.json.get('song')
    if not song_name:
        return jsonify({"error": "No song name provided"}), 400

    # Use the recommend_songs function from model.py
    from model import recommend_songs
    recommendations = recommend_songs(song_name)

    return jsonify({"recommendations": recommendations})

if __name__ == '__main__':
    app.run(debug=True)  # Flask 애플리케이션 실행
