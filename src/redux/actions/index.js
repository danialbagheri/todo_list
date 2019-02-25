import { ADD_TODO, TOGGLE_TODO, SET_FILTER } from "../actionTypes";

let nextTodoId = 0;

export const addTodo = data => ({
  type: ADD_TODO,
  payload: {
    id: ++nextTodoId,
    requested_by: data.requested_by,
    input: data.input
  }
});

export const toggleTodo = id => ({
  type: TOGGLE_TODO,
  payload: { id }
});

export const setFilter = filter => ({ type: SET_FILTER, payload: { filter } });
