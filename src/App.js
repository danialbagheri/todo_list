import React from "react";
// import logo from "./logo.svg";
import "./App.css";

import AddTodo from "./components/AddTodo";
import TodoList from "./components/TodoList";
import VisibilityFilters from "./components/VisibilityFilters";

class App extends React.Component {
  render() {
    return (
      <div className="todo-app">
        <h1>Todo List</h1>
        <AddTodo />
        <TodoList />
        <VisibilityFilters />
      </div>
    );
  }
}

export default App;
