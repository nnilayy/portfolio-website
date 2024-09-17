// src/components/Blob.js
import React from 'react';
import './styles/Blob.css';

const Blob = ({ color, size, top, left, delay }) => (
  <div
    className="blob"
    style={{
      backgroundColor: color,
      width: size,
      height: size,
      top,
      left,
      animationDelay: `${delay}s`,
    }}
  />
);

export const BlobContainer = () => (
  <div className="blob-container">
    <Blob color="#ffffff" size="300px" top="10%" left="10%" delay={0} />
    <Blob color="#39ff14" size="400px" top="40%" left="50%" delay={2} />
    <Blob color="#0ff" size="200px" top="40%" left="30%" delay={5} />
  </div>
);

export default Blob;
