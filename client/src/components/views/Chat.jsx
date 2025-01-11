import React, { useState } from 'react';
import styled from 'styled-components';
import Header from '../utils/Header/Header';

const Chat = () => {
  const [input, setInput] = useState('');
  const [response, setResponse] = useState('');

  const handleInputChange = (e) => {
    setInput(e.target.value);
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      setResponse(`You entered: ${input}`);
      setInput('');
    }
  };

  return (
    <Container>
      <Header />
      <ChatContainer>
        <Input
          type="text"
          value={input}
          onChange={handleInputChange}
          onKeyPress={handleKeyPress}
          placeholder={input || "✨ I’m looking for..."}
        />
      </ChatContainer>
    </Container>
  );
};

const Container = styled.div`
  background-color: #1e1e1e;
  color: #fff;
  text-align: center;
  padding: 50px;
  min-height: 100vh;
`;

const ChatContainer = styled.div`
  margin-top: 20px;
`;


const Input = styled.input`
  width: 800px;
  padding: 15px;
  margin-top: 0px;
  font-size: 1em;
  border: none;
  border-radius: 5px;
  background-color: #2e2e2e;
  color: #fff;
  outline: none;
  box-shadow: 0 0 5px rgba(255, 255, 255, 0.2);
`;

export default Chat;
