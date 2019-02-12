import React, { Component } from 'react';
import axios from 'axios';
import './App.css';

// Components
import Movement from './Movement/Movement';
import Room from './Room/Room';

require('dotenv').config();

axios.defaults.baseURL = 'https://lambda-treasure-hunt.herokuapp.com/api/adv';
axios.defaults.headers.common['Authorization'] = process.env.TOKEN_KEY;
axios.defaults.headers.post['Content-Type'] = 'application/json';

class App extends Component {
  constructor() {
    super();
  }
  componentDidMount() {
    axios.get('/init/')
      .then(res => {
        console.log(res)
      })

  }
  render() {
    return (
      <div className="App">
        <h1>Lambda Treasure Hunt</h1>
        <Room />
        <Movement />
      </div>
    );
  }
}

export default App;
