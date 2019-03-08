import React from "react";
import { NavLink } from "react-router-dom";

class Header extends React.Component {
  render() {
    return (
      <header>
        <nav className="navbar">
          <ul className="navbar-nav">
            <span className="navbar-brand">
              <h1>Marketing Project List</h1>
            </span>
            <li>
              <NavLink exact className="nav-link" to="/">
                LIST
              </NavLink>
            </li>
            <li>
              <NavLink exact className="nav-link" to="/add-todo">
                ADD
              </NavLink>
            </li>
            <li>
              <NavLink exact className="nav-link" to="/create-user">
                Create user
              </NavLink>
            </li>
          </ul>
        </nav>
      </header>
    );
  }
}

export default Header;
