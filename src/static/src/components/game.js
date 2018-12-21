import React, { Component } from 'react';
import '../stylesheets/game.css';
import '../stylesheets/team-colors.css';
import 'bootstrap';

export default class Game extends Component {
    render(){
        const { home_team, away_team, kicking_team } = this.props
        return (
            <div className='gameContainer container'>
                <div className='row'>
                    <span className={`${home_team} teamColor`}></span><p className='teamName grey-bg'>{`@${home_team}`}</p>
                </div>
                <div className='row'>
                    <span className={`${away_team} teamColor`}></span><p className='teamName grey-bg'>{away_team}</p>
                </div>
            </div>
        )
    }
}