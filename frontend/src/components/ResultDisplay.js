import React from 'react';
import './ResultDisplay.css';

function ResultDisplay({ tweet, error }) {
  if (error) {
    return (
      <div className="result-display error">
        <h2>Error:</h2>
        <p>{error}</p>
      </div>
    );
  }

  if (tweet) {
    return (
      <div className="result-display success">
        <h2>Result:</h2>
        <p>{tweet}</p>
      </div>
    );
  }

  return null;
}

export default ResultDisplay;

