import React from 'react';
import './styles/Footer.css';
import githubIcon from './styles/icons/github.svg';
import linkedinIcon from './styles/icons/linkedin.svg';
import twitterIcon from './styles/icons/twitter.svg';
import emailIcon from './styles/icons/email.png';
import huggingFaceIcon from './styles/icons/hugging-face.svg';
const Footer = () => {
  return (
    <footer className="footer">
      <div className="footer-content">
        <div className="footer-left">
          <div className="footer-links">
            <a href="https://github.com/nnilayy" className="footer-link" target="_blank" rel="noopener noreferrer">
              <img src={githubIcon} alt="GitHub" className="footer-icon" />
            </a>
            <a href="https://linkedin.com/in/nnilayy" className="footer-link" target="_blank" rel="noopener noreferrer">
              <img src={linkedinIcon} alt="LinkedIn" className="footer-icon" />
            </a>
            <a href="https://twitter.com/nnilayy_" className="footer-link" target="_blank" rel="noopener noreferrer">
              <img src={twitterIcon} alt="Twitter" className="footer-icon" />
            </a>
            <a href="https://huggingface.co/nnilayy" className="footer-link" target="_blank" rel="noopener noreferrer">
              <img src={huggingFaceIcon} alt="Hugging Face" className="footer-icon" />
            </a>
            <a href="mailto:nnilayy.work@gmail.com" className="footer-link">
              <img src={emailIcon} alt="Email" className="footer-icon" />
            </a>
          </div>
        </div>
        <div className="footer-center">
          <p>© 2024 Nilay Kumar Bhatnagar. All rights reserved.</p>
        </div>
        <div className="footer-right"></div>
      </div>
    </footer>
  );
};

export default Footer;
