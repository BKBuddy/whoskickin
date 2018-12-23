import React, { Component } from 'react';
import '../stylesheets/game.css';
import '../stylesheets/team-colors.css';
import 'bootstrap';

export default class Game extends Component {
    render(){
        const { home_team, away_team, kicking_team } = this.props
        const isTBD = kicking_team === null;
        const homeTeamStatus = isTBD ? 'TBD' : home_team === kicking_team ? 'kicking' : 'receiving';
        const awayTeamStatus = isTBD ? 'TBD' : away_team === kicking_team ? 'kicking' : 'receiving';
        return (
            <div className='gameContainer container'>
                <div className='row grey-bg'>
                    <span className={`${home_team} teamColor col-1`}></span>
                    <p className='teamName col-3'>{`@${home_team}`}</p>
                    <p className='status col-4'>{homeTeamStatus}</p>
                </div>
                <div className='row grey-bg'>
                    <span className={`${away_team} teamColor col-1`}></span>
                    <p className='teamName col-3'>{away_team}</p>
                    <p className='status col-4'>{awayTeamStatus}</p>
                </div>
            </div>
        )
    }
}