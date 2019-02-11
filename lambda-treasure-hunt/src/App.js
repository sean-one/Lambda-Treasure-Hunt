import React, { Component } from 'react';
import './App.css';

// Components
import Movement from './Movement/Movement';

class App extends Component {
  constructor() {
    super();
  }
  render() {
    return (
      <div className="App">
        <h1>Lambda Treasure Hunt</h1>
        <Movement />
      </div>
    );
  }
}

export default App;
