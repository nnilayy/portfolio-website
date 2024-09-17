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
    <Blob color="#7e7b77" size="30vw" top="10%" left="5%" delay={0} />
    <Blob color="rgba(105, 42, 213)" size="25vw" top="20%" left="45%" delay={3} />
    <Blob color="rgb(216, 216, 42)" size="30vw" top="20%" left="60%" delay={5} />
  </div>
);

export default Blob;
