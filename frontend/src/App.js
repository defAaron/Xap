import React, { useState } from 'react';
import './App.css';
import SearchForm from './components/SearchForm';
import ResultDisplay from './components/ResultDisplay';

function App() {
  const [tweet, setTweet] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSearch = async (handle, date) => {
    setLoading(true);
    setError(null);
    setTweet(null);

    try {
      const formData = new FormData();
      formData.append('handle', handle);
      formData.append('date', date);

      // Use environment variable or fallback to proxy/relative URL
      const apiUrl = process.env.REACT_APP_API_URL || '/api/search';
      const response = await fetch(apiUrl, {
        method: 'POST',
        body: formData,
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || 'An error occurred');
      }

      setTweet(data.tweet);
    } catch (err) {
      setError(err.message);
      setTweet(null);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <div className="container">
        <h1>Find a Tweet</h1>
        <SearchForm onSearch={handleSearch} loading={loading} />
        {(tweet || error) && (
          <ResultDisplay tweet={tweet} error={error} />
        )}
      </div>
    </div>
  );
}

export default App;
