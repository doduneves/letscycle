import React from "react";
import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom";

import {
  Container,
  Nav,
  Navbar,
} from 'react-bootstrap';


import Routes from './routes'

export default function App() {
  return (
    <>
    <Navbar bg="light" expand="lg">
      <Container>
        <Navbar.Brand href="#home">letscycle</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link href="/about">About</Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
    <Router>
      <div>

        <Switch>
          <Route path="/">
            <Routes />
          </Route>

        </Switch>
      </div>
    </Router>
    </>
  );
}