import React, { Component } from "react";
import { BrowserRouter } from "react-router-dom";
import { Route, Link, withRouter } from "react-router-dom";
import ClientList from "./StocksList";
import SGList from "./SGList";
import StatusList from "./status"; 
import "./App.css";
import { Button } from "react-bootstrap";
import StocksHistory from "./stock_history";

import {
  Nav,
  Navbar,
  NavItem,
  NavForm,
  Form,
  FormControl
} from "react-bootstrap";
import StocksService from "./StocksService";
import "w3-css/w3.css";
const stocksService = new StocksService();

class BaseLayout extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      stockData: []
    };
    this.handleSubmit = this.handleSubmit.bind(this);
    
    this.serachInput = React.createRef();
  }

  handleSubmit(e) {
    let self = this;
    e.preventDefault();

    stocksService
      .getStockHistory(
        this.serachInput.current.value
      )
      .then(function(result) {
        console.log(result.data);
        self.props.history.push(
          `/history/${self.serachInput.current.value}`
        );
        self.setState({
          stockData: result.data
        });
      });
  }

  render() {
    return (
      <div>
        <Navbar bg="dark" variant="dark" fixed="top">
          <Nav className="mr-auto">
            <Nav.Link>
              {" "}
              <Link to="/client">ClientList</Link>
            </Nav.Link>
            <Nav.Link>
              {" "}
              <Link to="/sg">SGList</Link>
            </Nav.Link>
           <Nav.Link>
              {" "}
              <Link to="/status">Status</Link>
            </Nav.Link>
          </Nav>
          <Form inline onSubmit={this.handleSubmit}>
            <FormControl
              type="text"
              placeholder="Search by Reference"
              className="mr-sm-2"
              ref={this.serachInput}
            />
           
            <Button variant="outline-info" onClick={this.handleSubmit}>
              Search
            </Button>
          </Form>
        </Navbar>

        <div className="container-fluid">
          <nav className="navbar navbar-expand-lg navbar-light bg-light ">
            <a className="navbar-brand" href="#">
              Easter Egg
            </a>
          </nav>
        </div>

        <div className="container-fluid">
          <nav
            className="navbar navbar-expand-lg navbar-light bg-light"
            position="fixed"
          >
            <div className="w3-center">
              <h4>Stocks</h4>
            </div>
          </nav>

          <div className="content">
            
            <Route path="/client" exact component={ClientList} />
            <Route path="/sg" component={SGList} />
            <Route path="/status" component={StatusList} />
            <Route
              path="/history"
              render={props => (
                <StocksHistory {...props} stockList={this.state.stockData} />
              )}
            />
            
           
          </div>
        </div>
      </div>
    );
  }
}

const Layout = withRouter(BaseLayout);

class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <Layout />
      </BrowserRouter>
    );
  }
}

export default App;
