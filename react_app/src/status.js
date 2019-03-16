import  React, { Component } from  'react';

import  StocksService  from  './StocksService';

const  stocksService  =  new  StocksService();


class  StatusList  extends  Component {

    constructor(props) {
        super(props);
        this.state  = {
            stocks: []
        };
        
    }

    componentDidMount() {
        var  self  =  this;
        stocksService.getStatus().then(function (result) {
            self.setState({ stocks:  result.data, nextPageURL:  result.nextlink})
        });
    }

    
    render() {

    return (
        <div  className="customers--list">
            <table  className="table" class="w3-table w3-striped w3-border w3-centered w3-hoverable w3-card-4">
            <thead  key="thead">
            <tr>
                
                <th>Client</th>
                <th>GC</th>
                <th>Status</th>


                
            </tr>
            </thead>
            <tbody>
            {this.state.stocks.map( c  =>
            <tr  key={c.id}>
                <td>{c.client}</td>
                <td>{c.sg}</td>
                <td>{c.status}</td>
                
            </tr>)}
            </tbody>
            </table>
           
 
        </div>
        );
  }
}
export  default  StatusList;




