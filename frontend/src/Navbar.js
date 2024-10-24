// src/Navbar.js
import React from 'react';
import './styles/Navbar.css';

const Navbar = () => {
  const handleLinkClick = (e, targetId) => {
    e.preventDefault();
    const targetElement = document.getElementById(targetId);
    if (targetElement) {
      targetElement.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <nav className="navbar">
      <div className="navbar-links">
        <a href="#introduction" onClick={(e) => handleLinkClick(e, 'introduction')}>
          About
        </a>
        <a href="#work" onClick={(e) => handleLinkClick(e, 'work')}>
          Work
        </a>
        <a href="#contacts" onClick={(e) => handleLinkClick(e, 'contacts')}>
          Contact
        </a>
      </div>
    </nav>
  );
};

export default Navbar;
