import { ADD_TODO } from "../actionTypes";

const todoState = {
  // allIds: [],
  // byIds: {},
  todo: [],
  error: null
};

export default function(state = todoState, action) {
  switch (action.type) {
    case ADD_TODO:
      console.log("todo-added");
      return {
        ...state,
        loading: false,
        error: null,
        todo: [...state.todo, action.payload]
      };
    default:
      return state;
  }
}
console.log(todoState);
