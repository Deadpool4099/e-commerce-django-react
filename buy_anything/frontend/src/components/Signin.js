import React, { useState } from "react";

import { render } from "react-dom";

import {
  BrowserRouter as Router,
  Route,
  Routes,
  Switch,
} from "react-router-dom";
// import { Switch } from "react-router-dom/cjs/react-router-dom.min";

const Signin = () => {
  const [state, setState] = useState({});

  const onUsernameChange = (e) => {
    setState((prevState) => ({
      ...prevState,
      username: e.target.value,
    }));
  };

  const onPasswordChange = (e) => {
    setState((prevState) => ({
      ...prevState,
      password: e.target.value,
    }));
  };

  const onSubmit = (e) => {
    const requestOptions = {
      method: "POST",
      body: JSON.stringify(state),
      headers: {
        "Content-Type": "application/json",
      },
    };
    console.log(state);
    fetch("api/auth/signin", requestOptions)
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
      })
      .catch((error) => {
        window.alert(error);
      });
  };
  return (
    <div>
      <form className="login-form">
        <h3 className="heading">Signin</h3>
        <label>
          Username:
          <input type="text" onChange={onUsernameChange} />
        </label>
        <br />
        <label>
          Password:
          <input type="password" onChange={onPasswordChange} />
        </label>
        <br />
        <button
          type="submit"
          value="Login"
          onClick={onSubmit}
          className="submit"
        >
          Login
        </button>
      </form>
    </div>
  );
};

export default Signin;
