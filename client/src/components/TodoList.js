import React from "react";
import { connect } from "react-redux";
import { fetchTodos } from "../redux/actions/fetchTodos";
import store from "../redux/store";

const mapStateToProps = state => {
  return {
    todo_list: state.todos.todo_list
  };
};

class TodoList extends React.Component {
  state = {};
  componentDidMount() {
    this.props.fetchTodos();
  }
  render() {
    console.log("here");
    console.log(this.props);
    const mySate = store.getState();
    console.log(mySate);
    return (
      <div>
        <p>List</p>
      </div>
    );
  }
}

// export default TodoList;
export default connect(
  mapStateToProps,
  { fetchTodos }
)(TodoList);
