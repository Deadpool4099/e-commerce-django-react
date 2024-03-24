import React, { useState, useEffect } from "react";
import axios from "axios";

const Signup = () => {

  const [state, setState] = useState({});
  const [isValid, setIsValid] = useState(true);


  const onUsernameChange = (e) => {
    setState((prevState) => ({
      ...prevState, username: e.target.value
    }))
  };

  const onEmailChange = (e) => {
    setState((prevState) => ({
      ...prevState, email: e.target.value
    }))
  };

  const onPasswordChange = (e) => {
    setState((prevState) => ({
      ...prevState, password: e.target.value
    }))
  };

  const onPassword2Change = (e) => {
    setState((prevState) => ({
      ...prevState, password2: e.target.value
    }))
  };

  const onFirstNameChange = (e) => {
    setState((prevState) => ({
      ...prevState, first_name: e.target.value
    }))
  };

  const onLastNameChange = (e) => {
    // console.log(state)
    setState((prevState) => ({
      ...prevState, last_name: e.target.value
    }))
  };


  const onSubmit = (e) => {
    console.log(state);
    const requestOptions = {
      method: "POST",
      body: JSON.stringify(state),
      headers: {
        "Content-Type": "application/json",
      },
    };
    console.log(state);
    fetch("api/auth/signup", requestOptions)
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
      })
      .catch((error) => {
        console.log(error);
        setIsValid(false)
      });
  };

  // const onSubmit = (e) => {
  //   console.log(state);
  //   // axios.post("http://127.0.0.1:8000/api/auth/signup", state)
  //   //   .then((response) => {
  //   //     let data = response.data.json();
  //   //     console.log(data);
  //   //   }).catch((error) => {
  //   //     setIsValid(false);
  //   //   })
  //   axios.post("http://127.0.0.1:8000/api/auth/signup", state)
  //     .then(({ data }) => {
  //       console.log(data);
  //     }).catch((error) => {
  //       setIsValid(false);
  //     })
  // }

  useEffect(() => {
  }, [])

  return (
    <div>
      <form className="login-form">
        <h3 className="heading">Signup</h3>
        <label>
          First Name:
          <input type="text" onChange={onFirstNameChange} />
        </label>
        <br />
        <label>
          Last Name:
          <input type="text" onChange={onLastNameChange} />
        </label>
        <br />
        <label>
          Username:
          <input type="text" onChange={onUsernameChange} />
        </label>
        <br />
        <label>
          Email:
          <input type="email" onChange={onEmailChange} />
        </label>
        <br />
        <label>
          Password:
          <input type="password" onChange={onPasswordChange} />
        </label>
        <br />
        <label>
          Re Enter Password:
          <input type="password" onChange={onPassword2Change} />
        </label>
        <br />
        <button
          type="submit"
          value="Signup"
          onClick={onSubmit}
          className="submit"
        >
          Signup
        </button>
        <br />
        {
          !isValid &&
          <p1>User Details Not Correct</p1>
        }
      </form >
    </div >
  );
  // return (<div>
  //   <h1>
  //     Hi
  //   </h1>
  //   <button
  //     type="submit"
  //     value="Signup"
  //     onClick={onSubmit}
  //     className="submit"
  //   >
  //     Signup
  //   </button>
  // </div>);
}

export default Signup;
