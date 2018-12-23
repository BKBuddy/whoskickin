import React, { Component } from 'react';
import _ from 'lodash';
import Game from './game.js';

export default class GameList extends Component {
    constructor(props){
        super(props);
        this.state = null;
    }

    componentDidUpdate(prevProps){
        if(prevProps.gameData !==  this.props.gameData){
            return this.setState({gameData: this.props.gameData})
        }
    }

    render(){
        return (
            <div style={{'width':'100%'}}>
                <div className='slideOut container' onClick={this.handleClick}>
                    <div className='textAlignCenter row justify-content-center'>
                        <strong className='slideout-title col-12'>WHO'S KICKING?</strong>
                        <i className='slideout-text col-9'>find out which teams will be kicking off in the second half...</i>
                        <span className="fas fa-times fa-lg col-12 close"></span>
                    </div>
                </div>
                <div className='container weekNumber'>
                    <div className='row justify-content-center'>
                        <strong className='col-12'>WEEK 16</strong>
                    </div>
                </div>
                <div className='searchBox'>
                    <input 
                        type='text'
                        placeholder='search teams...'
                        onChange={e => this.handleChange(e)}>
                    </input>
                </div>
                    {this.state && _.values(this.state.gameData).map((game, i) => {
                        return (<Game key={i}
                                    home_team={game.home_team_abbr}
                                    away_team={game.away_team_abbr}
                                    kicking_team={game.kicking_team}>
                                </Game>);
                    })}
            </div>
        )
    }

    handleChange(e){
        if(e.target.value === "") {
             return this.setState({gameData: this.props.gameData})
        }
        let filteredGames = _.pickBy(this.props.gameData, game => {
           const userInput = e.target.value.toLowerCase();
           const home_team_searchable_name = game.home_team_searchable_name.toLowerCase();
           const away_team_searchable_name = game.away_team_searchable_name.toLowerCase();
           if(home_team_searchable_name.includes(userInput) || away_team_searchable_name.includes(userInput)) {
               return game;
           }
        });
        this.setState({gameData: filteredGames});
    }

    handleClick(e){
        let slideOutPanel = e.currentTarget;
        if (slideOutPanel) {
            slideOutPanel.classList.add('slideIn');
        }
    }

    
}