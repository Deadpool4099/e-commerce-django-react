import React from "react";
import { render } from "react-dom";

import { BrowserRouter as Router, Route, Routes, Switch } from 'react-router-dom'
import Signin from './Signin';
import Home from './Home';
import Signup from './Signup'
// import { Switch } from "react-router-dom/cjs/react-router-dom.min";

const App = () => {
  return (
    <Router>
      <Switch>
        <Route exact path="/">
          <Home />
        </Route>
        <Route exact path='/signin'>
          <Signin />
        </Route>
        <Route exact path='/signup'>
          <Signup />
        </Route>
      </Switch>
    </Router>
  );
}

export default App;
