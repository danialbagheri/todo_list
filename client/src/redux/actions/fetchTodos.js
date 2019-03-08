import { FETCH_TODOS } from "../actionTypes";
const fetchUrl = "http://127.0.0.1:8000/todo";

export const fetchTodos = () => dispatch => {
  fetch(fetchUrl)
    .then(res => {
      return res.json();
    })
    .then(data => {
      dispatch({ type: FETCH_TODOS, payload: data });
    });
};
