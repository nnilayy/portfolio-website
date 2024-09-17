// src/components/Blob.js
import React from 'react';
import './styles/Blob.css';

const Blob = ({ className }) => (
  <div className={`blob ${className}`} />
);

export const BlobContainer = () => (
  <div className="blob-container">
    <Blob className="blob-1" />
    <Blob className="blob-2" />
    <Blob className="blob-3" />
  </div>
);

export default Blob;
