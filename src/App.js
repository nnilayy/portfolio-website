// src/App.js
import React from 'react';
import Navbar from './Navbar';
import Introduction from './Introduction';
import Timeline from './Timeline';
import Footer from './Footer';
import './styles/App.css';

function App() {
  return (
    <div>
      <Navbar />
      <Introduction />
      <Timeline />
      <Footer />
    </div>
  );
}

export default App;
