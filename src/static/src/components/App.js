import React, { Component } from 'react';
import _ from 'lodash';
import 'jquery';
import 'popper.js'
import 'bootstrap';
import axios from 'axios';
import Game from './game';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

componentDidMount(){
  return axios.get('http://localhost:5000/all_kicks')
    .then(response => this.setState(response.data));
}

  render() {
    return (
      <div className="container">
        <div className='justify-content-center'>
          {_.keys(this.state).map((key)=>{
              return <Game className='row' key={key}
                        home_team={this.state[key]['home_team']}
                        away_team={this.state[key]['away_team']}
                        kicking_team={this.state[key]['kicking_team']}>
                    </Game>
          })}
        </div>
      </div>
    );
  }
}

export default App;
