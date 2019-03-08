import { ADD_TODO } from "../actionTypes";

const url = "http://127.0.0.1:8000/addtodo";
export const addTodo = data => dispatch => {
  console.log("adding todo...");
  // Default options are marked with *
  fetch(url, {
    method: "POST",
    mode: "cors",
    body: JSON.stringify(data) // body data type must match "Content-Type" header
  })
    .then(res => res.json())
    .then(data => dispatch(addTodoSuccess(data))); // parses response to JSON
};

const addTodoSuccess = todos => ({
  type: ADD_TODO,
  payload: {
    ...todos
  }
});
