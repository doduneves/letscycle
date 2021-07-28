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


import Routes from './routes/index'
import EditRoute from './routes/edit'

export default function App() {
  return (
    <>
      <Navbar bg="light" expand="lg">
        <Container>
          <Navbar.Brand href="/">letscycle</Navbar.Brand>
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
            <Route exact path="/">
              <Routes />
            </Route>
            <Route path="/edit/:id">
              <EditRoute />
            </Route>
          </Switch>
        </div>
      </Router>
    </>
  );
}