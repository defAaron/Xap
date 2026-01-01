import React, { useState } from 'react';
import './SearchForm.css';

function SearchForm({ onSearch, loading }) {
  const [handle, setHandle] = useState('');
  const [date, setDate] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!handle.trim() || !date) {
      return;
    }
    onSearch(handle.trim(), date);
  };

  return (
    <form onSubmit={handleSubmit} className="search-form">
      <div className="form-group">
        <label htmlFor="handle">Twitter Handle (without @):</label>
        <input
          type="text"
          id="handle"
          value={handle}
          onChange={(e) => setHandle(e.target.value)}
          placeholder="username"
          required
          disabled={loading}
        />
      </div>

      <div className="form-group">
        <label htmlFor="date">Date (YYYY-MM-DD):</label>
        <input
          type="date"
          id="date"
          value={date}
          onChange={(e) => setDate(e.target.value)}
          required
          disabled={loading}
        />
      </div>

      <button type="submit" disabled={loading} className="submit-button">
        {loading ? 'Searching...' : 'Search'}
      </button>
    </form>
  );
}

export default SearchForm;

