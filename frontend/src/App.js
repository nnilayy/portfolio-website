import React, { useEffect } from 'react';
import Navbar from './Navbar';
import Introduction from './Introduction';
import Timeline from './Timeline';
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

  return (
    <div className="App">
      {/* Grid Background */}
      <div className="grid-background"></div>

      {/* Main Content */}
      <div className="grid-container">
        <Navbar />
        <Introduction />
        <Timeline />
        <Footer />
      </div>

      {/* Cursor Follower Circle */}
      <div className="cursor-circle"></div>
    </div>
  );
}

export default App;
