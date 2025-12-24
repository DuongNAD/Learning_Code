import React from "react";
import { Link, NavLink } from "react-router-dom";

const Navbar = () => {
    return(
        <nav className="navbar">
            <h2>Cua hang</h2>
            <ul>
                <li><NavLink to="/" exact activeClassName="active">Trang chu</NavLink></li>
                <li><NavLink to="/products" activeClassName="active">San pham</NavLink></li>
                <li><NavLink to="/contact" activeClassName="active">Lien he</NavLink></li>
            </ul>
        </nav>
    );
}

export default Navbar;