import React from 'react';
import './styles/BackToHomeButton.css';
import homeIcon from './styles/icons/home.svg'; // or .png

const BackToHomeButton = () => {
  const scrollToTop = () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  };

  return (
    <div className="back-to-home-container">
      <button className="back-to-home-button" onClick={scrollToTop}>
        <img src={homeIcon} alt="Home" className="home-icon" />
        <span>Back to Home</span>
      </button>
    </div>
  );
};

export default BackToHomeButton;
