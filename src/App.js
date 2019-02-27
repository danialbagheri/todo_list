import React from "react";
// import logo from "./logo.svg";
import "./App.css";

import AddTodo from "./components/AddTodo";
import AddUser from "./components/AddUser";
import List from "./pages/list";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import Header from "./components/Header";
class App extends React.Component {
  render() {
    return (
      <BrowserRouter>
        <div>
          <div className="todo-app">
            <Header />
          </div>
          <Switch>
            <Route path="/" component={List} exact />
            <Route path="/add-todo" component={AddTodo} />
            <Route path="/create-user" component={AddUser} />
            <Route component={Error} />
          </Switch>
        </div>
      </BrowserRouter>
    );
  }
}

export default App;
