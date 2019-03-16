import  React, { Component } from  'react';

import  StocksService  from  './StocksService';

const  stocksService  =  new  StocksService();


class  ClientList  extends  Component {

    constructor(props) {
        super(props);
        this.state  = {
            stocks: []
        };
        
    }

    componentDidMount() {
    	var  self  =  this;
    	stocksService.getClient().then(function (result) {
        	self.setState({ stocks:  result.data, nextPageURL:  result.nextlink})
    	});
    }

    
	render() {

    return (
        <div  className="customers--list">
            <table  className="table" class="w3-table w3-striped w3-border w3-centered w3-hoverable w3-card-4">
            <thead  key="thead">
            <tr>
                
                <th>ID</th>
                
            </tr>
            </thead>
            <tbody>
            {this.state.stocks.map( c  =>
            <tr  key={c.id}>
                <td>{c.id}</td>
                
            </tr>)}
            </tbody>
            </table>
           
 
        </div>
        );
  }
}
export  default  ClientList;




