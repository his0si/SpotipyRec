import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import styled from 'styled-components';
import Header from '../utils/Header/Header';

const Main = () => {
  const [inputValue, setInputValue] = useState('');
  const navigate = useNavigate();

  const handleKeyPress = (event) => {
    if (event.key === 'Enter') {
      navigate('/chat');
    }
  };

  return (
    <Container>
      <Header />
      <HeaderContainer>
        <Title>Find songs <br /> that beat your heart</Title>
        <Subtitle>Talk freely and our AI will fit the best songs for you</Subtitle>
      </HeaderContainer>
      <SearchBar>
        <SearchInput
          type="text"
          placeholder="✨ I’m looking for..."
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          onKeyPress={handleKeyPress}
        />
      </SearchBar>
      <AskText>You may ask</AskText>
      <Suggestions>
        <SuggestionCard text="Can you recommend some great songs in this category for me? I love K-pop!" />
        <SuggestionCard text="Show me the perfect song for me! My favorite is 'Butter' by BTS." />
        <SuggestionCard text="Help me discover some quality music! I especially enjoy songs from the 2020s." />
        <SuggestionCard text="I’m looking for meaningful and emotional songs." />
      </Suggestions>
    </Container>
  );
};

const SuggestionCard = ({ text }) => (
  <Card>
    <p>{text}</p>
    <AskLink href="#">Ask this ↗</AskLink>
  </Card>
);

const Container = styled.div`
  background-color: #1e1e1e;
  color: #fff;
  text-align: center;
  padding: 50px;
  min-height: 100vh;
`;

const HeaderContainer = styled.header`
  margin-bottom: 30px;
`;

const Title = styled.h1`
  font-size: 3em;
  font-weight: bold;
  margin-bottom: 10px;
  background: linear-gradient(to right, #ff7e5f, #feb47b);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
`;

const Subtitle = styled.p`
  font-size: 1.2em;
`;

const SearchBar = styled.div`
  margin-bottom: 40px;
`;

const SearchInput = styled.input`
  width: 60%;
  max-width: 600px;
  padding: 15px;
  border-radius: 25px;
  border: none;
  font-size: 1em;
`;

const Suggestions = styled.div`
  display: flex;
  justify-content: center;
  gap: 20px;
`;

const Card = styled.div`
  background-color: #333;
  padding: 20px;
  border-radius: 10px;
  width: 200px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  text-align: left;
  position: relative;
`;

const AskLink = styled.a`
  color: #ff7e5f;
  text-decoration: none;
  position: relative;
  width: auto;
  margin-top: auto;
  white-space: nowrap;
`;

const AskText = styled.p`
  color: gray;
  font-size: 1em;
  margin-bottom: 50px;
`;

export default Main;
