import React from "react";

function UserInfo({name, email}){
    return(
        <div className="user-info">
            <h2>{name}</h2>
            <p>Email: {email}</p>
        </div>
    );
}
export default UserInfo;