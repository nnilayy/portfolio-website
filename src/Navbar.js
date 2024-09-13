// src/Navbar.js
import React from 'react';
import './Navbar.css';

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="navbar-links">
        <a href="https://linkedin.com/in/yourusername" target="_blank" rel="noopener noreferrer">
          LinkedIn
        </a>
        <a href="https://twitter.com/yourusername" target="_blank" rel="noopener noreferrer">
          Twitter
        </a>
        <a href="https://github.com/yourusername" target="_blank" rel="noopener noreferrer">
          GitHub
        </a>
        <a href="/resume.pdf" target="_blank" rel="noopener noreferrer">
          Resume
        </a>
        <a href="mailto:your.email@example.com">
          Email
        </a>
      </div>
    </nav>
  );
};

export default Navbar;
