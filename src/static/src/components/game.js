import React, { Component } from 'react';
import '../stylesheets/game.css';
import 'bootstrap';

export default class Game extends Component {
    render(){
        return (
            <div className='container'>
                <div className='row'>
                    <div className='col-sm-4'>
                        @{this.props.home_team}
                    </div>
                    <div className='col-sm-4'></div>
                    <div className='col-sm-4'>
                        {this.props.away_team}
                    </div>
                </div>
            </div>
        )
    }
}