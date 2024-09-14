// src/Navbar.js
import React from 'react';
import './styles/Navbar.css';

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="navbar-links">
        <a href="https://linkedin.com/in/nnilayy" target="_blank" rel="noopener noreferrer">
          LinkedIn
        </a>
        <a href="https://twitter.com/nnilayy_" target="_blank" rel="noopener noreferrer">
          Twitter
        </a>
        <a href="https://github.com/nnilayy" target="_blank" rel="noopener noreferrer">
          GitHub
        </a>
        <a href="/resume.pdf" target="_blank" rel="noopener noreferrer">
          Resume
        </a>
        <a href="mailto:nnilayy.work@gmail.com">
          Email
        </a>
      </div>
    </nav>
  );
};

export default Navbar;
