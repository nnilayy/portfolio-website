import React, { useEffect } from 'react';
import Navbar from './Navbar';
import Introduction from './Introduction';
import Timeline from './Timeline';
import BackToHomeButton from './BackToHomeButton';
import Footer from './Footer';
import './styles/App.css';

function App() {
  useEffect(() => {
    const cursorCircle = document.querySelector('.cursor-circle');

    const moveCursor = (e) => {
      const circleRadius = cursorCircle.offsetWidth / 2;
      cursorCircle.style.transform = `translate(${e.clientX - circleRadius}px, ${e.clientY - circleRadius}px)`;
    };

    window.addEventListener('mousemove', moveCursor);

    return () => {
      window.removeEventListener('mousemove', moveCursor);
    };
  }, []);

  const backIcon = (
    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <path d="M19 12H5M12 19l-7-7 7-7"/>
    </svg>
  );

  return (
    <div className="App">
      {/* Grid Background */}
      <div className="grid-background"></div>

      {/* Main Content */}
      <div className="grid-container">
        <Navbar />
        <Introduction />
        <Timeline numCheckpoints={5} />
        <BackToHomeButton svgIcon={backIcon} />
        <Footer />
      </div>

      {/* Cursor Follower Circle */}
      <div className="cursor-circle"></div>
    </div>
  );
}

export default App;
