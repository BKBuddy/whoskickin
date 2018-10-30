import React, { Component } from 'react';
import _ from 'lodash';
import '../stylesheets/App.css';
import Game from './game';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      "2018102500": {
        "away_team": "MIA",
        "home_team": "HOU",
        "kicking_team": "MIA"
      },
      "2018102800": {
        "away_team": "PHI",
        "home_team": "JAX",
        "kicking_team": null
      },
      "2018102801": {
        "away_team": "BAL",
        "home_team": "CAR",
        "kicking_team": null
      },
      "2018102802": {
        "away_team": "NYJ",
        "home_team": "CHI",
        "kicking_team": null
      },
      "2018102803": {
        "away_team": "TB",
        "home_team": "CIN",
        "kicking_team": null
      },
      "2018102804": {
        "away_team": "SEA",
        "home_team": "DET",
        "kicking_team": null
      },
      "2018102805": {
        "away_team": "DEN",
        "home_team": "KC",
        "kicking_team": null
      },
      "2018102806": {
        "away_team": "WAS",
        "home_team": "NYG",
        "kicking_team": null
      },
      "2018102807": {
        "away_team": "CLE",
        "home_team": "PIT",
        "kicking_team": null
      },
      "2018102808": {
        "away_team": "IND",
        "home_team": "OAK",
        "kicking_team": null
      },
      "2018102809": {
        "away_team": "SF",
        "home_team": "ARI",
        "kicking_team": null
      },
      "2018102810": {
        "away_team": "GB",
        "home_team": "LA",
        "kicking_team": null
      },
      "2018102811": {
        "away_team": "NO",
        "home_team": "MIN",
        "kicking_team": null
      },
      "2018102900": {
        "away_team": "NE",
        "home_team": "BUF",
        "kicking_team": null
      }
    }
  }
  render() {
    return (
      <div className="App">
        {_.keys(this.state).map((key)=>{
            return <Game key={key}
                      home_team={this.state[key]['home_team']}
                      away_team={this.state[key]['away_team']}
                      kicking_team={this.state[key]['kicking_team']}>
                   </Game>
        })}
      </div>
    );
  }
}

export default App;
