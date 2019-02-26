import TodoList from "../components/TodoList";
import VisibilityFilters from "../components/VisibilityFilters";
import React from "react";

class List extends React.Component {
  render() {
    return (
      <div>
        <TodoList />
        <VisibilityFilters />
      </div>
    );
  }
}

export default List;
